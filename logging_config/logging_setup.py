import logging
from datetime import datetime
from logging.config import fileConfig


# logs = ["root_out", "root_err", "sqlalchemy_out", "sqlalchemy_err", "alembic_out", "alembic_err", "flask_migrate_out", "flask_migrate_err"]

def setup_logging(config_path, log_dir, logs):
    """Load logging configuration"""
    logging_config_defaults = {}
    timestamp = datetime.now().strftime("%Y%m%d")
    for log in logs:
        logging_config_defaults.update({f"{log}": f"{log_dir}/{log}/{timestamp}.log"})

    return fileConfig(
        config_path,
        disable_existing_loggers=False,
        defaults=logging_config_defaults
    )
