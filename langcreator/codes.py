from typing import Union, Any


class Codes:
    def __init__(self, **codes: Any) -> None:
        """
        Create dictionary with codes.
        If key not string, or value not integer, codes will be None.

        :param codes: Dictionary of codes.
        """
        self.codes = codes

        for code in self.codes:
            if type(self.codes[code]) is not int:
                self.codes = None
                break

    def get(self) -> Union[None, dict]:
        """Get codes."""
        return self.codes

    def update(self, **codes: Any) -> None:
        """
        Update dictionary of codes.
        Calls class constructor.

        :param codes: Dictionary of codes.
        """
        self.__init__(**codes)

    def add(self, key: str, value: int) -> int:
        """
        Add code to dictionary.
        Returns code.

        :param key: Code key.
        :param value: Code value.
        """
        if self.codes is None:
            return 1

        elif type(key) is not str or type(value) is not int:
            return 1

        else:
            self.codes[key] = value

    def clear(self) -> None:
        """Clear codes."""
        self.codes = None
