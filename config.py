class Config(object):

    SQLALCHEMY_DATABASE_URI = 'postgres://inqemahooylwml:6c57827b5f83d30b51104a18e7bce497140540a56b13159286bfb9d97e4609bc@ec2-3-210-255-177.compute-1.amazonaws.com:5432/dcr2mtcqdg08c'
    DEBUG=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY='6c57827b5f83d30b51104a18e7bce497140540a56b13159286bfb9d97e4609bc'

   

class DevelopmentConfig(Config):
    pass
   

class ProductionConfig(Config):
    pass

 

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}