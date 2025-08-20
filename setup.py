import os
from distutils.command.build import build

from django.core import management
from setuptools import setup, find_packages


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix-header-injector',
    version='1.0.0',
    description='Embed any code into Pretix header event pages',
    long_description=long_description,
    url='https://github.com/jxs714/pretix-header-injector',
    author='Your Name',
    author_email='your.email@example.com',
    license='Apache',

    install_requires=[],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,

    entry_points="""
[pretix.plugin]
pretix_header_injector=pretix_header_injector:PretixPluginMeta
""",
)
