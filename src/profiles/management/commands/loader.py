from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

from cfehome import utils2 as cfehome_utils


User = get_user_model()

class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument("count", nargs='?', default=10, type=int)


    def handle(self, *args, **options):
        #print(f"hello there are {User.objects.count()} users")

        count = options.get('count')

        profiles = cfehome_utils.get_fake_profiles(count=count)

        new_users = []

        for profile in profiles:
            new_users.append(
                User.objects.create(**profile)
            )
        user_bulk = User.objects.bulk_create(new_users, ignore_conflicts=True)

        print(f"New users created {len(user_bulk)}")
