from typing import Union, Any


class FileParser:
    def __init__(self, file: str) -> None:
        """
        Tools for file parsing.

        :param file: Target file.
        """
        self.file = file

    def getfile(self, mode: str) -> Any:
        """
        Get user file wrapper.

        :param mode: Wrapper mode.
        """
        return open(self.file, mode)

    def readfile(self) -> str:
        """Read a file."""
        with self.getfile('r') as file:
            return file.read()

    def getlines(self, endsym: str, delend: bool) -> list:
        """
        Get lines from file.
        If file is empty, returning [].

        :param endsym: Lines separator.
        :param delend: If last line in file is '', and delend is True, deleting this empty line.
        """
        content = self.readfile().split(f'{endsym}\n')

        if content == []:
            return content

        if delend:
            if content[-1] == '':
                content.pop()

            return content

        elif not delend:
            return content

    def getline(self, endsym: str, linenum: int) -> Union[None, str]:
        """
        Get line from lines of file.
        If line doesn't exists, returning None.

        :param endsym: Line separator.
        :param linenum: Line number.
        """
        lines = self.getlines(endsym, False)

        try:
            return lines[linenum]
        except IndexError:
            return None

    def getbycategory(self, endsym: str, category: str) -> Union[None, list]:
        """
        Get lines by category.
        If category is invalid, returning None.

        Categories:
            Startswith "*" - Get all lines which starts a symbols after "*" in category.
            Endswith "*" - Get all lines which ends a symbols after "*" in category.
            Startswith "%" - Get lines, where symbols after "%" in category, are on line.

        :param endsym: Lines separator.
        :param category: Search category.
        """
        lines = self.getlines(endsym, False)
        filtered = []

        if category.startswith('*'):
            for line in lines:
                if line.startswith(category[1:]):
                    filtered.append(line)

            return filtered

        elif category.endswith('*'):
            for line in lines:
                if line.endswith(category[:-1]):
                    filtered.append(line)

            return filtered

        elif category.startswith('%'):
            for line in lines:
                if category[1:] in line:
                    filtered.append(line)

            return filtered

        else:
            return None
