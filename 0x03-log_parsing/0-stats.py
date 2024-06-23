#!/usr/bin/python3
"""Reads stdin line by line and prints statistics about each line"""
import re
import signal
import sys

# Define the regex pattern for log entries
line_pattern = re.compile(
    r'(?P<ip>\S+?)\s*-\s*\[(?P<date>.*?)\] '
    r'".*?" (?P<status>\d{3}) (?P<size>\d+)')

count = 0
file_size = 0
metric_dict = {}

valid_codes = [200, 301, 400, 401, 403, 404, 405, 500]


def print_metrics():
    """Print out the metrics to the standard output."""
    sys.stdout.write(f'File size: {file_size}\n')

    for key in sorted(metric_dict.keys()):
        sys.stdout.write(f'{key}: {metric_dict[key]}\n')
    sys.stdout.flush()


def signal_handler(signal, frame):
    """Handler for Ctrl+C"""
    print_metrics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

for line in sys.stdin:
    size = line.strip().split()[-1]
    file_size += int(size)

    match = line_pattern.match(line.strip())

    if match:
        extracts = match.groupdict()
        status_code = extracts['status']

        if status_code.isdigit():  # Check if status_code is numeric
            status_code = int(status_code)
            if status_code in valid_codes:
                if status_code in metric_dict:
                    metric_dict[status_code] += 1
                else:
                    metric_dict[status_code] = 1

    count += 1
    if count == 10:
        print_metrics()
        count = 0

print_metrics()
