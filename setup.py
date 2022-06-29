from setuptools import setup
import sys

# note: this check is not technically required as imports default to standard libraries where available, but it
# ensures that we cannot cause any adverse effects where existing code is somehow reliant on behaviours of the
# standard library asynchat module that are different to the one provided here
packages = []
if sys.version_info[0] == 3 and sys.version_info[1] >= 12:
    packages.append('asyncore')
    packages.append('asynchat')

python_classifiers = ['Programming Language :: Python :: %s' % version for version in ['3.12']]

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='pyasynchat',
    version='1.0.0',
    description='Make asynchat available for Python 3.12 onwards',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Simon Robinson',
    author_email='simon@robinson.ac',
    url='https://github.com/simonrob/pyasynchat',

    platforms='any',
    packages=packages,

    license='Python Software Foundation License Version 2',
    classifiers=['Development Status :: 5 - Production/Stable',
                 'License :: OSI Approved :: Python Software Foundation License'] + python_classifiers,
)
