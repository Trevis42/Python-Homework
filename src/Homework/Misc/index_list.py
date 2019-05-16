# This program demonstrates how to get the
# index of an item in a list and then replace
# that item with a new item.

ROWS = 3
COLS = 5

def main():
    # Create a list with some items.
    list2D = [[0,0,0,0,0],
              [0,0,0,0,0],
              [0,0,0,0,0]]
    for r in range(ROWS):
        for c in range(COLS):
            list2D[r][c] = int(input('Enter numbers:'))

    print(list2D)

# Call the main function.
main()

        
    
    
    
