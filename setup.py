from setuptools import setup

setup(
    name='pretix-header-injector',
    version='1.0.1',
    description='A pretix plugin to inject custom code into the HTML head.',
    author='Your Name',
    author_email='your.email@example.com',
    packages=['pretix_header_injector'], # This line was changed
    include_package_data=True,
    entry_points="""
[pretix.plugin]
pretix_header_injector=pretix_header_injector:PretixPluginMeta
"""
)