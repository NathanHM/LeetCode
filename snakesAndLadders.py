board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]

def snakesAndLadders(board):
        # Rearrange array - for simplicity
        board = board[::-1]

        for i in range(1, len(board), 2):
            board[i] = board[i][::-1]

        new_board = []

        for i in range(len(board)):
            new_board.extend(board[i])

        
        position = 0
        moves = 0
        queue = [(position, moves)]


        while len(queue) > 0:

            (position, moves) = queue.pop(0)

            if position + 1 == len(new_board):
                return moves

            for i in range(1, 7):
                if position + i < len(new_board) and new_board[position + i] > 0:
                    queue.append((new_board[position + i] - 1, moves + 1))
                    new_board[position + i] = 0

            i = min(position + 6, len(new_board) - 1)
            while position < i and new_board[i] > -1:
                i -= 1

            if i > position:
                queue.append((i, moves + 1))

        return -1

print(snakesAndLadders(board))