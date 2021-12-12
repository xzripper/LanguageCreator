from typing import Union
from sys import argv


class CMDArgs:
    def __init__(self, **commands) -> None:
        """
        CMD Args tools.
        If value in dictionary not will be function, it will be None.

        :param commands: The commands.
        """
        self.commands = commands

        for command in commands:
            if not callable(self.commands[command]):
                self.commands = None

    def args(self):
        """Get console args."""
        return argv[1:]

    def getarg(self, index: int) -> Union[None, str]:
        """
        Get argument by index.
        If argument doesn't exist, returning None.

        :param index: Argument index.
        """
        try:
            return self.args()[index]
        except IndexError:
            return None

    def handle(self, mustbe: int) -> int:
        """
        Handle args. If all done returns 0, else 1.

        :param mustbe: Must be args count.
        """
        if self.commands is None:
            return 1

        args = self.args()

        if len(args) < mustbe:
            print('You missed arguments!')

        elif len(args) >= mustbe:
            for arg, comm in zip(args, self.commands):
                if arg == comm:
                    self.commands[comm]()

    def get(self) -> Union[None, dict]:
        """Get commands."""
        return self.commands
