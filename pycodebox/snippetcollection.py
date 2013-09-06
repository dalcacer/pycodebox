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

import elementtree.ElementTree as ET
import base64
import constants as const
class SnippetCollection():

    """
        represents a snippetcollection stored within an cbxml-file
    """
    _file = None
    _shorthand = ""
    _tagobjects = list()
    _assetobjects = list()
    _snippetobjects = list()
    _listobjects = list()
    _folderobjects = list()

    def __init__(self, cbxmlfile, shorthand=""):
        self._shorthand = shorthand
        self._file = cbxmlfile
        pass

    def parse(self):
        """
        parses the associated cbxml-file.
        """
        #tree = ET.parse(self._file)
        #root = tree.getroot()

        #first things first
        self.__parseForFolders()
        self.__parseForLists()
        self.__parseForTags()
        self.__parseForAssets()
        self.__parseForSnippets()
        # for child in root._children:
        #     childType = child.attrib.get(const.ATTRIB_CHILDTYPE)
        #     childType = str(childType).strip().lower()
        #     if childType == const.CHILDTYPE_ASSET:
        #         self._parseAsset(child)
        #     elif childType == const.CHILDTYPE_SNIPPET:
        #         pass
        #     elif childType == const.CHILDTYPE_TAG:
        #         self._parseTag(child)
        #     elif childType == const.CHILDTYPE_LIST:
        #         self._parseList(child)
        #     elif childType == const.CHILDTYPE_FOLDER:
        #         self._parseFolder(child)
        #     elif childType == const.CHILDTYPE_SEARCH:
        #         pass
        #     elif childType == const.CHILDTYPE_NONE:
        #         pass
        #     else:
        #         print "Oh. A new type: ", childType
        

    def __parseForAssets(self):
        """
        parses the associated cbxml-file.
        """
        tree = ET.parse(self._file)
        root = tree.getroot()

        for child in root._children:
            childType = child.attrib.get(const.ATTRIB_CHILDTYPE)
            childType = str(childType).strip().lower()
            if childType == const.CHILDTYPE_ASSET:
                self._parseAsset(child)

    def __parseForTags(self):
        """
        parses the associated cbxml-file.
        """
        tree = ET.parse(self._file)
        root = tree.getroot()

        for child in root._children:
            childType = child.attrib.get(const.ATTRIB_CHILDTYPE)
            childType = str(childType).strip().lower()
            if childType == const.CHILDTYPE_TAG:
                self._parseTag(child)

    def __parseForFolders(self):
        """
        parses the associated cbxml-file.
        """
        tree = ET.parse(self._file)
        root = tree.getroot()

        for child in root._children:
            childType = child.attrib.get(const.ATTRIB_CHILDTYPE)
            childType = str(childType).strip().lower()
            if childType == const.CHILDTYPE_FOLDER:
                self._parseFolder(child)

    def __parseForLists(self):
        """
        parses the associated cbxml-file.
        """
        tree = ET.parse(self._file)
        root = tree.getroot()

        for child in root._children:
            childType = child.attrib.get(const.ATTRIB_CHILDTYPE)
            childType = str(childType).strip().lower()
            if childType == const.CHILDTYPE_LIST:
                self._parseList(child)
    
    def __parseForSnippets(self):
        """
        parses the associated cbxml-file.
        """
        tree = ET.parse(self._file)
        root = tree.getroot()

        for child in root._children:
            childType = child.attrib.get(const.ATTRIB_CHILDTYPE)
            childType = str(childType).strip().lower()
            if childType == const.CHILDTYPE_SNIPPET:
                self._parseSnippet(child)
     
    def update(self):
        """
        updates this collection.
        """
        self._tagobjects = list()
        self._assetobjects = list()
        self._snippetobjects = list()
        self._parse()

    def find(self, keywords):
        """
        finds snippets based on TAG,TITLE,LIST, ASSET itself.
        """
        resultset = list()
        for snippet in self._snippetobjects:
            snippid=""
            for  k, v in snippet:
                if k is "id":
                    snippid=v
                if k is "title" or k is "tags" or k is "lists" or k is "assets":
                    if keywords == list():
                        if self._containsSnippet(resultset,snippid) == True:
                            pass
                        else:
                            resultset.append(snippet)
                    else:
                        for keyword in keywords:
                            if keyword in v:
                                if self._containsSnippet(resultset,snippid) == True:
                                    pass
                                else:
                                    resultset.append(snippet)
        return resultset

    def _parseTag(self, tag):
        """
        parses a tag-tag :)
        0.1 id and content
        <object type="TAG" id="z106">
            <attribute name="name" type="string">gitignore</attribute>
            <relationship name="snippets" type="0/0" destination="SNIPPET"></relationship>
        </object>
        """
        tagid = tag.attrib.get('id')
        atag = list()
        atag.append(('id', tagid))
        for child in tag._children:
            if child.tag == "attribute":
                # attribute tags
                atag.append(('content', child.text))
            elif child.tag == 'relationship':
                # relationship tags
                pass
        self._tagobjects.append(atag)

    def _parseAsset(self, asset):
        """
        parses and decodes an asset-tag
        0.1 id, content
        <object type="ASSET" id="z116">
            <attribute name="sort" type="int32">-1</attribute>
            <attribute name="path" type="string">Asset.java</attribute>
            <attribute name="content" type="binary">LyoqCiAgICAgKiBXcml0ZXMgYW4gYnl0ZSBhcnJheSBpbnRvIGEgZmlsZS4KICAgICAqIEBwYXJh
            bSBkYXRhIERhdGEgdGhhdCBzaG91bGQgYmUgd3JpdHRlbiBpbnRvIGEgZmlsZS4KICAgICAqIEBwYXJhbSBmaWxlbmFtZSBUaGUgZmlsZSwgdGhhdCBzaG91bGQgYmUgdXNlZC4KICAgICAqIEB0aHJvd3MgSU9FeGNlcHRpb24KICAgICAqLwogICAgcHVibGljIHN0YXRpYyB2b2lkIHdyaXRlQnl0ZTJGaWxlKGJ5dGVbXSBkYXRhLCBTdHJpbmcgZmlsZW5hbWUpIHRocm93cyBJT0V4Y2VwdGlvbiB7CiAgICAgICAgT3V0cHV0U3RyZWFtIG91dCA9IG5ldyBGaWxlT3V0cHV0U3RyZWFtKGZpbGVuYW1lKTsKICAgICAgICBvdXQud3JpdGUoZGF0YSk7CiAgICAgICAgb3V0LmNsb3NlKCk7CiAgICB9
            </attribute>
            <relationship name="snippet" type="1/1" destination="SNIPPET" idrefs="z113"></relationship>
        </object>
        """
        assetid = asset.attrib.get('id')
        anasset = list()
        anasset.append(('id', assetid))
        for child in asset._children:
            if child.tag == "attribute":
                # attribute tags
                attributeType = child.attrib.get("name")
                if attributeType == 'content':
                    encoded = child.text
                    decoded = base64.b64decode(encoded)
                    anasset.append(('content', decoded))
            elif child.tag == 'relationship':
                # relationship tags
                pass
        self._assetobjects.append(anasset)

    def _parseList(self, aList):
        """
        <object type="LIST" id="z131">
            <attribute name="sort" type="int16">6</attribute>
            <attribute name="name" type="string">actionscript</attribute>
            <attribute name="expanded" type="bool">0</attribute>
            <relationship name="parent" type="1/1" destination="FOLDER"></relationship>
            <relationship name="children" type="0/0" destination="FOLDER"></relationship>
            <relationship name="snippets" type="0/0" destination="SNIPPET" idrefs="z135"></relationship>
        </object>
        """
        listid = aList.attrib.get('id')
        anlist = list()
        anlist.append(('id', listid))
        for child in aList._children:
            if child.tag == "attribute":
                # attribute tags
                attributeType = child.attrib.get("name")
                if attributeType == 'name':
                    anlist.append(('name', child.text))
            elif child.tag == 'relationship':
                pass
                #attributeType = child.attrib.get("name")
                #if (attributeType == 'parent') or (attributeType == 'children'):
                #    # folder relationship
                #    refsStr = str(child.attrib.get('idrefs'))
                #    refs = refsStr.split(' ')
                #    folders = ""
                #    for ref in refs:
                #        resolvedfolder = self._findFolderById(ref)
                #        if not resolvedfolder is "":
                #            folders += " " + resolvedfolder
                #    anlist.append(("folders", folders))
        #print "adding list ", anlist
        self._listobjects.append(anlist)

    def _parseFolder(self, folder):
        """
        object type="FOLDER" id="z229">
            <attribute name="sort" type="int16">7</attribute>
            <attribute name="name" type="string">java</attribute>
            <attribute name="expanded" type="bool">1</attribute>
            <relationship name="parent" type="1/1" destination="FOLDER"></relationship>
            <relationship name="children" type="0/0" destination="FOLDER" idrefs="z223 z222 z333 z228"></relationship>
        </object>
        """
        folderid = folder.attrib.get('id')
        afolder = list()
        afolder.append(('id', folderid))
        for child in folder._children:
            if child.tag == "attribute":
                # attribute tags
                attributeType = child.attrib.get("name")
                if attributeType == 'name':
                    afolder.append(('name', child.text))
            elif child.tag == 'relationship':
                # relationship tags
                pass
        self._folderobjects.append(afolder)

    def _parseSnippet(self, snippet):
        """
        parses a snippet-tag
        0.1 id, assetes, tags
        <object type="SNIPPET" id="z108">
            <attribute name="name" type="string">.gitignore</attribute>
            <attribute name="modified" type="date">336046917.00164198875427246094</attribute>
            <attribute name="locked" type="bool">0</attribute>
            <relationship name="list" type="1/1" destination="LIST" idrefs="z114"></relationship>
            <relationship name="assets" type="0/0" destination="ASSET" idrefs="z107"></relationship>
            <relationship name="tags" type="0/0" destination="TAG"></relationship>
        </object>
        """
        
        snippid = snippet.attrib.get('id')
        ansnippet = list()
        ansnippet.append(('id', snippid))
        ansnippet.append(('shorthand', self._shorthand))
        for child in snippet._children:
            if child.tag == "attribute":
                # attribute tags
                attributeType = child.attrib.get("name")
                if attributeType == 'name':
                    ansnippet.append(('title', child.text))
                elif attributeType == 'modified':
                    pass
                elif attributeType == 'locked':
                    pass
                else:
                    print "Unknown cbxml-attributetype."
            elif child.tag == 'relationship':
                # relationship-tag
                attributeType = child.attrib.get("name")
                if attributeType == 'list':
                    # list relationship
                    refsStr = str(child.attrib.get('idrefs'))
                    refs = refsStr.split(' ')
                    lists = ""
                    for ref in refs:
                        resolvedlist = self._findListById(ref)
                        if not resolvedlist is "" and type(resolvedlist) is str:
                            lists += " " + resolvedlist
                    ansnippet.append(("lists", lists))
                elif attributeType == 'assets':
                    # assets relationship
                    refsStr = str(child.attrib.get('idrefs'))
                    refs = refsStr.split(' ')
                    assets = ""
                    for ref in refs:
                        resolvedasset = self._findAssetById(ref)
                        if not resolvedasset is "" and type(resolvedasset) is str:
                            assets += " " + resolvedasset
                    ansnippet.append(("assets", assets))
                elif attributeType == 'tags':
                    # tags relationships
                    refsStr = str(child.attrib.get('idrefs'))
                    refs = refsStr.split(' ')
                    tags = ""
                    for ref in refs:
                        resolvedtag = self._findTagById(ref)
                        if not resolvedtag is "" and type(resolvedtag) is str:
                            tags += " " + resolvedtag
                    ansnippet.append(("tags", tags))
        self._snippetobjects.append(ansnippet)


    def _containsSnippet(self, alist, snippid):
        """
        """
        if snippid is None:
            return False;
        for snippet in alist:
            givenid = str(snippet[0][1])
            if snippid == givenid:
                return True
        return False

    def _findTagById(self, tagid):
        """
        """
        for tag in self._tagobjects:
            givenid = tag[0][1]
            if tagid == givenid:
                try:
                    return tag[1][1]
                except:
                    pass
        return ""

    def _findListById(self, listid):
        """
        """
        for alist in self._listobjects:
            givenid = alist[0][1]
            if listid == givenid:
                try:
                    return alist[1][1]
                except:
                    pass
        return ""

    def _findFolderById(self, folderid):
        """
        """
        for folder in self._folderobjects:
            givenid = folder[0][1]
            if folderid == givenid:
                try:
                    return folder[1][1]
                except:
                    pass
        return ""

    def _findAssetById(self, assetid):
        """
        """
        for asset in self._assetobjects:
            givenid = asset[0][1]
            if assetid == givenid:
                try:
                    return asset[1][1]
                except:
                    pass
        return ""


if __name__ == '__main__':
    """
    testpurpose only
    """
    snippetcollection = SnippetCollection("snippets.cbxml", "local/mine")
    snippetcollection.parse()
    snippetcollection.find(["git"])
    snippetcollection.find(["virtualbox"])
