# th2 gRPC common library (4.0.0)

This library contains common proto messages that are used in all th2 components. See [common.proto](https://github.com/th2-net/th2-grpc-common/blob/master/src/main/proto/th2_grpc_common/common.proto "common.proto") file for details. <br>
Tool generates code from `.proto` files and uploads built packages (`.proto` files and generated code) to specified repositories.

## How to maintain a project
1. Perform the necessary changes.
2. Update the package version of Java in `gradle.properties` file.
3. Update the package version of Python in `package_info.json` file.
4. Commit everything.

### Java
If you wish to manually create and publish a package for Java, run the following command:
```
gradle --no-daemon clean build publish artifactoryPublish \
       -Purl=${URL} \ 
       -Puser=${USER} \
       -Ppassword=${PASSWORD}
```
`URL`, `USER` and `PASSWORD` are parameters for publishing.

### Python
If you wish to manually create and publish a package for Python:
1. Generate services with `Gradle`:
    ```
       gradle --no-daemon clean generateProto
    ```
   You can find the generated files by following path: `src/gen/main/services/python`
2. Generate code from `.proto` files and publish everything using `twine`:
    ```
    pip install -r requirements.txt
    pip install twine
    python setup.py generate
    python setup.py sdist
    twine upload --repository-url ${PYPI_REPOSITORY_URL} --username ${PYPI_USER} --password ${PYPI_PASSWORD} dist/*
    ```
    `PYPI_REPOSITORY_URL`, `PYPI_USER` and `PYPI_PASSWORD` are parameters for publishing.

## Release notes

### 4.0.0
+ Marked deprecated fields as `reserved`
+ Moved `timestamp` from `MessageMetadata`/`RawMessageMetadata` to `MessageID`
+ Moved `start_timestamp` from `Event` to `EventID`
+ Added `book_name` to `MessageID` and `EventID`
+ Added `scope` to `EventID`
+ Added `map<string, SessionAliasToDirectionCheckpoint>` to `Checkpoint`. It describes book to session alias to direction.

### 3.11.0

+ Added `session_group` parameter to `ConnectionID`

### 3.10.0

+ Updated grpc-service-generator (added support for gRPC pins filters).

### 3.9.0

+ Added `null_value` in `ValueFilter`. Should be used only with EQUAL and NOT_EQUAL operations.

### 3.8.0
+ Added `time_precision` and `decimal_precision` parameters to `RootComparisonSettings`
+ Added `EQ_TIME_PRECISION` and `EQ_DECIMAL_PRECISION` filter operation, witch filter a field by comparing values(`date/time` in ISO format and `numeric` types) with the precision. The timestamps will be compared with the protobuf duration format. Numbers use string format, for example _0.0001_, _0.125_, _125E-3_

### 3.7.0
+ Added `check_repeating_group_order` parameter to `RootComparisonSettings`

### 3.6.0
+ Added `description` parameter to `RootMessageFilter`.

### 3.5.0
+ Added SimpleList parameter to SimpleFilter. 

### 3.4.0

+ Added `IN` and `NOT_IN` filter operation, which filter a field by value from list of `String`.
+ Added `LIKE` and `NOT_LIKE` filter operation, which filter a field by `String` regEx expression.
+ Added `MORE`, `LESS`, `NOT_MORE`, `NOT_LESS` filter operations, which filter a field by comparing values(`numeric` types and `date/time` in ISO format).
+ Added `WILDCARD` and `NOT_WILDCARD`  filter operations, which filter a field by `String` specified wildcard expression.
The wildcard matcher uses the characters `?` and `*` to represent a single or multiple (zero or more) wildcard characters.
This is the same as often found on Dos/Unix command lines.
+ "abc-123", "*-123"     --&gt; true
+ "abc-123", "*-xyz"     --&gt; false
+ "abc-123", "ab*"       --&gt; true
+ "abc-123", "*-???"     --&gt; true
+ "abc-123", "*-????"    --&gt; false

N.B. the sequence `*?` does not work properly at present in match strings.

### 3.3.0

+ Added information about message timestamp into checkpoint message

### 3.2.0

+ Implement stubs creation for Python
