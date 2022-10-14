import setuptools
import os
from pathlib import Path

module_path = Path(os.path.abspath(__file__)).parent.absolute()

ver = {}
with open(module_path.joinpath('version.py')) as ver_file:
    exec(ver_file.read(), ver)

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="empty",
    version=ver['__version__'],
    author="Kwang Eun Jang",
    author_email="kejang@stanford.edu",
    description="Bare-bones Python package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kejang/empty",
    project_urls={
        "Bug Tracker": "https://github.com/kejang/empty/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(where="."),
    python_requires=">=3.7",
    install_requires=[
    ],
    include_package_data=True
)
