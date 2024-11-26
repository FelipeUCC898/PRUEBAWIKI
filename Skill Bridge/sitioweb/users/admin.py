from django.contrib import admin
from .models import personal_Information

# Register your models here.

class personal_Information_admin(admin.ModelAdmin):
    readonly_fields = ('user', 'create_at', 'update_at')
    search_fields = ('names', 'last_names', 'user__username', 'position')
    # list_filter = ('public')
    list_display = ('names', 'last_names', 'create_at', 'user')
    ordering = ('-create_at',)

    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

admin.site.register(personal_Information, personal_Information_admin)