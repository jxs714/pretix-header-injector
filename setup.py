from setuptools import setup, find_packages

setup(
    name='pretix-header-injector',
    version='1.0.0',
    description='A pretix plugin to inject custom code into the HTML head.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    entry_points="""
[pretix.plugin]
pretix_header_injector=pretix_header_injector:HeaderInjectorApp
"""
)
