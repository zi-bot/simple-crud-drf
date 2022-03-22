from faker import Faker
from operator import index
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE','config.settings')
django.setup()
from userprofile.models import UserProfile

def create_user_profile():
    for i in range(200):
        fake = Faker()
        UserProfile.objects.create(
            lname=fake.last_name(),
            fname=fake.first_name(),
            is_active=True,
        )

if __name__ == '__main__':
    create_user_profile()