from tkinter import *
import random

# Create a list of numbers to be used in the game
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Duplicate the list to create pairs of numbers
pairs = numbers * 2

# Shuffle the pairs
random.shuffle(pairs)

# Create a board with the shuffled pairs
board = [pairs[:5], pairs[5:10], pairs[10:15], pairs[15:20]]

# Create a Tkinter window and set its properties
window = Tk()
window.title("Memory Game")
window.geometry("500x500")

# Create a 5x4 grid of buttons and add them to the window
buttons = []
for row in range(5):
    button_row = []
    for col in range(4):
        button = Button(window, text="", width=10, height=5, command=lambda row=row, col=col: flip_card(row, col))
        button.grid(row=row, column=col)
        button_row.append(button)
    buttons.append(button_row)

# Keep track of the number of matches
matches = 0

# Keep track of the number of attempts
attempts = 0

# Keep track of the positions of the cards that have been flipped
flipped = []

# Create a function to flip the cards when they are clicked
def flip_card(row, col):
    global matches
    global attempts
    global flipped
    
    # Get the card at the specified position
    card = board[row][col]
    
    # Flip the card and update the button text
    buttons[row][col].config(text=str(card))
    
    # Disable the button
    buttons[row][col].config(state=DISABLED)
    
    # Add the flipped card to the list
    flipped.append([row, col])
    
    # Check if two cards have been flipped
    if len(flipped) == 2:
        # Increment the number of attempts
        attempts += 1
        
        # Get the positions of the flipped cards
        row1, col1 = flipped[0]
        row2, col2 = flipped[1]
        
        # Get the cards at the specified positions
        card1 = board[row1][col1]
        card2 = board[row2][col2]
        
        # Check if the cards match
        if card1 == card2:
            # Increment the number of matches
            matches += 1
            
            # Clear the flipped list
            flipped = []
            
            # Check if all matches have been found
            if matches == 10:
                # Display a message box with the number of attempts
                messagebox.showinfo("Congratulations!", "You found all the matches in " + str(attempts) + " attempts!")
        else:
            # Flip the cards back over after a delay
            window.after(1000, lambda: flip_back(row1, col1, row2, col2))

# Create a function to flip the cards back over
def flip_back(row1, col1, row2, col2):
    # Flip the cards back over and update the button text
    buttons[row1][col1].config(text="")
    buttons[row2][col2].config(text="")
    
    # Enable the buttons
    buttons[row1][col1].config(state=NORMAL)
    buttons[row2][col2].config(state=NORMAL)
    
    # Clear the flipped list
    flipped.clear()

# Start the Tkinter event loop
window.mainloop()