from setuptools import setup

setup (
  name = 'rhine',
  version = '1.0.1',
  description = 'Rhine Python Client',
  long_description = 'For documentation, please see [http://www.rhine.io/docs].',
  url = 'https://github.com/Speare/rhine-python',
  license = 'New BSD',
  author = 'Speare Inc.',
  author_email = 'admin@rhine.io',
  packages = ['rhine'],
  package_dir = {'rhine': 'rhine'},
  include_package_data = True,
  install_requires = ['requests'],
  classifiers = [
    'Intended Audience :: Developers',
    'Natural Language :: English',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3'
  ]
)
