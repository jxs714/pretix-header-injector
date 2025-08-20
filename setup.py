from setuptools import setup, find_packages

setup(
    name='pretix-header-injector',
    version='1.0.0',
    description='Embed any code into Pretix header event pages',
    author='Your Name',
    author_email='your.email@example.com',
    license='Apache Software License',
    
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    
    install_requires=[],
    
    entry_points="""
[pretix.plugin]
pretix_header_injector=pretix_header_injector:PretixPluginMeta
""",
)
