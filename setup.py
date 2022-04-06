import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="gen-pygments-css",
    version="0.0.3",
    description="Generate CSS stylesheets for each Pygments supported style.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/hreikin/gen-pygments-css",
    author="hreikin",
    author_email="hreikin@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["gen_pygments_css"],
    include_package_data=True,
    install_requires=["pygments"],
    entry_points={
        "console_scripts": [
            "gen_pygments_css=gen_pygments_css.__main__:main",
        ]
    },
)
