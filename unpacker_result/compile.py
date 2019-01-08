'''
ColourApp/compile.py
Auto-compiler for Qt UI Files
By:
* Ken Shibata, Dec 2018
'''
print('      Auto-compiler for Qt UI Files')
print('Info  Importing libraries...', end=' ')
try:
    from PyQt5.uic import compileUi
    import os
except Exception as error:
    print('Error.\nError Occured @ Line 10~11: {}'.format(error))
else:
    print('Done.')

print('Info  Listing files...', end=' ')
try:
    files = os.listdir()
except Exception as error:
    print('Error.\nError Occurred @ Line 18: {}'.format(error))
else:
    print('Done.')

try:
    for file in files:
        if '.ui' in file:
            print('Info  Compiling {} to {}...'.format(file, file.replace('.ui', '_ui.py')), end=' ') # TODO Fix so test.ui.ui won't turn into test_ui.py_ui.py instead of test.ui_ui.py
            compileUi(open(file), open(file.replace('.ui', '_ui.py'), mode='w'))
            print('Done.')
except Exception as error:
    print('Error.\nError Occured @ Line 24~27: {}'.format(error))