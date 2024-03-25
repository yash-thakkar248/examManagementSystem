from django.db import models
from .regex import item
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(models.Model):
    # USER_TYPE_CHOICES = (
    #     ('student', 'Student'),
    #     ('instructor', 'Instructor'),
    # )

    first_name = models.CharField(max_length=30, validators=[item.name_validator])
    last_name = models.CharField(max_length=30, validators=[item.name_validator])
    username = models.CharField(max_length=150, validators=[item.username_validator])
    email = models.EmailField(validators=[item.email_validator],unique=True)
    password = models.CharField(max_length=30, validators=[item.password_validator])
    user_type = models.CharField(max_length=150)
    # user_type = models.CharField(max_length=150, choices=USER_TYPE_CHOICES)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['user_type']
 
    def __str__(self) -> str:
        return self.username