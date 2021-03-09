#!/usr/bin/env python3

import os
import sys

# Determine if we need to include the -Zinstrument-coverage flag for this crate:
# Iterate through the crate names that need to be instrumented and check if the
# current crate
def include_coverage(start, crate_names):
    for i in range(start, len(sys.argv) - 1):
        if sys.argv[i] == "--crate-name" and sys.argv[i + 1] in crate_names:
            return True
    return False


def adjust_rustc_command():
    num_of_crates_with_coverage = int(sys.argv[1])
    # The argument input to this wrapper will be as follows:
    # wrapper.py num_of_crates_with_coverage crate_names... rustc rustc_args...
    # ^0         ^1                          ^2...
    # For example,
    # wrapper.py 2 crate_name1 crate_name2 rustc ...
    if num_of_crates_with_coverage > 0:
        rustc_index = 2 + num_of_crates_with_coverage
        crates_with_coverage = sys.argv[2: rustc_index]
        rust_args = sys.argv[rustc_index:]
        coverage = include_coverage(rustc_index, crates_with_coverage)
        args = rust_args + (["-Zinstrument-coverage"] if coverage else [])
        return os.execvp(sys.argv[num_of_crates_with_coverage], args)
    return os.execvp(sys.argv[2], sys.argv[2:])


adjust_rustc_command()
