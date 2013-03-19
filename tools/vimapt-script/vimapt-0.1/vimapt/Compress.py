#!/usr/bin/env python

import os
from yaml import dump
try:
    from yaml import CDumper as Dumper
except ImportError:
    from yaml import Dumper


class Compress():
    def __init__(self, source_dir, output_file):
        self.source_dir = source_dir
        self.output_file = output_file
        self.hook_object = False
        self.filter_object = False

    def compress(self):
        ball_file_list = self.scan_dir()
        ball_data = []
        ball_content = []
        for f in ball_file_list:
            fd = open(f, 'r')
            file_lines = fd.readlines()
            fd.close()
            relfile_path = os.path.relpath(f, self.source_dir)
            if self.filter_object:
                if not self.filter_object(relfile_path, file_lines):
                    continue
            if self.hook_object:
                f, file_lines = self.hook_object(f, file_lines)
            line_number = len(file_lines)
            #if is not empty file
            if line_number:
                last_line = file_lines[-1]
                if not last_line.endswith("\n"):
                    file_lines[-1] += "\n"
                ball_content += file_lines
            ball_data.append([relfile_path, line_number])

        meta_output = dump(ball_data, Dumper=Dumper)
        ball_output = "".join(ball_content)
        output = meta_output + "\n" + ball_output
        fd = open(self.output_file, 'w')
        fd.write(output)
        fd.close()

    def scan_dir(self):
        file_path_list = []
        yid = os.walk(self.source_dir)
        for root_dir, path_list, file_list in yid:
            for f in file_list:
                abspath = os.path.join(root_dir, f)
                file_path_list.append(abspath)
        return file_path_list

    def hook(self, hook_object):
        self.hook_object = hook_object

    def filter(self, filter_object):
        self.filter_object = filter_object
