# Write programs to:
# Create a dictionary where keys are numbers from 1 to 5 and values are their cubes.


def activity_1():
    cubes = dict()
    for i in range(1,6):
        cubes[i] = i**3
    print('Dictionary of integers with their cubes : ', cubes)


activity_1()