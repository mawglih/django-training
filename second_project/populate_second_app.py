import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','second_project.settings')

import django
django.setup()


from second_app.models import User
from faker import Faker

fakegen = Faker()

def populate(N=10):
  for n in range(N):
    fake_fn = fakegen.first_name()
    fake_ln = fakegen.last_name()
    fake_en = fakegen.ascii_safe_email()

    user = User.objects.get_or_create(first_name=fake_fn,last_name=fake_ln,email=fake_en)[0]

if __name__ == '__main__':
  print("populating script")
  populate(100)
  print("population complete")