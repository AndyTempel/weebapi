import re

from setuptools import setup


def get_requirements():
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


version = ''
with open('weebapi/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('Version is not set')

readme = ''
with open('README.md') as f:
    readme = f.read()

print(readme)
setup(
    name='weebapi',
    packages=['weebapi'],
    version=version,
    description='Weeb.sh API Wrapper, customised for use in discord.py',
    long_description=str(readme),
    author='AndyTempel',
    author_email='andraz@korenc.eu',
    url='https://github.com/AndyTempel/weebapi',
    download_url=f'https://github.com/AndyTempel/weebapi/archive/{version}.tar.gz',
    keywords=['weebapi'],
    include_package_data=True,
    install_requires=get_requirements(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities',
    ]
)
