from decouple import config

secret_key = config("SECRET_KEY", default="")
debug = config("DEBUG", cast=bool, default=True)
allowed_hosts = config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')], default=['127.0.0.1',])