# Refactoring Metrics — Assignment 8

| Measure | Before | After |
|---|---:|---:|
| Total lines in `bill.py` | 63 | 126 |
| Lines in the longest function | 30 | 31 |
| Number of places where the slab arithmetic appears | 4 | 1 |
| Number of magic numbers left | 11 distinct billing values | 0 |
| Tests passing | 19 | 19 |

## Observations

- The slab calculation is now centralized in `calculate_slab_amount()`.
- Tax, senior discount and late surcharge have separate helper functions.
- Both `calc()` and `calc2()` use the shared `calculate_total()` function.
- Named constants improve the readability of billing rates and percentages.
- The characterization tests verify that the existing behavior is preserved.
