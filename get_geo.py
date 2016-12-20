#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/1 21:14
# @Author  : Sww
# @Site    : 
# @File    : get_geo.py
# @Software: PyCharm Community Edition

import json
import pandas
import csv


# def get_coordinates(file_list=None):
#     """
#     从json文件中提取用户id和geo
#     :param file_list:
#     :return:
#     """
#     for filename in file_list:
#         # file_path = "/pegasus/twitter-p-or-t-uae-201603.json.dxb/" + filename
#         file_path = "E:/Sunweiwei/eHealth/twitter/data/json/" + filename + ".json"
#         with open(file_path, "r") as jsonfile:
#             for line in jsonfile:
#                 temp_list = []
#                 t_json = json.loads(line)
#                 id = t_json['actor']['id']
#                 df_1 = pandas.DataFrame([id], dtype=str)
#                 temp_list.append(df_1)
#                 try:
#                     geo_list = t_json['tweet']['location']['geo']['coordinates'][0]
#                     for each in geo_list:
#                         coordinates = str(each[0]) + "#" + str(each[1])
#                         df_2 = pandas.DataFrame([coordinates], dtype=str)
#                         temp_list.append(df_2)
#                 except:
#                     pass
#                     # print id + " ************ no geo **************** "
#                 df_res = pandas.concat(temp_list)
#
#                 df_res = pandas.DataFrame(data=df_res).T
#                 outpath = "E:/Sunweiwei/eHealth/twitter/data/json/" + filename + "_geo.csv"
#                 df_res.to_csv(outpath, header=None, index=False, mode="a")

# def tweet_have_coordinates(file_list=None):
#     """
#     从Json文件中找出所发的tweet中包含geo的tweet的id
#     :param file_list:
#     :return:
#     """
#     for filename in file_list:
#         file_path = "/pegasus/twitter-p-or-t-uae-201603.json.dxb/" + filename + ".json"
#         # file_path = "E:/Sunweiwei/eHealth/twitter/data/json/" + filename + ".json"
#         with open(file_path, "r") as jsonfile:
#             for line in jsonfile:
#                 t_json = json.loads(line)
#                 id = t_json['tweet']['id']
#                 df_1 = pandas.DataFrame([id], dtype=str)
#                 try:
#                     coordinates = t_json['tweet']['location']['geo']['coordinates'][0][0]
#                     if coordinates:
#                         have_coo = 1
#                     else:
#                         have_coo = 0
#                 except:
#                     have_coo = 0
#
#                 df_2 = pandas.DataFrame([have_coo])
#                 df_res = pandas.concat([df_1, df_2])
#                 print df_res
#                 df_res = pandas.DataFrame(data=df_res).T
#                 outpath = "/pegasus/harir/sunweiwei/geo/tweet_geo.csv"
#                 df_res.to_csv(outpath, header=None, index=False, mode="a")
#         print file_path

def actor_have_coordinates(file_list=None):
    """
    从Json文件中找出每个用户所发的带有geo的推特数
    :param file_list:
    :return:
    """
    for filename in file_list:
        # file_path = "/pegasus/twitter-p-or-t-uae-201603.json.dxb/" + filename + ".json"
        file_path = "E:/Sunweiwei/eHealth/twitter/data/json/" + filename + ".json"
        data_dict = {}
        with open(file_path, "r") as jsonfile:
            temp_list = []
            for line in jsonfile:
                t_json = json.loads(line)
                id = t_json['actor']['id']
                df_1 = pandas.DataFrame([id], dtype=str)
                temp_list.append(df_1)
                # try:
                #     coordinates = t_json['tweet']['location']['geo']['coordinates'][0][0]
                #     if coordinates:
                #         have_coo = 1
                #     else:
                #         have_coo = 0
                # except:
                #     have_coo = 0
        #         have_coo = 1
        #         df_2 = pandas.DataFrame([have_coo])
        #         df_res = pandas.concat([df_1, df_2])
        #         df_res = pandas.DataFrame(data=df_res).T
        #         temp_list.append(df_res)
        df_file_res = pandas.concat(temp_list)
        df_file_res = pandas.DataFrame(data=df_file_res)
        # df_file_res.columns = ['a', 'b']
        df_file_res = df_file_res.groupby([0]).size()
        print df_file_res
        # df_file_res.to_csv(r"E:/Sunweiwei/eHealth/twitter/data/json/14.csv", header=None, mode="a")
        # df_file_res = df_file_res.groupby()
        # count_actor_geo(df_actor_geo=df_file_res)
        # print file_path


