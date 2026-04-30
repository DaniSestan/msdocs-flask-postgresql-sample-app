# TODO: change the logging config
from logging.config import dictConfig

dictConfig({
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'default': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        }
    },

    'handlers': {
        'db_sqlalchemy_engine_file': {
            'class': 'logging.FileHandler',
            'filename': 'sqlalchemy_engine.log',          # ✅ file output
            'mode': 'a',
            'formatter': 'default',
        },
        'db_sqlalchemy_dialects_file': {
            'class': 'logging.FileHandler',
            'filename': 'sqlalchemy_dialects.log',          # ✅ file output
            'mode': 'a',
            'formatter': 'default',
        },
        'db_sqlalchemy_pool_file': {
            'class': 'logging.FileHandler',
            'filename': 'sqlalchemy_pool.log',          # ✅ file output
            'mode': 'a',
            'formatter': 'default',
        },
        'db_sqlalchemy_orm_file': {
            'class': 'logging.FileHandler',
            'filename': 'sqlalchemy_orm.log',          # ✅ file output
            'mode': 'a',
            'formatter': 'default',
        }
    },

    'loggers': {
        'python-flask-app': {
            'level': 'INFO',
            'handlers': [],       # ✅ use file handler
            'propagate': False,            # ✅ critical: stop stdout
        },
        'sqlalchemy.engine': {
            'level': 'INFO',
            'handlers': ['db_sqlalchemy_engine_file'],       # ✅ use file handler
            'propagate': False,            # ✅ critical: stop stdout
        },
        'sqlalchemy.dialects': {
            'level': 'INFO',
            'handlers': ['db_sqlalchemy_dialects_file'],       # ✅ use file handler
            'propagate': False,            # ✅ critical: stop stdout
        },
        'sqlalchemy.pool': {
            'level': 'INFO',
            'handlers': ['db_sqlalchemy_pool_file'],       # ✅ use file handler
            'propagate': False,            # ✅ critical: stop stdout
        },
        'sqlalchemy.orm': {
            'level': 'INFO',
            'handlers': ['db_sqlalchemy_orm_file'],       # ✅ use file handler
            'propagate': False,            # ✅ critical: stop stdout
        }
    }
})
