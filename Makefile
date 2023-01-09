GEN_DIR=out

gen: clean
	mkdir ${GEN_DIR}
	protoc --proto_path=src/main/proto --go_out=${GEN_DIR} --go_opt=paths=source_relative th2_grpc_common/common.proto

clean:
	rm -rf ${GEN_DIR}