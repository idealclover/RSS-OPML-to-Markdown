import setuptools
import RSS_OPML_to_Markdown

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="RSS-OPML-to-Markdown",
    version="0.0.7",
    author="idealclover",
    author_email="shadowspacex@163.com",
    description="Convert RSS OPML file to Markdown - easy to read and share",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/idealclover/RSS-OPML-to-Markdown",
    packages=setuptools.find_packages(),
    install_requires=[
        'listparser',
        'tabulate'
    ],
    entry_points={
        'console_scripts': [
            'RSS_OPML_to_Markdown = RSS_OPML_to_Markdown.RSS_OPML_to_Markdown:main'
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)