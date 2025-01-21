import math
def main():
    # first lets create the circle we will be using
    radius = float(input("Enter radius of circle: "))
    h, k = map(float, input("Enter center point of circle (h, k): ").split(","))
    num = int(input("How many points would you like to enter: "))
    
    points = []
    # get points from user
    for i in range(num):
        x, y = map(float, input(f"Enter point {i+1} (x, y): ").split(","))
        points.append((x,y))
    
    # Checking to see that the points will print
    #for i,point in enumerate(points):
    #    print(point)

    # now lets check if the points entered lie on the circumference
    print("Checking if points lie on the circumference")
    for i, (x,y) in enumerate(points):
        distance = math.sqrt(((x - h)**2 + (y - k)**2))
        if (distance < radius):
            print(f"point {i+1} with coords ({x}, {y}) is not on the circumference (inside)")
        elif (distance > radius):
            print(f"point {i+1} with coords ({x}, {y}) is not on the circumference (outside)")
        else:
            print(f"point {i+1} with coords ({x}, {y}) is on the circumference!")
    


main()