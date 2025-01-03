from setuptools import setup, find_packages

setup(
    name="empty",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,  # This line ensures data files are included
    install_requires=[],
)
