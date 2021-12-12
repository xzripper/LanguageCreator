# LanguageCreator - Simple library for easy creation transpilator.
Create transpilators in one hour!

# Install.
Download code, rename folder to "LanguageCreator", move it to "$Python\Lib\", Done!

# About.
Simple library for easy creation transpilator on Python.<br>
In this library prepared **90% functions** of transpilator.<br>

# Examples.
main.tt
```
5 + 5;
10 + 10;
```

test.py
```python
from LanguageCreator.langcreator.allobjs import *


exceptions = Exceptions([], {'TestUndefinedError': 'TestUndefinedError', 'TestSyntaxError': 'TestSyntaxError', 'TestExc': 'TestExc'})
exceptions.setscheme('Exception $type, $msg;')

kwds = Keywords(sem=Keyword(';')).get()

class TestLang:
    def __init__(self, file):
        self.parser = FileParser(file)

    def run(self):
        lines = self.parser.getlines('', True)

        for line in lines:
            if not line.endswith(str(kwds['sem'])):
                exceptions.throwscheme(exceptions.getexc('TestSyntaxError'), 'string must end on semicolon', True)

        for line in lines:
            _line = Code(StringParser(line).cutend(-1))
            res = _line.execute(True, True)

            if type(res) is tuple and len(res) == 2:
                exceptions.throwscheme(exceptions.getexc('TestExc'), res[1], True)

file = CMDArgs()
runtime = TestLang(file.getarg(0))
runtime.run()

```

To cmd.
```python test.py main.tt```

Result.
```
10
20
```

Yeap, this code doesn't clean, but it's works... In real projects i never do this.<br>
So, how you see, we maked this <a href="https://github.com/xzripper/MathLang">repository</a> in 1 minute.<br>
This code (not library) have many bugs, and this is very raw code.<br>

# Documentation info.
You can inspect this library via "docs" folder.<br>
Open interest to you parts of library, and look source code, whats do this function, how use it, when will be error, look all that can this library.<br>
You can see mini-doc of function in your IDE too.<br>

# Credits.
Author Ivan Perzhinsky.<br>
Version 1,0.<br>
License MIT License.<br>

# End.
Thank you for reading, have a good day, bye!
<br>
<hr>
<p align="center">^_^</p>
