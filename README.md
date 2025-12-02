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

**Timing**: `00:18:12`, `00:30:30`

Another slow day, but this time partially on purpose. This was one of the puzzles where regex works really well and is fast to write, but I personally think it's much more interesting way to use some math tricks instead of the "cop-out" solution that is regex. I was still slow at implementing the math, which I need to work on.

#### Part 1

In my opinion, the interesting part of this problem is that the ranges can theoretically be arbitrarily large (though the actual ranges in my puzzle input ended up being not that large).

The key insight I found is that an invalid ID $X = A_1 \cdots A_n A_1 \cdots A_n$ is divisible by $10^n + 1$ (alternatively, $11$ with $n-1$ zeroes inserted between the ones). Let $F_{2d, 2} = 10^d + 1$ be the corresponding "factor" for a candidate ID with $d$ digits. (ex. $F_{4, 2} = 101$). Notice that $10^{d - 1} \leq X / F_{d, 2} \leq 10^d - 1$ since $X / F_{n, 2} = A_1 \cdots A_n$.

When considering the range $\text{START}-\text{END}$, we can rewrite the problem as finding the sum of all IDs $X$ such that $F_{d, 2} | X$ and $\text{START}/ F_{d, 2} \leq X / F_{d, 2} \leq \text{END} / F_{k, 2}$.

Notice the bounds can be tightened to $\max(10^{d-1}, \lceil \text{START}/ F_{d, 2} \rceil)$ and $\min(10^d - 1, \lfloor \text{END} / F_{d, 2} \rfloor)$ because $10^{d - 1} \leq X / F_{d, 2} \leq 10^d - 1$. We can see that these must be the tightest possible bounds, which are also inclusive on both ends.

We can also bound $2d$ between the number of digits of $\text{START}$ and $\text{END}$.

Then, we can simply iterate through valid $d$ and generate the sets of invalid IDs by incrementing by $F_{d,2}$ within the bounds for each $d$. Finally, we sum these IDs.

#### Part 2

The solution for this part is very similar to the previous part. This time, we need to expand the definition $F_{d, k}$ to be the number with $k$ evenly spaced ones (including first and last digits) separated by $d / k - 1$ zeros between the ones. (ex. $F_{9, 3} = 1001001$). These new factors have the useful property that an ID $X$ with $d$ digits composed of a sequence repeating $k$ times is divisible by $F_{d, k}$ and $X / F_{d, k}$ is the repeating sequence, just like before. Notice that the previous definition of $F$ is a special case of this version, so this makes sense.

Most of the essential logic from part 1 still applies here, we just need to also iterate through valid $k$ (bounded by $2 \leq k \leq d$) in addition to $d$ when generating sets of invalid IDs and finding their sum.

One thing that we need to be careful with here in implementation is double-counting of the same invalid ID. For example, an 8-digit invalid ID with the same digit repeated 8 times will be caught by $k = 1, 2, 4, 8$. Therefore, we need to be careful to only sum such IDs exactly once.

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
