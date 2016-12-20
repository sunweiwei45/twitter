#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/11/29 16:06
# @Author  : Sww
# @Site    : 
# @File    : count_language.py
# @Software: PyCharm Community Edition

import json
import pandas
import csv


def get_lang(file_list=None):
    """
    从json文件中提取用户id和发推文所使用的语言
    :param file_list:
    :return:
    """
    df_json_list = []
    for filename in file_list:
        # file_path = "/pegasus/twitter-p-or-t-uae-201603.json.dxb/" + filename
        file_path = "E:/Sunweiwei/eHealth/twitter/data/json/" + filename
        with open(file_path, "r") as jsonfile:
            for line in jsonfile:
                t_json = json.loads(line)
                actor_id = t_json['actor']['id']
                tweet_id = t_json['tweet']['id']
                lang = t_json['tweet']['twitterLang']
                with open(r"E:/Sunweiwei/eHealth/twitter/data/json/actorid_tweetid_lang.csv", 'ab') as csvfile:
                    write = csv.writer(csvfile)
                    temp = [actor_id,tweet_id,lang]
                    write.writerow(temp)
                # temp_df = pandas.DataFrame({'actor_
                # id': [actor_id],'tweet_id':[tweet_id], 'lang': [lang]}, dtype=str)
                # temp_df.to_csv(r"E:/Sunweiwei/eHealth/twitter/data/json/actorid_tweetid_lang.csv", header=None, index=False, mode='a')
    #             df_json_list.append(temp_df)
    #             print temp_df
    #     print file_path
    # df_json_res = pandas.concat(df_json_list, ignore_index=True)
    # df_lang = pandas.DataFrame(data=df_json_res)
    # # df_lang.to_csv(r"/pegasus/harir/sunweiwei/lang/id_lang.csv", header=None, index=False)
    # return df_lang


def get_all_id(df_lang=None):
    """
    将所涉及到的用户id提取出来
    :param df_lang:
    :return:
    """
    all_id = df_lang['id'].drop_duplicates()
    all_id = pandas.DataFrame(data=all_id)
    print all_id
    all_id.to_csv(r"/pegasus/harir/sunweiwei/lang/all_id.csv", index=False, header=None)
    return all_id


def count_lang(df_lang=None, all_id=None):
    """
    统计每个用户使用各种语言发推文的数量
    :param df_lang:
    :param all_id:
    :return:
    """
    for index, row in all_id.iterrows():
        id = row['id']
        df_temp = df_lang[df_lang['id'] == id]
        df_id = df_temp['id']
        df_lang_num = df_temp['lang'].groupby(df_temp['lang']).count()
        df_lang_num = pandas.DataFrame(data=df_lang_num, dtype=str)
        df_lang_num['lang1'] = df_lang_num.index
        df_lang_num = df_lang_num.apply(stitching_columns, axis=1)
        df_lang_num = df_lang_num['res']
        df_res = pandas.concat([df_id, df_lang_num], ignore_index=True)
        df_res = pandas.DataFrame(data=df_res).drop_duplicates()
        print df_res
        df_res = df_res.T
        # df_res.to_csv(r"E:/Sunweiwei/eHealth/twitter/data/count_lang_1.csv", mode="a", header=None, index=False)
        df_res.to_csv(r"/pegasus/harir/sunweiwei/lang/count_lang.csv", mode="a", header=None, index=False)

def stitching_columns(row):
    """
    将语言与数目组合
    :param row:
    :return:
    """
    res = row['lang1'] + '#' + row['lang']
    row['res'] = res
    return row

if __name__ == '__main__':
    file_list = [
        "part-r-00000-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00001-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00002-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00003-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00004-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00005-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00006-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00007-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00008-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00009-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00010-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00011-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00012-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00013-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00014-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00015-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00016-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00017-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00018-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00019-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00020-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00021-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00022-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00023-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00024-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00025-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00026-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00027-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00028-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00029-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00030-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00031-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00032-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00033-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00034-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00035-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00036-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00037-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00038-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00039-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00040-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00041-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00042-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00043-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00044-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00045-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00046-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00047-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00048-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00049-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00050-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00051-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00052-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00053-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00054-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00055-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00056-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00057-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00058-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00059-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00060-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00061-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00062-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00063-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00064-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00065-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00066-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00067-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00068-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00069-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00070-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00071-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00072-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00073-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00074-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00075-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00076-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00077-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00078-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00079-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00080-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00081-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00082-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00083-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00084-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00085-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00086-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00087-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00088-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00089-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00090-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00091-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00092-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00093-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00094-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00095-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00096-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00097-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00098-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00099-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00100-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00101-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00102-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00103-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00104-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00105-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00106-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00107-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00108-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00109-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00110-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00111-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00112-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00113-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00114-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00115-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00116-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00117-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00118-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00119-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00120-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00121-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00122-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00123-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00124-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00125-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00126-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00127-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00128-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00129-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00130-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00131-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00132-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00133-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00134-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00135-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00136-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00137-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00138-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00139-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00140-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00141-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00142-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00143-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00144-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00145-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00146-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00147-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00148-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00149-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00150-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00151-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00152-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00153-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00154-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00155-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00156-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00157-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00158-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00159-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00160-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00161-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00162-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00163-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00164-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00165-37ac32d8-f424-4f7c-b21c-33b34d491577",
        "part-r-00166-37ac32d8-f424-4f7c-b21c-33b34d491577",
    ]

    get_lang(file_list=file_list)
    # all_id = get_all_id(df_lang=df_lang)
    # count_lang(df_lang=df_lang, all_id=all_id)
