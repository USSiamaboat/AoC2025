from functools import reduce

def solve_1(x):
    nums = [list([int(z) for z in y.split(" ") if z.strip()]) for y in x[:-1]]
    ops = [y for y in x[-1] if y.strip()]

    ans = 0

    for i in range(len(nums[0])):
        col = [nums[j][i] for j in range(len(nums))]
        if ops[i] == "+":
            ans += sum(col)
        else:
            ans += reduce(lambda a,b: a*b, col, 1)
    
    return ans

def solve_2(x):
    # Transpose to make numbers L-R
    transposed = [[x[i][j] for i in range(len(x))] for j in range(len(x[0]))]
    transposed += [[" "] * len(x)] # Add blanks to signal end of problem
    
    ans = 0
    nums = []
    curr_op = ""

    for row in transposed:
        curr_op = row[-1].strip() or curr_op
        if "".join(row).strip() == "": # Blank row
            if curr_op == "*":
                ans += reduce(lambda a,b: a*b, nums, 1)
            else:
                ans += sum(nums)
            nums = []
        else:
            nums.append(int("".join(row[:-1])))

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

