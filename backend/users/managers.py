from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    #Validacion de email, Login
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("Debe ingresar un correo válido."))
        
    def create_user(self, first_name, last_name, email, password, **extra_fields):
        if not first_name:
            raise ValueError(_(" Debe ingresar su nombre para el registro "))
        
        if not last_name:
            raise ValueError(_(" Debe ingresar sus apellidos para el registro "))
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_(" Usuario: Debe ingresar un correo electrónico "))
        
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        user.save()

        return user
    
    def create_superuser(self, first_name, last_name, email, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_(" No es un SuperUsuario "))

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_(" No forma parte del personal "))
        
        if not password:
            raise ValueError(_(" Los SuperUsuarios deben tener una contraseña "))

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_(" Administrador: Debe ingresar un correo electrónico "))
        
        user = self.create_user(first_name, last_name, email, password, **extra_fields)

        user.save()

        return user
    