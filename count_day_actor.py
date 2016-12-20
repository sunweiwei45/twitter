#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/13 12:38
# @Author  : Sww
# @Site    : 
# @File    : count_day_actor.py
# @Software: PyCharm Community Edition

import json
import csv

def json_day(file_list=None):
    """
    统计每一天的活跃人数
    :param filename:
    :return:
    """
    res_dict = {}
    for filename in file_list:
        inpath = "/pegasus/harir/yangjinfeng/commitresult4/tweet/" + filename + ""
        with open(inpath, "r") as jsonfile:
            read = jsonfile.readlines()
            for line in read:
                j_data = json.loads(line)
                ym = str(j_data["tweetTime"]).split(" ")[0]
                if res_dict.has_key(ym):
                    res_dict[ym] += 1
                else:
                    res_dict[ym] = 1
        print filename
    outpaht = "/pegasus/harir/sunweiwei/count_day_actor/total_count_day.csv"
    for key in res_dict:
        temp = []
        temp.append(key)
        temp.append(res_dict[key])
        with open(outpaht, "ab") as csvfile:
            write = csv.writer(csvfile)
            write.writerow(temp)

if __name__ == '__main__':
    file_list = [
        "allTweets_en",
        "allTweets_ar",
        "allTweets_am",
        "allTweets_bg",
        "allTweets_bn",
        "allTweets_ckb",
        "allTweets_cs",
        "allTweets_cy",
        "allTweets_da",
        "allTweets_de",
        "allTweets_el",
        "allTweets_es",
        "allTweets_et",
        "allTweets_eu",
        "allTweets_fa",
        "allTweets_fi",
        "allTweets_fr",
        "allTweets_gu",
        "allTweets_hi",
        "allTweets_ht",
        "allTweets_hu",
        "allTweets_hy",
        "allTweets_in",
        "allTweets_is",
        "allTweets_it",
        "allTweets_iw",
        "allTweets_ja",
        "allTweets_ka",
        "allTweets_kn",
        "allTweets_ko",
        "allTweets_lt",
        "allTweets_lv",
        "allTweets_ml",
        "allTweets_mr",
        "allTweets_my",
        "allTweets_ne",
        "allTweets_nl",
        "allTweets_no",
        "allTweets_pa",
        "allTweets_pl",
        "allTweets_ps",
        "allTweets_pt",
        "allTweets_ro",
        "allTweets_ru",
        "allTweets_sd",
        "allTweets_si",
        "allTweets_sl",
        "allTweets_sr",
        "allTweets_sv",
        "allTweets_ta",
        "allTweets_te",
        "allTweets_th",
        "allTweets_tl",
        "allTweets_tr",
        "allTweets_ug",
        "allTweets_uk",
        "allTweets_und",
        "allTweets_ur",
        "allTweets_vi",
        "allTweets_zh",
    ]
    json_day(file_list=file_list)
