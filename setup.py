from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="ziko-st-toc",
    version="2.0.0",
    author="zakaria.elalaloui",
    author_email="zakarialaoui10@gmail.com",
    description="A Streamlit component that generates an interactive Table of Contents (TOC) with smooth scrolling and navigation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ziko-st-toc.netlify.app/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license_files=("LICENSE"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: JavaScript",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing :: Markup :: HTML",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
    ],
    keywords="streamlit table-of-contents toc navigation zikojs",
    project_urls={
        "Source": "https://github.com/zikojs/ziko-st-toc",
        "Tracker": "https://github.com/zikojs/ziko-st-toc/issues",
        "Documentation": "https://ziko-st-toc.streamlit.app/",
    },
    python_requires=">=3.7",
    install_requires=[
        "streamlit >= 0.63",
    ],
    extras_require={
        "devel": [
            "wheel",
            "pytest==7.4.0",
            "playwright==1.48.0",
            "requests==2.31.0",
            "pytest-playwright-snapshot==1.0",
            "pytest-rerunfailures==12.0",
        ]
    }
)
