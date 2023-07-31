from django import forms
from django.contrib.auth.models import User
from .models import Location, Profile
from localflavor.us.forms import USZipCodeField

from .widgets import CustomPictureImageFieldWidget


class UserFrom(forms.ModelForm):
    # "disabled=True" It means we will able to see the value but we wouldn't able to change it.
    username = forms.CharField(disabled=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]


class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(widget=CustomPictureImageFieldWidget)

    class Meta:
        model = Profile
        fields = ["photo", "bio", "phone_number"]


class LocationForm(forms.ModelForm):
    address_1 = forms.CharField(required=True)
    zip_code = USZipCodeField(required=True)

    class Meta:
        model = Location
        fields = ("address_1", "address_2", "city", "state", "zip_code")
