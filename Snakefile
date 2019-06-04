IDS, = glob_wildcards("input/{id,\w+}")

rule all:
    input: expand('output/{id}', id=IDS)
    output: touch(".status")

rule copy:
    input: 'input/{id}'
    output: 'output/{id}'
    shell: 'python3 scripts/copy_files.py {input} {output}'
