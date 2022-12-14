from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator
from payments.models import Payment_method


class CustomUserManager(BaseUserManager):
    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(username, password, **extra_fields)

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Username', max_length=150, unique=True)
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    gender = models.IntegerField()
    telephone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    telephone = models.CharField(validators=[telephone_regex], max_length=17, blank=True)
    email = models.EmailField("email address", unique=True,error_messages={'unique': "A user with that email already exists."})
    payment_method = models.ForeignKey(Payment_method, on_delete=models.CASCADE, null=True, blank=True)
    email_verified_at = models.DateTimeField(auto_now=False, auto_now_add=False, null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email','name','last_name']
    is_coverer = models.BooleanField(default=False, help_text="Define if the user is someone that can create experiences")
    is_verified = models.BooleanField(default=False, help_text="Set to true when the user have verified its email")
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username
    def get_short_name(self):
        return self.username

