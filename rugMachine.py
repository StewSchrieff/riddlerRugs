
import random
import numpy as np
from datetime import datetime
import csv
import time



def pick_a_color():
    color = random.randint(0,2)
    return color


def build_a_rug():
    """Returns a 100x100 list of numbers"""
    # random.seed(2018)
    myRug = np.ndarray(shape=(100,100), dtype=int)
    for i in range(0,99):
        for j in range(0,99):
            myRug[i][j] = pick_a_color()

    return myRug



def build_a_rigged_rug():
    random.seed(2018)
    myRug = np.ndarray(shape=(11, 11), dtype=int)
    for i in range(0, 10):
        for j in range(0, 10):
            myRug[i][j] = pick_a_color()

    for i in range(0,4):
        for j in range(0,4):
            myRug[i][j] = 1
    return myRug

# def pretty_print(rug):
#     for i in (0,99):
#         [print(rug[i,j] +', ') for j in (0,99)]



def investigate_fours(fourinarow, rug, color):
    global numberOf1x4
    global numberOf4x4
    global numberOf2x4
    global numberOf3x4
    # print(fourinarow)

    numberOf1x4 = numberOf1x4 + len(fourinarow)
    for (i,j) in fourinarow:
        # check to see if another fourinarow is beneath ya
        if((i+1,j) in fourinarow):
            # print('found a block where there are is a 2x4 grid of ' + color)
            numberOf2x4 = numberOf2x4 + 1
            if((i+2,j) in fourinarow):
                # print('found a block where there are is a 3x4 grid of ' + color)
                numberOf3x4 = numberOf3x4 + 1
                if((i+3,j) in fourinarow):
                    print('found a block where there are is a 4x4 grid of ' + color)
                    numberOf4x4 = numberOf4x4 + 1



def check_rug(rug):
    """Checks if there are any 4x4 grids where the same color is used"""
    # needs to return where there are four in a row
    fourInARowGreen = []
    fourInARowSilver = []
    fourInARowWhite = []
    # for i in range(0,99):
    for i in range(0,99):
        # for j in range(0,96):
        for j in range(0, 96):
            compare = rug[i][j]
            # this will look at each single tile and check it's neighbors
            if(compare == rug[i][j+1]):
                # rug has two numbers together in the same row, so check another
                if(compare == rug[i][j+2]):
                    # print('three in a row')
                    # print((i,j))
                    if(compare == rug[i][j+3]):
                        # print('four in a row')
                        if(compare == 0):
                            fourInARowGreen.append((i,j))
                        if (compare == 1):
                            fourInARowSilver.append((i, j))
                        if (compare == 2):
                            fourInARowWhite.append((i, j))

    investigate_fours(fourInARowGreen, rug, 'Green')
    investigate_fours(fourInARowSilver, rug, 'Silver')
    investigate_fours(fourInARowWhite, rug, 'White')



def main():
    print('Are you sure you want to overwrite rugs.csv???? 10 seconds to decide')
    time.sleep(10)
    startTime = datetime.now()

    np.set_printoptions(threshold=np.nan)
    print('starting the rug machine up')
    # will need to bump up these numbers in order to better estimate the prob of getting a reject
    rugs = 0
    with open('rugs2.csv', 'wb') as f:
        writer = csv.writer(f)
        for i in range(0,80000):
            rugs = rugs +1
            currentRug = build_a_rug()
            fourinarow = check_rug(currentRug)
            # investigate_fours(fourinarow)
            # print(currentRug)

            if(i % 10 == 9):
                # print('total Number of 1x4: ' + str(numberOf1x4) + ' in ' + str(rugs) + ' rugs.')
                # print('total Number of 2x4: ' + str(numberOf2x4) + ' in ' + str(rugs) + ' rugs.')
                # print('total Number of 3x4: ' + str(numberOf3x4) + ' in ' + str(rugs) + ' rugs.')
                # print('total Number of 4x4: ' + str(numberOf4x4) + ' in ' + str(rugs) + ' rugs.')
                # print('')
                row = [rugs, numberOf1x4, numberOf2x4, numberOf3x4, numberOf4x4]
                writer.writerow(row)



    totalTime = datetime.now() - startTime
    print('Total Execution time: ' + str(totalTime))
    print('Average Time Per Rug: ' + str(totalTime / rugs))













numberOf1x4 = 0
numberOf2x4 = 0
numberOf3x4 = 0
numberOf4x4 = 0


main()