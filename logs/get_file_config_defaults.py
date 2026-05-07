from datetime import datetime


def get_file_config_defaults():
    timestamp = datetime.now().strftime("%Y%m%d")
    logs_subdirs = ["root", "sqlalchemy", "alembic", "flask_migrate"]
    config_defaults = {}
    for log in logs_subdirs:
        log_filename= f"logs/{log}/{log}_{timestamp}.log"
        open(log_filename, "a").close()
        config_defaults.update({f"{log}": log_filename})

    return config_defaults
