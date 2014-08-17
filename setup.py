from setuptools import setup

import banana.caching


setup(
    name='banana-cache-machine',
    version=banana.caching.__version__,
    description='Automatic caching and invalidation for Django models '
                'through the ORM. '
                'Fork from django-cache-machine, we have bulk_insert return ids.',
    author='Emiliano Dalla Verde Marcozzi',
    author_email='edvm@fedoraproject.org',
    url='https://github.com/BananaDesk/banana-cache-machine.git',
    license='BSD',
    packages=['banana.caching',],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
