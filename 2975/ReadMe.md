# 2975. Maximum Square Area by Removing Fences From a Field

**Difficulty:** Medium  
**Status:** Solved  

---

## 🧠 Problem Description

There is a large rectangular field of size **(m - 1) × (n - 1)** with corners at **(1, 1)** and **(m, n)**.

Inside the field, there are:

- **Horizontal fences** at positions given in array `hFences`
- **Vertical fences** at positions given in array `vFences`

### Fence Details

- A horizontal fence at `hFences[i]` spans from **(hFences[i], 1)** to **(hFences[i], n)**
- A vertical fence at `vFences[i]` spans from **(1, vFences[i])** to **(m, vFences[i])**

The outer boundary of the field is surrounded by fences on all four sides, **and these boundary fences cannot be removed**.

---

## 🎯 Objective

Remove **any number of internal fences (possibly none)** to form a **square field**.

- Return the **maximum possible area** of such a square.
- If it is **not possible** to form a square, return `-1`.
- Since the answer may be large, return it **modulo**:

