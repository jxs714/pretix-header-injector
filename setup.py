from setuptools import setup, find_packages

setup(
    name='pretix-header-injector',
    version='1.0.0',
    description='Embed code into Pretix headers',
    packages=find_packages(),
    include_package_data=True,
    entry_points="""
[pretix.plugin]
pretix_header_injector=pretix_header_injector:PretixPluginMeta
""",
)
