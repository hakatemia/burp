from setuptools import setup
description = "Burp interface with typing hints"

setup(
    name='burp',
    version='1.00',
    packages=['burp'],
    url='https://github.com/hakatemia/burp',
    license='MIT',
    description='Annotated burp interfaces for python/jython',
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: Jython',
        'Intended Audience :: Developers',
    ]
)
