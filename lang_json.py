#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/5 19:23
# @Author  : Sww
# @Site    : 
# @File    : lang_json.py
# @Software: PyCharm Community Edition

import csv
import json


# def to_json(path=None):
#     with open(path, "rb") as csvfile:
#         read = csv.reader(csvfile)
#         for each in read:
#             line_dict = {}
#             lang_dict = {}
#             for i in range(1,len(each)):
#                 lang = str(each[i]).split("#")[0]
#                 num = str(each[i]).split("#")[1]
#                 lang_dict[str(lang)] = num
#             line_dict[str(each[0])] = lang_dict
#             with open("E:/Sunweiwei/eHealth/twitter/data/statistics/count_lang.json","a") as jsonfile:
#                 json.dump(line_dict, jsonfile)
#                 jsonfile.write("\n")
#             print line_dict


def get_lang_group(path=None):
    with open(path, "r") as jsonfile:
        res_list = []
        for each in jsonfile:
            line = json.loads(each)
            for key in line:
                key_list = sorted(line[key].keys())
                res = "#".join(key_list)
                res_list.append(res)
    res_list = list(set(res_list))
    print len(res_list)
    for each in res_list:
        print each


if __name__ == '__main__':

    path = "E:/Sunweiwei/eHealth/twitter/data/statistics/count_lang.json"
    get_lang_group(path)
