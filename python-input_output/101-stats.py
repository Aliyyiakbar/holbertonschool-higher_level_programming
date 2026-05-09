#!/usr/bin/python3
"""Read stdin line by line and compute log statistics."""

import sys


def print_stats(total_size, status_codes):
    """Print the total file size and status code counts."""
    print("File size: {}".format(total_size))

    for code in sorted(status_codes):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def main():
    """Read log lines from stdin and print metrics."""
    total_size = 0
    line_count = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()

            if len(parts) >= 2:
                status_code = parts[-2]
                file_size = parts[-1]

                if status_code in status_codes:
                    status_codes[status_code] += 1

                try:
                    total_size += int(file_size)
                except ValueError:
                    pass

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

        if line_count == 0 or line_count % 10 != 0:
            print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise


if __name__ == "__main__":
    main()
