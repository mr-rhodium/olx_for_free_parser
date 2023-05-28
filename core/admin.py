from django.contrib import admin
from .models import StopWord


class AdminWord(admin.ModelAdmin):
    pass


admin.site.register(StopWord, AdminWord)