#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/9 14:03
# @Author  : Sww
# @Site    : 
# @File    : know_json.py
# @Software: PyCharm Community Edition

import json
import pandas
import csv


def json_structure(filename=None, outpath=None):
    inpath = "E:/Sunweiwei/eHealth/twitter/data/json/" + filename + ".json"
    outpath = "E:/Sunweiwei/eHealth/twitter/data/json/structure/" + filename + "_k_originTweet_location.csv"
    with open(inpath, "r") as jsonfile:
        i = 0
        j = 0
        k = 0
        temp_list = []
        for line in jsonfile:
            j_data = json.loads(line)
            i += 1
            if j_data.has_key("entities"):
                j += 1
                if j_data["entities"]:
                    print j_data["tweet"]["id"]
                    print j_data["entities"]
                    # temp_list.append(j_data["originActor"]["location"].keys())
                    k += 1
                    # # for each in j_data["actor"]["phonesFromBody"]:
                    # temp = j_data["originTweet"]["location"].keys()
                    # with open(outpath, "ab") as csvfile:
                    #     write = csv.writer(csvfile)
                    #     write.writerow(temp)

        print str(i) + " " + str(j) + " " + str(k)
        print set(temp_list)

            # structure_1 = j_data.keys()
            # print structure_1
            # with open(outpath, "ab") as csvfile:
            #     write = csv.writer(csvfile)
            #     write.writerow(structure_1)



if __name__ == '__main__':
    file_list = [
        "part-r-00080-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00081-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00082-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00083-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00084-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00085-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00086-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00087-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00088-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00089-37ac32d8-f424-4f7c-b21c-33b34d491577",
    ]
    for filename in file_list:
        json_structure(filename=filename)
