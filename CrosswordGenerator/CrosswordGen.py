def CrosswordGen(Words, TheGridSize):
    # The input words
    n = TheGridSize  # The grid size
    GridSize = n * 3 - 1  # The possible places

    # Making The Vertical and horizontal grids
    VGrid = [[None] * GridSize for x in range((n - len(Words[0])) * 2 + len(Words[0]) + n)]

    # Setting the first word in the Vertical grid
    for i in range(len(Words[0])):
        VGrid[i + (n - len(Words[0]))+1][int(GridSize / 2)] = Words[0][i]

    Answers = []
    def Recertion(Grid, WordLeft):
        # if there is no word left finish the Recertion and add to Answers if the answer is new
        if len(WordLeft) == 0:
            #Removes the extra lines
            for i in range(len(Grid[0])):
                if not [Grid[j][i] is None for j in range(len(Grid))].count(False) == 0:
                    break
            Grid = [row[i:i+n] for row in Grid]
            for i1 in range(len(Grid)):
                if not [Grid[i1][j] is None for j in range(len(Grid[0]))].count(False) == 0:
                    break
            Grid = Grid[i1:i1+n]
            if Grid not in Answers:
                Answers.append(Grid)
        else:
            # Checks every Char in the grid that isnt None
            for Line in range(len(Grid)):
                for Char in range(len(Grid[Line])):
                    if not Grid[Line][Char] is None:
                        # if the char is in a new word start an adding presiger
                        for Word in WordLeft:
                            for i in range(len(Word)):
                                if Grid[Line][Char] == Word[i]:
                                    # if there weren't be any errors try placing it Vertically
                                    if Char - i >= 0 and Char + len(Word) - 1 < len(Grid[Line]):
                                        # if the word can fit in the place place it and go deeper in the Recetrion
                                        if [Grid[Line][Char - i + i1] == Word[i1] or ((Grid[Line][Char - i + i1] is None) and (Grid[Line + 1][Char - i + i1] is None) and (Grid[Line - 1][Char - i + i1] is None)) for i1 in range(len(Word))].count(False) == 0:
                                            if Grid[Line][Char - i - 1] is None and Grid[Line][Char - i + len(Word)] is None:
                                                NewGrid = [row[:] for row in Grid]
                                                for i2 in range(len(Word)):
                                                    NewGrid[Line][Char - i + i2] = Word[i2]
                                                # Checks if the grid uesd is not our of bounds
                                                if not [[NewGrid[j][j1] is None for j in range(len(NewGrid))].count(False) == 0 for j1 in range(len(NewGrid[Line]))].count(False) > n:
                                                    Recertion(NewGrid, [n1 for n1 in WordLeft if n1 != Word])
                                    # if there werent be any errors try placing it horizontaly
                                    if Line - i >= 0 and Line + len(Word) - 1 < len(Grid):
                                        # if the word can fit in the place place it and go deeper in the Recetrion
                                        if [Grid[Line - i + i1][Char] == Word[i1] or ((Grid[Line - i + i1][Char] is None) and (Grid[Line - i + i1][Char+1] is None) and (Grid[Line - i + i1][Char-1] is None)) for i1 in range(len(Word))].count(False) == 0:
                                            if Grid[Line - i - 1][Char] is None and Grid[Line - i + len(Word)][Char] is None:
                                                NewGrid = [row[:] for row in Grid]
                                                for i1 in range(len(Word)):
                                                    NewGrid[Line - i + i1][Char] = Word[i1]
                                                # Checks if the grid used is not our of bounds
                                                if not [[NewGrid[j1][j] is None for j in range(len(NewGrid[Line]))].count(False) == 0 for j1 in range(len(NewGrid))].count(False) > n:
                                                    Recertion(NewGrid, [n1 for n1 in WordLeft if n1 != Word])

    # Callingthe recertion
    Recertion(VGrid, Words[1:])

    # Priniting the Answers
    #for Grid in Answers:
    #    for g in Grid:
    #        print(g)
    #    print()
##
    #print(Answers)
    #print(len(Answers))
    if len(Answers) == 0:
        return [[[None] * n for x in range(n)]]
    else:
        return Answers

print(CrosswordGen(["bauble", "advent", "tinsel", "bing"], 7))