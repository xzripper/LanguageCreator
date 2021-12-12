from typing import Union, Any
from io import StringIO
from contextlib import redirect_stdout
from os import system
from atexit import register
from shutil import rmtree
from os.path import exists


class Code:
    def __init__(self, source: str) -> None:
        """
        Code tools.

        :param source: Source code.
        """
        if type(source) is str:
            self.source = source

        elif type(source) is not str:
            self.source = None

    def execute(self, useeval: bool, getexc: bool) -> Union[None, tuple]:
        """
        Execute source code. If getexc is True, function returns exception type and exception msg from func,
        but if in function not raised exception, it returns None.

        :param useeval: Execute code using eval.
        :param getexc: Get exception from function.
        """
        if self.source is None:
            return self.source

        if useeval:
            if getexc:
                try:
                    return eval(self.source)
                except Exception as err:
                    return type(err), str(err)

            elif not getexc:
                return eval(self.source)

        elif not useeval:
            if getexc:
                try:
                    exec(self.source)
                except Exception as err:
                    return type(err), str(err)

            elif not getexc:
                exec(self.source)

    @staticmethod
    def getstd(func: Any, remlastc: bool, *args: Any) -> Union[None, Any]:
        """
        Get output from function.
        If error, returns None.

        :param func: The function.
        :param remlastc: Remove last character from output.
        :param args: Args to function.
        """
        if not callable(func):
            return None

        output = StringIO()

        with redirect_stdout(output):
            func(*args)

        return output.getvalue()[:-1] if remlastc else output.getvalue()

    @staticmethod
    def tryexcept(func: Any, *args: Any) -> Union[None, tuple]:
        """
        Get exception from function.
        If exception not raised, returns None.

        :param func: The function.
        :param args: Function args.
        """
        if not callable(func):
            return None

        try:
            func(*args)
        except Exception as err:
            return type(err), str(err)

    @staticmethod
    def getmodules(modules: Union[tuple, list], imp: Union[tuple, list]):
        """
        Create import syntax, and get as string.
        If error, returns None.

        :param modules: Modules to import.
        :param imp: Import N from module.
        """
        res = ''

        if len(imp) < len(modules):
            return None

        for module, fromimp in zip(modules, imp):
            if module == modules[-1]:
                res += f'from {module} import {fromimp}'

            else:
                res += f'from {module} import {fromimp}\n'

        return res

    @staticmethod
    def runpy(file: str) -> None:
        """
        Run python file.

        :param file: Python file.
        """
        system(f'python {file}')

    @staticmethod
    def cleancache() -> None:
        """Clear "__pycache__"."""
        import __main__

        cache = (('\\'.join(__main__.__file__.split('\\')[:-1])) + '\\__pycache__')

        if exists(cache):
            rmtree(cache)

def onend(func):
    def _onend():
        register(func)
    return _onend()
