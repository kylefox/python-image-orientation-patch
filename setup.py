from setuptools import setup

setup(
    name='img_rotate',
    version='0.1',
    description="""Rotates PIL Image instances after EXIF-tagged image orientation""",
    url="https://github.com/kylefox/python-image-orientation-patch",
    author="Kyle Fox",
    author_email="kyle.fox@gmail.com",
    license="MIT",
    packages=['img_rotate'],
    scripts=['bin/img_rotate'],
    zip_safe=False,
)
