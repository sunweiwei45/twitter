#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/27 20:21
# @Author  : Sww
# @Site    : 
# @File    : get_edge_weight_old.py
# @Software: PyCharm Community Edition

import pandas
import csv


def main(filename=None):
    """
    计算每个点的交互权重
    :return:
    """
    network_path = "/pegasus/harir/yangjinfeng/date_network/" + filename
    relate_time_path = "/pegasus/harir/sunweiwei/relate_time/mention/" + filename + "_out.csv"
    inpath = "/pegasus/harir/sunweiwei/weight/mention/" + filename + "_weight.csv"
    # data = pandas.read_table("E:/Sunweiwei/eHealth/twitter/temp/2016-03-23-dateedge_network", names=['id1', 'id2', 'num'], dtype={'id1': np.str, 'id2': np.str}, header=None)
    network = pandas.read_table(network_path, dtype={0: str, 1: str}, header=None)
    network = pandas.DataFrame(data=network)
    with open(relate_time_path, r"rb") as csvfile:
        read = csv.reader(csvfile)
        for each in read:
            edges = network[network[0] == str(each[0])]
            edges[3] = edges[2] / int(each[1])
            edges.to_csv(inpath, index=False, header=None, mode="a")
            print edges

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
