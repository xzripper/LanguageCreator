from typing import Union


class StringParser:
    def __init__(self, string: str) -> None:
        """
        String parser tools.
        If string is not str, string will be None.

        :param string: String to parse.
        """
        if type(string) is not str:
            self.string = None

        elif type(string) is str:
            self.string = string

    def getstr(self) -> Union[None, str]:
        """Get user string."""
        return self.string

    def updatestr(self, string: str) -> None:
        """
        Replace old string on new string.

        :param string: Updated string.
        """
        self.__init__(string)

    def cutstart(self, fr: int) -> Union[None, str]:
        """
        Cut string from start.

        :param fr: Cut from.
        """
        if self.string is None:
            return self.string

        return self.string[fr:]

    def cutend(self, fr: int) -> Union[None, str]:
        """
        Cut string from end.

        :param fr: Cut from.
        """
        if self.string is None:
            return self.string

        return self.string[:fr]

    def cut(self, start: int, end: int) -> Union[None, str]:
        """
        Cut string by start and end.

        :param start: Cut from start.
        :param end: Cut from end.
        """
        if self.string is None:
            return self.string

        return self.string[start:][:end]

    def remspaces(self, side: str) -> Union[None, str]:
        """
        Remove spaces from n side.
        Returns None if error.

        :param side: Remove spaces from n side.
        """
        if self.string is None:
            return self.string

        if side == 'right':
            return self.string.rstrip()

        elif side == 'left':
            return self.string.lstrip()

        elif side == 'all':
            return self.string.rstrip().lstrip()

        else:
            return None

    def replace(self, old: Union[tuple, list, str], new: Union[tuple, list, str]) -> Union[None, str]:
        """
        Replace old character on new.
        If old and new is tuple or list, it's removes old characters on new characters.

        :param old: Old character.
        :param new: New character.
        """
        if self.string is None:
            return self.string

        replaced = self.string

        if (type(old) is tuple or type(old) is list) and (type(new) is tuple or type(new) is list):
            if len(new) < len(old) or len(new) > len(old):
                return None

            for i in range(len(old)):
                replaced = replaced.replace(old[i], new[i])

            return replaced

        elif (type(old) is str) and (type(new) is str):
            return self.string.replace(old, new)

        else:
            return None

    def crash(self, separator: Union[tuple, list, str], getdict: bool = False) -> Union[None, list, dict]:
        """
        Crash a string by separator.
        If separator is tuple or list, it will be splitting step by step.
        If separator is not str or tuple or list, returns None.

        :param separator: Separator to crash.
        :param getdict: Get dict as return when separator is tuple or list.
        """
        if self.string is None:
            return self.string

        dsplitted = {}
        splitted = []

        if type(separator) is tuple or type(separator) is list:
            if getdict:
                for divider in separator:
                    dsplitted[divider] = self.string.split(divider)

                return dsplitted

            elif not getdict:
                for divider in separator:
                    splitted.append(self.string.split(divider))

                return splitted

        elif type(separator) is str:
            return self.string.split(separator)

        else:
            return None

    def remove(self, char: str, times: int) -> Union[None, str]:
        """
        Remove character from string.
        If times is -1, removing all, else removing only N times.

        :param char: Character to remove.
        :param times: Remove character N times.
        """
        if self.string is None:
            return self.string

        if times == -1:
            return self.string.replace(char, '')

        elif times != -1:
            return self.string.replace(char, '', times)

    def tocase(self, case: int) -> Union[None, str]:
        """
        Convert string to case.

        Types:
            1 - To lower.
            2 - To upper.
            3 - To title.
            4 - Capitalize.

        :param case: Type of case.
        """
        if self.string is None:
            return self.string

        if case == 1:
            return self.string.lower()

        elif case == 2:
            return self.string.upper()

        elif case == 3:
            return self.string.title()

        elif case == 4:
            return self.string.capitalize()

        else:
            return None

    def inscobes(self, rlcs: bool) -> Union[None, bool]:
        """
        Is string in scobes.
        If rlcs is not True and not False, returns None.

        :param rlcs: Is "<>" scobes too.
        """
        if self.string is None:
            return self.string

        scobes = f'{self.string[0]}{self.string[-1]}'

        if rlcs:
            return scobes == '()' or scobes == '[]' or scobes == '{}' or scobes == '<>'

        elif not rlcs:
            return scobes == '()' or scobes == '[]' or scobes == '{}'

        else:
            return None

    def getfromscobes(self) -> Union[None, str]:
        """
        Get string from scobes.
        If string not in scobes, returns None.
        """
        if self.string is None:
            return self.string

        if not self.inscobes(True):
            return None

        elif self.inscobes(True):
            return self.cut(1, -1)

    def instring(self, string: str) -> Union[None, bool]:
        """
        Is sub-string in string.

        :param string: Sub-string.
        """
        if self.string is None:
            return None

        return string in self.string

    @staticmethod
    def newstr(string: str) -> str:
        """
        Get user object from args converted in str.

        :param string: Target string.
        """
        return str(string)

    def clearstr(self) -> None:
        """Clear string."""
        self.string = None
