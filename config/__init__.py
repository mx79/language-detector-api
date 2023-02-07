import os


class Config:
    DEBUG = False
    DEVELOPMENT = False
    PROPAGATE_EXCEPTIONS = False

    X_API_KEY = os.getenv("X_API_KEY", "dev-secret-not-so-easy-to-find")


class ProductionConfig(Config):
    pass


class DevelopmentConfig(Config):
    DEBUG = True
    DEVELOPMENT = True
