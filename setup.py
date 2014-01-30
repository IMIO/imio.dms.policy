from setuptools import setup, find_packages

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
      description="DMS policy containing all packages required for dms to work",
      long_description=long_description,
      classifiers=[
          "Programming Language :: Python",
      ],
      keywords='',
      author='IMIO',
      author_email='support@imio.be',
      url='http://svn.communesplone.org/svn/communesplone/imio.dms.policy',
      license='gpl',
      packages=find_packages('src'),
      package_dir={'': 'src'},
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
