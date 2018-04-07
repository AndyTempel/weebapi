Image generation
==================

This module represents the image generation interface.

.. note::
    All images retrieved with this module are placed in system default temporary folder. If the system doesn't
    have a temporary folder images are placed in a current directory. **Please note that you should practice
    file deletion after usage.**


Image file object
-------------------

To simplify file manipulation here is a :class:`weebapi.data_objects.ImageFile` object.
This also integrates nicely with discord.py

.. note::
    By accessing the ``discord_file`` property you can get :class:`discord.File` object.

.. autoclass:: weebapi.data_objects.ImageFile
    :members:

Generators
-----------

Here is the list and the description of all available generators.

.. note::
    Thus this is represented as a separate class, it's loaded automatically into the :class:`weebapi.Client`.
    If we assume that your client object is ``weeb = Client(token="SomeToken123")`` then you access simple
    image generator like this: ``generator = await weeb.img_gen.get_simple("won")``.

.. autoclass:: weebapi.img_gen.ImgGen
    :members:
