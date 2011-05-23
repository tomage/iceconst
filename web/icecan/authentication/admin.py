

from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User as ContribUser, Group as ContribGroup
from django.utils.translation import ugettext, ugettext_lazy as _

from models import User, Group

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User

class CustomUserAdmin(UserAdmin):
    model = User
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
        (_('Permissions'), {'fields': ('is_active', 'type', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('Groups'), {'fields': ('groups',)}),
    )
    form = CustomUserChangeForm
    #list_display = ('type',)
    list_filter = ('type',)

admin.site.unregister(ContribUser)
admin.site.unregister(ContribGroup)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Group)