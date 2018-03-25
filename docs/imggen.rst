Image generation
==================

This module represents the image generation interface.

.. note::
    All images retrieved with this module are placed in system default temporary folder. If the system doesn't
    have a temporary folder images are placed in a current directory. **Please note that you should practice
    file deletion after usage.**

Image generators
-------------------

Here is a collection of all available image generators.

.. note::
    Currently work in progress.

Image file object
-------------------

To simplify file manipulation here is a :class:`weebapi.data_objects.ImageFile` object.
This also integrates nicely with discord.py

.. note::
    By accessing the ``discord_file`` property you can get :class:`discord.File` object.

.. autoclass:: weebapi.data_objects.ImageFile
    :members:
