import csv
import requests
from lxml import etree


response = requests.get('https://www.cjavapy.com/article/1151/')
tree = etree.HTML(response.text)
lis1 = tree.xpath('//tr/td[1]/text()')
lis2 = tree.xpath('//tr/td[2]/text()')
lis3 = tree.xpath('//tr/td[3]/text()')
lis4 = tree.xpath('//tr/td[4]/text()')
lis5 = tree.xpath('//tr/td[5]/text()')
for i in range(0, len(lis1)):
    N = lis1[i]
    M = lis2[i]
    O = lis3[i]
    P = lis4[i]
    Q = lis5[i]

    rows2 = [N,M,O,P,Q]
    f = open("../学习/data/ok2.csv", 'a', newline='')
    writer = csv.writer(f)
    writer.writerow(rows2)
    f.close()