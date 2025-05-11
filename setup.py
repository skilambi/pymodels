
import getpass
from setuptools import setup, find_packages
from setuptools.command.install import install

class GetVersionCommand(install):
    description = "Get the version of this build"

    def run(self):
        print(find_version())


def find_version():
    build_base = "0" 
    build_num = f"0.dev0+{getpass.getuser()}"

    return build_base + f".{build_num}"

setup(
    name="pymodels",
    version=find_version(),
    packages=find_packages(where="."),
    package_dir={"": "."},
    package_data={},
    license="",
    author="Sai Mohan Kilambi",
    author_email="skilambi@gmail.com",
    description="Python Modelling Files",
    long_description="Set of python modelling files.",
    keywords="pymodels",
    python_requires=">=3.12",
    install_requires=[
        "dataclasses",
        "docopt",
        "junitparser",
        "pyyaml",
        "tabulate",
        "termcolor",
        "teamcity-messages",
        "edalize",
        "dohq_teamcity",
        "pydantic",
        "networkx",
        "pytest",
        "scipy",
        "numpy",
        "matplotlib",
        "pandas",
        "seaborn",
        "scikit-learn",
        "statsmodels",

    ],
    cmdclass={"get_version": GetVersionCommand},
)