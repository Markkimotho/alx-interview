#!/usr/bin/python3
import sys

total_size = 0
status_counts = {}

try:
    for i, line in enumerate(sys.stdin, start=1):
        line = line.strip()
        parts = line.split()

        if len(parts) != 7:
            continue

        ip_address, _, _, status_code, file_size = parts[0], parts[3], parts[5], int(parts[6])

        total_size += file_size

        if status_code.isdigit():
            status_code = int(status_code)
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

        if i % 10 == 0:
            print("Total file size:", total_size)
            for code in sorted(status_counts.keys()):
                print(code, ":", status_counts[code])
            print()

except KeyboardInterrupt:
    pass

print("Total file size:", total_size)
for code in sorted(status_counts.keys()):
    print(code, ":", status_counts[code])
