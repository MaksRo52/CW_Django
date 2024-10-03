from django.contrib import admin

from newsletter.models import Client, Message, Mailing
from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "token")

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("theme",)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


