I was `wrong`.

# Why

Two reasons:

1. failed to account for ranges being 0 indexed.
2. the main thread will not wait for child threads to complete

# What else I learned
Setting `daemon=False` will yield my prediction.
Adding `thr.join()` will yield the intended behaviour.
