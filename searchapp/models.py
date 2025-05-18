from django.db import models
from django.contrib.postgres.indexes import GinIndex
from django.contrib.postgres.search import SearchVectorField, SearchVector

class Category(models.Model): 
    name = models.CharField(max_length=255)
    class Meta:
        indexes = [
            GinIndex(
                name='category_name_trigram_idx',
                fields=['name'],
                opclasses=['gin_trgm_ops']
            ),
        ]
    def __str__(self):
        return self.name

class Brand(models.Model): 
    name = models.CharField(max_length=255)
    class Meta:
        indexes = [
            GinIndex(
                name='brand_name_trigram_idx',
                fields=['name'],
                opclasses=['gin_trgm_ops']
            ),
        ]
    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE) 
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    nutrition_facts = models.TextField()
    search_vector = SearchVectorField(null=True)

    class Meta:
        indexes = [
            GinIndex(fields=['search_vector']),
            GinIndex(
                name='name_trigram_idx',
                fields=['name'],
                opclasses=['gin_trgm_ops']
            ),
        ]
    
    def save(self, *args, **kwargs):
        brand_name = self.brand.name if self.brand else ''
        category_name = self.category.name if self.category else ''
        
        self.search_vector = SearchVector(
            models.Value(self.name, output_field=models.TextField()),
            models.Value(brand_name, output_field=models.TextField()),
            models.Value(category_name, output_field=models.TextField()),
            models.Value(self.nutrition_facts, output_field=models.TextField()),
            config='english'
        ) + SearchVector(
            models.Value(self.name, output_field=models.TextField()),
            models.Value(brand_name, output_field=models.TextField()),
            models.Value(category_name, output_field=models.TextField()),
            models.Value(self.nutrition_facts, output_field=models.TextField()),
            config='arabic'
        )
        
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name