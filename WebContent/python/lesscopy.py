import sys
import os
import re

def lesslist():
    '''Returns the relative file paths of all .less files in ../less,
       relative to the /python directory this file is assumed to be
       running in.'''
    dirlist = os.listdir('../less')
    relpaths = []
    for fname in dirlist:
        match = re.search(r'(\S+[.less])', fname)
        if match:
            relpaths.append('../less/' + match.group(1))
    return relpaths

# The below script is Linux / Unix compatible; it has not been tested on Windows.
def main():
    ''' Invokes lessc compiler on all .less files in ../less 
        and moves those files to ../css, using relative filepaths.'''
    fnames = lesslist()
    for fname in fnames:
        match = re.search(r'../..../(\S+[.less])', fname)
        if match:
            fname2 = match.group(1)
            # Remove the "less" in the filename and replace it with "css"
            csspath = '../css/' + fname2[:-4] + 'css'
            temppath = fname2[:-4] + 'css'
            # Passed to shell as a command of the form "lessc foo.less > foo.css"
            cmdstring = 'lessc ' + fname + ' > ' + temppath
            print cmdstring + '\n' + temppath + ' will be copied to /css.'
            os.system(cmdstring)
            os.system('cp ' + temppath + ' ' + csspath)
            os.system('rm ' + temppath)
            # Print path to output
            print "Output: " + os.path.abspath(csspath)

if __name__ == '__main__':
    main()
