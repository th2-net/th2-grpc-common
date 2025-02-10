TARGET_DIR?=$(shell pwd)
PROTO_DIR=src/main/proto
MODULE_NAME=$(PROTO_DIR)
MODULE_DIR=$(TARGET_DIR)/$(MODULE_NAME)

configure-go:
	go install google.golang.org/protobuf/cmd/protoc-gen-go@latest

clean-module:
	rm -rf $(MODULE_DIR)/*.go

generate-module: clean-module configure-go
	protoc --proto_path=$(PROTO_DIR) \
	    --go_out=$(MODULE_DIR) \
	    --go_opt=paths=source_relative \
	    $(shell find $(PROTO_DIR) -name '*.proto')