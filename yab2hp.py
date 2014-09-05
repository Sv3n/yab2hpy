#!/usr/bin/env python

import argparse
parser = argparse.ArgumentParser(description='Convert binary file to c-header.')
parser.add_argument('infile'  , type=str, nargs=1, help='infile')
parser.add_argument('outfile' , type=str, nargs=1, help='outfile')
parser.add_argument('--blobName' , dest='blobName', type=str, required=False,  default='rom')
args = parser.parse_args()

infile = args.infile[0]
outfile = args.outfile[0]

b = ''
with open(infile, 'rb') as f:
    b = f.read();

i = 0
with open(outfile, 'w') as g:
    g.write('#ifndef __%s_H\n#define __%s_H\n\nunsigned char %s[] = {\n\t\t' % (args.blobName, args.blobName, args.blobName))
    first = 1
    for c in b:
        i += 1;
        if first:
            first = 0
            g.write(" ")
        else:
            g.write(', ')
        g.write("0x%02x" % ord(c))
        if i % 12 == 0:
            g.write('\n\t\t')
    g.write('};\n#endif\n')

