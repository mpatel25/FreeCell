Freecell in Python

Purpose:
    Improve and practice skill in Python by implementing the card game freecell.
    Practice the following features in Python:
        -Classes
        -Opening and modifying files
        -Try-except statements
        -List comprehension
        -Other smaller features provided by python syntax

Implementation:
    The game is implemented in python 3.
    To run the game, a game text file name is passed in through the arguments
        and the game is played through the os terminal.
    For example on a linux os the game can be run like this:
        python3 freecell.py ex_game.txt
    The game represents a card with two characters.
    The first characer is the suit and the character is the card face value.
    The suits are represented by d, s, h, c.
    d is for diamond, s is for spade, h is for heart, and c is for club.
    The Face values are represented by a number (2-9) or a, t, j, q, k.
    a is for ace, t is for 10, j is for jack, q is for queen, and k is for king.
    For example ct is eqivalent to ten of clubs
    The ex_game.txt is an example game text file for a typical freecell game.
    The game is played through commands. The following are the valid commands:
        exit - to exit the game
        moves - to show all possible moves
        cxcx - to move a card from one column to another.
            The x's represent numbers from 0 to 7 for the columns.
        cxay - to move a card from a column to a free cell.
            The x represents a number from 0 to 7 for the columns.
            The y represents a number from 0 to 3 for the free cells.
        cxf - to move a card from a column to the foundation.
            The x represents a number from 0 to 7 for the columns.
        aycx - to move a card from a free cell to a column.
            The x represents a number from 0 to 7 for the columns.
            The y represents a number from 0 to 3 for the free cells.
        ayf - to move a card from a free cell to the foundation.
            The y represents a number from 0 to 3 for the free cells.
  
 
