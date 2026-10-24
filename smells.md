# Code Smell Inventory

| Smell name | Function and line numbers | Why it hurts | Refactoring to apply |
|---|---|---|---|
| Duplicated code | `calc` and `calc2`, approximately lines 7–42 and 57–86 | Slab arithmetic, tax, discount and surcharge logic are repeated, so a bug fix may be applied to only one function. | Extract shared calculation functions and use them from both wrappers. |
| Long method | `calc`, approximately lines 3–29 | Printing, billing rules and total calculation are mixed in one function. | Extract slab and total calculation into small functions. |
| Long method | `calc2`, approximately lines 32–58 | Receipt formatting and billing logic are combined. | Separate calculation from receipt formatting. |
| Magic numbers | Both functions | Values such as 100, 300, 3, 5, 8, 6, 9, 12, 0.18, 0.05 and 0.02 have no explanatory names. | Replace them with named constants. |
| Unclear names | Both functions, parameter lists and local variables | Names such as `n`, `a`, `u`, `t`, `p`, `f`, `amt`, and `s` hide their meanings. | Rename parameters and variables using descriptive names. |
| Comment standing in for names | Both functions, first comment | The comment explains the abbreviations because the identifiers themselves are unclear. | Rename the parameters and remove the now-redundant comment. |
| Unused variable | `calc`, the assignment to `temp` | `temp` is calculated but never read, adding noise and suggesting a missing operation. | Remove the dead assignment. |
| Function doing two jobs | `calc` | It handles customer output and billing calculations. | Keep printing in `calc`; move calculations into shared helpers. |
| Primitive flag | Both functions, `f` parameter | A numeric flag hides the meaning of the senior discount condition and makes calls difficult to understand. | Rename to `senior` while preserving the existing `senior == 1` rule. |
| Repeated conditional structure | Both functions, H and C branches | The same slab algorithm is copied with only rates changed. | Extract a slab function accepting three rates and the slab boundaries. |
| Hidden ordering dependency | Both functions, tax and senior-discount statements | Tax uses the pre-discount amount, which may look accidental but is existing behavior. | Preserve the calculation order and lock it down with characterization tests. |
