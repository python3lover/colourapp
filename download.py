'''
ColourApp/download.py
Download ColourApp from source URL.
By:
* Ken Shibata, Dec 2018
'''

import urllib

class download():
    def __init__(self, source_url, save_path):
        self.source_url = source_url
        self.save_path  = save_path
    def download(self):
        testfile = urllib.URLopener()
        testfile.retrieve(self.source_url, self.save_path)

if __name__ == '__main__':
    print('      ColourApp/download.py')
    download_inst = download(input('Input Source URL '), input('Input Save Path'))
    print('Info  Downloading ColourApp...', end=' ')
    download_inst.download()
    print('Done.')