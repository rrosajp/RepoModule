#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os
import xbmcaddon
import cfscrape
#import cloudscraper as cfscrape
#import cloudscraper-dev as cfscrape

def fix_encoding(path):
	if sys.platform.startswith('win'):return unicode(path,'utf-8')
	else:return unicode(path,'utf-8').encode('ISO-8859-1')
	
addon_ =  xbmcaddon.Addon()
addon_path_ = fix_encoding(addon_.getAddonInfo('path'))

def test_viewer(s):
    import xbmcgui
    xbmcgui.Dialog().textviewer('TEST VIEWER', str(s))
    d = open(os.path.join(addon_path_,'TEST_WRITER.txt'),'wb')
    d.write(str(s))
    d.close()

def test_scraper(url):
	scraper = cfscrape.create_scraper()  # returns  instance
	# Or: scraper = cloudscraper.CloudScraper()  # CloudScraper inherits from requests.Session
	return scraper.get(url).content

content = test_scraper('https://hdfilme.cc')
test_viewer(content)