REPO_ROOT := $(abspath .)
GENERATED_PYTHON_DIR := $(REPO_ROOT)/caikit_nlp_client/generated

.PHONY: generate_proto generate_python build clean clean-generated help integration-test test stop-test-server start-test-server

help: ## Display this help.
	@awk 'BEGIN {FS = ":.*##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n"} /^[a-zA-Z_0-9-]+:.*?##/ { printf "  \033[36m%-20s\033[0m %s\n", $$1, $$2 } /^##@/ { printf "\n\033[1m%s\033[0m\n", substr($$0, 5) } ' $(MAKEFILE_LIST)

$(REPO_ROOT)/protobuf:
	mkdir -pv $(REPO_ROOT)/protobuf

$(GENERATED_PYTHON_DIR):
	mkdir -pv $(GENERATED_PYTHON_DIR)

$(REPO_ROOT)/caikit_nlp_client/__init__.py:
	touch $(REPO_ROOT)/caikit_nlp_client/__init__.py

generate-proto: $(REPO_ROOT)/protobuf ##Generate the .proto files from a running instance of caikit-nlp grpc server
	RUNTIME_LIBRARY=caikit_nlp python -m caikit.runtime.dump_services $(REPO_ROOT)/protobuf

PREFIX:="caikit_nlp_client.generated."
generate-python: $(GENERATED_PYTHON_DIR) $(REPO_ROOT)/caikit_nlp_client/__init__.py ##Generate the _pb2.py files from the generated *.proto
	python -m grpc_tools.protoc -I$(REPO_ROOT)/protobuf --python_out=$(GENERATED_PYTHON_DIR) --pyi_out=$(GENERATED_PYTHON_DIR) --grpc_python_out=$(GENERATED_PYTHON_DIR) $(REPO_ROOT)/protobuf/nlpservice.proto
	python -m grpc_tools.protoc -I$(REPO_ROOT)/protobuf --python_out=$(GENERATED_PYTHON_DIR) --pyi_out=$(GENERATED_PYTHON_DIR)  $(REPO_ROOT)/protobuf/caikit.runtime.*.proto
	python -m grpc_tools.protoc -I$(REPO_ROOT)/protobuf --python_out=$(GENERATED_PYTHON_DIR) --pyi_out=$(GENERATED_PYTHON_DIR)  $(REPO_ROOT)/protobuf/caikit_data_model.*.proto
	find $(GENERATED_PYTHON_DIR) -type directory -exec touch {}/__init__.py \;
	find $(GENERATED_PYTHON_DIR) -type f \( -name "*.py" -o -name "*.pyi" \) -exec $(REPO_ROOT)/hack/patch-imports.sh {} \;

clean: ##Clean the created artifacts
	rm -rf dist

clean-generated: ##Clean the generated python directory
	rm -rf $(GENERATED_PYTHON_DIR)

build: ##Build the wheel
	poetry build

test:  ## Run unit tests / integration tests against a running server
	pytest --log-level=DEBUG tests

integration-test: start-test-server test stop-test-server ## Start a server and run the tests

start-test-server:
	echo "Starting a server"
	docker-compose up -d
	sleep 10

stop-test-server:
	echo "Stopping the server"
	docker-compose logs
	docker-compose down