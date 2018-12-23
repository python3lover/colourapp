'''
ColourApp/copy.py
Copies to destination directory.
By:
* Ken Shibata, Dec 2018
'''

import shutil, os, json

class copy():
    def __init__(self):
        self.unpacker_result_path = 'unpacker_result'
        app_data_file = open(os.path.join(self.unpacker_result_path, 'app_data.json'))
        app_data = json.load(app_data_file)
        app_data_file.close()
        self.destination_path = '/home/kenxshibata/Apps/{id}/{edition}/{ver}/{channel}/{language0}-{language1}'.format(id=app_data['id'], ver=app_data['ver'], channel=app_data['channel'], edition=app_data['edition'], language0=app_data['language'][0], language1=app_data['language'][1])
    def _copy(self):
        print('Info  Copying from {} to {}...'.format(self.unpacker_result_path, self.destination_path))
        try:
            shutil.copytree(self.unpacker_result_path, self.destination_path)
        except FileExistsError:
            print('Info  File exists, exiting w/ code 0.')
        else:
            print('Info  Done.')

if __name__ == '__main__':
    copy_inst = copy()
    copy_inst._copy()
