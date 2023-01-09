TARGET_DIR?=$(shell pwd)
MODULE_NAME=th2-grpc-common
MODULE_DIR=$(TARGET_DIR)/$(MODULE_NAME)

gen: clean
	mkdir ${GEN_DIR}
	protoc --proto_path=src/main/proto --go_out=${GEN_DIR} --go_opt=paths=source_relative th2_grpc_common/common.proto

clean-module:
	rm -rf $(MODULE_DIR)

generate-module: clean-module
	mkdir $(MODULE_DIR)
	protoc --proto_path=src/main/proto --go_out=$(MODULE_DIR) --go_opt=paths=source_relative $(shell find src/main/proto/ -name '*.proto')
	cd $(MODULE_DIR) && go mod init github.com/th2-net/$(MODULE_NAME)

clean:
	rm -rf ${GEN_DIR}