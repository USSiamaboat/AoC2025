def solve_1(x):
    pass


def solve_2(x):
    pass


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

