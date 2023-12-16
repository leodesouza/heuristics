import re


class Scp:
    def __init__(self):
        self.seed = 1234567
        self.scp_file = ""
        self.output_file = "output.txt"

        # Instance static variables
        self.n = 0
        self.m = 0
        self.rows = []  # rows[i] that are covered by column i
        self.col = []  # col[i] columns that cover row i
        self.ncol = []  # ncol[i] number of columns that cover row i
        self.nrow = []  # nrow[i] number of rows that are covered by column i
        self.cost = []  # cost[i] cost of column i

        # solution variables
        x = []
        y = []
        fx = 0  # sum of the cost of the columns selected in the solution

        # Dynamic variables
        col_cover = []
        ncol_cover = 0

    def open_file(self, scp_file):
        self.scp_file = scp_file
        with open(scp_file, 'r') as file:

            rows_columns_number = list(map(int, file.readline().split()))

            self.m = rows_columns_number[0]  # number of rows
            self.n = rows_columns_number[1]  # number of columns

            # cost of all columns
            self.cost = list(map(int, file.readline().split()))

            # Info of the columns that cover each row
            for i in range(self.m):

                ncol_i = int(file.readline().strip())
                self.ncol.append(ncol_i)

                col_i = list(map(int, file.readline().split()))
                if len(col_i) != ncol_i:
                    # throws an exception
                    pass
                self.col.append([x - 1 for x in col_i])

            # Info of rows that are covered by each column
            self.rows = [[] for _ in range(self.n)]
            self.nrow = [0] * self.n
            k = [0] * self.n

            for i in range(self.m):
                for h in range(self.ncol[i]):
                    self.nrow[self.col[i][h]] += 1

            for j in range(self.n):
                self.rows[j] = [0] * self.nrow[j]
                k[j] = 0

            for i in range(self.m):
                for h in range(self.ncol[i]):
                    self.rows[self.col[i][h]][k[self.col[i][h]]] = i
                    k[self.col[i][h]] += 1

    def print_instance(self, level):
        print('************************************************')
        print(f'SCP INSTANCE {self.scp_file}')
        print()
        print('PROBLEM SIZE')
        print(f'm = {self.m}\t n = {self.n}')
        print()

        if level >= 1:
            print('COLUMN COST')
            print(' '.join(map(str, self.cost)))
            print()
            print(f'NUMBER OF ELEMENTS COVERED BY SUBSET 1 is {self.nrow[0]}')
            print(' '.join(map(str, self.rows[0])))
            print(f'NUMBER OF SUBSETS COVERING ELEMENT 1 is {self.ncol[0]}')
            print(' '.join(map(str, self.col[0])))
            print()
        print('*************************************************\n')

    def get_subets_and_costs(self):
        subs_and_costs = [(self.rows[i], self.cost[i]) for i in range(len(self.rows))]
        return subs_and_costs
