from setuptools import setup


setup(
    name="dqa",
    version="1.1",
    packages=find_packages(),
    install_requires=["pygame==2.5.0", "requests==2.28.2", "Flask==2.3.2", "gTTS==2.3.2"]

)
