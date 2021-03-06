#!/usr/bin/env python

import sys
import os
import serial
import time

def loader(fname, port, baud):
    s = serial.Serial(port=port, baudrate=baud)
    f = open(fname)

    s.write("\r\n\r\n\r\n")
    s.write("$PASHS,NME,ALL,A,OFF\r\n")
    s.write("$PASHS,NME,ALL,B,OFF\r\n")
    s.timeout = 0.1
    time.sleep(1)
    s.read()

    for line in f.readlines():
        if not line.startswith(';'):
            l = line.strip()
            print '>> ' + l
            s.write(l + '\r\n')
            print '<< ' + s.readline().strip()

    s.write("$PASHQ,CPD\r\n")
    s.write("$PASHQ,PAR\r\n")
    while True:
        line = s.readline()
        if not line.startswith("$"):
            print line.rstrip()

def main(argv, stdout):
    usage = "usage: %prog [options] /path/to/config"
    parser = OptionParser(usage=usage)
    parser.add_option("-p", "--port", action="store", type="string", dest="port",
            default="/dev/gps",
            help="Serial port connected to GPS")
    parser.add_option("-b", "--baud", action="store", type="int", dest="baud",
            default=115200,
            help="Serial port baud rate")
    (options, args) = parser.parse_args(argv)
    if len(args) < 2:
        parser.error("Please specify a config file.")
        syst.exit(1)

    configFile = args[1]

    try:
        loader(configFile, options.port, options.baud)
    except ValueError:
        pass

if __name__ == '__main__':
    from optparse import OptionParser
    main(sys.argv, sys.stdout)
