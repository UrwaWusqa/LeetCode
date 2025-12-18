# [**Best Time to Buy and Sell Stock using Strategy**](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/)

## Problem Overview

You are given two integer arrays, `prices` and `strategy`, representing stock prices and trading actions over consecutive days.

- `prices[i]`: Price of the stock on the *i-th* day.
- `strategy[i]`: Trading action on the *i-th* day:
  - `-1` → Buy one unit of stock
  - `0` → Hold
  - `1` → Sell one unit of stock

You are also given an **even integer \*\*\*\***``. You may perform **at most one modification** to the `strategy` array.

### Allowed Modification

A modification consists of:

1. Selecting **exactly **``** consecutive elements** in `strategy`.
2. Setting:
   - The **first **``** elements** to `0` (hold)
   - The **last **``** elements** to `1` (sell)

### Profit Definition

The profit is calculated as:

```
profit = Σ(strategy[i] × prices[i])
```

> **Note:** There are no constraints on budget or stock ownership. All buy and sell operations are always feasible, regardless of past actions.

Your task is to **return the maximum possible profit** achievable after applying **at most one modification**.

---

## Examples

### Example 1

**Input:**

```
prices   = [4, 2, 8]
strategy = [-1, 0, 1]
k = 2
```

**Evaluation:**

| Modification | Strategy   | Profit Calculation     | Profit |
| ------------ | ---------- | ---------------------- | ------ |
| Original     | [-1, 0, 1] | (-1×4) + (0×2) + (1×8) | 4      |
| Modify [0,1] | [0, 1, 1]  | (0×4) + (1×2) + (1×8)  | 10     |
| Modify [1,2] | [-1, 0, 1] | (-1×4) + (0×2) + (1×8) | 4      |

**Output:**

```
10
```

The maximum profit is achieved by modifying the subarray `[0, 1]`.

---

### Example 2

**Input:**

```
prices   = [5, 4, 3]
strategy = [1, 1, 0]
k = 2
```

**Evaluation:**

| Modification | Strategy  | Profit Calculation    | Profit |
| ------------ | --------- | --------------------- | ------ |
| Original     | [1, 1, 0] | (1×5) + (1×4) + (0×3) | 9      |
| Modify [0,1] | [0, 1, 0] | (0×5) + (1×4) + (0×3) | 4      |
| Modify [1,2] | [1, 0, 1] | (1×5) + (0×4) + (1×3) | 8      |

**Output:**

```
9
```

The optimal solution is to **not apply any modification**.

---

## Constraints

- `2 ≤ prices.length == strategy.length ≤ 10^5`
- `1 ≤ prices[i] ≤ 10^5`
- `-1 ≤ strategy[i] ≤ 1`
- `2 ≤ k ≤ prices.length`
- `k` is even

---

## Key Observations

- You are allowed **at most one modification**, including the option of making **no modification**.
- The modification enforces a fixed pattern: *hold → sell*.
- Since there are no ownership constraints, this problem is purely a **numerical optimization** problem.

---

## Goal

Efficiently determine the subarray (or no modification) that yields the **maximum possible profit** under the given rules.

