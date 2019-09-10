from django.contrib import admin
from django.contrib.auth.models import User

admin.site.unregister(User)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    
    def group(self, user):
        groups = [group.name for group in user.groups.all()]

        return ' '.join(groups)

    group.short_description = 'groups'

    list_display = ('id', 'username', 'group', 'is_superuser', 'password', )