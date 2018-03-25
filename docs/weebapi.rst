API Reference
===============

The following section outlines the API of weeb.sh.

.. note::

    This module uses the Python logging module to log diagnostic and errors
    in an output independent way.  If the logging module is not configured,
    these logs will not be output anywhere.

Version Related Info
---------------------

There are two main ways to query version information about the library.

.. data:: version_info

    A named tuple that is similar to `sys.version_info`_.

    Just like `sys.version_info`_ the valid values for ``releaselevel`` are
    'alpha', 'beta', 'candidate' and 'final'.

    .. _sys.version_info: https://docs.python.org/3.6/library/sys.html#sys.version_info

.. data:: __version__

    A string representation of the version. e.g. ``'0.1.0-alpha0'``.


Weeb.sh Client
---------------------

.. autoclass:: weebapi.client.Client
    :members:

Data objects
--------------------

Here is the collection of all data objects that this API wrapper uses.

Image
~~~~~~
.. autoclass:: weebapi.data_objects.Image
    :members:

Preview
~~~~~~~~~
.. autoclass:: weebapi.data_objects.Preview
    :members:

ImageType
~~~~~~~~~~
.. autoclass:: weebapi.data_objects.ImageType
    :members:

Tag
~~~~~~~~
.. autoclass:: weebapi.data_objects.Tag
    :members:
