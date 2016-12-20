#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/25 19:12
# @Author  : Sww
# @Site    : 
# @File    : test.py
# @Software: PyCharm Community Edition
import csv
import pandas


def stitching_columns(row):
    """
    将pandas中的两列简单拼接，such as：column1=[a,c,3], column2=[3,2,d], res = [a3,c2,3d]
    :param x:(Dataform),一行
    :return:(object)
    """
    id_1 = str(row[0]).zfill(20) #将id从int转为string，并
    id_2 = str(row[1]).zfill(20)
    res = id_1 + '#' + id_2 + '#' + str(row[2])
    return res

def main():
    data = pandas.read_csv(r"")


    # with open(r"E:/Sunweiwei/eHealth/twitter/temp/2016-03-23-dateedge_network", r"rb") as csvfile:
    #     read = csv.reader(csvfile)
    #     for each in read:
    #         temp_list = each[0].split("\t")
    #         # print repr(temp_list)
    #         with open(r"E:/Sunweiwei/eHealth/twitter/temp/2016-03-23-dateedge_network.csv",r"ab") as csvfile:
    #             write = csv.writer(csvfile)
    #             write.writerow(temp_list)
    df = pandas.read_csv(r"E:/Sunweiwei/eHealth/twitter/temp/123.csv", header=None, index_col=None)
    df = df.T
    df.to_csv("E:/Sunweiwei/eHealth/twitter/temp/123.csv", header=None, index=False, mode="a")
    # for i in range(2):
    #     df.dropna()
    #     df.to_csv(r"E:/Sunweiwei/eHealth/twitter/temp/123.csv", mode="a")
    # df = df.drop_duplicates()
    # print df

    # df = pandas.read_table("E:/Sunweiwei/eHealth/twitter/temp/total_network", header=None)
    # df.to_csv()
    # with open(r"E:/Sunweiwei/eHealth/twitter/temp/123.icpm", r"rb") as csvfile:
    #     read = csvfile.readlines()
    #     for each in read:
    #         line = each.strip().split(' ')  # 一个line便是一个community
    #         # print line
    #         df_list = []
    #         for use in line:
    #             # 在network中获得该社区所有用户发出的edge
    #             use_in = df[df[0] == int(use)].apply(stitching_columns, axis=1)
    #             df_list.append(use_in)
    #         for use in line:
    #             # 在network中获得该社区所有用户接受的edge
    #             use_out = df[df[1] == int(use)].apply(stitching_columns, axis=1)
    #             df_list.append(use_out)
    #         temp_use_community = pandas.concat(df_list).dropna(axis=1)  # 将同一个社区内的用户涉及的边合并,去除为空的行
    #         use_community = temp_use_community.drop_duplicates()  # 去重


    # #
    # list = []
    # ss1 = "00000000000708212528"
    # res1 = df[df[0] == int(ss1)].apply(stitching_columns, axis=1)
    # print res1
    #
    # list.append(res1)
    # # print res1
    # ss2 = "00000000000711716023"
    # res1 = df[df[0] == int(ss2)].apply(stitching_columns, axis=1)
    # # sdf = [res1,res2]
    # # print sdf
    # # res = pandas.concat(sdf, axis=1)
    # # print res
    # list.append(res1)
    # ss3 = "00000000000346667546"
    # res1 = df[df[0] == int(ss2)].apply(stitching_columns, axis=1)
    # list.append(res1)
    # # res = pandas.concat(list,axis=1)
    # print list
    # # res = res.drop_duplicates()
    # # res.to_csv("E:/Sunweiwei/eHealth/twitter/temp/123.csv", index=False)

if __name__ == '__main__':
    main()
