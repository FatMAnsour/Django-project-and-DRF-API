from django.contrib.postgres.search import SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
from rest_framework.pagination import PageNumberPagination
from django.db.models import Q, F
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class CustomPageNumberPagination(PageNumberPagination):
    page_size = 10  
    page_size_query_param = 'page_size'
    max_page_size = 100 
class ProductSearchView(APIView):
    pagination_class = CustomPageNumberPagination
    def get(self, request, *args, **kwargs):

        query = request.GET.get('q', '').strip()
        category = request.GET.get('category',None)
        brand = request.GET.get('brand',None)
        
        if not query:
            return Response({'error': 'Please enter a search query'}, status=status.HTTP_400_BAD_REQUEST)
        search_query_en = SearchQuery(query,config='english') 
        search_query_ar = SearchQuery(query,config='arabic')
        search_rank = SearchRank(F('search_vector'),search_query_en) + SearchRank(F('search_vector'),search_query_ar)

        products = Product.objects.annotate(
            rank=search_rank,
            similarity=TrigramSimilarity('name', query) + TrigramSimilarity('brand__name', query) + TrigramSimilarity('category__name', query)
            ).filter(
                Q(search_vector=search_query_en) | Q(search_vector=search_query_ar) | Q(similarity__gt=0.3)
            ).select_related('brand', 'category').order_by('-rank', '-similarity')
        if category:
            products = products.filter(category__name__iexact=category)
        if brand:
            products = products.filter(brand__name__iexact=brand)

        
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(page, many=True)

        return paginator.get_paginated_response(serializer.data)    
        
     
        