#!usr/bin/env python  
#-*- coding:utf-8 -*-

""" 
@author:    nico 
@file:      file_spilter_asyncio.py 
@time:      2018/09/27 
""" 

import asyncio
import shutil
import os

import aiofiles


class FileSpilter:
    async def split_file(self, fromfile_name, todir, chunksize=200 * 1024 ** 2, verbose=True, removeall=True):
        """

        :param fromfile_name:
        :param todir:
        :param chunksize:
        :param verbose:
        :param removeall:
        :return:
        """

    async def split_files(self, fromdir, todir, chunksize=200 * 1024 ** 2, concurrency=1, verbose=True):
        """

        :param fromdir:
        :param todir:
        :param chunksize:
        :param concurrency:
        :param verbose:
        :return:
        """

    async def join_file(self, fromdir, todir, filename=None, verbose=True, removeall=False):
        """

        :param fromdir:
        :param todir:
        :param filename:
        :param verbose:
        :param removeall:
        :return:
        """

    async def join_files(self, fromdir, todir, concurrency=1, verbose=True):
        """

        :param fromdir:
        :param todir:
        :param concurrency:
        :param verbose:
        :return:
        """

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