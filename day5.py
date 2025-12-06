def solve_1(x):
    ranges, ids = x.split("\n\n")
    ranges = [tuple(map(int, line.split("-"))) for line in ranges.split("\n")]
    ids = [int(i) for i in ids.split("\n")]
    
    return sum(any(start <= i <= end for start, end in ranges) for i in ids)


def solve_2(x):
    ranges, ids = x.split("\n\n")
    ranges = [tuple(map(int, line.split("-"))) for line in ranges.split("\n")]

    ranges.sort(key = lambda x: x[0])
    min_start = 0
    ans = 0
    for start, end in ranges:
        start = max(start, min_start)
        ans += max(0, end - start + 1)
        min_start = max(min_start, end + 1)
    return ans


# ============= TEMPLATE =============
from utils.input_reader import load

RUN_SAMPLE_ONLY = False

sample_data, data = load(
    file_path = __file__,
    sample_file_name = "sample.txt",
    input_file_name = "input.txt",
    row_delimeter = None,
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

