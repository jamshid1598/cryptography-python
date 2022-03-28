from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from import_export.admin import (
    ImportExportModelAdmin,
    ImportExportActionModelAdmin,
)
from .resources import UserResource
     
class UserAdmin(BaseUserAdmin, ImportExportModelAdmin, ImportExportActionModelAdmin):
    resource_class = UserResource

    fieldsets = (
        
        ('User Info', 
            {'fields': (
                "username",
                "image",
                "first_name",
                "last_name", 
                "middle_name",
                'birthday',
                'passport',
                'jshshir',
            )
        }),
        ('Contact Info', 
            {'fields': (
                'email', 
                'phonenumber',
            )
        }),
        # ('User Type', 
        #     {'fields': (
        #         'is_student', 
        #         'is_teacher',
        #     )
        # }),
        ('Status/Groups/Permissions', 
            {'fields': (  
                'is_active', 
                'is_staff', 
                'is_superuser',
                'groups', 
                'user_permissions',
            )
        }),
    )

    add_fieldsets = (
        ("Create New User", {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2')
        }),
    )

    list_display = ('username', 'first_name', 'last_name', 'middle_name',  'birthday', 'passport', 'jshshir', 
                    'phonenumber', 'email',
                    'is_staff', 'is_superuser', 'is_active', 
                    'last_login', 'updated_at', 'created_at',)
    list_display_links = ('username', 'first_name', 'last_name', 'middle_name', 'birthday', 'passport', 'jshshir',)
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'updated_at', 'created_at',)
    search_fields = ('username', 'first_name', 'last_name', 'middle_name', 'birthday', 'passport', 'jshshir', 'email', 'phonenumber')
    ordering = ('username', 'first_name', 'last_name', 'middle_name', 'birthday', 'passport', 'jshshir', 
                'is_staff', 'is_superuser', 'is_active', 'updated_at', 'created_at', )
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(User, UserAdmin)

