N = 100
DIAL_INIT = 50


def solve_1(x):
    ans = 0
    curr = DIAL_INIT
    for instr in x:
        amount = int(instr[1:])
        if instr[0] == "L":
            curr -= amount
        else:
            curr += amount
        ans += curr % N == 0
    return ans


def solve_2(x):
    ans = 0
    curr = DIAL_INIT
    for instr in x:
        amount = int(instr[1:])
        if instr[0] == "L":
            min_val = curr - amount
            max_val = curr - 1
            curr -= amount
        else:
            min_val = curr + 1
            max_val = curr + amount
            curr += amount
        ans += (max_val // N) - ((min_val - 1) // N)
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

