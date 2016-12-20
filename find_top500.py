#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/11 21:27
# @Author  : Sww
# @Site    : 
# @File    : find_top500.py
# @Software: PyCharm Community Edition

import pandas
import csv

def top_500(filename=None):
    """
    找出前500个社区
    :param filename:
    :return:
    """
    inpath = "E:/Sunweiwei/eHealth/twitter/April/data/icpm_degree/" + filename + ".icpm_degree"
    outpath = "E:/Sunweiwei/eHealth/twitter/April/data/icpm_degree_top_500/" + filename + "_top_100.csv"
    # with open(inpath, "r") as tablefile:
    #     read = tablefile.readlines()
    #     for line in read:
    #         line_list = line.strip().split(",")
    #         if int(line_list[0]) < 101:
    #             with open(outpath,"ab") as csvfile:
    #                 write = csv.writer(csvfile)
    #                 write.writerow(line_list)
    data = pandas.read_table(inpath, header=None, sep=",", dtype=str)
    for i in range(1, 501):
        df_temp = data[data[0] == str(i)]
        print df_temp
        df_temp.to_csv(outpath, mode="a", header=None, index=False)


def change_from(filename=None):
    """
    保留社区号，degree和出入度标志（0,1）
    :param filename:
    :return:
    """
    inpath = "E:/Sunweiwei/eHealth/twitter/April/" + filename + ".icpm_degree"
    outpath = "E:/Sunweiwei/eHealth/twitter/April/" + filename + "_clean.csv"
    data = pandas.read_table(inpath, header=None, dtype=str, sep=",")
    df_out = data.loc[:, [0, 2]]
    df_out[4] = 0 ## out
    df_out.columns = ["comm", "degree", "type"]
    data = pandas.read_csv(inpath, header=None, dtype=str)
    df_in = data.loc[:, [0, 3]]
    df_in[4] = 1  ## in
    df_in.columns = ["comm", "degree", "type"]
    df_res = pandas.concat([df_out,df_in])
    df_res = pandas.DataFrame(data=df_res)
    df_res.to_csv(outpath, mode="a", header=None, index=False)


if __name__ == '__main__':
    file_list = [
        # "201604_01_07",
        # "201604_08_14",
        # "201604_15_21",
        # "201604_22_28",
        # "201604_29_30",
        "01_07_retweet"
    ]
    for filename in file_list:
        # top_500(filename=filename)
        change_from(filename=filename)





