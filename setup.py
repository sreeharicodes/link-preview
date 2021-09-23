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
    keywords='link preview, preview link, preview url',
    long_description_content_type="text/markdown",
    install_requires=[
        "requests>=2.22.0",
        "beautifulsoup4>=4.4.0"
    ],
    extras_require={
        "dev": {
            "pytest==6.2.5",
            "pytest-cov==2.12.1",
            "pytest-httpserver==1.0.1"
        }
    },
    url="https://github.com/sreehari1997/link-preview/",
    project_urls={
        "Bug Tracker": "https://github.com/sreehari1997/link-preview/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)