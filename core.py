'''
ColourApp/core.py
Core starter library
By:
* Ken Shibata, Dec 2018
'''

import unpack, validate, copy_

class core():
    def __init__(self):
        self.pack_path = None
    def _start(self, pack_path):
        self.pack_path = pack_path
        unpacker_inst = unpack.unpack(self.pack_path)
        unpacker_inst._find_format()
        unpacker_inst._unpack()
        validator_inst = validate.validate()
        validator_inst._validate_app_data()
        copier_inst = copy_.copy()
        copier_inst._copy()

def auto(pack_path):
    core_inst = core()
    core_inst._start(pack_path)

if __name__ == '__main__':
    print('      ColourApp/core.py Direct Run')
    pack_path = input('Input Pack Path ')
    print('Info  Starting...')
    core_inst = core()
    core_inst._start(pack_path)
    print('Info  Done.')
