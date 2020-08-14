# Guess
```
1
2 3
```

# Why
The intent seems to be to print 1, 2, and 3 on the same line with a 0.1s interval and then print a new line. However because the printer is sent to a new thread and then sleeps after 1 with printed. Execution returns to the main thread and the new line is printed earlier.
