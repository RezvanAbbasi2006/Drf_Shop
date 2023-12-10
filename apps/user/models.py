import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Set user information in database
    """
    username = models.CharField(
        unique=True,
        max_length=150,
        verbose_name=_("username"),
    )
    email = models.EmailField(
        verbose_name=_("email"),
        unique=True,
    )
    avatar = models.ImageField(verbose_name=_("avatar"))
    phone_number = models.CharField(
        verbose_name=_("phone number"),
        max_length=11,
        unique=True,
        null=True,
        blank=True,
    )
    uid = models.CharField(_("uid"), max_length=300, default=uuid.uuid4())

    def set_password(self, raw_password):
        self.password = raw_password

    class Meta:
        verbose_name = _("کاربر")
        verbose_name_plural = _("کاربران")

    def __str__(self):
        return self.email
