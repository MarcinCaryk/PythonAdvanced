def division_a_b(a, b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)

division_a_b(2.0, 3.0)
division_a_b(3.0, 3.0)

#####################################################################
import sys

def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')

def windows_interaction():
    assert ('win' in sys.platform), "Function can only run on Windows systems."
    print('Windows setting up')
#####################################################################
try:
    windows_interaction()
    #linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')
#####################################################################
try:
    windows_interaction()
    #linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)