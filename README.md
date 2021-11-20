# MathLang, simple language for math, on Python.
MathLang is strong language with very simple syntax.

Here is simple example.

Main.mtl
```
? Simple example;
5 * 2;
4 / 2;
2 * 2;
sin(1);
```

Run file.
```
mathlang Main.mtl solve
```

It's return's.
```python
[10, 2.0, 4, 0.8414709848078965]
```

Run file and get results as dict.
```
mathlang Main.mtl asdict
```

It's return's.
```python
{'5 * 2': 10, '4 / 2': 2.0, '2 * 2': 4, 'sin(1)': 0.8414709848078965}
```
