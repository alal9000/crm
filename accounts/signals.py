from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

from . models import Customer


def create_profile(sender, instance, created, **kwargs):

  if created:
    group = Group.objects.get(name='customer')
    instance.groups.add(group)
    Customer.objects.create(user=instance, name=instance.username)
    print("profile was created")


post_save.connect(create_profile, sender=User)
def update_profile():
  """
  if created == False:
    print()
    try:
      instance.profile.save()
      print('Profile updated!')
    except:
      Profile.objects.create(user=instance)
      print('Profile created for existing user')
  """