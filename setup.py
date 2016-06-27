from setuptools import setup, find_packages

__author__ = "Knights Lab"
__copyright__ = "Copyright (c) 2016--, %s" % __author__
__credits__ = ["Gabe Al-Ghalith", "Benjamin Hillmann", "Tonya Ward", "Pajua Vangay", "Dan Knights"]
__email__ = "hillmannben@gmail.com"
__license__ = "GPL"
__maintainer__ = "Benjamin Hillmann"
__version__ = "0.0.1-dev"

long_description = ''

setup(
    name='ninja_ops',
    version=__version__,
    packages=find_packages(),
    url='',
    license=__license__,
    author=__author__,
    author_email=__email__,
    description='',
    long_description=long_description,
    # scripts=glob(os.path.join('scripts', '*py')),
    keywords='',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ninja_ops' = 'ninja_ops.scripts:main',
        ]
    },
)