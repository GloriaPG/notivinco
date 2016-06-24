# -*- coding: utf-8 -*-
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin
)


from django.db import models
from django.utils.translation import ugettext_lazy as _


class UsersManager(BaseUserManager):
    """
    Manager personalizado para el modelo usuario.
    """

    def _create_user(
        self,
        email,
        password,
        is_superuser=False,
        is_staff=False,
        is_active=False,
        **extra_fields
    ):
        """
        Método base para la creación de nuevos usuarios.
        """
        if not email:
            raise ValueError('The given email address must be set.')

        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_superuser=is_superuser,
            is_staff=is_staff,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Crea un nuevo usuario.
        """
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Crea un nuevo usuario marcándolo como super usuario.
        """
        return self._create_user(email, password, True, True, **extra_fields)


class Users(AbstractBaseUser, PermissionsMixin):
    name = models.TextField(
        max_length=50,
        blank=False,
        null=False
    )
    last_name = models.TextField(
        max_length=100,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        max_length=100,
        unique=True,
        null=False
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_('is_staff')
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_('is_active')
    )
    objects = UsersManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'is_active'
    ]

    def get_full_name(self):
        """
        Return full name user:
             name last_name mothers_maiden_name
        """
        parts = [self.name, self.last_name]
        return ' '.join(filter(None, parts))

    def get_short_name(self):
        """
        Return short name user:
            name last_name
        """
        parts = [self.name]
        return ' '.join(filter(None, parts))


class Notice(models.Model):
    title = models.TextField(
        max_length=60,
        null=False,
        blank=False
    )
    content = models.TextField(
        max_length=250,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        default=True
    )
    user = models.ForeignKey(
        Users,
        null=False,
        related_name='notice'
    )


class Comment(models.Model):
    comment = models.TextField(
        max_length=160,
        null=False,
        blank=False
    )
    is_active = models.BooleanField(
        default=True
    )
    notice = models.ForeignKey(
        Notice,
        null=True,
        related_name='notices'
    )
    user = models.ForeignKey(
        Users,
        null=True,
        related_name='comments'
    )
