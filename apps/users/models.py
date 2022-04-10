# django
from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import gettext_lazy as _
import uuid

# other packages
from phonenumber_field.modelfields import PhoneNumberField

# local import
from .manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    id       = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(_("Username"), max_length=100, help_text='This field must be required', unique=True)
    image    = models.ImageField(_('Image'), blank=True, null=True, upload_to=f'user-images/')
    
    # user private info
    first_name  = models.CharField(_("First Name"), max_length=200, blank=True, null=True)
    last_name   = models.CharField(_("Last Name"), max_length=200, blank=True, null=True)
    middle_name = models.CharField(_("Middle Name"), max_length=200, blank=True, null=True)
    birthday    = models.DateField(_("Birthday"), max_length=20, help_text=_('optional'), blank=True, null=True,)
    passport    = models.CharField(_("Passport"), max_length=100, help_text=_('optional'), blank=True, null=True)
    jshshir     = models.CharField(_("JSHSHIR"), max_length=100, help_text=_('optional'), blank=True, null=True) 
    
    # contact info
    email       = models.EmailField(_('Email'), max_length=200, blank=True, null=True, help_text=_('this field must be required'), unique=True)
    phonenumber = PhoneNumberField(_('Phone-number'), blank=True, null=True, help_text=_('this field must be required'), unique=True)
    
    # user type
    # is_student   = models.BooleanField(_("is student"), help_text=_('optional'), default=False)
    # is_teacher   = models.BooleanField(_('is teacher'), help_text=_('optional'), default=False)
    
    # user status
    is_active    = models.BooleanField(_('is_active'), default=True)
    is_staff     = models.BooleanField(_('is_staff'), default=False)
    is_superuser = models.BooleanField(_('is_superuser'), default=False)
    
    # created, updated and last login dates
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)
    created_at = models.DateTimeField(_("created at"), auto_now_add=True)
    last_login = models.DateTimeField(_("last login"), blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'

    class Meta:
        ordering = ('username',)
        verbose_name = _('User')
        verbose_name_plural = _('Users')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return "/user/%i/" % (self.pk)