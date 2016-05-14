# This file is for generating a simple table of contents.
#!/usr/bin/env python
from glob import glob
from urllib import quote
from os import chdir

def process_problem_set(ps, out_file):
    s = '<big>[%s](./%s)<big/>\n\n' % (ps, quote(ps))
    out_file.write(s)
    out_file.write('---\n\n')
    chdir(ps)
    files = glob("*")
    for file in files:
        s = '[%s](./%s)\n\n' % (file, quote(ps + '/' + file))
        out_file.write(s)
    out_file.write('---\n\n')
    chdir('..')

def main():
    out_file_name = 'table-of-contents.md'
    out_file = open(out_file_name, 'w')
    ps_list = glob('Problem Set *')
    for ps in ps_list:
        process_problem_set(ps, out_file)
    out_file.close()

if __name__ == '__main__':
    main()
    