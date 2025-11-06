"""
Typhoon-Core: Multi-Domain Adaptive Optimization Engine
Copyright (c) 2025 Nicolas E. Santiago, Safeway Guardian

SAFEWAY GUARDIAN | Nicolas E. Santiago | Saitama, Japan | Nov. 6, 2025
Powered by DEEPSEEK AI
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="typhoon-core",
    version="1.0.0",
    author="Nicolas E. Santiago",
    author_email="nicolas.santiago@safeway-guardian.jp",
    description="Multi-Domain Adaptive Optimization Engine Inspired by Typhoon Formation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SG/python-core",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.21.0",
        "pandas>=1.3.0", 
        "scikit-learn>=1.0.0",
    ],
)
