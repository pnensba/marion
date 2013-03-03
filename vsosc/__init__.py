__version__ = "0.3"
__author__ = "Daniel Holth, Clinton McChesney, Vincent Rioux"
__license__ = "GNU General Public License"
__all__ = ["OSC", "OSC_interface"]

import platform
PY3 = (platform.python_version_tuple()[0]=='3')

if PY3==True:
    exec("from .OSC_interface import *")
    exec("from .OSC3 import *")
else:
    from OSC_interface import *
    from OSC import *



