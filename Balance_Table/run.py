import numpy as np
import sys
from numpy import array
import balance as bal
import random
# import interface as gui

np.set_printoptions(threshold=324) # total number of matrix elements before truncation occurs (18x18 square)

if (len(sys.argv) >= 2):
    argv = sys.argv[1:]
else:
    argv = ["none"]

def createTable(size):
    grid = [[0] * (size) for _ in range(size)]
    return grid
# end createTable method

# this method randomly fills an nxn table with blocks from the block array
def randomizeTable(table, blocks, size):
    for x in range(size):
        for y in range (size):
            number = random.choice(blocks)
            table[x][y] = number
            blocks = blocks[blocks != number]
    return table


def main():
    size = input("How big would you like the table? ")
    try:
        size = int(size)
        if (size >= 4):
            # create an array with weighted blocks
            blocks = array(range(1, (size * size) +1))
            opening = "\nThe Weighted Blocks For A {} x {} Square Are:\n".format(size,size)
            print(opening,blocks, "\n")

           # create empty table
            print("Empty Table:")
            table = createTable(size)
            print("\n", np.matrix(table), "\n")

            if(size % 4 == 0):
                print("Creating a doubly even magic square:")
                table = bal.doublyEven(size)
                print("\n",np.matrix(table),"\n")
                print("Table is a Magic Square: ", bal.isMagicSquare(table), "\n")
                isBalanced = bal.checkBalance(table, blocks, size)
                print("Table is balanced: ", isBalanced, "\n")
                if (argv[0] == "-r"):
                    print("Randomizing Table: -------------------------------------")
                    table = randomizeTable(table, blocks, size)
                    print("\n",np.matrix(table),"\n")
                    isBalanced = bal.checkBalance(table, blocks, size)
                    while (not isBalanced):
                        table = randomizeTable(table, blocks, size)
                        isBalanced = bal.checkBalance(table, blocks, size)
                    print("Table is balanced: ", isBalanced, "\n")
            elif(size % 2 == 0):
                print("Creating singly even magic square:")
                table = bal.build_sems(size)
                print("\n",np.matrix(table),"\n")
                print("Table is a Magic Square: ", bal.isMagicSquare(table), "\n")
                isBalanced = bal.checkBalance(table, blocks, size)
                print("Table is balanced: ", isBalanced, "\n")
                if (argv[0] == "-r"):
                    print("Randomizing Table: -------------------------------------")
                    table = randomizeTable(table, blocks, size)
                    print("\n",np.matrix(table),"\n")
                    isBalanced = bal.checkBalance(table, blocks, size)
                    while (not isBalanced):
                        table = randomizeTable(table, blocks, size)
                        isBalanced = bal.checkBalance(table, blocks, size)
                    print("Table is balanced: ", isBalanced, "\n")
            else:
                print("Creating odd magic square:")
                table = bal.generateSquare(size)
                print("\n",np.matrix(table),"\n")
                print("Table is a Magic Square: ", bal.isMagicSquare(table), "\n")
                isBalanced = bal.checkBalance(table, blocks, size)
                print("Table is balanced: ", isBalanced, "\n")
                if (argv[0] == "-r"):
                    print("Randomizing Table: -------------------------------------")
                    table = randomizeTable(table, blocks, size)
                    print("\n",np.matrix(table),"\n")
                    isBalanced = bal.checkBalance(table, blocks, size)
                    while (not isBalanced):
                        table = randomizeTable(table, blocks, size)
                        isBalanced = bal.checkBalance(table, blocks, size)
                    print("Table is balanced: ", isBalanced, "\n")

        else:
           print("Table must be greater than or equal to 4x4")

    except ValueError:
       print("That's not an integer!")

# end main method


# Executes the main function
if __name__ == '__main__':
    main()
