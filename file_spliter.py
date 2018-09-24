#!usr/bin/env python  
# -*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      file_spliter.py 
@time:      2018/09/24 
"""

import os
import shutil
import collections
import concurrent.futures
import multiprocessing

import fire
from tqdm import tqdm


class FileSpilter:
    def split_file(self, fromfile_name, todir, chunksize=200 * 1024 ** 2, verbose=True, removeall=True):
        """
        分割文件
        :param fromfile_name:要分割文件路径
        :param todir:分割后，文件存放目录
        :param chunksize:分割的文件块大小
        :return:
        """
        self.__make_dir(todir, remove_all=removeall)
        part_num = 0
        file_size = os.path.getsize(fromfile_name)
        if verbose:
            p_bar = tqdm(total=file_size / chunksize)

        with open(fromfile_name, 'rb') as input_file:
            while True:
                file_chunk = input_file.read(chunksize)
                if not file_chunk: break
                part_num += 1
                output_filename = "{filename}.part{ext:0>4}".format(filename=self.__get_filename(fromfile_name),
                                                                ext=part_num)
                output_filename = os.path.join(todir, output_filename)

                if verbose:
                    p_bar.set_description("{filename}".format(filename=output_filename))
                with open(output_filename, 'wb') as output_file:
                    output_file.write(file_chunk)
                if verbose:
                    p_bar.update(1)
        if verbose:
            p_bar.close()
        Result = collections.namedtuple('Result', "filename partnums")
        return Result(self.__get_filename(fromfile_name), part_num)

    def split_files(self, fromdir, todir, chunksize=200 * 1024 ** 2, verbose=True, concurrency=multiprocessing.cpu_count()):
        """
        分割目录下所有文件
        :param fromdir: 待分割文件所在目录
        :param todir: 分割后文件块存放目录
        :param chunksize: 分割块大小
        :param verbose: 显示日志
        :param concurrency: 并发数
        :return:
        """
        self.__make_dir(todir)
        if not os.path.exists(fromdir):
            raise FileNotFoundError

        counter = collections.Counter()
        file_names = os.listdir(fromdir)

        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            todo_map = {}
            for file_name in file_names:
                future = executor.submit(self.split_file, os.path.join(fromdir, file_name), os.path.join(todir, file_name), chunksize, False, False)
                todo_map[future] = file_name

            done_iter = concurrent.futures.as_completed(todo_map)

            if verbose:
                done_iter = tqdm(done_iter, total=len(file_names))

            for future in done_iter:
                try:
                    res = future.result()
                    counter[res.filename] = res.partnums
                except:
                    raise
        return counter

    def join_file(self, fromdir, todir, filename=None, verbose=True, removeall=False):
        """
        合并文件
        :param fromdir:文件块所在目录
        :param filename: 最终文件名
        :param todir:合并后存放路径
        :return:
        """
        self.__make_dir(todir, remove_all=removeall)
        if not os.path.exists(fromdir):
            raise FileNotFoundError

        file_names = os.listdir(fromdir)
        file_names.sort()
        if not filename:
            if file_names:
                filename = self.__get_filename(file_names[0], ext=False)
            else:
                raise Exception(f'{fromdir} is empty!')

        part_nums = 0
        if verbose:
            p_bar = tqdm(total=len(file_names))
        with open(os.path.join(todir, filename), 'wb') as output_file:
            for file_name in file_names:
                with open(os.path.join(fromdir, file_name), 'rb') as input_file:
                    output_file.write(input_file.read())
                    part_nums += 1
                if verbose:
                    p_bar.update(1)
        if verbose:
            p_bar.close()
        Result = collections.namedtuple('Result', "filename partnums")
        return Result(filename, part_nums)

    def join_files(self, fromdir, todir, concurrency=multiprocessing.cpu_count(), verbose=True):
        """
        合并目录下各个文件的所有文件块
        :param fromdir:文件块所在目录
        :param todir:文件合成后存放目录
        :param concurrency:并发数
        :param verbose:打印日志
        :return:
        """
        self.__make_dir(todir)
        if not os.path.exists(fromdir):
            raise FileNotFoundError

        file_names = os.listdir(fromdir)
        todo_map = {}
        counter = collections.Counter()
        for file_name in file_names:
            file_path = os.path.join(fromdir, file_name)
            if os.path.isdir(file_path):
                file_parts = os.listdir(file_path)
                file_parts.sort()
                if file_parts:
                    todo_map[file_path] = file_parts
                else:
                    raise Exception(f"{file_path} is empty!")
            else:
                raise Exception("split file directories not exists!")

        with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as executor:
            futures = []
            for file_path, parts in todo_map.items():
                future = executor.submit(self.join_file, file_path, todir, None, False, False)
                futures.append(future)

            done_iter = concurrent.futures.as_completed(futures)
            if verbose:
                done_iter = tqdm(done_iter, total=len(file_names))

            for future in done_iter:
                try:
                    res = future.result()
                    counter[res.filename] = res.partnums
                except:
                    raise
        return counter

    def __make_dir(self, todir, remove_all=True):
        if not os.path.exists(todir):
            os.mkdir(todir)

        if remove_all:
            for file_name in os.listdir(todir):
                try:
                    os.remove(os.path.join(todir, file_name))
                except IsADirectoryError:
                    shutil.rmtree(os.path.join(todir, file_name))

    def __get_filename(self, fromfile, ext=True):
        full_name = os.path.split(fromfile)[1]
        file_name = os.path.splitext(full_name)[0]
        return full_name if ext else file_name


if __name__ == '__main__':
    fire.Fire(FileSpilter)
