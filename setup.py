from setuptools import find_packages
from setuptools import setup


version = "4.0.0.dev0"

long_description = (
    open("README.txt").read() + "\n" + "Contributors\n"
    "============\n" + "\n" + open("CONTRIBUTORS.txt").read() + "\n" + open("CHANGES.txt").read() + "\n"
)

setup(
    name="imio.dms.policy",
    version=version,
    description="DMS policy containing all packages required for dms to work",
    long_description=long_description,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="Plone Python IMIO",
    author="IMIO",
    author_email="support@imio.be",
    url="https://github.com/IMIO/imio.dms.policy",
    license="gpl",
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "Plone",
        "Pillow",
        "imio.dms.mail",
        "imio.pyutils",
        "Products.CPUtils",
        "collective.behavior.internalnumber",
        "collective.contact.importexport",
        "collective.externaleditor",
        "collective.messagesviewlet",
        "communesplone.layout",
        "imio.transmogrifier.contact",
        "imio.transmogrifier.iadocs",
        "plonetheme.imioapps",
    ],
    extras_require={
        "test": [
            "plone.app.testing",
        ],
    },
)
