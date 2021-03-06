FROM python:3.8-slim as first-build

LABEL maintainer="{{ cookiecutter.full_name }} <{{ cookiecutter.email }}>"

ARG packagr_url

# Environment varialbes to control python and pip behaviour.
ENV PYTHONFAULTHANDLER=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONHASHSEED=random \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100

# Application specific variables.
ENV GRPC_SERVICE_PORT="50051" \
    # Specify the environment where this container is deployed. For list of
    # available environments, refer config/settings.toml.
    ENV_FOR_DYNACONF="DEVELOPMENT" \
    DEBUG_LEVEL_FOR_DYNACONF="DEBUG" \
    VAULT_ENABLED_FOR_DYNACONF=false

WORKDIR /{{ cookiecutter.project_slug }}

COPY {{ cookiecutter.project_slug }}/requirements.txt /{{ cookiecutter.project_slug }}/

RUN PIP_EXTRA_INDEX_URL=${packagr_url} pip install \
    -r /{{ cookiecutter.project_slug }}/requirements.txt

from first-build as second-build
COPY . /{{ cookiecutter.project_slug }}/

from second-build as third-build
ENTRYPOINT ["python", "-m", "{{cookiecutter.project_team}}.{{cookiecutter.project_name}}.app.py.server"]

EXPOSE ${GRPC_SERVICE_PORT}

