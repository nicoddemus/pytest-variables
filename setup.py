from setuptools import setup

setup(name='pytest-variables',
      version='1.0',
      description='pytest plugin for providing variables to tests/fixtures',
      long_description=open('README.rst').read(),
      author='Dave Hunt',
      author_email='dhunt@mozilla.com',
      url='https://github.com/davehunt/pytest-variables',
      py_modules=['pytest_variables'],
      entry_points={'pytest11': ['variables = pytest_variables']},
      install_requires=['pytest>=2.3'],
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest json variables',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7'])
