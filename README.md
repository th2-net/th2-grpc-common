# th2 gRPC common library (2.6.0)

This library contains common proto messages that are used in all th2 components. See [common.proto](https://github.com/th2-net/th2-grpc-common/blob/master/src/main/proto/th2_grpc_common/common.proto "common.proto") file for details. <br>
Tool generates code from `.proto` files and uploads built packages (`.proto` files and generated code) to specified repositories.

## How to maintain a project:
1. Make your changes.
2. Update the version of Java package in `gradle.properties` file.
3. Update the version of Python package in `package_info.json` file.
4. Commit everything.

### Java
If you wish to manually create and publish a package for Java, run these commands:
```
gradle --no-daemon clean build publish artifactoryPublish \
       -Pbintray_user=${BINTRAY_USER} \
       -Pbintray_key=${BINTRAY_KEY}
```
`BINTRAY_USER` and `BINTRAY_KEY` are parameters for publishing.

### Python
If you wish to manually create and publish a package for Python:
1. Generate services from `.proto` files:
    - Download and build [th2 Python service generator](https://github.com/th2-net/th2-python-service-generator "th2-python-service-generator") project with Gradle:
        ```
        gradle clean build
        ```
    - Run th2 Python service generator:
        ```
        java -jar {path_to_jar} -p src/main/proto/{package_name} -w PythonServiceWriter -o src/gen/main/python/{package_name}
       ```
2. Generate code from `.proto` files and publish everything:
    ```
    pip install -r requirements.txt
    pip install twine
    python setup.py generate
    python setup.py sdist
    twine upload --repository-url ${PYPI_REPOSITORY_URL} --username ${PYPI_USER} --password ${PYPI_PASSWORD} dist/*
    ```
    `PYPI_REPOSITORY_URL`, `PYPI_USER` and `PYPI_PASSWORD` are parameters for publishing.

## Release Notes

### 2.6.0

+ Added information about message timestamp into checkpoint message 