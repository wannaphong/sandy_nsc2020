# -*- coding: utf-8 -*-

from setuptools import find_packages, setup
with open("README.md", "r", encoding="utf-8") as readme_file:
    readme = readme_file.read()

requirements = ['pyaudio','webrtcvad']

setup(
    name="pyvadrun",
    version="0.1",
    description="VAD",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="thainlp",
    packages=find_packages(),
    package_data={},
    url="https://github.com/wannaphong/pyvadrun",
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords="thainlp",
    test_suite="tests",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Text Processing :: Linguistic",
    ],
)
