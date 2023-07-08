'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    follower = 0
    followed_by = 0
    for x in social_graph[from_member]['following']:
        if to_member in x:
            follower = 1
        else:
            continue
    for y in social_graph[to_member]['following']:
        if from_member in y:  
            followed_by = 1
        else:
            continue
    if follower and followed_by == 1:
        return('friends')
    elif follower == 1:
        return('follower')
    elif followed_by == 1:
        return('followed by')
    else:
        return('no relationship')            


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    size_count = 0
    win_checker = 0
    column_counter = 0
    row_counter = 0
    X_count = 0
    O_count = 0
    for a in board:
        size_count += 1
    #check horizontal:
    for x in board:
        if win_checker == 0:
            for y in x:
                if y == 'X':
                    X_count += 1
                elif y == 'O':
                    O_count += 1
                else:
                    continue
            if X_count == len(x):
                win_checker = 1
                continue
            elif O_count == len(x):
                win_checker = 1
                continue
            else: 
                X_count = 0
                O_count = 0
        else:
            continue
    #check vertical:
    while column_counter < size_count:
        if win_checker == 0:
            while row_counter < size_count:
                if board[row_counter][column_counter] == 'X':
                    X_count += 1
                elif board[row_counter][column_counter] == 'O':
                    O_count += 1
                elif board[row_counter][column_counter] == '':
                    row_counter += 1
                    continue
                row_counter += 1
            if X_count == size_count:
                    win_checker = 1
                    continue
            elif O_count == size_count:
                    win_checker = 1
                    continue
            else: 
                    X_count = 0
                    O_count = 0
            row_counter = 0
            column_counter += 1
        else:
            column_counter += 1
            continue
    #check diagonal:
    #1st Diagonal
    column_counter = 0
    row_counter = 0
    if win_checker == 0:
        while row_counter < size_count:
            if board[row_counter][column_counter] == 'X':
                X_count += 1
            elif board[row_counter][column_counter] == 'O':
                O_count += 1
            elif board[row_counter][column_counter] == '':
                row_counter += 1
                column_counter += 1
                continue
            row_counter += 1
            column_counter += 1
        if X_count == size_count:
            win_checker = 1
        elif O_count == size_count:
            win_checker = 1
        else: 
            X_count = 0
            O_count = 0

    #2nd Diagonal
    column_counter = 0
    row_counter = size_count - 1
    if win_checker == 0:
        while column_counter < size_count:
            if board[row_counter][column_counter] == 'X':
                X_count += 1
            elif board[row_counter][column_counter] == 'O':
                O_count += 1
            elif board[row_counter][column_counter] == '':
                row_counter -= 1
                column_counter += 1
                continue
            row_counter -= 1
            column_counter += 1
        if X_count == size_count:
            win_checker = 1
        elif O_count == size_count:
            win_checker = 1
        else: 
            X_count = 0
            O_count = 0

    #Win checker
    if win_checker == 0:
        return('NO WINNER')
    else: 
        if X_count == len(x):
            return('X Wins')
        elif O_count == len(x):
            return('O wins')



def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    time_dummy = ''
    time_spent = 0
    time_add = ''
    search_condition = 0
    new_first = first_stop
    loop_search = 0
    legs_list = list(route_map.keys())
    while loop_search == 0:
        for x in legs_list:
            if search_condition == 0:
                if new_first in x[0]:
                    time_dummy = str(legs[x])
                    for y in time_dummy:
                        if y.isnumeric() == True:
                            time_add = time_add + y
                        else:
                            continue
                    time_spent = time_spent + int(time_add)
                    time_dummy = ''
                    time_add = ''
                    new_first = x[1]
                    search_condition = 1
                    if second_stop in x[1]:
                        loop_search = 1
                        search_condition = 1
                    else:
                        continue
                else:
                    continue
            else:
                continue
        search_condition = 0
    return(time_spent)