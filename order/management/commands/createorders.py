# import os
# import random
# from termcolor import colored
# import requests
# from django.core.management import BaseCommand
# from faker import Faker
# from blog.models import BlogModel, BlogTagModel, CommentModel, AuthorModel
#
# fake = Faker()
#
#
# class Command(BaseCommand):
#     help = colored('''
#         You can create dummy data. \nLike this:
#     Authors      -> 20
#     Tags         -> 15
#     Blogs        -> 1000
#     Comments     -> 20
#     ''', 'blue')
#
#     def add_arguments(self, parser):
#         parser.add_argument('-a', '--author', type=int, help='Define a author number prefix', )
#         parser.add_argument('-t', '--tag', type=int, help='Define a tag number prefix', )
#         parser.add_argument('-b', '--blog', type=int, help='Define a product number prefix', )
#         parser.add_argument('-c', '--comment', type=int, help='Define a comment number prefix', )
#
#     def handle(self, *args, **options):
#         a = options['author'] if options['author'] else 0
#         t = options['tag'] if options['tag'] else 0
#         b = options['blog'] if options['blog'] else 0
#         c = options['comment'] if options['comment'] else 0
#
#         if a:
#             print(colored('\n\n\t\tCREATING Authors', 'blue'))
#             for i in range(a):
#                 first_name = fake.first_name()
#                 last_name = fake.last_name()
#                 try:
#                     img = download_image(500, 500, 'images/authors/', fake.unique.word())
#                 except:
#                     print(colored('No answer', 'red'))
#                     continue
#                 AuthorModel.objects.create(first_name=first_name, last_name=last_name, image=img)
#                 print(colored(f'{first_name} {last_name} -> author added'), colored("   OK", 'green'))
#
#         if t:
#             print(colored('\n\n\t\tCREATING Tags', 'blue'))
#             for i in range(t):
#                 name = fake.word()
#                 BlogTagModel.objects.create(name=name)
#                 print(colored(f'{name} -> tag added'), colored("    OK", 'green'))
#
#         if b:
#             print(colored('\n\n\t\tCREATING Blogs', 'blue'))
#             authors = AuthorModel.objects.all()
#             for i in range(b):
#                 title = fake.sentence()
#                 # text = '<br><br>'.join(fake.paragraphs(nb=random.randint(20, 50)))
#                 text = ""
#                 for _ in range(random.randint(3, 10)):
#                     paragraph = fake.text(max_nb_chars=random.randint(300, 800))
#                     text += paragraph + "<br><br>"
#
#                 try:
#                     img = download_image(1140, 584, 'images/blog/', fake.unique.word())
#                 except:
#                     print(colored('No answer', 'red'))
#                     continue
#                 author = random.choice(authors)
#                 tags = BlogTagModel.objects.order_by('?')[:random.randint(1, 5)]
#                 entry = BlogModel.objects.create(title=title, author=author, text=text, image=img)
#                 entry.tags.set(tags)
#                 print(colored(f'{title} -> blog added'), colored("  OK", 'green'))
#
#         if c:
#             print(colored('\n\n\t\tCREATING Comments', 'blue'))
#             blogs = BlogModel.objects.all()
#             for i in range(c):
#                 name = fake.name()
#                 email = fake.email()
#                 phone = fake.phone_number()
#                 comment = fake.paragraph()
#                 blog = random.choice(blogs)
#                 CommentModel.objects.create(name=name, email=email, phone=phone, blog=blog,
#                                             comment=comment)
#                 print(colored(f'comment added to {blog}'), colored("    OK", 'green'))
