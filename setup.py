from setuptools import setup, find_packages

setup(
    name='ProTester',
    version='0.1.0',  # Replace with your desired version
    packages=find_packages(exclude=['tests*']),  # Automatically find packages
    install_requires=[],  # List any dependencies here
    # ... other metadata like author, description, etc. ...
)
