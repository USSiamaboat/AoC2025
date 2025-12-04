from itertools import product


ROLL = "@"
EMPTY = "."
MAX_ROLLS = 3
INF = MAX_ROLLS + 8 + 1 # Max 8 neighbors -> Min = MAX_ROLLS + 1 -> Never accessible


OFFS = [(di,dj) for di in (-1,0,1) for dj in (-1,0,1) if not (di==0 and dj==0)]
def neighbors(i, j, N, M):
    return [(i+di, j+dj) for di, dj in OFFS if (0 <= i+di < N) and (0 <= j+dj < M)]


def adj_rolls(grid, i, j):
    if grid[i][j] == EMPTY:
        return INF # Empty is never accessible
    N, M = len(grid), len(grid[0])
    return sum(grid[k][l] == ROLL for k, l in neighbors(i, j, N, M))


def solve_1(x):
    x = [list(r) for r in x]
    N, M = len(x), len(x[0])
    return sum(adj_rolls(x, i, j) <= MAX_ROLLS for i, j in product(range(N), range(M)))


def solve_2(x):
    x = [list(r) for r in x]
    N, M = len(x), len(x[0])
    ans = 0
    adj_counts = [[adj_rolls(x, i, j) for j in range(M)] for i in range(N)]
    stack = [(i, j) for i, j in product(range(N), range(M)) if adj_counts[i][j] <= MAX_ROLLS]
    while stack:
        i, j = stack.pop()
        adj_counts[i][j] = INF # "Inf" adj = never consider again = removed
        for k, l in neighbors(i, j, N, M):
            adj_counts[k][l] -= 1
            if adj_counts[k][l] == MAX_ROLLS:
                stack.append((k, l))
        ans += 1
    return ans


# ============= TEMPLATE =============
from utils.input_reader import load

RUN_SAMPLE_ONLY = False

sample_data, data = load(
    file_path = __file__,
    sample_file_name = "sample.txt",
    input_file_name = "input.txt",
    row_delimeter = "\n",
    col_delimeter = None
)

print("PART 1:")
print("SAMPLE:", solve_1(sample_data))
if not RUN_SAMPLE_ONLY:
    print("INPUT:", solve_1(data))

print()

print("PART 2:")
print("SAMPLE:", solve_2(sample_data))
if not RUN_SAMPLE_ONLY:
    print("INPUT:", solve_2(data))
# ============= TEMPLATE =============

