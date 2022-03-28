# django-import-export
from import_export import (
    resources,
    fields,
)
# local files
from .widgets import (
    BooleanWidget,
    CustomDateWidget,
    CustomDateTimeWidget,
)
from .models import (
    User,
)

class UserResource(resources.ModelResource):
    id           = fields.Field(attribute="id", column_name="id")
    username     = fields.Field(attribute="username", column_name="(username)")
    first_name   = fields.Field(attribute="first_name", column_name="first name")
    last_name    = fields.Field(attribute="last_name", column_name="last name")
    middle_name  = fields.Field(attribute="middle_name", column_name="middle name")
    passport     = fields.Field(attribute="passport", column_name="passport")
    birthday     = fields.Field(attribute="birthday", column_name="birthday")
    
    is_active    = fields.Field(attribute="is_active", column_name="active user", widget=BooleanWidget())
    is_staff     = fields.Field(attribute="is_staff", column_name="staff user", widget=BooleanWidget())
    is_superuser = fields.Field(attribute="is_superuser", column_name="superuser user", widget=BooleanWidget())
    
    last_login = fields.Field(attribute="last_login", column_name="last login", widget=CustomDateTimeWidget("%d-%m-%Y %H:%M:%S"))
    updated_at = fields.Field(attribute="updated_at", column_name="updated date", widget=CustomDateTimeWidget("%d-%m-%Y %H:%M:%S"))
    created_at = fields.Field(attribute="created_at", column_name="created date", widget=CustomDateTimeWidget("%d-%m-%Y %H:%M:%S"))

    class Meta:
        model = User
        fields = (
            "id", "username", "first_name", "last_name", "middle_name", "passport", "birthday",
            "is_student", "is_active", "is_staff", "is_superuser",
            "last_login", "updated_at", "created_at",
        )
        export_order = (
            "id", "username", "first_name", "last_name", "middle_name", "passport", "birthday", 
            "is_student", "is_active", "is_staff", "is_superuser",
            "last_login", "updated_at", "created_at",
        )
        exclude = (
            "groups", "user_permissionss",
        )
    # def dehydrate_full_name(self, user):
    #     return "%s %s %s"%(user.first_name, user.last_name, user.middle_name)
    
    def after_save_instance(self, instance, using_transactions, dry_run):
        """
        
        """
        birthday = instance.birthday
        instance.set_password(birthday)
        instance.save()
        
