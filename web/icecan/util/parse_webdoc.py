#!/usr/bin/env python

import urllib2
from HTMLParser import HTMLParser

class DocParser(HTMLParser):
    def handle_starttag(tag, attrs):
        print 'STARTTAG:', tag, attrs

    def handle_endtag(tag):
        print 'ENDTAG:', tag
    
    def handle_data(data):
        print 'DATA:', data

def get_page(url):
    site = urllib2.urlopen(url)
    return site.read()

def parse_webdoc():
    url = 'http://stjornlagarad.is/starfid/afangaskjal/oll/'
    doc_selector = 'div.oll_afangaskjol'
    html = get_page(url)
    parser = DocParser()
    parser.feed('<tag1>hello<tag2 class="inner">nice</tag2>world</tag1>')

def main():
    # do we need any command ine stuff...?
    return parse_webdoc()

if __name__=='__main__':
    return main()
