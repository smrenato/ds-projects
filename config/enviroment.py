from dynaconf import Dynaconf

env = Dynaconf(
    envvar_prefix="DS_PROJECTS",
    settings_files=["enviroment.toml"],
    environments=["hparam"],
    env_switcher="PARAM_MODE",
    # validator=Validator("MSG", "required", is_type_of=str),
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.
