#! /usr/bin/env python
# -*- coding: utf-8 -*-

# 疫查询，搜集疫苗数据的Python后台程序

import re
import time
from urllib import request

import mysql.connector
from bs4 import BeautifulSoup

# 网页url前缀
url_prefix = "http://bio.nifdc.org.cn/pqf/"
# 首页url
base_url = "http://bio.nifdc.org.cn/pqf/search.do?formAction=pqfGsByJG&orgId=1"


class Collector(object):
    def __init__(self):
        self.links = []

    # 搜集所有URLs
    def collect_all_urls(self):
        req_url = base_url
        req = request.Request(req_url)
        req.add_header('User-agent',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                       'Chrome/67.0.3396.99 '
                       'Safari/537.36')

        # 读取网页
        response = request.urlopen(req)
        the_page = response.read()

        # 解析网页
        page = BeautifulSoup(the_page, "html.parser")

        anchors = page.find_all(name="a")
        for anchor in anchors:
            self.links.append(anchor['href'])

    # 根据collect_all_urls()搜集的urls查询数据
    def query(self):
        num = 0

        # 在这里修改成你的数据库连接信息
        conn = mysql.connector.connect(user='root', password='123456', host='127.0.0.1', database='yimiao')
        cursor = conn.cursor()

        for parturl in self.links:
            req_url = url_prefix + parturl
            req = request.Request(req_url)
            req.add_header('User-agent',
                           'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                           'Chrome/67.0.3396.99 '
                           'Safari/537.36')

            # 读取网页
            response = request.urlopen(req)
            the_page = response.read()

            # 解析网页
            page = BeautifulSoup(the_page, "html.parser")

            table = page.find(name="table", attrs={"class": re.compile("list_table")})

            num += 1
            print("Visit link No.%i: " % num, req_url)

            rows = table.find_all(name="tr")

            print("Start writing link No.%i: " % num, req_url)

            for row in rows[1:]:
                items = row.find_all(name="td")
                itemlist = []
                for item in items:
                    itemlist.append(item.text)
                cursor.execute(
                    'insert into yimiao_info (product_name, spec, batch_no, issue_or_not_volume, expiration_date, '
                    'manufacturer, '
                    'checking_no, certificate_no, report_no, issue_date, issue_conclusion, issue_authority)'
                    ' values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', itemlist[1:13])

            conn.commit()
            print("Fishing writing link No.%i: " % num, req_url)

        cursor.close()


if __name__ == "__main__":
    start_time = time.time()

    collector = Collector()
    collector.collect_all_urls()

    num = 1
    for link in collector.links:
        print(num, '. ', link)
        num = num + 1

    collector.query()

    finish_time = time.time() - start_time

    print('Used time(s):' + repr(finish_time))
