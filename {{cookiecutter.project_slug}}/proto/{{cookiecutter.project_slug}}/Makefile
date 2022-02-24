
RESOURCE_PROTOS := $(shell find . -path "./sentieo/**/type/*.proto")
SERVICE_PROTOS := $(shell find . -path "./sentieo/**/v*/*.proto")

clean:
	-find sentieo -name '*.py' -delete
	-find sentieo -name '*.py[ico]' -delete
	-rm -rf dist/*

setup:
	poetry install

python-protobuf:
	python -m grpc_tools.protoc -I . \
	--python_out=. --grpc_python_out=. $(SERVICE_PROTOS)

package: python-protobuf
	# Proto compiler doesn't automatically generates the `__init__.py` file for
	# python packages. So, we explicitly generate the files just before package
	# is built.
	find sentieo -type d -exec touch {}/__init__.py \;
	poetry build

dist: protobuf clean
	poetry build

update:
	poetry self:update
	poetry update

proto-docs:
	docker run \
	--rm -v $(CURDIR)/docs:/out \
	-v $(CURDIR)/{{ cookiecutter.project_slug }}/proto:/{{ cookiecutter.project_slug }}/proto \
	pseudomuto/protoc-gen-doc -I . $(SERVICE_PROTOS)

	# Open generated file with default application
	xdg-open docs/index.html
