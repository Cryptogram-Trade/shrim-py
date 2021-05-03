import setuptools

install_requires = [
    "requests>=2.25.1"
]

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="shrim-py",
    version="0.0.2",
    author="Cryptogram Trade",
    author_email="dev@cryptogram.trade",
    description="The Better Shrimpy Python Client for Dev and User APIs",
    license="GNU",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Cryptogram-Trade/shrim-py",
    install_requires=install_requires,
    packages=["shrimpy"],
    python_requires=">=3.6",
    keywords=[
        "shrimpy", "social", "bitcoin", "client", "api",
        "exchange", "crypto", "currency", "trading",
        "ETH", "BTC", "3commas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
)
