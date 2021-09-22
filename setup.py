import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="previewlink",
    version="0.0.1",
    author="SREEHARI K V",
    author_email="sreeharivijayan619@gmail.com",
    description="Get the preview of a website",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "requests>=2.22.0",
        "beautifulsoup4>=4.4.0"
    ],
    url="https://github.com/sreehari1997/link-preview/",
    project_urls={
        "Bug Tracker": "https://github.com/sreehari1997/link-preview/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)