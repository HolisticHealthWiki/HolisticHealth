import os

from dynaconf import Dynaconf

settings = Dynaconf(
    environments=True,
    envvar_prefix="HHCONF",
    root_path=os.path.dirname(os.path.realpath(__file__)),
    settings_files=["settings.toml", ".secrets.toml"],
)
