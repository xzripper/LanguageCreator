from typing import Union


class Keyword:
    def __init__(self, keyword: str) -> None:
        """
        Create new keyword.
        If keyword not string, result will be ''.

        :param keyword: The keyword.
        """
        if type(keyword) is not str:
            self.keyword = ''

        elif type(keyword) is str:
            self.keyword = keyword

    def __str__(self) -> str:
        return self.keyword


class Keywords:
    def __init__(self, **keywords) -> None:
        """
        Create dictionary with keywords.
        But if value in dictionary, not will be Keyword, it's being None.

        :param keywords: The keywords.
        """
        self.keywords = keywords

        for keyword in self.keywords:
            if type(self.keywords[keyword]) is not Keyword:
                self.keywords = None

    def get(self) -> Union[None, dict]:
        """Get keywords."""
        return self.keywords
