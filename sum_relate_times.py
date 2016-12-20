#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/27 21:50
# @Author  : Sww
# @Site    : 
# @File    : sum_relate_times.py
# @Software: PyCharm Community Edition
import pandas


def main(filename):
    """
    统计每个点的交互次数
    :param filename:
    :return:
    """
    sourcepath = "/pegasus/harir/yangjinfeng/date_network/" + filename
    inpath = "/pegasus/harir/sunweiwei/community/ralate_time/mention/" + filename + "_in.csv"
    outpath = "/pegasus/harir/sunweiwei/community/relate_time/mention/" + filename + "_out.csv"

    data = pandas.read_table(r"E:/Sunweiwei/eHealth/twitter/temp/total_network", header=None, dtype={0: str, 1: str})
    dataframe = pandas.DataFrame(data=data)  #数据形式的转化很重要
    df_out = dataframe.groupby([0]).sum() #分组累加
    df_in = dataframe.groupby([1]).sum()
    df_out.to_csv(r"E:/Sunweiwei/eHealth/twitter/temp/total_network_out.csv", header=None)
    df_in.to_csv(r"E:/Sunweiwei/eHealth/twitter/temp/total_network_in.csv", header=None)


if __name__ == '__main__':
    file_list = [
        # "2016-03-23-dateedge_network",
        # "2016-03-24-dateedge_network",
        # "2016-03-25-dateedge_network",
        # "2016-03-26-dateedge_network",
        # "2016-03-27-dateedge_network",
        # "2016-03-28-dateedge_network",
        # "2016-03-29-dateedge_network",
        # "2016-03-30-dateedge_network",
        # "2016-03-31-dateedge_network",
        # "total_network",
        # "2016-03-23-dateedge_network_retweet",
        # "2016-03-24-dateedge_network_retweet",
        # "2016-03-25-dateedge_network_retweet",
        # "2016-03-26-dateedge_network_retweet",
        # "2016-03-27-dateedge_network_retweet",
        # "2016-03-28-dateedge_network_retweet",
        # "2016-03-29-dateedge_network_retweet",
        # "2016-03-30-dateedge_network_retweet",
        # "2016-03-31-dateedge_network_retweet",
        # "total_network_retweet",
        "2016-03-23-dateedge_network_mention",
        "2016-03-24-dateedge_network_mention",
        "2016-03-25-dateedge_network_mention",
        "2016-03-26-dateedge_network_mention",
        "2016-03-27-dateedge_network_mention",
        "2016-03-28-dateedge_network_mention",
        "2016-03-29-dateedge_network_mention",
        "2016-03-30-dateedge_network_mention",
        "2016-03-31-dateedge_network_mention",
        "total_network_mention",
    ]
    for filename in file_list:
        main(filename=filename)
