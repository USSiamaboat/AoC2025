# Advent of Code 2025

I've been doing Advent of Code since the 2023 iteration and participated to compete on timings, but the quality of my solutions and clarity of my approach have been very inconsistent.

This year, I will be focusing on writing up cleaner solutions and explanations of my approach + thoughts on my performance. My solves will probably be much slower than before, but the solutions are hopefully going to be much better.

## Structure

Note that this repo will *not* run out of the box because all input files are untracked ([see this FAQ](https://adventofcode.com/2025/about#faq_copying)). Adding valid `sample.txt` and `input.txt` files to the correct directories fixes this.

For day `N`, my solution is `dayN.py` and uses the inputs stored in the `dayN` directory.
By default, the included sample input is assumed to be at `dayN/sample.txt` and the puzzle input to be at `dayN/input.txt`.

For example, `day1.py` assumes the day 1 files are at `day1/sample.txt` and `day1/input.txt`

## Daily Notes

<details>
<summary><b>Day 1</b></summary>

**Timing**: `00:07:16`, `00:27:55`

This was alot slower than it needed to be, partially because my train was delayed and I didn't open my computer until ~5 mins. For B, I got caught by a combination of edge cases, stubbornness to make bad approaches work, and was probably thinking poorly from being tired. Overall, pretty bad but not hard to fix.

#### Part 1

Counting the number of times we land on 0 is the same as counting the number of times we land a multiple of 100, so we can simply track an "unwrapped" value (no mod, just add or subtract) and count. One consideration is for very large inputs, the unwrapped value we track can itself become very large, but Python allows for arbitrarily large numbers within system limits, so I think this is okay for inputs like the typical AoC inputs.

#### Part 2

For each instruction, we can compute inclusive lower and upper bounds `min` and `max` for the (unwrapped) numbers that we pass by or land on. Then, the number of 0s we encounter while turning is the number of multiples of 100 within this bound. This can be computed with some fiddly int division: `(max // 100) - ((min - 1) // 100)`

It's also completely possible to simply just brute force every tick and get a result very quickly, but that's super boring and not helpful since there isn't a global leaderboard anymore.

</details>

<details>
<summary><b>Day 2</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 3</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 4</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 5</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 6</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 7</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 8</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 9</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 10</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 11</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>

<details>
<summary><b>Day 12</b></summary>

**Timing**: Unsolved

#### Part 1

Unsolved

#### Part 2

Unsolved

</details>
