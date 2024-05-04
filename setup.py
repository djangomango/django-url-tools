from setuptools import setup


with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='django-url-tools',
    version='0.1',
    author='buswedg',
    author_email='buswedg@djangomango.com',
    url='https://github.com/djangomango/django-url-tools/',
    license='GNU Lesser General Public License v3 (LGPLv3)',
    description='Package provides a set of url tools for Django.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
    python_requires='>=3'
)