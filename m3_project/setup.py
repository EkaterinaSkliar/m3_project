from setuptools import setup, find_packages

setup(
    name='m3_project',
    version='1.0.0',
    description='A project based on the m3-core and Objectpack modules',
    author='EkaterinaSkl',
    author_email='ekaterinaskliar@gmail.com',
    url='https://github.com/EkaterinaSkl/m3_project',
    packages=find_packages(),
    install_requires=[
        # список зависимостей
        'django==2.2.2',
        'm3-django-compat==1.9.2',
        'm3-objectpack==2.2.47',
    ],
)