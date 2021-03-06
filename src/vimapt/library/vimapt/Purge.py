#!/usr/bin/env python

import os

from .data_format import loads


class Purge(object):
    def __init__(self, vim_dir):
        self.vim_dir = vim_dir
        self.package_name = None

    def purge_package(self, package_name):
        self.package_name = package_name

        file_install_path = os.path.join(self.vim_dir,
                                         'vimapt/install',
                                         self.package_name)
        file_remove_path = os.path.join(self.vim_dir,
                                        'vimapt/remove',
                                        self.package_name)
        if os.path.isfile(file_install_path):
            file_path = file_install_path
        else:
            file_path = file_remove_path
        fd = open(file_path, 'r')
        file_stream = fd.read()
        fd.close()
        meta_data = loads(file_stream)

        for file_name, _ in meta_data:
            target_path = os.path.join(self.vim_dir, file_name)
            if os.path.isfile(target_path):
                os.unlink(target_path)
            else:
                pass
        os.unlink(file_path)
