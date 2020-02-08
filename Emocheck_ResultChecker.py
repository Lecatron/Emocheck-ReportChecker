
#!/bin/bash
#! Python3.8
# This Script is build to check as many repoirts of the EmoChecker-Tool as you want and sorts the result for a very fast overview.
# This tool is written by Lecatron
# https://Github.com/lecatron

import os
import sys
import argparse
import configparser

# read Config-File
config = configparser.ConfigParser()
config.read('./config.ini')
c_opath = config['Default']['outpath']
destpath = config['Default']['destpath']

# create Argumentparser
# options = options_list()
parser = argparse.ArgumentParser(description='This Tool will check all Reports of the EmoCheck.exe given in a directory for a positive result and sorts the Results for a veryy fast overview.\nThis Tool is written by Lecatron\nThis Tool is free of use and/or modification.', argument_default='-h', formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-d', dest='destination', default=destpath, help='Sets the Directory to scan in.', type=str)
parser.add_argument('-o', dest='outpath', default=c_opath, help='Sets the output Directory to build the Result structure.', type=str)
parser.add_argument('-dl', dest='destlist', default=None, help='Iterates a given .txt files with paths for Emocheck.exe Results.', nargs="?", type=str)
args = parser.parse_args()

######## FUNCTIONS

# Set Directory and prepare for Scan.
def set_outpath(path = "./"):
    if not os.path.exists(path):
        os.mkdir(path)
    if not os.path.exists('{0}/infected'.format(path)):
        os.mkdir('{0}/infected'.format(path))
    if not os.path.exists('{0}/clear'.format(path)):
        os.mkdir('{0}/clear'.format(path))


# This is the Scanning function, which checks the given reportfiles.
def check_reports(dest_path, outpath):
    for filename in os.listdir(dest_path):
        with open('{0}{1}'.format(dest_path, filename), 'r') as report:
            for line in report:
                if line == "[Emotet Process]":
                    print('{0} {1}'.format(line, filename))
                    os.system('copy {0}{1} {2}\infected\{1}'.format(dest_path, filename, outpath))
                    continue                
        report.close()
        os.system('copy {0}{1} {2}\clear\{1}'.format(dest_path, filename, outpath))


set_outpath(args.outpath)

if args.destlist:
    with open(args.destlist, 'r') as dlist:
        for line in dlist:
            line = line.strip('\n')
            check_reports(line, args.outpath)
else:
    check_reports(args.destination, args.outpath)

##### DEBUG
print(args)

#check_reports(args.destination, args.outpath)

