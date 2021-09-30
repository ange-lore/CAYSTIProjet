
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User, UserManager
from django.contrib.auth.models import (
        AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator
from django.utils.timezone import now
'''definition des differents choix du sexe
... sex_choice=
        dictionnaire des differents choix de sexe.
'''


sex_choice = {
    ('FEMININ', 'feminin'),
    ('MASCULIN', 'masculin'),
}
'''
creation de notre model
creation de la classe Patients pour creer notre model
'''
class UserManager(BaseUserManager):
    def create_user(
            self,
            email,
            username,
            password,
            is_active=False,
            is_staff=False,
            is_admin=False,
            is_superuser=False
    ):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have an username")

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            is_active = is_active,
            is_staff = is_staff,
            is_admin = is_admin,
            is_superuser = is_superuser
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username, password):
        return self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            is_admin = True,
            is_staff = True,
            is_active = True,
            is_superuser=True
        )



class Utilisateur(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True, null=False)
    email = models.EmailField(max_length=200, unique=True, null=True)
    phone_regex = RegexValidator(regex=r"^\+?237?\d{9,15}$",
                                 message="Phone number must be entered in the format: '+237699968301'. Up to 15 digits allowed.")
    phone = models.CharField(validators=[phone_regex], max_length=17)
    address = models.CharField(max_length=500, default="")
    sex = models.CharField(max_length=200, default="", choices=sex_choice)
    birth_date = models.DateField(default="1995-5-10")
    password = models.CharField(_('password'), max_length=128, default="")

    date_joined = models.DateTimeField(default=now)
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    #is_supseruser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD ='username'
    #REQUIRED_FIELDS = [ 'email', 'phone', 'address', 'sex', 'birth_date', 'password', ]
    REQUIRED_FIELDS = ['email']



    def __str__(self):
        return self.username
    # @property
    # def is_supervisor(self):
    #     return self.is_admin
    #
    # def has_perm(self, perm, obj=None):
    #     return self.is_admin




# Create your models here.
# class UtilisateurAdmin(admin.ModelAdmin):
#     list_display = ('phone', 'address', 'sex', 'birth_date')
#     list_filter = ('name',)
#     search_fields = ['name', 'email']

class Hopital(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=30, decimal_places=20)
    longitude = models.DecimalField(max_digits=30, decimal_places=20)

class HopitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name',)
    search_fields = ['name', 'address']

"""class Reservation(models.Model):
    hospital = models.forieng
    reservation_date = models.CharField(max_length=200)"""

"""
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('hospital', 'reservation_date')
    list_filter = ('hospital',)
    search_fields = ['hospital', 'reservation_date']"""
# user = models.ForeignKey(User,
    #                          related_name="%(app_label)s_%(class)s_patient_id",
    #                          on_delete=models.CASCADE,
    #                          default=1)
  #  phone = models.IntegerField()