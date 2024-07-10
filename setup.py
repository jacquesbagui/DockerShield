from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dockershield",
    version="0.1.0",
    author="Jean Jacques BAGUI",
    author_email="jacques.bagui@gmail.com",
    description="Un outil d'audit de sécurité pour conteneurs Docker",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jacquesbagui/DockerShield.git",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.7",
    install_requires=[
        "docker>=6.1.3",
        "yara-python>=4.3.1",
        "psutil>=5.9.5",
        "requests>=2.31.0",
        "jinja2>=3.1.2",
        "PyYAML>=6.0.1",
    ],
    entry_points={
        "console_scripts": [
            'dockershield=src.docker_shield:main',
        ],
    },
    include_package_data=True,
    package_data={
        "dockershield": ["config/*.yaml", "data/**/*"],
    },
)