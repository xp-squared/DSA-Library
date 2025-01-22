class Point: 
    def __init__(self, x, y): 
        self.x = x 
        self.y = y


# Given three collinear points p, q, r, the function checks if  
# point q lies on line segment 'pr'  
def onSegment(p, q, r): 
    if ( (q.x <= max(p.x, r.x)) and (q.x >= min(p.x, r.x)) and 
           (q.y <= max(p.y, r.y)) and (q.y >= min(p.y, r.y))): 
        return True
    return False

def orientation(p, q, r):
    # 0 --> p, q and r are collinear
    # 1 --> Clockwise
    # 2 --> Counterclockwise
    value = (float(q.y - p.y) * (r.x - q.x)) - (float(q.x - p.x) * (r.y - q.y))
    if value > 0: # meaning this is clockwise
        return 1
    elif value < 0: # counterclockwise
        return 2
    else: # collinear 
        return 0


# this function will either return true or false if the lines intersect
def intersection(p1,q1,p2,q2):
    # lets find the orientations now
    orientation1 = orientation(p1, q1, p2) 
    orientation2 = orientation(p1, q1, q2) 
    orientation3 = orientation(p2, q2, p1) 
    orientation4 = orientation(p2, q2, q1)

    # basic case of this problem 
    #(p1, q1, p2) and (p1, q1, q2) have different orientations and 
    #(p2, q2, p1) and (p2, q2, q1) have different orientations.
    if ((orientation1 != orientation2) and (orientation3 != orientation4)): 
        return True
    
    # special cases 
    # (p1, q1, p2), (p1, q1, q2), (p2, q2, p1), and (p2, q2, q1) are all collinear and 
    # the x-projections of (p1, q1) and (p2, q2) intersect 
    # the y-projections of (p1, q1) and (p2, q2) intersect

    # p1 , q1 and p2 are collinear  p2 lies on  p1q1 
    if ((o1 == 0) and onSegment(p1, p2, q1)): 
        return True
  
    # p1 , q1 and q2 are collinear q2 lies on  p1q1 
    if ((o2 == 0) and onSegment(p1, q2, q1)): 
        return True
  
    # p2 , q2 and p1 are collinear p1 lies on p2q2 
    if ((o3 == 0) and onSegment(p2, p1, q2)): 
        return True
  
    # p2 , q2 and q1 are collinear,  q1 lies on p2q2 
    if ((o4 == 0) and onSegment(p2, q1, q2)): 
        return True
  
    # If none of the cases 
    return False

def main():
    x1, y1 = map(float, input("Enter starting point for line 1 (x,y): ").split(","))
    x2, y2 = map(float, input("Enter end point for line 1 (x,y): ").split(","))
    x3, y3 = map(float, input("Enter starting point for line 2 (x,y): ").split(","))
    x4, y4 = map(float, input("Enter end point for line 2 (x,y): ").split(","))

    # create our point objects
    p1 = Point(x1, y1) 
    q1 = Point(x2, y2) 
    p2 = Point(x3, y3) 
    q2 = Point(x4, y4)

    # https://www.geeksforgeeks.org/check-if-two-given-line-segments-intersect/ important reference for this problem and a guide
    # now lets test if the lines intersect
    if intersection(p1,q1,p2,q2):
        print("The lines intersect!")
    else:
        print("The lines do not intersect")


main()