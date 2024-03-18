from scapy.all import *
from scapy.layers.inet import *
dst=input('dst:')
dport=int(input('dport:'))
def success(packet):
    print(packet.summary())
while(True):
    syn_packet=IP(dst=dst)/TCP(dport=dport,flags='S',seq=114514)
    syn_ack_packet=sr1(syn_packet)

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# driver=webdriver.Chrome()
# driver.get('https://www.baidu.com')
# data=driver.find_element(by='id',value='s-hotsearch-wrapper')
# print(driver.title)
# print(data)
# driver.quit()

# from bs4 import BeautifulSoup
# import requests


# url='http://www.huanxiangji.com/book/19/14621.html'
# headers={
#     'User-Agent':
# 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'
# }

# response=requests.get(url=url,headers=headers)
# response.encoding=response.apparent_encoding
# html=response.text

# # 假设HTML内容存储在变量html中
# # html = '''
# # <html>
# # <body>
# # <div id="my-div">Hello, World!</div>
# # <p id="my-paragraph">This is a paragraph.</p>
# # <a id="my-link" href="https://www.example.com">Example</a>
# # </body>
# # </html>
# # '''

# # 创建BeautifulSoup对象
# soup = BeautifulSoup(html, 'html.parser')

# # 使用find方法筛选指定ID的标签
# element = soup.find('h1',class_='title')

# # 打印获取到的标签的值
# print(element.text)

# # 或者使用string属性
# print(element.string)
