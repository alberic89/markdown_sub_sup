
from setuptools import setup
from pathlib import Path

setup(
    name="markdown_sub_sup",
    version="0.0.1",
    license="LGPLv3",
    url="https://github.com/alberic89/markdown_sub_sup",
    description="A markdown python extension for use <sub> and <sup> tags with ^text^ and ~text~.",
    author="alberic89",
    author_email="alberic89@gmx.com",
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    py_modules=['markdown_sub_sup'],
    install_requires=['markdown>=3.0'],
    classifiers=[
        'Operating System :: OS Independent',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)