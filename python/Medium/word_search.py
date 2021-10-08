class Solution:

    rowLength = 0
    columnLength = 0
    board = [[]]
    traversed = {}

    def word_search(self, search, row, column):

        self.traversed[str(row) + "," + str(column)] = True

        if search == "":
            return True

        #top
        if row != 0 and str(row - 1) + "," + str(column) not in self.traversed:
            if self.board[row - 1][column] == search[0]:
                if self.word_search(search[1:], row - 1, column):
                    return True
        # left
        if column != 0 and str(row) + "," + str(column - 1) not in self.traversed and self.board[row][column - 1] == search[0]:
            if self.word_search(search[1:], row, column - 1):
                return True

        # right
        if column + 1 < self.columnLength and str(row) + "," + str(column + 1) not in self.traversed and self.board[row][column + 1] == search[0]:
            if self.word_search(search[1:], row, column + 1):
                return True

        # bottom
        if row + 1 < self.rowLength and str(row + 1) + "," + str(column) not in self.traversed and self.board[row + 1][column] == search[0]:
            if self.word_search(search[1:], row + 1, column):
                return True

        return False

    def exist(self, board: [[str]], word: str) -> bool:

        self.rowLength = len(board)
        self.columnLength = len(board[0])
        self.board = board

        first_letter = word[0]
        i = j = 0
        for letter_list in board:
            j = 0
            for letter in letter_list:
                if letter == first_letter:
                    print("Found first letter - lets see")
                    self.traversed = {}
                    result = self.word_search(word[1:], i, j)
                    print("Found some result")
                    if result:
                        return result
                j += 1
            i += 1


if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    solution = Solution()
    print(solution.exist(board, word))