from interpreter import Interpreter
from sys import argv

from shutil import rmtree
from os.path import exists

if exists('__pycache__'):
    rmtree('__pycache__')

args = argv

if len(args) == 0x3:
    src = args[0x1]
    method = args[0x2]

    srcintpr = Interpreter(src)

    if method == 'solve':
        print(srcintpr.solve())

    elif method == 'asdict':
        print(srcintpr.asdict())

    else:
        print('Unknown method. Methods: solve, asdict')

elif args == ['mathlang.py', '--version']:
    print(Interpreter.version)

else:
    print('Some arguments missed, example: "mathlang *.mtl solve".')
