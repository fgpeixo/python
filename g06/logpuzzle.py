#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import os
import re
import sys
import urllib

"""Logpuzzle exercise
Given an apache logfile, find the puzzle urls and download the images.

Here's what a puzzle url looks like:
10.254.254.28 - - [06/Aug/2007:00:13:48 -0700] "GET /~foo/puzzle-bar-aaab.jpg HTTP/1.0" 302 528 "-" "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.6) Gecko/20070725 Firefox/2.0.0.6"
"""
def get_key(url):

  m = re.search(r'-\w+-(\w+).jpg',url)
  if m:
    return m.group(1)
  else:
    return url  

def read_urls(filename):
  """Returns a list of the puzzle urls from the given log file,
  extracting the hostname from the filename itself.
  Screens out duplicate urls and returns the urls sorted into
  increasing order."""
  # +++your code here+++
  
  urls = []
  host = ''

  # find host
  match = re.search(r'_([\w.-]+)',filename)
  if match:
    host = 'http://' + match.group(1)
  
  file = open(filename, 'rU')
  text = file.read()
  file.close()

  urls = re.findall(r'GET\s+(\S*puzzle\S*)\s+',text)
  
  urls_dict = {}
  # remove duplicates
  for url in urls:
    if url not in urls_dict:
      urls_dict[url] = host + url

  urls = []

  for (k, v) in urls_dict.items():
    urls.append(v)    
  
  return sorted(urls,key=get_key)

def download_images(img_urls, dest_dir):
  """Given the urls already in the correct order, downloads
  each image into the given directory.
  Gives the images local filenames img0, img1, and so on.
  Creates an index.html in the directory
  with an img tag to show each local image file.
  Creates the directory if necessary.
  """
  # +++your code here+++
  html_content = '<html><body>'

  if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)
  
  counter = 1
  for url in img_urls:  
    # build target path
    dest_file = 'img' + str(counter) + '.jpg'
    (filename, status) = urllib.urlretrieve(url,os.path.join(dest_dir,dest_file))
    html_content = html_content + '<img src="' + dest_file + '" />'
    counter += 1

  html_content = html_content + '</body></html>'
  html_filename = os.path.join(dest_dir, 'index.html')
  
  file = open(html_filename, 'w')
  file.write(html_content)

def main():
  args = sys.argv[1:]

  if not args:
    print 'usage: [--todir dir] logfile '
    sys.exit(1)

  todir = ''
  if args[0] == '--todir':
    todir = args[1]
    del args[0:2]

  img_urls = read_urls(args[0])

  if todir:
    download_images(img_urls, todir)
  else:
    print '\n'.join(img_urls)

if __name__ == '__main__':
  main()
