from collections import defaultdict


def solve_1(x):
    x = [list(y) for y in x]
    curr = {x[0].index("S"): 1}
    ans = 0
    for row in x[1:]:
        splitters = set(i for i, val in enumerate(row) if val == "^")
        next_curr = set()
        both = splitters.intersection(curr)
        ans += len(both)
        for v in curr:
            if v in both:
                next_curr.add(v-1)
                next_curr.add(v+1)
            else:
                next_curr.add(v)
        curr = next_curr
    return ans


def solve_2(x):
    x = [list(y) for y in x]
    curr = {x[0].index("S"): 1}
    for row in x[1:]:
        splitters = set(i for i, val in enumerate(row) if val == "^")
        next_curr = defaultdict(int)
        both = splitters.intersection(curr)
        for v in curr:
            if v in both:
                next_curr[v-1] += curr[v]
                next_curr[v+1] += curr[v]
            else:
                next_curr[v] += curr[v]
        curr = next_curr
    return sum(curr.values())


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

