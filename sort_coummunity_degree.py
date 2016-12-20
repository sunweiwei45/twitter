#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/25 18:08
# @Author  : Sww
# @Site    : 
# @File    : sort_coummunity_degree.py
# @Software: PyCharm Community Edition
import pandas


def simple_splice(row):
    res = str(row['id']) + "#" + str(row['degree'])
    return res

def point_degree(filename=None):
    """
    将社区具体化，慢
    :return:
    """
    df_ntework = pandas.read_table("/pegasus/harir/yangjinfeng/date_network/total_network", dtype=str, header=None)
    df_ntework.columns = ['id1', 'id2', 'times']
    inpath = "/pegasus/harir/yangjinfeng/date_network/output/" + filename + ".icpm"
    outpath = "/pegasus/harir/sunweiwei/community/sort_out_degree/mention/" + filename + "_out_degree"

    with open(inpath, r"rb") as csvfile:
        read = csvfile.readlines()
        for each in read:
            #找出社区内每一个点在社区内的出度
            community = each.strip().split(' ')  #一个line便是一个community
            s_community = set(community)  #将list放到集合中
            df_list = []
            for point in community:
                #循环找出每一个点的社区出度
                df_query = df_ntework[df_ntework['id1'] == str(point)]
                list_out = df_query['id2'].values.tolist()
                s_out = set(list_out)  #取集合
                s_result = s_community & s_out #取交集
                degree = len(s_result)  #交集中的元素数即id的社区出度
                df_id_deg = pandas.DataFrame({'id': [point], 'degree': [degree]}, dtype=str)
                print df_id_deg
                df_list.append(df_id_deg) #添加id_degree
            df_community_deg = pandas.concat(df_list, ignore_index=True)  #组合同一个社区内的计算结果
            df_community_deg = pandas.DataFrame(data=df_community_deg).sort(['degree'], ascending=False) #排序，升序
            print df_community_deg
            df_community_deg = df_community_deg.apply(simple_splice, axis=1)
            df_community_deg = df_community_deg.T
            df_community_deg.to_csv(outpath, header=None, index=False, sep="\t", mode="a")


if __name__ == '__main__':
    file_list = [
        "SLPAw_total_network_mention_run1_r0.01_v3_T100",
        "SLPAw_total_network_mention_run1_r0.05_v3_T100",
        "SLPAw_total_network_mention_run1_r0.15_v3_T100",
        "SLPAw_total_network_mention_run1_r0.1_v3_T100",
        "SLPAw_total_network_mention_run1_r0.25_v3_T100",
        "SLPAw_total_network_mention_run1_r0.2_v3_T100",
        "SLPAw_total_network_mention_run1_r0.35_v3_T100",
        "SLPAw_total_network_mention_run1_r0.3_v3_T100",
        "SLPAw_total_network_mention_run1_r0.45_v3_T100",
        "SLPAw_total_network_mention_run1_r0.4_v3_T100",
        "SLPAw_total_network_mention_run1_r0.5_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.01_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.05_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.15_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.1_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.25_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.2_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.35_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.3_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.45_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.4_v3_T100",
        # "SLPAw_total_network_retweet_run1_r0.5_v3_T100",
        # "SLPAw_total_network_run1_r0.01_v3_T100",
        # "SLPAw_total_network_run1_r0.05_v3_T100",
        # "SLPAw_total_network_run1_r0.15_v3_T100",
        # "SLPAw_total_network_run1_r0.1_v3_T100",
        # "SLPAw_total_network_run1_r0.25_v3_T100",
        # "SLPAw_total_network_run1_r0.2_v3_T100",
        # "SLPAw_total_network_run1_r0.35_v3_T100",
        # "SLPAw_total_network_run1_r0.3_v3_T100",
        # "SLPAw_total_network_run1_r0.45_v3_T100",
        # "SLPAw_total_network_run1_r0.4_v3_T100",
        # "SLPAw_total_network_run1_r0.5_v3_T100",
    ]
    for filename in file_list:
        point_degree(filename)
