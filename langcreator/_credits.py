class Credits:
    """Library credits."""

    license = 'MIT License'
    author = 'Ivan Perzhinsky'
    year = '2021'
    version = 1.0
    finished = True

    def get(self) -> str:
        """Get all credits."""
        return f'{self.license}, {self.author}, {self.year}, {self.version}, {self.finished}.'
