from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="news-google-api",
    version="0.1.5",
    author="Amos Maru",
    author_email="amosmaru10@gmail.com",
    description="A Python library to fetch and parse Google News feeds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AmosMaru/googlenews",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "feedparser",
        "beautifulsoup4",
        "requests",
        "dateparser",
    ],
    entry_points={
        "console_scripts": [
            "googlenews=googlenews.cli:main"
        ]
    }
)