# Sprint Retrospective — Assignment 10

## Start

I started by committing the original billing code and writing characterization tests before refactoring. This provided a safety net for preserving existing behavior. My 19 tests covered both connection types, slab boundaries, senior discounts, previous dues, invalid types, printed output, and receipt strings. I also documented the code smells before changing the implementation.

## Stop

I stopped relying on short variable names and duplicated billing logic. The original functions repeated the slab calculations, making maintenance difficult. I replaced magic numbers with named constants and extracted the slab, tax, senior discount, and surcharge calculations into separate functions. I learned that even unusual behavior, such as calculating tax before the senior discount, must remain unchanged during behavior-preserving refactoring.

## Continue

I will continue testing after every small change and committing only passing code. My Git history contains [number] refactoring commits. One important commit was [actual commit message]. The test for [specific behavior] helped protect the implementation by checking [actual behavior verified].

### Action items

1. I will run the full test suite before every refactoring commit, starting with the next module.
2. I will record baseline metrics and code smells before editing, by the first lab session of the next module.
