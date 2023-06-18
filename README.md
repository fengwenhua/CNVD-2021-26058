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

## 免责声明
本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建靶机环境。

在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。

在安装并使用本工具前，请您务必审慎阅读、充分理解各条款内容，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要安装并使用本工具。您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。
