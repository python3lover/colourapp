'''
ColourApp/validate.py
Parses and validates the unpacked archive/pack
By:
* Ken Shibata, Dec 2018
'''

import os, json

class validate():
    def __init__(self):
        self.unpacker_result_path = 'unpacker_result'
        app_data_file = open(os.path.join(self.unpacker_result_path, 'app_data.json'))
        self.app_data = json.load(app_data_file)
        app_data_file.close()
    def _validate_app_data(self):
        print('Info  Validating app...')
        self.app_data['name']
        self.app_data['desc']
        for icon in range(len(self.app_data['icons'])):
            icon['name']
            icon['path']
        self.app_data['id']
        self.app_data['uuid']
        self.app_data['ver']
        self.app_data['edition']
        self.app_data['language']
        self.app_data['ver_name']
        self.app_data['channel']
        self.app_data['build']
        self.app_data['ver_string']
        self.app_data['ver_build_string']
        print('Info  Validated {} Version {} Build {} {} Edition {} (Language)'.format(self.app_data['name'], self.app_data['ver'], self.app_data['build'], self.app_data['edition'], self.app_data['language']))

if __name__ == '__main__':
    valid = validate()
    valid._validate_app_data()
