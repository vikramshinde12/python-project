import setuptools

with open("README.rst", "r") as file:
    long_description = file.read()

setuptools.setup(
    name="python-project-vik",
    version="1.1.1",
    author="Vikram Shinde",
    author_email="vik.shinde@gmail.com",
    description="Python project for testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vikramshinde12/python-project",
    packages=setuptools.find_packages(exclude=["tests*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
    ],
    python_requires=">=3.7",
    include_package_data=True,
    install_requires=[],
)
