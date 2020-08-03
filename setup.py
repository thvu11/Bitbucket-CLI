from setuptools import setup

setup(
    name="bitbucket CLI",
    version="0.1",
    py_modules=["repo"],
    packages=["lib", "lib.bitbucketCLI"],
    include_package_data=True,
    install_requires=["click", "requests"],
    entry_points="""
        [console_scripts]
        bb=lib.bb:cli
    """,
)
