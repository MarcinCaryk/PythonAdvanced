try:
    print(int('a'))
except ValueError as e_variable:
    print(e_variable.args)



try:
    import abcdefghijk

except ImportError as e:
    print(e.args)
    print(e.name)
    print(e.path)