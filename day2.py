from math import floor, ceil

int_digits = lambda n: len(str(abs(n)))

def get_ranges(x):
    return [[int(z) for z in y.split("-")] for y in x[0]]


def get_invalids(start, end, k):
    invalids = set()

    for length in range(int_digits(start), int_digits(end) + 1):
        if length % k != 0:
            continue
        
        factor = int(("0" * (length // k - 1) + "1") * k)

        min_sequence = max(ceil(start / factor), 10**(length // k - 1))
        max_sequence = min(floor(end / factor), 10**(length // k) - 1)

        invalids.update(range(min_sequence*factor, (max_sequence + 1)*factor, factor))

    return invalids


def solve_1(x):
    ans = 0
    
    for start, end in get_ranges(x):
        ans += sum(get_invalids(start, end, 2))

    return ans


def solve_2(x):
    ans = 0

    for start, end in get_ranges(x):
        invalids = set()
        for k in range(2, int_digits(end)+1):
            invalids.update(get_invalids(start, end, k))
        ans += sum(invalids)

    return ans


# ============= TEMPLATE =============
from utils.input_reader import load

RUN_SAMPLE_ONLY = False

sample_data, data = load(
    file_path = __file__,
    sample_file_name = "sample.txt",
    input_file_name = "input.txt",
    row_delimeter = "\n",
    col_delimeter = ","
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

