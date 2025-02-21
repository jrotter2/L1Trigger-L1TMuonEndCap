#! /usr/bin/env python

import glob
import sys, os, fnmatch
import argparse
import getpass
import subprocess
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import tostring

allowedModes = [15, 14, 13, 12, 11, 10, 9, 7, 6, 5, 3]
#allowedModes = [15, 14, 13, 11]

target_directory = "/eos/user/j/jrotter/PT_XMLS/pt_xmls" #"/src/L1Trigger/L1TMuonEndCap/data/pt_xmls"

for mode in allowedModes:
    print(mode)
    fname = f"{mode}.xml"

    forest = ET.parse(fname) #NEED TO CHANGE NAME OF Wgt
    forest = forest.getroot()
    all_trees = list(forest)[1:]
    print(len(all_trees))

    for itree in range(0,len(all_trees)):
        mydata = ET.tostring(all_trees[itree]).decode()
        #print(mydata.split("\n"))
        myfile = open(f"{target_directory}/v4p0/{mode}/{itree}.xml", "w")
        myfile.write("""<?xml version="1.0"?>\n""")
        myfile.write(f'<BinaryTree boostWeight="1.0e+00" itree="{itree}" type="DecisionTree">\n')
        myfile.write(mydata)
        myfile.write('</BinaryTree>')
        myfile.close()
