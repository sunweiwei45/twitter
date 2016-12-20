#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/1 19:49
# @Author  : Sww
# @Site    : 
# @File    : get_edge_weight.py
# @Software: PyCharm Community Edition
import pandas


def get_relate_time(inpath=None):
    """
    统计每个点向外的交互次数
    :param filename:网络的路径
    :return:每个点的向外的交互次数
    """
    data = pandas.read_table(inpath, header=None, dtype={0: str, 1: str})
    df_data = pandas.DataFrame(data=data)  #数据形式的转化很重要
    df_out = df_data.groupby([0]).sum() #分组累加
    df_out = pandas.DataFrame(data=df_out)
    df_out.columns = ['num'] #修改列名
    df_out.index.name = 'id' #修改索引名
    print df_out
    return df_out


def get_edge_weight(inpath=None, outpath=None):
    """
    计算每个点的交互权重
    :param inpath: 输入数据的路径
    :param outpath: 输出数据的路径
    :return:
    """
    df_out = get_relate_time(inpath=inpath)
    network = pandas.read_table(inpath, dtype={0: str, 1: str}, header=None)
    network = pandas.DataFrame(data=network)
    for index, row in df_out.iterrows():
        print row['num']
        edges = network[network[0] == row.name]
        weight = edges[2] / int(row['num'])
        edges[3] = weight
        edges = edges.drop([2], axis=1)
        print edges
        edges.to_csv(outpath, index=False, header=None, mode="a", sep='\t')


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
        inpath = "/pegasus/harir/yangjinfeng/date_network/" + filename
        outpath = "/pegasus/harir/sunweiwei/weight/mention/" + filename + "_weight"

        get_edge_weight(inpath=inpath, outpath=outpath)
