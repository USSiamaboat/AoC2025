from functools import cache


def solve_1(x):
    x = map(lambda y: map(int, y), x) # Convert to Iterator[Iterator[int]]
    ans = 0
    for bank in x:
        best_battery = 0
        best_joltage = 0
        for battery in bank:
            best_joltage = max(best_joltage, 10 * best_battery + battery)
            best_battery = max(best_battery, battery)
        ans += best_joltage
    return ans


@cache
def dp(bank, i, k):
    if (k == 0) or (len(bank) - i < k):
        return 0
    return max(bank[i] * 10**(k-1) + dp(bank, i+1, k-1), dp(bank, i+1, k))


def solve_2(x):
    x = map(lambda y: tuple(map(int, y)), x) # Convert to Iterator[Tuple[int]]
    return sum(dp(bank, 0, 12) for bank in x)


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

