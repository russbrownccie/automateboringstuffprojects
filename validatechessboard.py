# Russ Brown Chessboard Validator v 0.3

# changes in 0.2 - cleaned up steps 1 and 2 verification - used lists instead of multiple match statements
# changes in 0.3 - new dictionary is created of lowercase values from main dictionary, cleaning up checks

# Project from Automate the Boring Stuff with Python, 2nd ed by Al Sweigart
# This is supposed to validate a proper chess board - there are a LOT of problems but we meet requirements
# Additional things to check are any adjacent kings would be an invalid board trigger
# Also, any pawns on the 1 or 8 file would technically be invalid as they are promoted or backward
# 8 pawns and bishops on the same color would be invalid - two kings both in check, etc, etc
# but this meets the project requirements and took a lot of time
# Future improvements would be giving each test it's own function to easier compartmentalize and cleanup code
# Also should set it up as a while loop, so the moment a check fails, the check can be stopped


board = {'e8': 'Bking',
         'd1': 'WQUEEN',
         'c8': 'bbishop',
         'd8': 'bqueen',
         'e1': 'wking',
         'a2': 'wpawn',
         'b2': 'wpawn',
         'c2': 'wpawn',
         'd2': 'wpawn',
         'e2': 'wpawn',
         'f2': 'wpawn',
         'g2': 'wpawn',
         'h2': 'wpawn',
         'a7': 'bpawn',
         'b7': 'bpawn',
         'c7': 'bpawn',
         'd7': 'bpawn',
         'e7': 'bpawn',
         'f7': 'bpawn',
         'g7': 'bpawn',
         'h7': 'bpawn',
         'a1': 'wRook',
         'b1': 'wknight',
         'c1': 'wbishop',
         'f1': 'wbishop',
         'g1': 'wknight',
         'h1': 'wrook',
         }


def isvalidchessboard(initialboard):
    firstcheckgood = False
    secondcheckgood = False
    thirdcheckgood = False
    fourthcheckgood = False
    fifthcheckgood = False
    boardrows = ["a", "b", "c", "d", "e", "f", "g", "h"]
    chesspieces = ["pawn", "knight", "bishop", "rook", "queen", 'king']
    # First Check - verify all Valid Coordinates between A1 and H8:

    trialboard = {k.lower(): v.lower() for k, v in initialboard.items()}

    coordinates = (list(trialboard.keys()))
    for chessrow in coordinates:
        if chessrow[0] in boardrows:
            if 0 < int(chessrow[1:]) < 9:
                firstcheckgood = True
            else:
                firstcheckgood = False
                break

        else:
            firstcheckgood = False
            break
    # Second Check - Verify only valid Chess Pieces and Colors allowed
    pieces = (list(trialboard.values()))
    for color in pieces:
        if color[0] == 'w' or color[0] == 'b':
            if color[1:] in chesspieces:
                secondcheckgood = True
            else:
                secondcheckgood = False
                break
        else:
            secondcheckgood = False
            break

    # Third and Fourth Checks - Verify counts of Kings = 1 and Pawns less than 9
    # Had to work a little harder here to get an uppercase check correct - note 'Bking' works here

    allpieces = list(trialboard.values())
    finalpieces = []

    for i in range(len(allpieces)):
        allpieces[i] = allpieces[i]
        finalpieces.append(allpieces[i])

    if finalpieces.count('wking') == 1 and finalpieces.count('bking') == 1:
        thirdcheckgood = True

    if finalpieces.count('wpawn') < 9 and finalpieces.count('bpawn') < 9:
        fourthcheckgood = True

    # Fifth Check - Verify total number of pieces per side less than 17

    whitepieces = 0
    blackpieces = 0
    for color in finalpieces:

        if color[0] == 'w':
            whitepieces += 1
        elif color[0] == 'b':
            blackpieces += 1
    if whitepieces < 17 and blackpieces < 17:
        fifthcheckgood = True

    # Test lines within the function if needed to verify checks
    # print(f'Valid Coordinates between A1 and H8: {firstcheckgood}')
    # print(f'Valid colors and pieces: {secondcheckgood}')
    # print(f'Only one king per side: {thirdcheckgood}')
    # print(f'Only 8 pawns or less per side: {fourthcheckgood}')
    # print(f'Only 16 pieces or less per side: {fifthcheckgood}')

    if firstcheckgood and secondcheckgood and thirdcheckgood and fourthcheckgood and fifthcheckgood:
        return True
    else:
        return False


print(isvalidchessboard(board))

