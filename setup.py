import setuptools

with open("README.md", "r") as file:
    long_description=file.read()

setuptools.setup(
    name="python-project",
    version="1.0.0",
    author="Vikram Shinde",
    author_email="vik.shinde@gmail.com",
    description="Python project for testing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vikramshinde12/python-project",
    packages=setuptools.find_packages(exclude=['tests*']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires='>=2.7',
    include_package_data=True,
    install_requires=[]
)