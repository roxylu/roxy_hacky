#!/usr/bin/env python
import argparse
import itertools
import zipfile
from threading import Thread
from zipfile import BadZipfile


def extract_file(z_file, password):
    # Extract with correct pwd
    # z_file.extractall(pwd='roxy')
    try:
        z_file.extractall(pwd=password)
        print '[+] Password = ' + password
    except BadZipfile:
        print '[-] Bad zip file with ' + password
        pass
    except Exception, e:
        pass


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', dest='z_name',
                      help='specify zip file')
    parser.add_argument('-d', dest='d_name',
                      help='specify dictionary file')
    args = parser.parse_args()
    if (args.z_name == None) | (args.d_name == None):
        parser.print_help()
        exit(0)
    else:
        z_name = args.z_name
        d_name = args.d_name

    z_file = zipfile.ZipFile(z_name)
    pass_file = open(d_name)
    for line in pass_file.readlines():
        password = line.strip()

        #extract_file(z_file, password)
        # Multithreading
        t = Thread(target=extract_file, args=(z_file, password))
        t.start()


if __name__ == '__main__':
    main()
