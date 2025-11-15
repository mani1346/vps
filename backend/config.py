class Config():
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Corrected the typo from your previous version

class LocalDevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite3"
    DEBUG = True
    SECURITY_PASSWORD_HASH = 'bcrypt'
    SECURITY_PASSWORD_SALT = 'thisshouldbekeptsecret'
    SECRET_KEY = "shouldbekeyveryhidden"
    SECURITY_TOKEN_AUTHENTICATION_HEADER = 'Authentication-Token'
    SECURITY_LOGIN_URL = '/login'

    # --- THIS IS THE FIX ---
    # This line tells Flask-Security to return a 401 error for APIs
    # instead of trying to redirect to a login page.
    SECURITY_UNAUTHORIZED_VIEW = None
    
    # cache specific
    CACHE_TYPE =  "RedisCache"
    CACHE_DEFAULT_TIMEOUT = 30
    CACHE_REDIS_URL = "redis://localhost:6379/0"
    CACHE_REDIS_PORT = 6379
    WTF_CSRF_ENABLED = False

    CELERY_BROKER_URL = "redis://localhost:6379/0"
    CELERY_RESULT_BACKEND = "redis://localhost:6379/0"

MAIL_SERVER = "localhost"
MAIL_PORT = 1025
MAIL_USE_TLS = False
MAIL_USE_SSL = False
MAIL_USERNAME = None
MAIL_PASSWORD = None
MAIL_DEFAULT_SENDER = "admin@study.iitm.ac.in"
