import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fb_ad_analysis",
    version="0.0.1",
    author="Robert Tykocki-Crow",
    author_email="r.tykocki.crow@gmail.com",
    description="Package for analyzing Facebook ad library entries",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robertcrow/fb_ad_analysis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
