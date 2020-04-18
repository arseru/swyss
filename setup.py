"""More info on https://setuptools.readthedocs.io/en/latest/setuptools.html"""

from os import path

from setuptools import setup

from swyss import __version__


def setup_pkg():
    # Get the long description from the README file
    root_dir = path.abspath(path.dirname(__file__))
    with open(path.join(root_dir, "README.md"), encoding="utf-8") as f:
        readme = f.read()

    setup(
        name="swyss",
        author="Arnau",
        author_email="arseru@protonmail.com",
        # https://packaging.python.org/en/latest/single_source_version.html
        version=__version__,
        description="Multiconverter file tool written in Python",
        long_description=readme,
        long_description_content_type="text/markdown",
        url="https://github.com/arseru/swyss",
        project_urls={
            "Bug Tracker": "https://gitlab.com/arseru/swyss/issues",
            "Documentation": "https://gitlab.com/arseru/swyss/wikis"
        },
        license="GPL3",

        # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
        classifiers=[
            # How mature is this project? Common values are
            #   3 - Alpha
            #   4 - Beta
            #   5 - Production/Stable
            "Development Status :: 3 - Alpha",

            # Indicate who your project is intended for
            "Intended Audience :: Developers",
            "Topic :: Software Development :: Libraries",

            # Pick your license as you wish (should match "license" above)
            "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

            # Specify the Python versions you support here. In particular,
            # ensure that you indicate whether you support Python 2, Python 3
            # or both
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.3",
            "Programming Language :: Python :: 3.4",
            "Programming Language :: Python :: 3.5",
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
        ],

        # What does your project relate to?
        keywords="pandas converter xlsx json yaml csv odt",

        # You can just specify the packages manually here if your project is
        # simple. Or you can use find_packages().
        packages=["swyss"],

        # Specify the Python versions supported
        python_requires=" >= 3.3",

        # List run-time dependencies here.  These will be installed by pip when
        # your project is installed. For an analysis of "install_requires" vs
        # pip's requirements files see:
        # https://packaging.python.org/en/latest/requirements.html
        install_requires=[
            "lxml",  # to read html
            "odfpy",  # to read ods
            "openpyxl",  # to write to xlsx
            "pandas",
            "PyYAML",
            "xlrd",  # to read xls/xlsx
            "xlwt"  # to write to xls
        ],

        # requirements for tests
        tests_require=[
            "pytest"
        ],

        # List additional groups of dependencies here
        extras_require={
            "dev": [],
            "test": [],
        },

        # To provide executable scripts, use entry points in preference to the
        # "scripts" keyword. Entry points provide cross-platform support and
        # allow pip to create the appropriate form of executable for the target
        # platform. More info on:
        # https://setuptools.readthedocs.io/en/latest/setuptools.html#automatic-script-creation
        entry_points={
            "console_scripts": ["swyss = swyss.__main__:main", ],
        },
    )


if __name__ == "__main__":
    setup_pkg()
