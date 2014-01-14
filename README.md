About
=====
I discovered that some clients' images were mysteriously rotating 90 or 270 degrees after uploading them to their website.  The file would display correctly in Photoshop, but would be rotated incorrectly once uploaded.

To add to the weirdness, if you re-downloaded the image and opened it in Photoshop -- _it looked correct!_

To be honest, I'm not sure what exactly causes this.  There's a piece of EXIF data, "Image Orientation" that somehow gets set, and somehow causes PIL to show the image incorrectly (or perhaps correctly, depending on your view).

This patch simply looks at the EXIF data and re-rotates it to undo the "Image Orientation" tag.  *It doesn't modify the EXIF data*.  In fact, some quick tests reveal most EXIF data will be lost once running the script (which is not a concern of mine at the moment).

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


License
=======

The MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.