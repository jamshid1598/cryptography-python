from django.utils.translation import gettext_lazy as _
from datetime import timedelta
from django.conf import settings

# import default settings and credentials
from .base import *
from .credentials import *


SECRET_KEY = secret_key
DEBUG = debug
ALLOWED_HOSTS = allowed_hosts


#  tinymce configuration
TINYMCE_DEFAULT_CONFIG = {
    'height': 400, 
    'width': 800, 
    'cleanup_on_startup': True, 
    'custom_undo_redo_levels': 20, 
    'selector': 'textarea', 
    'theme': 'modern', 
    'plugins': ''' textcolor save link image media preview codesample contextmenu 
                   table code lists fullscreen insertdatetime nonbreaking contextmenu 
                   directionality searchreplace wordcount visualblocks visualchars 
                   code fullscreen autolink lists charmap print hr anchor pagebreak ''', 
    'toolbar1': ''' fullscreen preview bold italic underline | fontselect, fontsizeselect | 
                    forecolor backcolor | alignleft alignright | aligncenter alignjustify | 
                    indent outdent | bullist numlist table | | link image media | codesample | ''', 
    'toolbar2': ''' visualblocks visualchars | charmap hr pagebreak nonbreaking anchor | code | ''', 
    'contextmenu': 'formats | link image', 
    'menubar': True, 
    'statusbar': True, 
}


# Application definition
INSTALLED_APPS += [
    # 3rd party apps
    'tinymce',                  # django-tinymce4-lite==1.8.0
    'phonenumber_field',        # django-phonenumber-field[phonenumbers]==5.2.0 (django-phonenumber-field[phonenumbers] or django-phonenumber-field[phonenumberslite]) 
    'rest_framework',           # djangorestframework==3.12.4 (django-rest-framework)
    'rest_framework_simplejwt', # djangorestframework-simplejwt==5.0.0 (django-rest-framework-simplejwt)
    'smart_selects',            # django-smart-selects==1.5.9
    'import_export',            # django-import-export==2.6.1
    
    # local apps
    'apps.users.apps.UsersConfig',
    'apps.core.apps.CoreConfig',
    
]


# custom student user model
AUTH_USER_MODEL = "users.User"

LOGIN_REDIRECT_URL = "core:home"
LOGOUT_REDIRECT_URL = "user:login"
LOGIN_URL = 'user:login'

# django-rest-framework-simplejwt configuration
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': False,
    'UPDATE_LAST_LOGIN': True,

    'ALGORITHM': 'HS256',
    'SIGNING_KEY': settings.SECRET_KEY,
    'VERIFYING_KEY': None,
    'AUDIENCE': None,
    'ISSUER': None,
    'JWK_URL': None,
    'LEEWAY': 0,

    'AUTH_HEADER_TYPES': ('Bearer',),
    'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
    'USER_ID_FIELD': 'id',
    'USER_ID_CLAIM': 'user_id',
    'USER_AUTHENTICATION_RULE': 'rest_framework_simplejwt.authentication.default_user_authentication_rule',

    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
    'TOKEN_USER_CLASS': 'rest_framework_simplejwt.models.TokenUser',

    'JTI_CLAIM': 'jti',

    'SLIDING_TOKEN_REFRESH_EXP_CLAIM': 'refresh_exp',
    'SLIDING_TOKEN_LIFETIME': timedelta(minutes=30),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=1),
}


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / '../templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tashkent'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# django-smart-select configuration
JQUERY_URL = False
USE_DJANGO_JQUERY = True


# django-phonenumber-field default region configuration
PHONENUMBER_DEFAULT_REGION = "UZ"


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = "/media/"

STATIC_ROOT = BASE_DIR / "static_root/"
MEDIA_ROOT  = BASE_DIR / "media_root/"

staticfiles_dirs = BASE_DIR / 'static/'
STATICFILES_DIRS = [
    staticfiles_dirs,
]