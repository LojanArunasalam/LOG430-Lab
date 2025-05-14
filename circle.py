import math

def diameter(radius):
    return radius * 2

def circumference(radius):
    return 2*radius*math.pi

def main():
    print(circumference(3))
    print(diameter(3))

if __name__ == "__main__":
    main()