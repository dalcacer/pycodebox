#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


"""


__author__ = "dalcacer"
__copyright__ = "Copyright 2013"
__credits__ = [""]
__license__ = ""
__version__ = "0.1"
__maintainer__ = "dalcacer"
__email__ = "github@alcacer.de"
__status__ = ""

import sys, getopt

from termcolor import colored
from pyperclip import pyperclip
from optparse import OptionParser
from SnippetCollection import SnippetCollection



#pyperclip.copy('The text to be copied to the clipboard.')
#spam = pyperclip.paste()



#print colored("test", 'green', attrs=['bold'])
#print colored(u"\u2717", 'red')


class PyCB():

    _collections=list()

    def __init__(self):
        # identify os
        # load config
        # load snippetcollections
        snippetcollection = SnippetCollection("snippets.cbxml", "local/mine")
        snippetcollection.parse()
        self._collections.append(snippetcollection)
        
        

    def find(self, keywords):
        results = list()
        for collection in self._collections:
            results.append(collection.find(keywords))
        return results

    def printResults(self, results, verbose=True):
        """
        """
        for result in results:
            no=1
            for snippet in result:
                shorthand = ""
                title = ""
                tags = ""
                lists =""
                assets =""
                for  k, v in snippet:
                    if k is "shorthand":
                        shorthand = v
                    elif k is "title":
                        title = v
                    elif k is "tags":
                        tags = v
                    elif k is "lists":
                        lists = v
                    elif k is "assets":
                        assets = v
                if verbose:
                    self._printResultVerbose(no, shorthand, title, tags, lists, assets)
                else:
                    self._printResultShort(no, shorthand, title, tags, lists)
                no += 1
    
    def getAsset(self, resultlist, ino):
        """
        """
        ino = int(ino)
        for result in resultlist:
            no = 1
            for snippet in result:
                assets =""
                for  k, v in snippet:
                    if k is "assets":
                        assets = v
                if ino is no:
                    return assets
                else:
                    no += 1

    def printResult(self, resultlist, ino):
        """
        """
        ino = int(ino)
        for result in resultlist:
            no=1
            for snippet in result:
                shorthand = ""
                title = ""
                tags = ""
                lists =""
                assets =""
                for  k, v in snippet:
                    if k is "shorthand":
                        shorthand = v
                    elif k is "title":
                        title = v
                    elif k is "tags":
                        tags = v
                    elif k is "lists":
                        lists = v
                    elif k is "assets":
                        assets = v
                if ino is no:
                    self._printResultVerbose(no, shorthand, title, tags, lists, assets)
                    return
                else:
                    no+=1
      

    def _printResultVerbose(self, no, shorthand, title, tags, lists, assets):
        """
        """
        print no, shorthand, ":", title, "\t", tags, "\t", lists
        print "\t\t",assets

    def _printResultShort(self, no, shorthand, title, tags, lists):
        """
        """
        print no, shorthand, ":", title, "\t", tags, "\t", lists

def main(argv):
    """
    """
    pycb = PyCB()
    res = pycb.find(argv)
    pycb.printResults(res, False)
    no = raw_input("Show No: ")
    pycb.printResult(res, no)
    var = raw_input("To clipboard? (Y/N) ")
    if var is "Y" or var is "y":
        asset = pycb.getAsset(res,no)
        pyperclip.copy(asset)
        #spam = pyperclip.paste()
    else:
        exit(1)
    
if __name__ == '__main__':
        main(sys.argv[1:])
