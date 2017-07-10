
__version__ = [0,1,0,'a1']

version = '.'.join(str(i) for i in __version__)
version_api = '.'.join(str(v).title() for v in __version__[:2])

PYGRID_UI_VERSION='.'.join(str(i) for i in __version__)
PYGRID_UI_MAJOR_VERSION=__version__[0]
PYGRID_UI_MINOR_VERSION=__version__[1]
PYGRID_UI_PATCH_VERSION=__version__[2]
PYGRID_UI_RELEASE_VERSION=__version__[-1]
