import random
# answer talks about walking intermittently left and right from initial position until door is reached
# this problem is related to exponential backoff: multiplicatively decrease rate of some profess in order to find acceptable rate

def findDoor(doorNumber):
    position = 0 # we are at the middle between all doors
    currentSteps = 1
    if (doorNumber == position): # if somehow we were at the base position door, probably doesnt needed to be included
        return True
    while True:

        # lets search the left side first to see if the door is there
        for i in range(currentSteps):
            position = position - 1 # move one step however many current steps we are on
            if (position == doorNumber):
                return position
        position = position + currentSteps # readd the steps we moved to move back to position 0 

        # search the right side
        for i in range(currentSteps):
            position = position + 1
            if (position == doorNumber):
                return position
        position = position - currentSteps # return to position 0 

        currentSteps = currentSteps * 2 
        

def main():
    random_number = random.randint(-100, 100)
    found = findDoor(random_number)
    #print(f"Door was found at {random_number}")
    print(f"Door was found at {found}")
    

main()