def count_actor_geo(df_actor_geo=None):
    """
    统计发过带有geo的tweet的用户
    :param df_actor_geo:
    :return:
    """
    df_actor_geo.columns = ['a', 'b']
    print df_actor_geo
    df_group_sum = df_actor_geo.groupby(['a']).sum()
    df_group_sum = pandas.DataFrame(data=df_group_sum)
    df_no_geo = df_group_sum[df_group_sum['b'] == 0]
    df_no_geo['c'] = 1
    df_no_geo = df_no_geo['c']
    df_no_geo = pandas.DataFrame(data=df_no_geo)
    df_no_geo['d'] = df_no_geo.index
    df_no_geo.columns = ['b', 'c']
    df_no_geo['d'] = df_no_geo['b']
    df_no_geo = df_no_geo.drop(['b'], axis=1)
    print df_no_geo

    df_have_geo = df_group_sum[df_group_sum['b'] > 0]
    df_have_geo['c'] = 1
    df_have_geo = df_have_geo['c']
    df_have_geo = pandas.DataFrame(data=df_have_geo)
    df_have_geo['d'] = df_have_geo.index
    df_have_geo.columns = ['b', 'c']
    df_have_geo['d'] = df_have_geo['b']
    df_have_geo = df_have_geo.drop(['b'], axis=1)
    print df_have_geo
    df_actor_geo = pandas.concat([df_no_geo, df_have_geo])
    df_actor_geo =pandas.DataFrame(data=df_actor_geo, index=None)
    print df_actor_geo
    df_actor_geo.to_csv("/pegasus/harir/sunweiwei/geo/actor_geo.csv", index=False, header=None, mode="a")

if __name__ == '__main__':
    file_list = [
        # "part-r-00000-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00001-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00002-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00003-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00004-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00005-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00006-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00007-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00008-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00009-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00010-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00011-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00012-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00013-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00014-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00015-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00016-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00017-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00018-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00019-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00020-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00021-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00022-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00023-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00024-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00025-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00026-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00027-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00028-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00029-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00030-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00031-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00032-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00033-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00034-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00035-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00036-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00037-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00038-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00039-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00040-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00041-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00042-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00043-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00044-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00045-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00046-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00047-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00048-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00049-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00050-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00051-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00052-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00053-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00054-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00055-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00056-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00057-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00058-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00059-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00060-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00061-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00062-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00063-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00064-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00065-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00066-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00067-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00068-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00069-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00070-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00071-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00072-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00073-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00074-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00075-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00076-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00077-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00078-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00079-37ac32d8-f424-4f7c-b21c-33b34d491577",
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
        # "part-r-00090-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00091-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00092-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00093-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00094-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00095-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00096-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00097-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00098-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00099-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00100-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00101-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00102-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00103-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00104-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00105-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00106-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00107-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00108-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00109-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00110-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00111-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00112-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00113-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00114-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00115-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00116-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00117-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00118-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00119-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00120-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00121-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00122-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00123-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00124-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00125-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00126-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00127-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00128-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00129-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00130-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00131-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00132-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00133-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00134-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00135-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00136-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00137-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00138-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00139-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00140-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00141-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00142-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00143-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00144-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00145-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00146-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00147-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00148-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00149-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00150-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00151-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00152-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00153-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00154-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00155-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00156-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00157-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00158-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00159-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00160-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00161-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00162-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00163-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00164-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00165-37ac32d8-f424-4f7c-b21c-33b34d491577",
        # "part-r-00166-37ac32d8-f424-4f7c-b21c-33b34d491577",
    ]
    actor_have_coordinates(file_list=file_list)
    df_1 = pandas.read_csv(r"/pegasus/harir/sunweiwei/geo/actor_geo_num.csv", header=None, dtype=str)
    df_2 = pandas.read_csv(r"/pegasus/harir/sunweiwei/geo/actor_tweet_num.csv", header=None, dtype=str)
    df_1 = df_1.set_index([0])
    df_2 = df_2.set_index([0])
    df_res = pandas.concat([df_1, df_2], axis=1)
    df_res = pandas.DataFrame(data=df_res)
    df_res.to_csv(r"/pegasus/harir/sunweiwei/geo/actor_geo_tweet.csv", header=None)
