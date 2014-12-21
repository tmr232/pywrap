import os

from setuptools import setup

def read(*paths):
    """Build a file path from *paths* and return the contents."""
    with open(os.path.join(*paths), 'r') as f:
        return f.read()

setup(
    name='pywrap',
    version='0.1.0',
    py_modules=['pywrap'],
    url='https://github.com/tmr232/pywrap',
    license='MIT',
    author='Tamir Bahar',
    author_email='',
    description='Ctypes made easy.',
    long_description=(read('README.rst')),
)
