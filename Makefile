TARGET_DIR?=$(shell pwd)
MODULE_NAME=th2-grpc-common
MODULE_DIR=$(TARGET_DIR)/$(MODULE_NAME)

clean-module:
	rm -rf $(MODULE_DIR)

generate-module: clean-module
	mkdir $(MODULE_DIR)
	protoc --proto_path=src/main/proto --go_out=$(MODULE_DIR) --go_opt=paths=source_relative $(shell find src/main/proto/ -name '*.proto')
	cd $(MODULE_DIR) && go mod init $(MODULE_NAME)