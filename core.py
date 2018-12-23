'''
ColourApp/core.py
Core starter library
By:
* Ken Shibata, Dec 2018
'''

import unpacker, validator, copier

class core():
    def __init__(self):
        self.pack_path = None
    def _start(self, pack_path):
        self.pack_path = pack_path
        unpacker_inst = unpacker.unpacker(self.pack_path)
        unpacker_inst._find_format()
        unpacker_inst._unpack()
        validator_inst = validator.validate()
        validator_inst._validate_app_data()
        copier_inst = copier.copy()
        copier_inst._copy()

if __name__ == '__main__':
    print('      ColourApp/core.py Direct Run')
    pack_path = input('Input Pack Path ')
    print('Info  Starting...')
    core_inst = core()
    core_inst._start(pack_path)
    print('Info  Done.')
