# CNVD-2021-26058
亿赛通电子文档安全管理系统-rce-exp

## 漏洞成因
使用了Apache Solr，漏洞编号：CVE-2019-0193

## Fofa
```
"电子文档安全管理系统" && country!="CN"
```

## 脚本使用
```shell
~# python3 yisaitong-exp.py -h
usage: yisaitong-exp.py [-h] [-u URL] [-c CMD] [-f FILE] [-k SKIP]

亿赛通rce利用工具

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     指定单个url
  -c CMD, --cmd CMD     要执行的命令
  -f FILE, --file FILE  指定要测试的urls文件
  -k SKIP, --skip SKIP  跳过core_name
```

![image](https://user-images.githubusercontent.com/26518808/119749983-de77da80-beca-11eb-8a45-159693feb8d3.png)

![image](https://user-images.githubusercontent.com/26518808/119750248-8097c280-becb-11eb-90aa-9a1ee30ac059.png)

![image](https://user-images.githubusercontent.com/26518808/119750581-37943e00-becc-11eb-859a-970281e14269.png)


```shell
python3 yisaitong-poc.py -h
usage: yisaitong-poc.py [-h] [-u URL] [-f FILE]

亿赛通rce poc工具-不一定有漏洞

optional arguments:
  -h, --help            show this help message and exit
  -u URL, --url URL     指定单个url
  -f FILE, --file FILE  指定要测试的urls文件
```

![image](https://user-images.githubusercontent.com/26518808/119750314-9efdbe00-becb-11eb-9fce-3f1e2cde9742.png)

最后，卑微小弟在线求关注！！

![微信公众号](./640.png)
