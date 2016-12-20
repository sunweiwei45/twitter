#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2016/12/3 10:25
# @Author  : Sww
# @Site    : 
# @File    : community_active_time.py
# @Software: PyCharm Community Edition
import json
import pandas
import csv
import time

def merge_json(file_list=None):
    """
    将多个文件中的部分信息抽取出来，合并到一个文件中
    :param file_list:
    :return:
    """
    for filename in file_list:
        # inpath = "E:/Sunweiwei/eHealth/twitter/April/" + filename + ""
        # outpath = "E:/Sunweiwei/eHealth/twitter/April/" + "total_aid_time" + ".csv"
        inpath = "/pegasus/harir/yangjinfeng/commitresult4/tweet/" + filename
        outpath = "/pegasus/harir/sunweiwei/active/" + "total_aid_time" + ".csv"
        res_list = []
        with open(inpath, r"rb") as infile:
            read = infile.readlines()
            for line in read:
                temp_list = []
                line = json.loads(line)
                temp_list.append(line['actorId'])
                temp_list.append(line['tweetTime'])
                res_list.append(temp_list)

        with open(outpath, "ab") as csvfile:
            #所有用户的id，时间
            write = csv.writer(csvfile)
            write.writerows(res_list)
        print filename



def community_active_time(file_list=None):
    """
    统计一个社区的所有发言时间，存储在JSON文件中
    :return:
    """
    all_aid_time = {}
    with open("/pegasus/harir/sunweiwei/active/total_aid_time.csv", "rb") as csvfile:
        # 将所有的actor及其发言时间一一对应，存在字典里
        read = csv.reader(csvfile)
        for line in read:
            if all_aid_time.has_key(line[0]):
                all_aid_time[line[0]].append(line[1])
            else:
                all_aid_time[line[0]] = [line[1]]

    for filename in file_list:
        inpath = "/pegasus/harir/yangjinfeng/commitresult4/community2/" + filename + ".icpm"
        outpath = "/pegasus/harir/sunweiwei/active/" + filename + "_community_active"
        with open(inpath, "r") as icpmfile:
            for line in icpmfile:
                community_dict = {}
                community_list = line.strip().split(" ")
                for each in community_list:
                    if all_aid_time.has_key(each):
                        community_dict[each] = all_aid_time[each]
                    else:
                        community_dict[each] = []
                with open(outpath, "a") as outfile:
                    outfile.write(repr(community_dict))
                    outfile.write("\n")


def count_community_active(file_list=None):
    """
    统计每个社区的每个时间段的活跃人数
    :param file_list:
    :return:
    """
    for filename in file_list:
        inpath = "E:/Sunweiwei/eHealth/twitter/April/data/community_active/" + filename + "_community_active"
        outpath1 = "E:/Sunweiwei/eHealth/twitter/April/data/community_active/" + filename + "_community_active_day1"
        outpath2 = "E:/Sunweiwei/eHealth/twitter/April/data/community_active/" + filename + "_community_active_hour1"
        with open(inpath, "r") as jsonfile:
            read = jsonfile.readlines()
            all_comm_time_list = []
            for line in read:
                one_comm_time_list = []
                line = json.loads(line.strip().replace("'",'"'))
                for each in line.values():
                    temp = []
                    for time in each:
                        date = str(time).split(" ")[0]
                        day = int(date.split("-")[2])
                        if day > 0 and day < 8:
                            temp.append(time)
                        else:
                            pass
                    one_comm_time_list.extend(temp)
                all_comm_time_list.append(one_comm_time_list)

        ###过滤不符合日期的时间
        # for comm_time in all_comm_time_list:
        #     for time in comm_time:
        #         date = str(time).split(" ")[0]
        #         day = int(date.split("-")[2])
        #         if day < 1 or day > 7:
        #             comm_time.remove(time)
        #         else:
        #             pass

        #统计每天
        for comm_time in all_comm_time_list:
            ym_comm_dict = {}
            for time in comm_time:
                ym = str(time).split(" ")[0]
                if ym_comm_dict.has_key(ym):
                    ym_comm_dict[ym] += 1
                else:
                    ym_comm_dict[ym] = 1
            with open(outpath1,"a") as outfile:
                outfile.write(repr(ym_comm_dict))
                outfile.write("\n")
        #统计每小时
        for comm_time in all_comm_time_list:
            hour_comm_dict = {}
            for time in comm_time:
                temp_time = str(time).split(" ")[1]
                hour = temp_time.split(":")[0]
                if hour_comm_dict.has_key(hour):
                    hour_comm_dict[hour] += 1
                else:
                    hour_comm_dict[hour] = 1
            with open(outpath2,"a") as outfile:
                outfile.write(repr(hour_comm_dict))
                outfile.write("\n")
        print filename

