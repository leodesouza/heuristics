import sys


def mymalloc(size):
    s = [0] * size
    if s is None:
        print("malloc : Not enough memory.", file=sys.stderr)
        sys.exit(EXIT_FAILURE)
    return s


def error_reading_file(text):
    print(text)
    sys.exit(EXIT_FAILURE)


# Algorithm parameters
seed = 1234567
scp_file = ""
output_file = "output.txt"

# Variables to activate algorithms
ch1 = 0
ch2 = 0
bi = 0
fi = 0
re = 0

# Instance static variables
m = 0  # number of rows
n = 0  # number of columns
row = []  # row[i] rows that are covered by column i
col = []  # col[i] columns that cover row i
ncol = []  # ncol[i] number of columns that cover row i
nrow = []  # nrow[i] number of rows that are covered by column i
cost = []  # cost[i] cost of column i

# Solution variables
x = []  # x[i] 0,1 if column i is selected
y = []  # y[i] 0,1 if row i covered by the actual solution
fx = 0  # sum of the cost of the columns selected in the solution (can be partial)

# Dynamic variables
col_cover = []  # col_colver[i] selected columns that cover row i
ncol_cover = 0  # number of selected columns that cover row i


def usage():
    print("\nUSAGE: lsscp [param_name, param_value] [options]...\n")
    print("Parameters:")
    print("  --seed : seed to initialize random number generator")
    print("  --instance: SCP instance to execute.")
    print("  --output: Filename for output results.")
    print("Options:")
    print("  --ch1: random solution construction")
    print("  --ch2: static cost-based greedy values.")
    print("  --re: applies redundancy elimination after construction.")
    print("  --bi: best improvement.\n")


def read_parameters(argv):
    global seed, scp_file, output_file, ch1, ch2, bi, fi, re
    i = 1
    while i < len(argv):
        if argv[i] == "--seed":
            seed = int(argv[i + 1])
            i += 2
        elif argv[i] == "--instance":
            scp_file = argv[i + 1]
            i += 2
        elif argv[i] == "--output":
            output_file = argv[i + 1]
            i += 2
        elif argv[i] == "--ch1":
            ch1 = 1
            i += 1
        elif argv[i] == "--ch2":
            ch2 = 1
            i += 1
        elif argv[i] == "--bi":
            bi = 1
            i += 1
        elif argv[i] == "--fi":
            fi = 1
            i += 1
        elif argv[i] == "--re":
            re = 1
            i += 1
        else:
            print("\nERROR: parameter", argv[i], "not recognized.")
            usage()
            sys.exit(EXIT_FAILURE)

    if not scp_file:
        print("Error: --instance must be provided.")
        usage()
        sys.exit(EXIT_FAILURE)


def read_scp(filename):
    global m, n, cost, col, ncol, row, nrow
    with open(filename, "r") as fp:
        m = int(fp.readline().strip())  # number of rows
        n = int(fp.readline().strip())  # number of columns

        # Cost of the n columns
        cost = list(map(int, fp.readline().split()))

        # Info of columns that cover each row
        col = []
        ncol = []
        for _ in range(m):
            line = list(map(int, fp.readline().split()))
            ncol.append(line[0])
            col.append(line[1:])

        # Info of rows that are covered by each column
        row = [[] for _ in range(n)]
        nrow = [0] * n
        for i in range(m):
            for h in range(ncol[i]):
                col[i][h] -= 1
                row[col[i][h]].append(i)
                nrow[col[i][h]] += 1


def print_instance(level):
    print("**********************************************")
    print(f"  SCP INSTANCE: {scp_file}")
    print(f"  PROBLEM SIZE\t m = {m}\t n = {n}")

    if level >= 1:
        print("  COLUMN COST:")
        print(" ".join(map(str, cost)))
        print()
        print(f"  NUMBER OF ROWS COVERED BY COLUMN 1 is {nrow[0]}")
        print(" ".join(map(str, row[0])))
        print(f"  NUMBER OF COLUMNS COVERING ROW 1 is {ncol[0]}")
        print(" ".join(map(str, col[0])))
        print()

    print("**********************************************\n")


def initialize():
    pass


def finalize():
    global row, col, nrow, ncol, cost
    del row
    del col
    del nrow
    del ncol
    del cost


def main(argv):
    global seed, scp_file, output_file
    read_parameters(argv)
    # Set seed
    # Note: Python does not directly set the seed for random number generators.
    #       You need to use random.seed() before using any random functions.

    read_scp(scp_file)
    print_instance(1)
    finalize()


if __name__ == "__main__":
    main(sys.argv)
