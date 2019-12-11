from tictactoe import determineWinner

def test_determineWinner_checks_full_rows():
    # Given player 1 has a top row full on the board
    board = [
        [1,1,1],
        [0,0,0],
        [2,2,0]
    ]

    # When I attempt to determine a winner
    actual = determineWinner(board)

    # Then player 1 is the winner
    expected = 1
    assert actual == expected

def test_determineWinner_determines_no_winner():
    # Given no player has a winning pattern
    board = [
        [1, 2, 1],
        [0, 2, 0],
        [1, 0, 0]
    ]

    # When I attempt to determine a winner
    actual = determineWinner(board)

    # Then no player is the winner
    expected = 0
    assert actual == expected

def test_determineWinner_checks_full_columns():
    # Given player 2 has a full column (second column)
    board = [
        [2, 2, 1],
        [1, 2, 0],
        [1, 2, 1]
    ]

    # When I attempt to determine a winner
    actual = determineWinner(board)

    # Then player 2 is the winner
    expected = 2
    assert actual == expected

def test_determineWinner_checks_full_diagnoal_top_left_to_bottom_right():
    # Given player 1 has a full diagonal (top left to bottom right)
    board = [
        [1, 2, 0],
        [2, 1, 0],
        [0, 2, 1]
    ]

    # When I attempt to determine a winner
    actual = determineWinner(board)

    # Then player 1 is the winner
    expected = 1
    assert actual == expected

def test_determineWinner_checks_full_diagnoal_bottom_left_to_top_right():
    # Given player 2 has a full diagonal (bottom left to top right)
    board = [
        [0, 1, 2],
        [1, 2, 0],
        [2, 1, 1]
    ]

    # When I attempt to determine a winner
    actual = determineWinner(board)

    # Then player 2 is the winner
    expected = 2
    assert actual == expected