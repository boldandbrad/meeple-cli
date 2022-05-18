from setuptools import setup, find_packages

# parse version number from makey/__init__.py:
with open("bgg/__init__.py") as f:
    info = {}
    for line in f.readlines():
        if line.startswith("version"):
            exec(line, info)
            break

setup_info = dict(
    name="bgg-cli",
    version=info["version"],
    author="Bradley Wojcik",
    author_email="bradleycwojcik@gmail.com",
    license="MIT",
    description="boardgamegeek cli",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://boldandbrad.github.io/bgg-cli/",
    project_urls={
        "Source": "https://github.com/boldandbrad/bgg-cli/",
        "Bug Tracker": "https://github.com/boldandbrad/bgg-cli/issues",
    },
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click>=8", "xmltodict>=0.12.0", "requests>=2"],
    extras_require={
        "dev": [
            "black",
            "pytest",
            "pytest-cov",
            "pytest-mock",
            "codecov",
            "homebrew-pypi-poet",
        ]
    },
    python_requires=">=3.8",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points="""
        [console_scripts]
        bgg=bgg.bgg:cli
    """,
)

setup(**setup_info)
