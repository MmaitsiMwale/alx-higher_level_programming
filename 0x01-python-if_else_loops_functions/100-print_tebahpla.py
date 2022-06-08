#!/usr/bin/python3
tracker = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print(f"{chr(i - tracker)}", end="")
    tracker = 32 if tracker == 0 else 0
