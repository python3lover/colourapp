'''
ColourApp/unpack.py
Unpackes archives/packs and puts them into a folder.
By:
* Ken Shibata, Dec 2018
'''

import zipfile, os, shutil#, fleep

class unpack():
    def __init__(self, pack_path):
        self.pack_path = pack_path
        self.pack_format = ''
        self.pack_compatible = None
        self.unpack_dir_raw = 'unpacker_result_raw'
        self.unpack_dir = 'unpacker_result'
    def _find_format(self):
        pass
        # print('Info  Finding format...')
        # with open(self.pack_path, 'rb') as pack:
        #     pack_info = fleep.get(pack.read(256))
        # self.pack_format = pack_info.extension
        # print('Info  Done. Format is {}.'.format(self.pack_format))
        # print('Info  Checking compatibility...')
        # self.pack_compatible = 'zip' in self.pack_format
        # if self.pack_compatible:
        #     print('Info  Done. Compatible.')
        # else:
        #     print('Info  Done. Incompatible; exiting w/ code 1.')
        #     exit(1)
    def _unpack(self):
        print('Info  Unpacking...')
        self.pack_format = ['zip']
        if 'zip' in self.pack_format:
            with zipfile.ZipFile(self.pack_path, 'r') as zip_ref:
                zip_ref.extractall(self.unpack_dir_raw)
        # Check if there is only 1 dir, if 1, move dir contents to ../*
        if len(list(os.listdir('./{}'.format(self.unpack_dir_raw)))) == 1:
            # shutil.copytree(self.unpacker_dir_raw, self.unpack_dir)
            shutil.rmtree('unpacker_result')
            only_dir = list(os.listdir('./{}'.format(self.unpack_dir_raw)))[0]
            shutil.copytree('unpacker_result_raw/{}'.format(only_dir), 'unpacker_result')
        # TODO Move file contents of dir if there is only one dir inside unpacker_result
        print('Info  Done. Results in {}.'.format(self.unpack_dir))

if __name__ == '__main__':
    pack_path = input('Input Pack Path ')
    unpack = unpacker(pack_path)
    unpack._find_format()
    unpack._unpack()
