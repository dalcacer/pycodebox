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

import sys, getopt, platform, os.path

from termcolor import colored
from pyperclip import pyperclip
from optparse import OptionParser
from snippetcollection import SnippetCollection
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


#pyperclip.copy('The text to be copied to the clipboard.')
#spam = pyperclip.paste()



#print colored("test", 'green', attrs=['bold'])
#print colored(u"\u2717", 'red')

class Confiuration():

    def __init__(self):
        """
        """
        pass

class PyCB():

    _collections=list()
    _usershome=""
    
    def __init__(self):
        """
        """
        # identify os
        runningos = platform.system()
        if runningos == "Linux":
            self._usershome = "/home/"+os.environ["USER"]+"/"
        elif runningos == "Darwin":
            self._usershome = "/Users/"+os.environ["USER"]+"/"
        else:
            print "Nope"
            return
        print self._usershome
        appdata = self._usershome + ".pycb"
        # load config
        self.loadConfiguration(appdata)


        # load snippetcollections
        snippetcollection1 = SnippetCollection("snippets.cbxml", "local/mine")
        snippetcollection1.parse()
        self._collections.append(snippetcollection1)
        #snippetcollection2 = SnippetCollection("CodeBox.cbxml", "local/mine2")
        #snippetcollection2.parse()
        #self._collections.append(snippetcollection2)
      
        
    def loadConfiguration(self, filename):
        """
        """
        print "loading", filename
        pass

    def find(self, keywords):
        """
        """
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
        self._printResultShort(no,shorthand,title,tags,lists)
        print "\t\t", highlight(assets, PythonLexer(), TerminalFormatter())

    def _printResultShort(self, no, shorthand, title, tags, lists):
        """
        """
        tagsstring = ""
        for tag in tags.split(" "):
            tagsstring+=colored(tag, 'grey')+" "
        listsstring = ""
        for alist in lists.split(" "):
            listsstring+=colored(tag, 'green')+";"
        

        uniquetitele = colored(shorthand, 'blue', attrs=['bold'])+listsstring+colored(title, 'green')
        if no <= 9:
            prno = "0"+str(no)
        else:
            prno = str(no)

        print prno, uniquetitele, "/", listsstring, "/", tagsstring

def main(argv):
    """
    """
    try:
        pycb = PyCB()
        res = pycb.find(argv)
        pycb.printResults(res, False)
        no = raw_input("Show No: ")
        pycb.printResult(res, no)
        var = raw_input("To clipboard? (Y/N) ")
        if var is "Y" or var is "y":
            asset = pycb.getAsset(res,no)
            pyperclip.copy(asset)
        else:
            exit(1)
    except KeyboardInterrupt:
        print "Do not cry because it is over, smile because it happened."

    
if __name__ == '__main__':
        main(sys.argv[1:])
