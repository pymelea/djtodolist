from django.contrib import admin
from .models import ToDo  # new

# Register your models here.
admin.register(ToDo)  # new
class ToDoAdmin(admin.ModelAdmin):  # new
    list_display = ['title', 'complete', 'created_at']  # new
    list_filter = ['complete', 'created_at']  # new
    readonly_fields = ['created_at']  # new
