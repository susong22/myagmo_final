from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.db import models

class User(AbstractUser):
    AREA = [
        ('Seoul','서울'),
        ('Suwon','수원'),
    ]

    name = models.CharField(_("이름"), blank=True, max_length=255,unique=True)
    phone_number = models.CharField(_("Phone Number"), blank=True, max_length=255,unique=True)
    email = models.EmailField(unique=True)
    area = models.CharField(blank=True, choices=AREA , max_length=225)
    password = models.CharField(max_length=128,unique=True)


    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
    
    class Meta:
        app_label = 'users'
