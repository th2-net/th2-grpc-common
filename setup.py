#   Copyright 2020-2020 Exactpro (Exactpro Systems Limited)
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from distutils.cmd import Command
from setuptools.command.sdist import sdist
import shutil
from pkg_resources import resource_filename
import os
from setuptools import setup, find_packages
from os import environ
from pathlib import Path
from lib2to3.main import main as convert2to3


class ProtoGenerator(Command):

    description = 'build protobuf modules'
    user_options = [('strict-mode', 's',
                     'exit with non-zero value if the proto compiling fails.')]

    def initialize_options(self):
        self.strict_mode = False

    def finalize_options(self):
        pass

    def run(self):
        proto_path = os.path.abspath('src/main/proto')
        gen_path = os.path.abspath('src/gen/main/python')

        if not os.path.exists(gen_path):
            os.makedirs(gen_path)

        proto_files = []
        for root, _, files in os.walk(proto_path):
            for filename in files:
                if filename.endswith('.proto'):
                    proto_files.append(os.path.abspath(os.path.join(root, filename)))

        protos = [('grpc_tools', '_proto')]
        protos_include = [f'--proto_path={proto_path}'] + \
                         [f'--proto_path={resource_filename(x[0], x[1])}' for x in protos]

        from grpc_tools import protoc
        for proto_file in proto_files:
            command = ['grpc_tools.protoc'] + \
                      protos_include + \
                      ['--python_out={}'.format(gen_path), '--grpc_python_out={}'.format(gen_path)] + \
                      [proto_file]
            if protoc.main(command) != 0:
                if self.strict_mode:
                    raise Exception('error: {} failed'.format(command))


class CustomDist(sdist):

    def run(self):
        shutil.copytree('src/main/proto/th2', f'{package_name}/proto')

        shutil.copytree('src/gen/main/python/th2', f'{package_name}/grpc')
        Path(f'{package_name}/grpc/__init__.py').touch()
        convert2to3('lib2to3.fixes', [f'{package_name}/grpc', '-w', '-n'])

        Path(f'{package_name}/__init__.py').touch()

        sdist.run(self)

        shutil.rmtree(package_name, ignore_errors=True)


package_name = environ['APP_NAME'].replace('-', '_') if 'APP_NAME' in environ else 'grpc_common'
package_version = environ['APP_VERSION'] if 'APP_VERSION' in environ else '1.0'

setup(
    name=package_name,
    version=package_version,
    url='https://gitlab.exactpro.com/vivarium/th2/th2-core-open-source/grpc-common',
    license='Apache License 2.0',
    author='TH2-devs',
    python_requires='>=3.7',
    author_email='th2-devs@exactprosystems.com',
    description='grpc-common',
    long_description=open('README.md').read(),
    packages=[package_name, f'{package_name}/proto', f'{package_name}/grpc'],
    package_data={f'{package_name}/proto': ['*.proto']},
    cmdclass={
        'generate': ProtoGenerator,
        'sdist': CustomDist
    }
)
