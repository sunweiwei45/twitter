#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/3 14:51
# @Author  : Sww
# @Site    : 
# @File    : simple_count.py
# @Software: PyCharm Community Edition


import pandas
import matplotlib.pyplot as plt
import csv
#
# def count_lang_num():
#     """
#     统计每个人使用语言的数量
#     :return:
#     """
#     inpath = "E:/Sunweiwei/eHealth/twitter/data/statistics/id lang#num.csv"
#     outpath = "E:/Sunweiwei/eHealth/twitter/data/statistics/id lang_num.csv"
#     with open(inpath, "rb") as csvfile1:
#         read = csv.reader(csvfile1)
#         for each in read:
#             id = each[0]
#             lang_num = len(each) - 1
#             temp_list = [id, lang_num]
#             with open(outpath, "ab") as csvfile2:
#                 write = csv.writer(csvfile2)
#                 write.writerow(temp_list)
#


def langnum_idnum():
    """
    统计使用1种，2种。。。。11种语言的人数
    :return:
    """
    inpath = "E:/Sunweiwei/eHealth/twitter/data/statistics/id lang_num.csv"
    outpaht = "E:/Sunweiwei/eHealth/twitter/data/statistics/lang_num id_num.csv"
    df = pandas.read_csv(inpath,header=None,dtype=str)
    df_lang_num = df.groupby(df[1]).count().sort()
    print df_lang_num
    # df_lang_num.to_csv(outpaht, header=None)
langnum_idnum()

# def count_important(filename=None):
#     path = "E:/Sunweiwei/eHealth/twitter/data/lang/" + filename
#     with open(path,'r') as file:
#         read = file.readlines()
#         lang = filename.split('-')[0]
#         num = len(read)
#         with open("E:/Sunweiwei/eHealth/twitter/data/output/lang_count.csv", "ab") as csvfile:
#             write = csv.writer(csvfile)
#             temp = [lang, num]
#             write.writerow(temp)
#
#
# if __name__ == '__main__':
#     file_list = [
#         "allTweets_am",
#         "allTweets_ar",
#         "allTweets_bg",
#         "allTweets_bn",
#         "allTweets_ckb",
#         "allTweets_cs",
#         "allTweets_cy",
#         "allTweets_da",
#         "allTweets_de",
#         "allTweets_el",
#         "allTweets_en",
#         "allTweets_es",
#         "allTweets_et",
#         "allTweets_eu",
#         "allTweets_fa",
#         "allTweets_fi",
#         "allTweets_fr",
#         "allTweets_gu",
#         "allTweets_hi",
#         "allTweets_ht",
#         "allTweets_hu",
#         "allTweets_hy",
#         "allTweets_in",
#         "allTweets_is",
#         "allTweets_it",
#         "allTweets_iw",
#         "allTweets_ja",
#         "allTweets_kn",
#         "allTweets_ko",
#         "allTweets_lo",
#         "allTweets_lt",
#         "allTweets_lv",
#         "allTweets_ml",
#         "allTweets_mr",
#         "allTweets_my",
#         "allTweets_ne",
#         "allTweets_nl",
#         "allTweets_no",
#         "allTweets_or",
#         "allTweets_pa",
#         "allTweets_pl",
#         "allTweets_ps",
#         "allTweets_pt",
#         "allTweets_ro",
#         "allTweets_ru",
#         "allTweets_sd",
#         "allTweets_si",
#         "allTweets_sl",
#         "allTweets_sr",
#         "allTweets_sv",
#         "allTweets_ta",
#         "allTweets_te",
#         "allTweets_th",
#         "allTweets_tl",
#         "allTweets_tr",
#         "allTweets_uk",
#         "allTweets_und",
#         "allTweets_ur",
#         "allTweets_vi",
#         "allTweets_zh",
#     ]
#     for filename in file_list:
#         count_important(filename=filename)
