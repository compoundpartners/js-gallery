# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from aldryn_gallery import __version__

REQUIREMENTS = [
    'djangocms_text_ckeditor>=2.1.2',
    'django-filer',
    'easy_thumbnails',
    'aldryn-boilerplates>=0.6',
]

CLASSIFIERS = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

setup(
    name='js-gallery',
    version=__version__,
    description='Gallery',
    author='Compound Partners Ltd',
    author_email='hello@compoundpartners.co.uk',
    url='https://github.com/compoundpartners/js-gallery',
    packages=find_packages(),
    license='LICENSE.txt',
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False
)
