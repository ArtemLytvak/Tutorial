from setuptools import setup
setup(name='clean',
      version='0.0.1',
      description='Code to sort folders',
      url='http://github.com/clean',
      author='Artem',
      author_email='artem@artem.com',
      license='MIT',
      entry_points={'console_scripts':[ 'clean-folder = clean_folder.Clean:main']}
      )