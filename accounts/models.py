from django.db import models
from django.contrib.auth.models import UserManager,AbstractBaseUser
# Create your models here.

class UserManager(AbstractBaseUser):
    def create_user(self,email,name,password=None):
        if not email:
            raise ValueError("Users must have an email address")
        
        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email,name, password=None):
        user = self.create_user(
            email,
            password=password,

            name=name,
        ),
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email",
        max_length=255,
        unique=True,
        null=False,
        blank=False
        
    )
    username = models.CharField(
        max_length=255,
        unique=False,
        null=False,
    )
    is_active=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects= UserManager()
    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin