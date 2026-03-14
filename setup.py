from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setuptools.setup(
    name="ziko-st-toc",
    version="0.4.1",
    author="zakaria elalaoui",
    author_email="zakarialaoui10@gmail.com",
    description="Zikojs based Interactive Table of Contents component for Streamlit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ziko-st-toc.streamlit.app/",
    packages=setuptools.find_packages(),
    include_package_data=True,
    license_files=("LICENSE"),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Framework :: Streamlit",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
    ],
    keywords="streamlit table-of-contents toc navigation zikojs",
    project_urls={
        "Source": "https://github.com/zakarialaoui10/ziko-st-toc",
        "Tracker": "https://github.com/zakarialaoui10/ziko-st-toc/issues",
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
