# Create your models here.
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations = True

    # Method to save user to the database
    def save_user(self, phone_number, password, **extra_fields):
        """
        Creates and saves a User with the given phone number and password.
        """
        if not phone_number:
            raise ValueError('The given phone number must be set')

        user = self.model(phone_number=phone_number, **extra_fields)

        # Call this method for password hashing
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, phone_number, password=None, **extra_fields):
        extra_fields['is_superuser'] = False
        extra_fields['is_staff'] = False
        return self.save_user(phone_number, password, **extra_fields)

    # Method called while creating a staff user
    def create_staffuser(self, phone_number, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = False

        return self.save_user(phone_number, password, **extra_fields)

        # Method called while calling creatsuperuser

    def create_superuser(self, phone_number, password, **extra_fields):

        # Set is_superuser parameter to true
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('is_superuser should be True')

        extra_fields['is_staff'] = True

        return self.save_user(phone_number, password, **extra_fields)