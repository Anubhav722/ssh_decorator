from distutils.core import setup
setup(
  name = 'ssh_decorate',
  packages = ['ssh_decorate'],
  install_requires=[
          'pandas',
          'paramiko',
  ],
  version = '0.3',
  python_requires='>=2.7',
  description = 'Run python code via ssh with a decorator',
  author = 'Uri Goren',
  author_email = 'uri@goren4u.com',
  url = 'https://github.com/urigoren/ssh_decorator',
  download_url = 'https://github.com/urigoren/ssh_decorator/archive/0.1.tar.gz',
  keywords = ['decorator', 'jupyter', 'ssh'],
  classifiers = [],
)
