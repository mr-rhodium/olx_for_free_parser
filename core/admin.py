from django.contrib import admin
from .models import StopWord, TelegramUser


class AdminWord(admin.ModelAdmin):
    pass

class AdminTelegramUser(admin.ModelAdmin):
    pass

admin.site.register(StopWord, AdminWord)
admin.site.register(TelegramUser, AdminTelegramUser)