def json_csv(file_list=None):
    """
    将JSON格式的数据抽取出来存到csv文件中
    :return:
    """
    for filename in file_list:

        inpath = "E:/Sunweiwei/eHealth/twitter/April/" + filename + ""
        outpath = "E:/Sunweiwei/eHealth/twitter/April/data/community_active/communityid_time_num/" + filename + "_result.csv"
        with open(inpath, "r") as jsonfile:
            read = jsonfile.readlines()
            i = 0
            for line in read:
                i += 1
                temp_line_list = []
                line = json.loads(line.strip().replace("'",'"'))
                for key in line:
                    temp_day_list = []
                    temp_day_list.append(i)
                    temp_day_list.append(key)
                    temp_day_list.append(line[key])
                    temp_line_list.append(temp_day_list)
                with open(outpath, "ab") as csvfile:
                    write = csv.writer(csvfile)
                    write.writerows(temp_line_list)


def clean_file(file_list=None):
    for filename in file_list:
        inpath = "E:/Sunweiwei/eHealth/twitter/April/data/community_active/communityid_time_num/day/" + filename + ".csv"
        outpath = "E:/Sunweiwei/eHealth/twitter/April/" + filename + ".csv"
        res_list = []
        with open(inpath, "rb") as infile:
            read = csv.reader(infile)
            for line in read:
                line[1] = str(line[1]).split("-")[2]
                res_list.append(line)
        with open(outpath,"ab") as outfile:
            write = csv.writer(outfile)
            write.writerows(res_list)


if __name__ == '__main__':
    # file_list1 = [
    # #aid,keyword,tweettime,lang.....
    #     "allTweets_en",
    #     "allTweets_ar",
    #     "allTweets_am",
    #     "allTweets_bg",
    #     "allTweets_bn",
    #     "allTweets_ckb",
    #     "allTweets_cs",
    #     "allTweets_cy",
    #     "allTweets_da",
    #     "allTweets_de",
    #     "allTweets_el",
    #     "allTweets_es",
    #     "allTweets_et",
    #     "allTweets_eu",
    #     "allTweets_fa",
    #     "allTweets_fi",
    #     "allTweets_fr",
    #     "allTweets_gu",
    #     "allTweets_hi",
    #     "allTweets_ht",
    #     "allTweets_hu",
    #     "allTweets_hy",
    #     "allTweets_in",
    #     "allTweets_is",
    #     "allTweets_it",
    #     "allTweets_iw",
    #     "allTweets_ja",
    #     "allTweets_ka",
    #     "allTweets_kn",
    #     "allTweets_ko",
    #     "allTweets_lt",
    #     "allTweets_lv",
    #     "allTweets_ml",
    #     "allTweets_mr",
    #     "allTweets_my",
    #     "allTweets_ne",
    #     "allTweets_nl",
    #     "allTweets_no",
    #     "allTweets_pa",
    #     "allTweets_pl",
    #     "allTweets_ps",
    #     "allTweets_pt",
    #     "allTweets_ro",
    #     "allTweets_ru",
    #     "allTweets_sd",
    #     "allTweets_si",
    #     "allTweets_sl",
    #     "allTweets_sr",
    #     "allTweets_sv",
    #     "allTweets_ta",
    #     "allTweets_te",
    #     "allTweets_th",
    #     "allTweets_tl",
    #     "allTweets_tr",
    #     "allTweets_ug",
    #     "allTweets_uk",
    #     "allTweets_und",
    #     "allTweets_ur",
    #     "allTweets_vi",
    #     "allTweets_zh",
    # ]
    # #
    # file_list2 = [
    #     "SLPAw_01_07-network_weighted_run1_r0.25_v3_T100",
    #     # "SLPAw_08_14-network_weighted_run1_r0.25_v3_T100",
    #     # "SLPAw_15_21-network_weighted_run1_r0.25_v3_T100",
    #     # "SLPAw_22_28-network_weighted_run1_r0.25_v3_T100",
    #     # "SLPAw_29_30-network_weighted_run1_r0.25_v3_T100",
    #     # "test"
    # ]
    # # merge_json(file_list=file_list1)
    # # community_active_time(file_list=file_list2)
    # print time.strftime('%Y-%m-%d %H:%M:%S')
    # count_community_active(file_list=file_list2)
    # print time.strftime('%Y-%m-%d %H:%M:%S')
    file_list = [
        "01_07_day",
        "08_14_day",
        "15_21_day",
        "22_28_day",
        "29_30_day",
    ]
    # json_csv(file_list=file_list)
    clean_file(file_list=file_list)
