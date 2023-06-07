from django.core.management import BaseCommand
from django.contrib.auth.models import User
from faker import Faker


class Command(BaseCommand):

    help = "help for user"

    def add_arguments(self, parser):
        parser.add_argument('-l', '--len', type=int, default=0)

    def handle(self, *args, **options):
        # user = User(username="alexx", first_name="alexandr", last_name="gg")
        # user.save()
        faker = Faker('ru')

        for i in range(options['len']):
            # print(faker.simple_profile())
            fake_user = faker.simple_profile()
            user = User(username=fake_user['username'], email=fake_user['mail'], first_name=fake_user['name'].split()[1], last_name=fake_user['name'].split()[0])
            user.save()
