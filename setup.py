from setuptools import find_packages, setup

with open('readme.md') as f:
    readme = f.read()

setup(
    name='tetry',
    packages=find_packages(include=['tetry', 'tetry.bot']),
    version='0.2',
    description='tetr.io api wrapper',
    long_description=readme,
    author='apes0',
    python_requires='>=3',
    install_requires=['requests', 'dateutils']
)