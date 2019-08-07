from setuptools import setup

setup(
    name = 'pv',
    version = '0.1',
    py_modules = ['pv'],#nombre del modulo
    install_requires=[
        'Click', # indica que necesita libreria click
    ],
    entry_points='''
        [console_scripts]
        pv=pv:cli
    ''',
)
