from setuptools import setup, find_packages

setup(
    name='pretix-header-injector',
    version='4.0.0', # Final version
    description='A pretix plugin to inject custom code into the HTML head.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
[pretix.plugin]
pretix_header_injector=pretix_header_injector:HeaderInjectorApp
"""
)
