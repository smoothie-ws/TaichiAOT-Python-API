import os
import sys
from ctypes import CDLL

from ._bindings import TAICHI_C_API_METHODS
from .exceptions import *


class C_API(object):
    """
    Primary C_API class used for fundamental handling of
    the Taichi C API.
    """

    _native_supported_platforms = ['linux', 'linux2', 'darwin', 'win32']

    def __init__(self, supported_platforms=None) -> None:
        if supported_platforms is None:
            supported_platforms = []

        self._supported_platforms = supported_platforms
        self._loaded = False
        self._cdll = None

        self._initialize()

    def __getattr__(self, name):
        if name.startswith('__') and name.endswith('__'):
            raise TaichiMethodNotFound(f"{name} method not found.")

        func = self.__getitem__(name)
        setattr(self, name, func)

        return func

    def _initialize(self) -> bool:
        """Initialize module by loading C API library

        :return: bool
        """

        platform = sys.platform

        if (self._supported_platforms and
                platform not in self._supported_platforms):
            raise UnsupportedPlatformException(
                f'"{platform}" has been excluded')

        if platform not in C_API._native_supported_platforms:
            raise UnsupportedPlatformException(
                f'"{platform}" is not being supported')

        if platform in ['linux', 'linux2']:
            library_file_name = 'libtaichi_c_api.so'

        elif platform == 'darwin':
            library_file_name = 'libtaichi_c_api.dylib'

        elif platform == 'win32':
            library_file_name = 'taichi_c_api.dll'

        else:
            # This case is theoretically unreachable
            raise UnsupportedPlatformException(
                f'"{platform}" is not being supported')

        if os.path.isfile(os.path.join(os.getcwd(), library_file_name)):
            library_path = os.path.join(os.getcwd(), library_file_name)

        elif os.path.isfile(
                os.path.join(os.path.dirname(__file__), library_file_name)):
            library_path = os.path.join(os.path.dirname(__file__),
                                        library_file_name)

        else:
            raise MissingTaichiLibraryException(
                f'Missing library {library_file_name}')

        self._cdll = CDLL(library_path)
        self._loaded = True

        self._load_taichi_c_api()
        return self._loaded

    def _load_taichi_c_api(self) -> None:
        """Load all methods from taichi api and assign their correct arg/res
        types based on method map

        :return: None
        """

        if not self._loaded:
            raise TaichiNotLoadedException('Taichi C API not yet loaded')

        for method_name, attributes in TAICHI_C_API_METHODS.items():
            f = getattr(self._cdll, method_name)

            if 'restype' in attributes:
                f.restype = attributes['restype']

            if 'argtypes' in attributes:
                f.argtypes = attributes['argtypes']

            setattr(self, method_name, f)

    @property
    def loaded(self) -> bool:
        """Is library loaded and everything populated

        :return: bool
        """

        return self._loaded and self._cdll
