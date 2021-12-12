from typing import Union, Any


class Exceptions:
    def __init__(self, exceptions: Union[tuple, list], dexc: dict=None) -> None:
        """
        Exceptions tools.

        :param exceptions: List of exceptions.
        :param dexc: Dictionary of exception.
        """
        self.scheme = None

        self.exceptions = exceptions
        self.dexc = dexc

    def getexc(self, key: str) -> Union[None, Any]:
        """
        Get exception from dictionary of exceptions.
        If dictionary is not defined, returning None.
        If key doesn't exist, returning None.

        :param key: Exception name.
        """
        if self.dexc is None:
            return None

        elif self.dexc is not None:
            try:
                return self.dexc[key]
            except KeyError:
                return None

    def excaslist(self) -> list:
        """Get exceptions list."""
        return self.exceptions

    def getscheme(self) -> Union[None, str]:
        """Get exception scheme."""
        return self.scheme

    def setscheme(self, scheme: str) -> int:
        """
        Set exceptions scheme.
        If all done, returning 0, else 1.

        Note:
            Write "$type" where you want to be exception type.
            Write "$msg$ where you want to be exception message.
            This is important.

        :param scheme: Exception scheme.
        """
        if '$type' not in scheme or '$msg' not in scheme:
            return 1

        elif '$type' in scheme and '$msg' in scheme:
            self.scheme = scheme

            return 0

    def throwscheme(self, exctype: str, msg: str, kills: bool) -> Union[None, int]:
        """
        Throw exception, where message and structure will be scheme.
        If scheme is None, returning 1, else None.

        :param exctype: Exception type.
        :param msg: Exception message.
        :param kills: Is exception kills app.
        """
        if self.scheme is None:
            return 1

        exc = self.scheme.replace('$type', exctype).replace('$msg', msg)

        print(exc)

        if kills:
            exit(1)

    def check(self, expression: bool, exctype: str, msg: str, kills: bool) -> Union[None, int]:
        """
        If expression is False, throwing exception.
        If scheme is None, returning 1.

        :param expression: Expression to check.
        :param exctype: Exception type.
        :param msg: Exception message.
        :param kills: Is exception kills app.
        """
        if self.scheme is None:
            return 1

        if not expression:
            self.throwscheme(exctype, msg, kills)

    def tryexcept(self, func, *args) -> Union[None, tuple]:
        """
        Get exception from function.
        If exception not raised, returning None, else returns type of exception and exception message.

        :param func: Function to call.
        """
        try:
            func(*args)
        except Exception as error:
            return type(error), str(error)
