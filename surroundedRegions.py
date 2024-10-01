board = [["X","O","X","X"],["O","X","O","X"],["X","O","X","O"],["O","X","O","X"]]

def solve(board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        # Create a duplicate board full of Xs
        # Examine the outer ring of the input board
        # If an O is found, mark it as an O on the dupe board
        # Then explore every connected O, also marking on the dupe board
        # Do not explore if the dupe board already has that cell marked

        # Then compare every cell of the input board to the dupe board, except the outer ring
        # If the dupe board has a cell marked as an X, the input board should be too


        m = len(board[0])
        n = len(board)

        answerBoard = [["X" for i in range(m)] for j in range(n)]

        def explore(x, y):

            if board[y][x] == "O" and answerBoard[y][x] == "X":
                answerBoard[y][x] = "O"
            else:
                return

            if x > 0:
                explore(x - 1, y)  
            if x < m - 1:
                explore(x + 1, y)
            if y > 0:
                explore(x, y - 1)
            if y < n - 1:
                explore(x, y + 1)

        for i in range(m - 1):
            explore(i, 0)
        for i in range(n - 1):
            explore(m - 1, i)
        for i in range(m - 1, 1, -1):
            explore(i, n - 1)
        for i in range(n - 1, 1, -1):
            explore(0, i)

        for i in range(1, n - 1):
            for j in range(1, m - 1):
                if answerBoard[i][j] == "X" and board[i][j] == "O":
                    board[i][j] = "X"

solve(board)