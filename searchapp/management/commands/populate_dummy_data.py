from django.core.management.base import BaseCommand
from django.contrib.postgres.search import SearchVector
from faker import Faker
import random
from searchapp.models import Product, Brand, Category  # Adjust to your app name

class Command(BaseCommand):
    help = 'Generates 1000 dummy products, 50 brands, and 20 categories with mixed English/Arabic names'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before populating',
        )

    def handle(self, *args, **options):
        # Initialize Faker for English and Arabic
        fake_en = Faker('en_US')
        fake_ar = Faker('ar_SA')

        # Clear existing data if --clear is provided
        if options['clear']:
            Category.objects.all().delete()
            Brand.objects.all().delete()
            Product.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Cleared existing data'))

        # Generate 20 Categories with mixed English/Arabic names
        categories = []
        category_names = [
            ("Beverages", "المشروبات"),
            ("Snacks", "الوجبات الخفيفة"),
            ("Dairy", "منتجات الألبان"),
            ("Bakery", "المخبوزات"),
            ("Canned Goods", "المعلبات"),
            ("Frozen Foods", "الأطعمة المجمدة"),
            ("Cereals", "الحبوب"),
            ("Condiments", "التوابل"),
            ("Sweets", "الحلويات"),
            ("Pasta", "المعكرونة"),
            ("Fruits", "الفواكه"),
            ("Vegetables", "الخضروات"),
            ("Meat", "اللحوم"),
            ("Seafood", "المأكولات البحرية"),
            ("Grains", "الحبوب الكاملة"),
            ("Spices", "البهارات"),
            ("Sauces", "الصلصات"),
            ("Desserts", "الحلويات"),
            ("Breakfast", "الإفطار"),
            ("Organic", "العضوية")
        ]
        for en_name, ar_name in category_names:
            # Randomly choose English, Arabic, or mixed name
            name = random.choice([en_name, ar_name, f"{en_name} {ar_name}"])
            category = Category.objects.create(name=name)
            categories.append(category)
        self.stdout.write(self.style.SUCCESS(f'Created {len(categories)} categories'))

        # Generate 50 Brands with mixed English/Arabic names
        brands = []
        brand_names = [
            ("Nestle", "نستله"),
            ("PepsiCo", "بيبسيكو"),
            ("Kraft", "كرافت"),
            ("Unilever", "يونيليفر"),
            ("Coca-Cola", "كوكاكولا"),
            ("Mars", "مارس"),
            ("Kellogg's", "كيلوغز"),
            ("General Mills", "جنرال ميلز"),
            ("Mondelez", "مونديليز"),
            ("Danone", "دانون"),
            ("P&G", "بروكتر وغامبل"),
            ("Colgate", "كولجيت"),
            ("Heinz", "هاينز"),
            ("Ferrero", "فيريرو"),
            ("Cadbury", "كادبوري"),
            ("Hershey's", "هيرشي"),
            ("Lays", "لايز"),
            ("Pringles", "برينجلز"),
            ("Tyson", "تايسون"),
            ("Barilla", "باريلا"),
            ("Knorr", "كنور"),
            ("Lipton", "ليبتون"),
            ("Schweppes", "شويبس"),
            ("Red Bull", "ريد بول"),
            ("Monster", "مونستر"),
            ("Oreo", "أوريو"),
            ("Bimbo", "بيمبو"),
            ("Arla", "أرلا"),
            ("Yoplait", "يوبلا"),
            ("Maggi", "ماجي"),
            ("Kinder", "كيندر"),
            ("Nabisco", "نابيسكو"),
            ("Quaker", "كويكر"),
            ("Gatorade", "جاتوريد"),
            ("Tropicana", "تروبيكانا"),
            ("Durex", "دوركس"),
            ("Lindt", "ليندت"),
            ("Toblerone", "توبليرون"),
            ("Clif", "كليف"),
            ("Nature Valley", "نيتشر فالي"),
            ("Blue Diamond", "بلو دايموند"),
            ("Altoids", "ألتويدز"),
            ("Starbucks", "ستاربكس"),
            ("Twinings", "تويننجز"),
            ("L'Oréal", "لوريال"),
            ("Dole", "دول"),
            ("Chiquita", "شيكيتا"),
            ("Perrier", "بيرييه"),
            ("Evian", "إيفيان"),
            ("Aquafina", "أكوافينا")
        ]
        for en_name, ar_name in brand_names:
            name = random.choice([en_name, ar_name, f"{en_name} {ar_name}"])
            brand = Brand.objects.create(name=name)
            brands.append(brand)
        self.stdout.write(self.style.SUCCESS(f'Created {len(brands)} brands'))

        # Generate 1000 Products with mixed English/Arabic names
        products = []
        for _ in range(1000):
            brand = random.choice(brands)
            category = random.choice(categories)
            # Generate product name (e.g., "Crispy Bar" or "شريط مقرمش")
            en_product = f"{fake_en.word().capitalize()} {fake_en.word().capitalize()} {random.choice(['Bar', 'Drink', 'Mix', 'Pack', 'Bites', 'Shake', 'Spread', 'Sauce'])}"
            ar_product = f"{fake_ar.word().capitalize()} {fake_ar.word().capitalize()} {random.choice(['شريط', 'مشروب', 'مزيج', 'عبوة', 'قطع', 'هزة', 'دهن', 'صلصة'])}"
            product_name = random.choice([en_product, ar_product, f"{en_product} {ar_product}"])
            
            # Generate nutrition facts in English and Arabic
            calories = random.randint(50, 600)
            fat = random.randint(0, 40)
            carbs = random.randint(0, 100)
            protein = random.randint(0, 30)
            sugar = random.randint(0, 60)
            sodium = random.randint(0, 1500)
            nutrition_facts = (
                f"Calories: {calories} kcal | السعرات الحرارية: {calories} سعرة\n"
                f"Fat: {fat}g | الدهون: {fat}غ\n"
                f"Carbohydrates: {carbs}g | الكربوهيدرات: {carbs}غ\n"
                f"Protein: {protein}g | البروتين: {protein}غ\n"
                f"Sugar: {sugar}g | السكر: {sugar}غ\n"
                f"Sodium: {sodium}mg | الصوديوم: {sodium}ملغ"
            )
            
            product = Product(
                name=product_name,
                brand=brand,
                category=category,
                nutrition_facts=nutrition_facts
            )
            products.append(product)

        # Bulk create products
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Created {len(products)} products'))

        # Update search_vector for all products
        updated_count = 0
        for product in Product.objects.all():
            product.save()  # Triggers search_vector generation
            updated_count += 1
        self.stdout.write(self.style.SUCCESS(f'Updated search_vector for {updated_count} products'))

        self.stdout.write(self.style.SUCCESS('Successfully generated 1000 dummy products, 50 brands, and 20 categories'))