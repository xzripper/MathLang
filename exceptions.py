class MathLangException(Exception):
    def __init__(self, _: str) -> None:
        """Default math lang exception."""
        self._ = _

class MathLangUnknownExtension(MathLangException):
    ...

class MathLangSourceNotExists(MathLangException):
    ...

class MathLangValueError(MathLangException):
    ...

class MathLangSyntaxError(MathLangException):
    ...

class MathLangZeroDivisionError(MathLangException):
    ...


class MathLangOverflowError(MathLangException):
    ...

class MathLangUnknownError(MathLangException):
    ...

def throwexc(exc: MathLangException, msg: str) -> None:
    """Throws an math lang exception."""
    raise exc(msg)
