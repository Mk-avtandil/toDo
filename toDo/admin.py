from django.contrib import admin

from .models import ToDo


class ToDoAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'created_at')
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(ToDo, ToDoAdmin)
