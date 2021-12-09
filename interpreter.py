from exceptions import *
from math import *

from os.path import exists
from typing import Union

class Interpreter:
    version = 1.0

    def __init__(self, source: str) -> None:
        """Get source file, throws MathLangUnknownExtension, MathLangSourceNotExists."""
        if not source.endswith('.mtl'):
            self.source = None

            throwexc(MathLangUnknownExtension, 'Unknown extension of source.')

        elif not exists(source):
            self.source = None

            throwexc(MathLangSourceNotExists, 'Source file not found.')

        else:
            self.source = source

    def readsource(self) -> Union[None, str]:
        """Read source file, get content."""
        if self.source is None:
            return None;

        else:
            with open(self.source, 'r', encoding='utf-8') as src:
                return src.read()

    def parse(self) -> Union[None, list]:
        """Parse source file."""
        if self.source is None:
            return None;

        else:
            content = self.readsource()

            if content is None:
                return None;

            else:
                lines = content.split(';\n')

                if lines == ['']:
                    return []

                else:
                    if lines[-1] == '':
                        lines.pop()

                    if lines[-1] != '':
                        if lines[-1][-1] == ';':
                            lines[-1] = lines[-1][:-1]

                    return lines

    def solve(self) -> Union[None, list]:
        """Solve math in source and get results as list."""
        if self.source is None:
            return None

        else:
            results = []
            parsed = self.parse()

            try:
                for line in parsed:
                    if str(line).startswith('?'):
                        continue

                    else:
                        results.append(eval(str(line)))
            except ValueError as VE:
                throwexc(MathLangValueError, str(VE))

            except SyntaxError as SE:
                throwexc(MathLangSyntaxError, str(SE))

            except ZeroDivisionError as ZDE:
                throwexc(MathLangZeroDivisionError, str(ZDE))

            except OverflowError as OE:
                throwexc(MathLangOverflowError, str(OE))

            except Exception as exc:
                throwexc(MathLangUnknownError, str(exc))

            return results

    def asdict(self) -> Union[None, list]:
        """Solve math in source and get results as dict."""
        if self.source is None:
            return None

        else:
            results = {}
            parsed = self.parse()

            try:
                for line in parsed:
                    if str(line).startswith('?'):
                        continue

                    else:
                        results[str(line)] = eval(str(line))
            except ValueError as VE:
                throwexc(MathLangValueError, str(VE))

            except SyntaxError as SE:
                throwexc(MathLangSyntaxError, str(SE))

            except ZeroDivisionError as ZDE:
                throwexc(MathLangZeroDivisionError, str(ZDE))

            except OverflowError as OE:
                throwexc(MathLangOverflowError, str(OE))

            except Exception as exc:
                throwexc(MathLangUnknownError, str(exc))

            return results
x