from setuptools import setup, find_packages
import os

version = '0.1'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='imio.dms.policy',
      version=version,
      description="DMS policy",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['imio', 'imio.dms'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Plone',
          'Pillow',
          'imio.dms.mail',
          'Products.DocFinderTab',
          'Products.csvreplicata',
          'collective.ckeditor',
          'collective.z3cform.rolefield',
          'communesplone.iconified_document_actions',
          'plonetheme.imioapps',
          'five.z2monitor',
          'Products.ZNagios',
          'zc.z3monitor'
      ])
