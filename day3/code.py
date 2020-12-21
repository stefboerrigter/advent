#from parse import parse
import re

lines = list()
maxCharLines = 0
numberOfLines = 0

def initializeList():
    global numberOfLines
    global maxCharLines
    f = open("input.txt", "r")
    for line in f:
        lines.append(line)
        numberOfLines = numberOfLines + 1
        
    maxCharLines = len(lines[0]) - 1
    ".....#......#....#........#.#.."
    #print("Charactes in line: {0} [{1}]".format(len(lines[0]),lines[0]))

def pattern(right, down):
    global numberOfLines
    global maxCharLines
    treesFound = 0
    print("Following {0:3} right and {1:3} down ({2})".format(right, down, numberOfLines))
    rCount = 0
    dCount = 0
    end = 0
    while end == 0:
        rCount = rCount + right
        dCount = dCount + down
        if rCount >= maxCharLines:
            print("Pos = now {0}, max = {1}, becomes {2}".format(rCount, maxCharLines, rCount - maxCharLines))
            rCount = rCount - maxCharLines
            
        if dCount >= numberOfLines:
            end = 1
        else:
            print("Position {0:3} right and {1:3} down: Char = {2}".format(rCount, dCount, lines[dCount][rCount]))
            if '#' == lines[dCount][rCount]:
                #print ("Tree")
                treesFound += 1
    print("Found {0} trees".format(treesFound))
    return treesFound
    
initializeList()
trees = 0
trees = pattern(1, 1)
trees *= pattern(3, 1)
trees *= pattern(5, 1)
trees *= pattern(7, 1)
trees *= pattern(1, 2)
print("Total trees: {0}".format(trees))