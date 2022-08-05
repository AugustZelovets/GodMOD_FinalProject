import re

from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.password_validation import UserAttributeSimilarityValidator, MinimumLengthValidator, \
    CommonPasswordValidator, NumericPasswordValidator
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.utils import timezone
from django.core import validators
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

from mod.models import Mod
from user.utils import UsernameValidator


class CustomUser(AbstractUser):
    username_validator = UsernameValidator(),
    username = models.CharField(
        max_length=20,
        unique=True,
        help_text='Required. 20 characters or less, may contain only English letters, numbers, and . _ characters.',

        validators=username_validator,
        error_messages={
            'unique': "A user with that username already exists.",
        },
    )
    following_mod = models.ManyToManyField(Mod, blank=True)
    # following_modpack = models.ManyToManyField()
    email = models.EmailField("email address", blank=True)

    class Meta:
        pass


# # class User(models.Model):
# #     username_validator = UsernameValidator(),
# #     password_validators = MyMinimumLengthValidator()  # UserAttributeSimilarityValidator() #  CommonPasswordValidator(), \
# #                          # NumericPasswordValidator()
# #
# #     username = models.CharField(
# #         max_length=20,
# #         unique=True,
# #         help_text='Required. 20 characters or fewer. Letters, digits and @/./+/-/_ only.',
# #         validators=username_validator,
# #         error_messages={
# #             'unique': "A user with that username already exists.",
# #         },
# #     )
# #     email = models.EmailField(max_length=254)
# #     password = models.CharField(max_length=20, validators=password_validators)
# #     is_staff = models.BooleanField(default=False, )
# #     is_active = models.BooleanField(
# #         default=False,
# #         help_text=(
# #             'Designates whether this user should be treated as active. '
# #             'Unselect this instead of deleting accounts.'
# #         ),
# #     )
# #     date_joined = models.DateTimeField(default=timezone.now)
# #
# #     # traceable m2m


# class CustomUserManager(BaseUserManager):
#     def create_user(self, email, phone, password, **kwargs):
#         """
#         Creates and saves an Account with the given email or phone and password.
#         """
#         now = timezone.now()
#         identifier = ''
#
#         if not email and not phone:
#             raise ValueError('Users must have a valid email or phone address.')
#
#         if not email:
#             identifier = phone
#         else:
#             email = self.normalize_email(email)
#             identifier = email
#
#         user = self.model(email=email, phone=phone,
#                           identifier=identifier,
#                           joined=now,
#                           **kwargs, )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password, **kwargs):
#         user = self.model(
#             email=email,
#             is_staff=True,
#             is_superuser=True,
#             **kwargs
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user



