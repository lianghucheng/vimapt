#!/usr/bin/env python

import os

from .data_format import loads


class Remove(object):
    def __init__(self, vim_dir):
        self.vim_dir = vim_dir

    def remove_package(self, package_name):
        file_path = os.path.join(self.vim_dir,
                                 'vimapt/install',
                                 package_name)
        # print file_path
        fd = open(file_path, 'r')
        file_stream = fd.read()
        fd.close()
        meta_data = loads(file_stream)

        for file_name, _ in meta_data:
            file_token = file_name.split("/")
            if file_token[0] == "vimrc":
                continue
            target_path = os.path.join(self.vim_dir, file_name)

            # print target_path
            if os.path.isfile(target_path):
                os.unlink(target_path)
            else:
                pass
        remove_path = os.path.join(self.vim_dir,
                                   'vimapt/remove',
                                   package_name)
        os.rename(file_path, remove_path)
