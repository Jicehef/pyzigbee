from setuptools import setup

setup(
    name = 'pyzigbee',
    version = '0.1.0',

    description = 'pyzigbee is a python library that lets you to talk to Legrand zigbee devices through gateways',
    long_description = open("README.md").read(),

    author = 'Pierre Roth',
    author_email = 'pierre.roth@legrand.fr',
    url = 'https://github.com/pierreroth/pyzigbee',
    license = 'MIT License',

    packages = [
        'pyzigbee'
    ],

    install_requires = [
        "pyserial",
    ],

    extras_require = {
        'windows': [
            'colorama'
        ],
        'colored_logs': [
            'colorlog'
        ]
    },

    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
)
