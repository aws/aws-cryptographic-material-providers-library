####################################################
aws-cryptographic-materials-providers-library-python
####################################################

.. image:: https://github.com/aws/aws-cryptographic-material-providers-library/actions/workflows/push.yml/badge.svg
   :target: https://github.com/aws/aws-cryptographic-material-providers-library/actions/workflows/push.yml
   :alt: MPL-python-tests

.. image:: https://img.shields.io/badge/code_style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Code style: black

.. image:: https://readthedocs.org/projects/aws-cryptographic-material-providers-library/badge/
   :target: https://aws-cryptographic-material-providers-library.readthedocs.io/en/latest/
   :alt: Documentation Status

These are the docs for the AWS Cryptographic Materials Providers Library for Python.

The latest full documentation can be found at `Read the Docs`_.

Find us on `GitHub`_.

Security
********

If you discover a potential security issue in this project
we ask that you notify AWS/Amazon Security via our
`vulnerability reporting page`_.
Please **do not** create a public GitHub issue.

***************
Getting Started
***************
Required Prerequisites
======================

* Python 3.11+
* cryptography >= 43.0.1
* boto3 >= 1.35.42

Installation
============

.. note::

   If you have not already installed `cryptography`_, you might need to install additional prerequisites as
   detailed in the `cryptography installation guide`_ for your operating system.

   .. code::

       $ pip install aws-cryptographic-material-providers


Concepts
========
The AWS Cryptographic Materials Providers Library (MPL) is available in multiple languages.
The concepts in the Python implementation of the MPL are the same as in other languages.
For more information on concepts in the MPL, see the `README`_ for all languages.

*************
Thread safety
*************

The ``MaterialProviders`` client and all provided ``CryptoMaterialsManagers`` (CMMs) are thread safe.
But keyrings that call AWS Key Management Service (KMS) and CMMs that use keyrings that call KMS MUST not be shared between threads, for reasons outlined in `the boto3 docs`_.

(Keyrings that call KMS are identified by the string ``Kms`` in their name. ex. ``AwsKmsKeyring``, ``AwsKmsMrkDiscoveryMultiKeyring``, etc.)

Finally, while the provided implementations of ``ICryptographicMaterialsCache`` are thread-safe,
there is currently no thread-safe keyring implementation that supports using a cache.

.. _cryptography: https://cryptography.io/en/latest/
.. _cryptography installation guide: https://cryptography.io/en/latest/installation/
.. _Read the Docs: https://aws-cryptographic-material-providers-library.readthedocs.io/en/latest/
.. _GitHub: https://github.com/aws/aws-cryptographic-material-providers-library
.. _vulnerability reporting page : http://aws.amazon.com/security/vulnerability-reporting/
.. _the boto3 docs: https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html#multithreading-or-multiprocessing-with-resources
.. _README: https://github.com/aws/aws-cryptographic-material-providers-library/blob/main/README.md