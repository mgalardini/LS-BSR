#!/usr/bin/env python
from distutils.core import setup
import re

__author__ = "Jason Sahl"
__credits__ = ["Jason Sahl"]
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Jason Sahl"
__email__ = "jsahl@tgen.org"
__status__ = "Development"
 
long_description = """Large scale blast score ratio (LS-BSR)
LS-BSR is a method to compare open reading frames betweeen
a set of bacterial isolates.  The result of the script is a
matrix that can be easily parsed to compare the genetic content
between groups
"""

setup(name='LS-BSR',
      version=__version__,
      description='Large scale blast score ratio',
      author=__maintainer__,
      author_email=__email__,
      maintainer=__maintainer__,
      maintainer_email=__email__,
      packages=['ls_bsr'],
      long_description=long_description
)
