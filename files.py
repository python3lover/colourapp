'''
ColourApp/files.py
Library for browsing files
By:
* Ken Shibata, Dec 2018
'''
import os, json

def list_files(path):
    old_wd = os.getcwd()
    os.chdir(path)
    tree = {}
    apps = os.listdir('.')
    for app in apps:
        tree[app] = {}
        edns = os.listdir(app)
        for edn in edns:
            tree[app][edn] = {}
            vers = os.listdir(os.path.join(app, edn))
            for ver in vers:
                tree[app][edn][ver] = {}
                chls = os.listdir(os.path.join(app, edn, ver))
                for chl in chls:
                    tree[app][edn][ver][chl] = {}
                    lngs = os.listdir(os.path.join(app, edn, ver, chl))
                    for lng in lngs:
                        tree[app][edn][ver][chl][lng] = None
    os.chdir(old_wd)
    return tree

def tree_to_path(tree):
    path = []
    apps = list(tree.keys())
    for app in apps:
        edns = list(tree[app].keys())
        for edn in edns:
            vers = list(tree[app][edn].keys())
            for ver in vers:
                chls = list(tree[app][edn][ver].keys())
                for chl in chls:
                    lngs = list(tree[app][edn][ver][chl].keys())
                    for lng in lngs:
                        path_to_appdata = os.path.expanduser('~/Apps/{}/{}/{}/{}/{}/app_data.json'.format(app, edn, ver, chl, lng))
                        appdata = json.load(open(path_to_appdata))
                        nam = appdata['name']
                        path.append('{nam} {edn} {ver} {chl} ({lng})'.format(nam=nam, app=app, edn=edn, ver=ver, chl=chl, lng=lng))
    return path
