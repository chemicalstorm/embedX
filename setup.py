from setuptools import setup, find_packages
from codecs import open
from os import path

# Load the README.md to `long_description`
here = path.abspath(path.dirname(__file__))
try:
    from pypandoc import convert
    long_description = convert('README.md', 'rst')
except(OSError, IOError, ImportError):
    with open(path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()

setup(
        name='embedx',
        packages=find_packages(),
        version='0.0.4',
        url='https://github.com/kmonsoor/embedX',
        license='MIT',
        author='Khaled Monsoor',
        author_email='k@kmonsoor.com',
        description='Generate responsive, embeddable HTML/JS code from URL of online content',
        keywords=['embed', 'html', 'javascript', 'embeddable', 'code generation', 'from url'],
        platforms='any',
        long_description=long_description,
        install_requires=[],
        classifiers=[
            'Development Status :: 3 - Alpha',
            'Programming Language :: Python',
            'Environment :: Console',
            'Environment :: Web Environment',
            'Intended Audience :: Developers',
            'Operating System :: OS Independent',
            'License :: OSI Approved :: MIT License',
            'Topic :: Utilities'
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
            'Topic :: Software Development :: Libraries :: Python Modules'
        ],
)
