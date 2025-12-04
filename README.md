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

An invalid ID has the form $X = SS$, where $S$ is an $n$-digit sequence with no leading zeros.
Such an $X$ is divisible by $F_{n,2} = 10^n + 1$.

Since $S$ is $n$ digits long, $10^{n-1} \leq S \leq 10^n - 1$

For a range $\text{START} – \text{END}$, we want all $X$ such that
$\text{START} \leq X \leq \text{END}$ and $F_{n,2} \mid X$.

Writing $X = S \cdot F_{n,2}$ gives
$\left\lceil \frac{START}{F_{n,2}} \right\rceil \leq S \leq \left\lfloor \frac{END}{F_{n,2}} \right\rfloor$

Combining with the digit constraint gives the tightest possible integer bounds:

$S_{\min} = \max\left(10^{n-1}, \Big\lceil \tfrac{START}{F_{n,2}} \Big\rceil \right),\quad S_{\max} = \min\left(10^{n}-1, \Big\lfloor \tfrac{END}{F_{n,2}} \Big\rfloor \right)$

Every invalid IDs can be written as $X = S \cdot F_{n,2}$ for some $S \in S_{\min},\dots,S_{\max}$

Only $n$ such that $2n$ is between the digit counts of $\text{START}$ and $\text{END}$ might work, so we can iterate only within these $n$ and sum the invalid IDs found.

#### Part 2

Following a similar approach to part 1, we can find the corresponding factor $F_{n,k} = \sum_{i=0}^{k-1} 10^{in}$ the number with $k$ ones spaced every $n$ digits (ex. $F_{3,3}=1001001$). We can simply substitute this $F$ into the work for part 1 to get most of the logic for part 2.

This time, instead of iterating through only values of $n$, we iterate all pairs $(n,k)$ with $k \geq 2$ and
$nk$ between the number of digits in $\text{START}$ and $\text{END}$.

Because some IDs can be found when searching by multiple $(n,k)$ pairs, we need to be careful to only use unique invalid IDs when summing.

</details>

<details>
<summary><b>Day 3</b></summary>

**Timing**: `00:03:58`, `00:17:55`

Finally started showing some signs of life in part 1, but an off-by-one error in my math for part 2 had me stuck for ~8 mins. Still an improvement from before, so that's nice to see.

#### Part 1

The first thing I noticed was that the best pair $AB$ if we fix $B$ simply uses the largest $A$ that occurs before $B$. Therefore, we can simply iterate through each bank's batteries to compute the joltage if each battery is the second one and taking the max. This entire process can be done fairly compactly in one pass.

#### Part 2

My first intution was to extend the greedy algorithm from part 1, but I felt that this would require more machinery than a simple DP solution, which I ended up implementing.

Let the optimal joltage for a bank $b=(b_1, \ldots, b_n)$ using exactly $k$ batteries be $J(b, k)$. The key recurrence relation is

$J(b, k) = \max( \ 10^{k-1} b_1 + J((b_2, \ldots, b_n), k-1), \ \ J((b_2, \ldots, b_n), k) \ )$

with base cases $J(b, k) = 0$ if $k = 0$ or $|b| < k$

This is because the optimal solution either uses the first battery in the bank (and therefore must optimally choose another $k-1$ batteries) or it doesn't (and therefore must optimally choose all $k$ batteries from the remaining $n-1$ in the bank).

If we cache results, then a top-down implementation actually achieves $O(n \cdot k)$ time, which is pretty close to the greedy solution and is well within reasonable time complexities for AoC input sizes. I didn't bother actually implementing the greedy solution because the DP solution is super compact and therefore has much more aura.

</details>

<details>
<summary><b>Day 4</b></summary>

**Timing**: `00:04:48`, `00:09:28`

Decently quick today minus a few minor slowdowns from forgetting that the forklift is only interested in moving rolls and not empty spaces. Hopefully this means I will be back on pace from previous years soon.

#### Part 1

This part is fairly straightforward and mechanical: we can simply iterate through each position, view the neighbors, and count the number of accessible rolls. The most interesting approach would be to convolve a 3x3 kernel on the input with empty padding with width 1, but this feels like driving an F1 car to get groceries.

#### Part 2

There is the intuitive brute-force solution that modifies the part 1 solution to remove any accessible rolls and keeps repeating this until the grid stops changing. Surprisingly, the puzzle input is small enough that this approach runs tolerably fast, but this is a very uninteresting solution.

The solution I ended up using relies on the fact that removing a roll impacts the accessibility of only its neighbors. Therefore, we can find all the rolls that can be immediately removed, then reconsider only the neighbors of each removed roll.

My implementation used an auxilliary grid tracking the number of neighboring rolls for each location and a stack for rolls that should be removed. Notice that, even though the problem description describes a breadth-first removal process, a depth-first process also works because any rolls that are already accessible don't become less accessible from removing some other roll. There wasn't a whole lot of thought behind stack vs queue because they're both correct and roughly equivalent speed for this problem, so I just chose the option I felt was easier to implement.

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
