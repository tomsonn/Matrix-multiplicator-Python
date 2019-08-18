from matrix import *


print('Matrix A')

# Be sure that user's inputs are valid. Catching ValueError and TypeError.
while True:
    try:
        width_a = int(input('width: '))
        if width_a < 1:
            raise ValueError

        height_a = int(input('height: '))
        if height_a < 1:
            raise ValueError

        break
    except ValueError:
        print('Your input is invalid, dimensions of matrix A should be an positive integer! Try again.')

print('\nMatrix B')
while True:
    try:
        width_b = int(input('width: '))
        if width_b < 1:
            raise ValueError

        height_b = int(input('height: '))
        if width_a != height_b:
            raise Exception
        break
    except ValueError:
        print('Your input is invalid, dimensions of matrix B should be an positive integer! Try again.')
    except Exception:
        print('Width of matrix A and height of matrix B should be the same! Try again.')

print('\nMatrix A values:')
data_a = []

# Everything except float and integer type is not supported
for i in range(height_a):
    while True:
        try:
            tmp = list(map(float, input().split(' ')))
            if len(tmp) != width_a:
                raise TypeError
            data_a.append(tmp)
            break
        except ValueError:
            print('Supported values are float or integer only! Try again.')
        except TypeError:
            print('Number of values should match with dimensions of matrix! Try again.')

print('\nMatrix B values:')
data_b = []

for i in range(height_b):
    while True:
        try:
            tmp = list(map(float, input().split(' ')))
            if len(tmp) != width_b:
                raise TypeError
            data_b.append(tmp)
            break
        except ValueError:
            print('Supported values are float or integer only! Try again.')
        except TypeError:
            print('Number of values should match with dimensions of matrix! Try again.')

# Creating matrix objects
try:
    mat_a = Matrix(width_a, height_a, data_a)
    mat_b = Matrix(width_b, height_b, data_b)
except ValueError:
    print('Inappropriate dimensions of matrix or its data.')

res = mat_a * mat_b

print('\nResult:')
res.print_mat()


