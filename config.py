import os


# Set default vars in Config
class Config:
    DATABASE_URI = ""


class DevelopmentConfig(Config):
    DATABASE_URI = 'postgresql+psycopg2://{dbuser}:{dbpass}@{dbhost}/{dbname}'.format(
        dbuser=os.environ['DBUSER'],
        dbpass=os.environ['DBPASS'],
        dbhost=os.environ['DBHOST'],
        dbname=os.environ['DBNAME']
    )

# class TestingConfig(Config):
#     DATABASE_URI = ""

# It's best to use system environment variables when deploying the app to Azure, as any sensitive data -- secrets and database credentials -- are not to be hardcoded in the app's source code.
class ProductionConfig(Config):
    DATABASE_URI = ""
