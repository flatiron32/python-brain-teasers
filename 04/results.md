I was `wrong`.

# Why

`heapq` will attempt to compare the second element of the tuple when there is a collision. That means an `int` and a `str` will be compared and these are incomparable resulting in the `TypeError`.

# What else I learned

Assume malintent from author.
