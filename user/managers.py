from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, user_id, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not id:
            raise ValueError('The Id must be set')
        if not extra_fields.get('username'):
            raise ValueError('The Username must be set')
        user = self.model(user_id=user_id, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, user_id, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        return self.create_user(user_id, password, **extra_fields)
