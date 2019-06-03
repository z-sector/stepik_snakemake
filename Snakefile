rule count_words:
    input: 'input/input'
    output: 'output/output'
    shell: 'python scripts/count_words.py {input} {output}'
