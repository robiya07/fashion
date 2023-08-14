from termcolor import colored
from django.core.management.base import BaseCommand
from faker import Faker
from blog.management.commands.createblogs import download_image
from product.models import CategoryModel, TagModel, SizeModel, ColorModel, CollectionModel, ProductModel
import random

fake = Faker()


class Command(BaseCommand):
    help = colored('''
        You can create dummy data. \nLike this:
    Categories      -> 100
    Tags            -> 50
    Colors          -> 7
    Collections     -> 20
    Products        -> 1000
    ''', 'blue')

    def add_arguments(self, parser):
        parser.add_argument('-cat', '--category', type=int, help='Define a author number prefix', )
        parser.add_argument('-t', '--tag', type=int, help='Define a tag number prefix', )
        parser.add_argument('-color', '--color', type=int, help='Define a comment number prefix', )
        parser.add_argument('-coll', '--collection', type=int, help='Define a comment number prefix', )
        parser.add_argument('-p', '--product', type=int, help='Define a comment number prefix', )

    def handle(self, *args, **options):
        cat = options['category'] if options['category'] else 0
        t = options['tag'] if options['tag'] else 0
        color = options['color'] if options['color'] else 0
        coll = options['collection'] if options['collection'] else 0
        p = options['product'] if options['product'] else 0

        if cat:
            print(colored('\n\n\t\tCREATING Categories', 'blue'))
            for _ in range(cat):
                name = fake.word()
                CategoryModel.objects.create(name=name)
                print(colored(f'{name} -> category added'), colored("   OK", 'green'))

        if t:
            print(colored('\n\n\t\tCREATING Tags', 'blue'))
            for _ in range(t):
                name = fake.word()
                TagModel.objects.create(name=name)
                print(colored(f'{name} -> tag added'), colored("   OK", 'green'))

        if not SizeModel.objects.all():
            print(colored('\n\n\t\tCREATING Sizes', 'blue'))
            sizes = ['XXS', 'XS', 'S', 'M', 'L', 'XL', 'XXL', 'XXXL']
            for i in sizes:
                SizeModel.objects.create(name=i)
                print(colored(f'{i} -> size added'), colored("   OK", 'green'))

        if color:
            print(colored('\n\n\t\tCREATING Colors', 'blue'))
            for _ in range(color):
                name = fake.hex_color()
                ColorModel.objects.create(name=name)
                print(colored(f'{name} -> color added'), colored("   OK", 'green'))

        if coll:
            print(colored('\n\n\t\tCREATING Collections', 'blue'))
            for _ in range(coll):
                name = fake.word()
                CollectionModel.objects.create(name=name)
                print(colored(f'{name} -> collection added'), colored("   OK", 'green'))

        if p:
            print(colored('\n\n\t\tCREATING Products', 'blue'))
            categories = CategoryModel.objects.all()
            collections = CollectionModel.objects.all()

            for i in range(p):
                try:
                    img = download_image(1140, 584, 'images/products/main/', fake.unique.word())
                except:
                    print(colored('No answer', 'red'))
                    continue

                name = fake.company()
                short_description = fake.catch_phrase()
                description = ""
                for _ in range(random.randint(3, 5)):
                    paragraph = fake.text(max_nb_chars=random.randint(300, 500))
                    description += paragraph + "<br><br>"

                price = fake.pydecimal(left_digits=random.randint(5, 8), right_digits=2, positive=True)
                sale_percent = random.randint(0, 50)
                sku = fake.unique.random_int(min=1, max=p+1000)
                category = random.choice(categories)
                tags = TagModel.objects.order_by('?')[:random.randint(1, 5)]
                sizes = SizeModel.objects.order_by('?')[:random.randint(1, 5)]
                colors = ColorModel.objects.order_by('?')[:random.randint(1, 5)]
                collection = random.choice(collections)

                entry = ProductModel(
                    main_image=img,
                    name=name,
                    short_description=short_description,
                    description=description,
                    price=price,
                    sku=sku,
                    category=category,
                    collection=collection
                )
                if i % 3 == 0 or i % 7 == 0:
                    entry.sale_percent = sale_percent
                entry.save()
                entry.tags.set(tags)
                entry.sizes.set(sizes)
                entry.colors.set(colors)
                print(colored(f'{name} -> product added'), colored("  OK", 'green'))
