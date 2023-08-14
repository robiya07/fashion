from termcolor import colored
from django.core.management.base import BaseCommand
from faker import Faker

from blog.management.commands.createblogs import download_image
from main.models import MemberModel, ContactModel

fake = Faker()


class Command(BaseCommand):
    help = colored('''
        You can create dummy data. \nLike this:
    Members      -> 20
    Contacts     -> 50
    ''', 'blue')

    def add_arguments(self, parser):
        parser.add_argument('-m', '--members', type=int, help='Define a member number prefix', )
        parser.add_argument('-c', '--contacts', type=int, help='Define a contact number prefix', )

    def handle(self, *args, **options):
        m = options['members'] if options['members'] else 0
        c = options['contacts'] if options['contacts'] else 0

        if m:
            print(colored('\n\n\t\tCREATING Members', 'blue'))
            for i in range(m):
                first_name = fake.first_name()
                last_name = fake.last_name()
                position = fake.job()
                try:
                    img = download_image(500, 500, 'images/members/', fake.unique.word())
                except:
                    print(colored('No answer', 'red'))
                    continue
                MemberModel.objects.create(first_name=first_name, last_name=last_name, position=position, image=img)
                print(f'{first_name} {last_name} -> member added', colored("   OK", 'green'))

        if c:
            print(colored('\n\n\t\tCREATING Contacts', 'blue'))
            for i in range(c):
                name = fake.name()
                email = fake.email()
                message = fake.paragraph()
                ContactModel.objects.create(name=name, email=email, message=message)
                print(f'Contact {name} added', colored("    OK", 'green'))
