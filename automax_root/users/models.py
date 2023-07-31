from django.db import models
from django.contrib.auth.models import User

from localflavor.us.models import USStateField, USZipCodeField

from .utils import user_directory_path


class Location(models.Model):
    address_1 = models.CharField(max_length=128, blank=True)
    address_2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64)
    state = USStateField(default="NY")
    zip_code = USZipCodeField(blank=True)

    def __str__(self):
        return f"Location {self.id}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(
        upload_to=user_directory_path, null=True, default="default/defualt_user_img.png"
    )
    bio = models.CharField(max_length=140, blank=True)
    phone_number = models.CharField(max_length=12, blank=True)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"


# -------------Difference Between (blank=True) and (null=True)---------------
#
#          blank=True             |               null=True
#  blank=True allow us to be      |   null=True allow us to be field can be
#  field can be left empty in a   |   empty in database. Field can be left empty
#  form.                          |   in the form.
#  Field can have empty value in  |   The Value will be stored as Null in the
#  database.                      |   database.