from setuptools import setup, find_packages

setup(
    name='WASEngine',
    version='1.0.0',
    description='Blizzard API Simulation Engine for Lua Addons',
    author='Your Name',
    packages=find_packages(),
    install_requires=[
        'lupa',
        'gdown'
    ],
    python_requires='>=3.9'
)