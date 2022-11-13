
class CrypterBaseException(Exception):
    """Base Crypter Exception"""
    pass


class ArgvException(CrypterBaseException):
    """Exception used when command line arguments are not ok."""
    pass


class NotATextFile(CrypterBaseException):
    """Raised when path does not contain a txt file"""
    pass