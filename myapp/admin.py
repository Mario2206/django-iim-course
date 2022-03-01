from django.contrib import admin

from .models import Question

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    fields = ['date', 'text']

admin.site.register(Question)
