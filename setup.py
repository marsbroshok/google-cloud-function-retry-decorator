from distutils.core import setup

with open('requirements.txt') as file_requirements:
    requirements = file_requirements.read().splitlines()
    
setup(
    name='Retry Decorator for Google Cloud Function',
    version='0.1',
    packages=['.',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires=requirements,
)
