from setuptools import setup
from setuptools_rust import Binding, RustExtension
from setuptools import find_packages

setup(
    name="symspell_rust",
    version="0.2.0",
    description="Fast and Accurate SpellChecker",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    keywords="Symspell Spellchecker rust python_bind PyO3",
    author="zoho-labs",
    url="https://github.com/zoho-labs/symspell",
    rust_extensions=[RustExtension("symspell_rust.symspell_rust", binding=Binding.PyO3)],
    packages=[
            "symspell_rust"
    ],
    zip_safe=False,
)