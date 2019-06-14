#!/usr/bin/env python3

import os

LARGE_DIR = 'mid_rus_conll'
SMALL_DIR = 'mid_rus_splitted'


def extract_small_fpath(line):
    line = line.strip()
    fpath_part = line.split(' = ')[1]
    fpath = os.path.join(SMALL_DIR, fpath_part) + '.txt'
    return fpath


def write_small_file(fpath, lines):
    fdir = os.path.dirname(fpath)
    os.makedirs(fdir, exist_ok=True)
    with open(fpath, 'w') as fh:
        fh.writelines(lines)


def split_file(large_fpath):
    small_fpath = None
    with open(large_fpath) as fh:
        for line in fh:
            if line.startswith('# newdoc id = '):
                if small_fpath:
                    write_small_file(small_fpath, small_file_lines)
                small_fpath = extract_small_fpath(line)
                small_file_lines = []
            else:
                small_file_lines.append(line)
    write_small_file(small_fpath, small_file_lines)

def main():
    os.makedirs(SMALL_DIR, exist_ok=True)
    for fname in os.listdir(LARGE_DIR):
        if not fname.endswith('.txt'):
            continue
        print(fname)
        fpath = os.path.join(LARGE_DIR, fname)
        split_file(fpath)


if __name__ == '__main__':
    main()
