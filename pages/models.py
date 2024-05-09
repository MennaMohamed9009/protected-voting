from django.db import models
import uuid
from django.contrib.auth.models import PermissionsMixin,Permission,Group
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils import timezone
from .management import CustomUserManager
from django.core.exceptions import ValidationError

# Create your models here.

def validate_national_id_length(value):
    if len(str(value)) != 14:
        raise ValidationError('National ID must be exactly 14 digits long.')

class nationality(models.Model):
      nationalityname=models.CharField(unique=True,max_length=40)
      def __str__(self):
            return self.nationalityname
      


class persons(models.Model):
    name = models.CharField(blank=True,max_length=20)
    nationalId=models.BigIntegerField(null=True, unique=True, validators=[validate_national_id_length])
    def __str__(self):
        return f"persons of {self.name}"
    
class Profile(models.Model):
    user = models.ForeignKey(persons, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(blank=True, upload_to='photos')
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"profile of {self.bio}"
    
class Log(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    photo = models.ImageField(upload_to='logs')
    is_correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class User(AbstractBaseUser, PermissionsMixin):
  

    GENDER_CHOICES = [
        ('male', 'ذكر'),
        ('female', 'انثي'),
    ]
    
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
  # These fields tie to the roles!
    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
    # Roles created here
    groups = models.ManyToManyField(Group, verbose_name='groups', blank=True, related_name='custom_user_set')
    user_permissions = models.ManyToManyField(Permission, verbose_name='user permissions', blank=True, related_name='custom_user_set')
    uid = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, verbose_name='Public identifier')
    username=models.CharField(max_length=40,null=True)
    email = models.EmailField(unique=True)
    FirstName = models.CharField(max_length=30, blank=True)
    lastName = models.CharField(max_length=30, blank=True)
    nationality=models.ForeignKey(nationality,on_delete=models.SET_NULL,null=True)
    phone_number = models.CharField(max_length=15,null=True)
    BIrthDate = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=True)

   


    USERNAME_FIELD = 'email'

    objects = CustomUserManager()
    def __str__(self):
            return self.email
    
class Car(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)


class DataStored(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    firstName = models.CharField(max_length=100, null=False, blank=False, default="Salma")
    familyName = models.CharField(max_length=100, null=False, blank=False, default="Hany")
    phoneNumber = models.DecimalField(max_digits=11, decimal_places=0, default=0)
    Nationality = models.CharField(max_length=100, null=False, blank=False, default="Egyptian")
    gamil = models.CharField(max_length=150, null=False, blank=False, default="add your gmail")
    password = models.CharField(max_length=150, null=False, blank=False, default="add your password")
    re_password = models.CharField(max_length=150, null=False, blank=False, default="confirm your password")
    sex = models.CharField(max_length=100, null=True, blank=True, choices=SEX_CHOICES)
    birth = models.DateField(default="2002-04-16")


    def __str__(self):
        return self.firstName


class Voter(models.Model):
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    firstName = models.CharField(max_length=100, null=True, blank=True)
    familyName = models.CharField(max_length=100, null=True, blank=True)
    phoneNumber = models.DecimalField(max_digits=11, decimal_places=0, default=0)
    Nationality = models.CharField(max_length=100, null=True, blank=True)
    gamil = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150, null=True, blank=True)
    re_password = models.CharField(max_length=150, null=True, blank=True)
    sex = models.CharField(max_length=100, null=True, blank=True, choices=SEX_CHOICES)
    birth = models.DateField(default="2002-04-16")


    def __str__(self):
        return self.firstName


class N_ID(models.Model):
    nationalID = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    activate = models.BooleanField(default=True)


class Election(models.Model):
    CANDIDATE_CHOICES = [
        ('sisi', 'Sisi'),
        ('hazem', 'Hazem'),
        ('abd el sanad', 'Abd El Sanad'),
        ('mohamed', 'Mohamed'),
    ]
    nationalID = models.DecimalField(max_digits=14, decimal_places=0, default=0)
    candidateName = models.CharField(max_length=100, null=True, blank=True, choices=CANDIDATE_CHOICES)
