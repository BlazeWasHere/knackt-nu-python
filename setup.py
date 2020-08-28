from setuptools import setup

setup(
    name="knackt",
    version="1.0.0",
    author="Blaze",
    description= "library for api.knackt.nu",
    packages=['knackt'],
    install_requires = [
        'requests'
    ]
)