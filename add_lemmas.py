#!/usr/bin/env python3

import os


INPUT_DIR = 'mid_rus_splitted'
OUTPUT_DIR = 'mid_rus_verbs'


def load_verbs(fpath):
    d = {}
    with open(fpath) as fh:
        fh.readline()
        for line in fh:
            line.strip()
            freq, word, lemma = line.split('\t')
            d[word] = lemma
    return d


def add_lemma_to_line(verbs, line):
    if line == '\n':
        return line
    if line.startswith('#'):
        return line
    line = line.strip()
    parts = line.split('\t')
    word = parts[2]
    lemma = verbs.get(word, '')
    parts.append(lemma)
    new_line = '\t'.join(parts) + '\n'
    return new_line


def improve_file(verbs, input_path, output_path):
    output_dir = os.path.dirname(output_path)
    os.makedirs(output_dir, exist_ok=True)
    with open(input_path) as inp, open(output_path, 'w') as out:
        for inp_line in inp:
            out_line = add_lemma_to_line(verbs, inp_line)
            out.write(out_line)


def main():
    verbs = load_verbs('mid_rus_verbs.txt')
    for root, dirs, files in os.walk(INPUT_DIR):
        for file in files:
            if not file.endswith('.txt'):
                continue
            print(file)
            input_path = os.path.join(root, file)
            rel_path = os.path.relpath(input_path, INPUT_DIR)
            output_path = os.path.join(OUTPUT_DIR, rel_path)
            improve_file(verbs, input_path, output_path)


if __name__ == '__main__':
    main()
