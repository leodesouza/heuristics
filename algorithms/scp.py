import re


class Scp:
    def __init__(self):
        self.seed = 1234567
        self.scp_file = ""
        self.output_file = "output.txt"

        # Instance static variables
        self.n = 0
        self.m = 0
        self.row = []
        self.col = []
        self.ncol = []
        self.nrow = []
        self.cost = []

        # solution variables
        x = []
        y = []
        fx = 0  # sum of the cost of the columns selected in the solution

        # Dynamic variables
        col_cover = []
        ncol_cover = 0

    def open_file(self, filename):
        with open(filename, 'r') as file:

            rows_columns_number = list(map(int, file.readline().split()))
            # number of rows
            self.m = rows_columns_number[0]
            # number of columns
            self.n = rows_columns_number[1]

            # cost of all columns
            self.cost = list(map(int, file.readline().split()))

            # Info of the columns that cover each row
            for _ in range(self.m):
                line = list(map(int, file.readline().split()))
                self.ncol.append(line[0])
                self.col.append(line[1:])

            # Info of rows that are covered by each column
            self.row = [[] for _ in range(self.n)]
            self.nrow = [0] * self.n
            for i in range(self.m):
                for h in range(self.ncol[i]):
                    self.col[i][h] -= 1
                    self.row[self.col[i][h]].append(i)
                    self.nrow[self.col[i][h]] += 1
