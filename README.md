About
=====
I discovered that some clients' images were mysteriously rotating 90 or 270 degrees after uploading them to their website.  The file would display correctly in Photoshop, but would be rotated incorrectly once uploaded.

To add to the weirdness, if you re-downloaded the image and opened it in Photoshop -- _it looked correct!_

To be honest, I'm not sure what exactly causes this.  There's a piece of EXIF data, "Image Orientation" that somehow gets set, and somehow causes PIL to show the image incorrectly (or perhaps correctly, depending on your view).

This patch simply looks at the EXIF data and re-rotates it to undo the "Image Orientation" tag.  *It doesn't modify the EXIF data*.  In fact, some quick test reveal that most EXIF data will be lost once running this script (which is not a concern of mine at the moment).

Command-line Use
================
The simplest way to use this script is from the command line, passing in the filename of the image to fix:

    >>> python img_rotate.py messed_up.jpg
    messed_up.jpg was rotated -90 degrees.
    
Using in your own scripts
=========================
The script basically consists of a single function, `fix_orientation`:

    fix_orientation(img, save_over=False)
    
Parameters
----------
* `img` : can be an Image instance or a path to an image file.
* `save_over` : indicates if the original image file should be replaced by the new image (only possible when `img` is a file path).

Return value
------------
`fix_orientation` returns a tuple in the format `(img, degrees_rotated)`.

* `img` will be the corrected Image instance.
* `degrees_rotated` is the number of degrees rotated(!).  Positive values indicate clockwise, negative indicates counter-clockwise.  `0` is returned if no rotation took place.

That's it!

**Questions or Bugs?** [Send me a message](http://github.com/inbox/new/kylefox) via github.