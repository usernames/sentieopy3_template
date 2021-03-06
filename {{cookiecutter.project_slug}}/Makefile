.PHONY: clean virtualenv test docker

DOCKER_BUILD_STAGE := prod-build
DOCKER_IMAGE_NAME := {{ cookiecutter.project_slug }}
DOCKER_IMAGE_TAG := latest
DOCKER_FILE_PATH := {{ cookiecutter.project_slug }}
GRPC_SERVER_PORT := 50051
ECR_PATH := 602037364990.dkr.ecr.us-east-1.amazonaws.com
CURRENT_APP_VERSION := $(lastword $(shell poetry version))
PACKAGR_URL_WITH_CREDS := $(lastword $(shell poetry export -f requirements.txt --with-credentials | head -n 1))

setup:
	pip install poetry==$(POETRY_VERSION)
	poetry install
	{% if cookiecutter.install_precommit_hooks == "y" %}
	git init
	pre-commit install --install-hooks --hook-type pre-commit --hook-type pre-push
	{% endif %}

docker-builddep:
	poetry export -f requirements.txt -o requirements.txt --without-hashes

docker-ci-builddep:
	poetry export -f requirements.txt -o requirements.txt --without-hashes --dev

docker-build:
	docker build \
		--build-arg packagr_url=$(PACKAGR_URL_WITH_CREDS) \
		-t $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) \
		-t $(DOCKER_IMAGE_NAME):$(CURRENT_APP_VERSION) \
		-t $(ECR_PATH)/$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG) \
		-f Dockerfile .

docker: docker-builddep docker-build

docker-push:
	docker push $(ECR_PATH)/$(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)

run-docker-server: 
	docker run -p $(GRPC_SERVER_PORT):(GRPC_SERVER_PORT) --name $(DOCKER_IMAGE_NAME) $(DOCKER_IMAGE_NAME):$(DOCKER_IMAGE_TAG)

run-server: 
	export ENV_FOR_DYNACONF="LOCAL" && python -m rms.settings.app.py.server

test: 
	-python -m pytest \
		-v \
		--cov={{ cookiecutter.project_slug }} \
		--cov-report=term \
		--cov-report=html:coverage-report \
		--cov-fail-under=80 \
		.

	xdg-open coverage-report/index.html

update:
	poetry update
	{% if cookiecutter.install_precommit_hooks == "y" %}
	pre-commit autoupdate
	{% endif %}


