#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import join
from setuptools import setup, find_packages

import {{ cookiecutter.app_name }}


def get_version():
    with open(join('{{ cookiecutter.app_name }}', '__init__.py')) as f:
        for line in f:
            if line.startswith('__version__ ='):
                return line.split('=')[1].strip().strip('"\'')


setup(
    name='{{ cookiecutter.project_name }}',
    version=get_version(),
    description="""{{ cookiecutter.project_short_description }}""",
    long_description='\n\n'.join((
        open('README.rst').read(),
        open('CHANGES.rst').read(),
    )),
    author='{{ cookiecutter.full_name }}',
    author_email='{{ cookiecutter.email }}',
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.repo_name }}',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['Django >= 1.5'],
    tests_require=['Django >= 1.5'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    test_suite='runtests.runtests',
)
