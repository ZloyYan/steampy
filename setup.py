from setuptools import setup, find_packages
import sys

if not sys.version_info[0] == 3 and sys.version_info[1] < 8:
    sys.exit('Python < 3.8 is not supported')

version = '1.1.3'

setup(
    name='steampy',
    packages=find_packages(),
    version=version,
    description='A Steam lib for trade automation',
    author='Michał Bukowski',
    author_email='gigibukson@gmail.com',
    license='MIT',
    url='https://github.com/ZloyYan/steampy',
    download_url='https://github.com/ZloyYan/steampy/tarball/' + version,
    keywords=['steam', 'trade'],
    classifiers=[],
    install_requires=[
        "requests",
        "beautifulsoup4",
        "rsa"
    ],
)
