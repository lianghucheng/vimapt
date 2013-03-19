#!/usr/bin/env python

import os
import sys
import vim


def main():
    vim_dir = sys.argv[1]
    install_dir = os.path.join(vim_dir, 'vimapt/install')
    file_list = [f for f in os.listdir(install_dir)
             if os.path.isfile(os.path.join(install_dir, f))]
    return file_list


if __name__ == "__main__":
    #current_file_path = os.path.dirname(sys.argv[3])
    package_list = main()
    pkg_list_string = "[" + ",".join(["'" + i + "'" for i in package_list ]) + "]"
    vim.command('let s:package_remove_list = ' + pkg_list_string)