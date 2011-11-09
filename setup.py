try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

#
# determine requirements
#
requirements = [
  "guachi"
]

setup(
    name                    = "dozo",
    version                 = "0.0.1",
    include_package_data    = True,
                            
    # metadata              
    author                  = "John Montero",
    author_email            = "jmonteroc [at] gmail [dot] com",
    description             = "Run commands",
    long_description        = open('README.rst').read(),
    packages                = find_packages(exclude=['ez_setup', 'tests']),
    classifiers             = [
        'Development Status :: 1 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Topic :: System :: Distributed Computing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    license                 = "BSD",
    keywords                = "command, run",
    url                     = "https://github.com/johnmontero/dozo",
                            
    install_requires        = requirements,
    entry_points            =  {
        'console_scripts': [
            'dozo = dozo:main'
            ]
        },

)