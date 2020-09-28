# config.py

class Config(object):
    """
    Common configurations
    """

    # Put any configurations here that are common across all environments


class DevelopmentConfig(Config):
    """
    Development configurations to be used when building the app & running it locally
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True #allows sqlalchemy to log errors


class ProductionConfig(Config):
    """
    Production configurations to be used when the app is deployed
    """

    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}