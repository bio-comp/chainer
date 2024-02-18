from pathlib import Path
from setuptools import find_namespace_packages, setup

# load libraries from requirements.txt
BASE_DIR = Path(__file__).parent
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

docs_packages = [
    "mypy==1.8.0",
    "mkdocs-material==9.5.9",
    "mkdocstrings-python==1.8.0"
]

style_packages = [
    "black==24.2",
    "flake8==7.0.0",
    "isort==5.13.2"
]

# define the package
setup(
    name="chainer",
    version=0.3,
    description="Lang Chain Example",
    author="Mike Hamilton",
    author_email="mike.hamilton7@gmail.com@gmail.com",
    url="",
    python_requires=">=3.9",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "dev": docs_packages + style_packages,
        "docs": docs_packages,
    },
)
