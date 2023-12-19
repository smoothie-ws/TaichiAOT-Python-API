class TaichiException(Exception):
    pass


class UnsupportedPlatformException(TaichiException):
    pass


class MissingTaichiLibraryException(TaichiException):
    pass


class TaichiNotLoadedException(TaichiException):
    pass


class TaichiMethodNotFound(TaichiException):
    pass
