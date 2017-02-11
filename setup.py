from setuptools import setup, find_packages

# makes __version__ a local variable
exec(open('attrs_utils/_version.py').read())
# http://python-packaging.readthedocs.org/en/latest/command-line-scripts.html

setup(name='attrs_utils',
      version=__version__,
      packages=find_packages(),
      url='https://github.com/gvoysey/attrs-utils',
      license='MIT',
      author='Graham Voysey',
      author_email='gvoysey@bu.edu',
      description='A collection of commonly used validators for the attrs package',
      install_requires=[
          'docopt >= 0.6',
          'attrs >=16.3.0',
      ],
      tests_require=[
          'pytest',
          'hypothesis'
      ],
      test_suite="py.test")
