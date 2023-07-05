#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='cobaltspeech',
    python_requires='>=3.5.0',
    version='1.0.0',
    description="Auto-generated python clients for Cobalt's gRPC APIs.",
    author='Cobalt Speech and Language Inc.',
    maintainer_email='tech@cobaltspeech.com',
    url='https://docs-v2.cobaltspeech.com/',
    packages=find_packages(include=["cobaltspeech", "cobaltspeech.*"]),
    install_requires=[
        'protobuf==4.22.1',
        'grpcio==1.53.0',
        'google-api-python-client==2.81.0'
    ]
)
