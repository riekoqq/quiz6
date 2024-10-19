from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):
    def create_user(self, username, email, contact, password=None, is_active=True, is_staff=False, is_superuser=False):
        """Create and return a `User` with an email, username, and password."""
        if not username:
            raise ValueError('Users must have a username')
        if not email:
            raise ValueError('Users must have an email address')
        if not password:
            raise ValueError('Users must have a password')

        email = self.normalize_email(email)  # Normalize email

        if User.objects.filter(email=email).exists():
            raise ValueError('Email address is already in use')
        if User.objects.filter(username=username).exists():
            raise ValueError('Username is already in use')
        if User.objects.filter(contact=contact).exists():
            raise ValueError('Contact number is already in use')

        user_obj = self.model(username=username, email=email, contact=contact)
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.staff = is_staff
        user_obj.is_superuser = is_superuser  # Use the consistent name
        user_obj.save(using=self._db)

        return user_obj

    def create_staffuser(self, username, email, contact, password=None):
        """Create and return a `User` with staff privileges."""
        return self.create_user(
            username,
            email,
            contact,
            password=password,
            is_staff=True,
            is_active=True,
        )

    def create_superuser(self, username, email, contact, password):
        """Create and return a `User` with superuser privileges."""
        return self.create_user(
            username,
            email,
            contact,
            password=password,
            is_staff=True,
            is_superuser=True,  # Use the consistent name
            is_active=True
        )


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    contact = models.CharField(max_length=11, unique=True, null=True, blank=True)
    username = models.CharField(max_length=100, unique=True)
    active = models.BooleanField(default=False, blank=True)  # Allows to create without this field being required
    staff = models.BooleanField(default=False)  # For staff status
    is_superuser = models.BooleanField(default=False)  # For superuser status

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'contact']  # Keep email and contact required

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        """Check if the user has a specific permission."""
        return True

    def has_module_perms(self, app_label):
        """Check if the user has permissions for the app `app_label`."""
        return True

    @property
    def is_staff(self):
        """Check if the user is a staff member."""
        return self.staff

    @property
    def is_active(self):
        """Check if the user is active."""
        return self.active


