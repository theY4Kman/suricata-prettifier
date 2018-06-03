from setuptools import setup

setup(
    name='suricata-prettifier',
    version='0.0.3',
    packages=['suricata_prettifier'],
    url='https://github.com/theY4Kman/suricata-prettifier',
    license='BSD 2-Clause',
    author='Zach "theY4Kman" Kanzler',
    author_email='they4kman@gmail.com',
    install_requires=list(open('requirements.txt')),
    description='Format and syntax highlight Suricata rules',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    entry_points='''
        [console_scripts]
        prettify-suricata=suricata_prettifier.main:prettify
    ''',
)
