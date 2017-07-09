# -*- coding: utf-8 -*-


try:
    from setuptools     import setup
except ImportError:
    from distutils.core import setup


setup(

    name = 'jsntlib',

    version = '1.0.2',

    description = 'Number theory library.',

    long_description =
        'A number theory library adapted from mathematic fundamentals of information security homework codes.',

    author = 'Jarry Shaw',

    author_email = 'jarryshaw@icloud.com',

    url = 'https://github.com/JarryShaw/jsntlib/tree/release',

    download_url = 'https://github.com/JarryShaw/jsntlib/archive/1.0.0.tar.gz',

    packages = [
        'jsntlib',
        'jsntlib.NTLArchive',
        'jsntlib.NTLArchive.__abc__',
    ],

    classifiers = [
        'Development Status :: 5 - Production/Stable',

        'Environment :: Console',
        'Environment :: MacOS X',
        'Environment :: Win32 (MS Windows)',

        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Natural Language :: Chinese (Traditional)',
        'Natural Language :: English',

        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',

        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',

        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Security',
        'Topic :: Utilities',
    ],

    license = 'LICENSE.txt',

    keywords = [
        'ntl',
        'number-theory',
        'mathematic-fundamentals',
    ],

    platforms = ['macOS', 'Windows', 'Linux', 'Unix',],

)
