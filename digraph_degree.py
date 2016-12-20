#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/25 10:56
# @Author  : Sww
# @Site    : 
# @File    : digraph_degree.py
# @Software: PyCharm Community Edition

import networkx
import csv
DG = networkx.DiGraph()

def main():
    with open(r"E:/Sunweiwei/eHealth/twitter/temp/2016-03-23-dateedge", r"rb") as csvfile:
        read = csv.reader(csvfile)
        for each in read:
            temp_list = each[0].split("\t")
            DG.add_edge(temp_list[0], temp_list[2])
            # print temp_list
    in_degree = DG.in_degree()
    out_degree = DG.out_degree()

    # print indegree
    # print outdegree
    with open(r"E:/Sunweiwei/eHealth/twitter/2016-03-23-indegree.csv", r"wb") as csvfile:
        write = csv.writer(csvfile)
        for key in in_degree:
            temp = []
            temp.append(key)
            temp.append(in_degree[key])
            write.writerow(temp)

    with open(r"E:/Sunweiwei/eHealth/twitter/2016-03-23-outdegree.csv", r"wb") as csvfile:
        write = csv.writer(csvfile)
        for key in out_degree:
            temp = []
            temp.append(key)
            temp.append(out_degree[key])
            write.writerow(temp)


if __name__ == '__main__':
    main()
