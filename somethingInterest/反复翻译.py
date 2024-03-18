# from multiprocessing import Process
# import os
# def runn(name):
#     print('子,name=%s,pid=%d...'%(name,os.getpid()))
# if __name__=='__main__':
#     print('父进程pid=%d'%(os.getpid()))
#     p=Process(target=runn,args=('tset',))
#     print('之间要运行')
#     p.start()
#     print('结束')

# import multiprocessing
# import os
# import time
# import random
# import threading
# # def runnn(name):
# #     tim=random.uniform(1,5)
# #     print('进程%d开始执行'%name)
# #     time.sleep(tim)
# #     print('进程%d执行完毕,执行时间%d'%(name,tim))
# def runnn(name):
#     time.sleep(1.14)
#     print("process {0} have run for time of 1.14 named {1}".format(os.getpid(),name))
#     time.sleep(5.14)
#     print("process {0} have run for time of 114514 name {1}".format(os.getpid(),name))

# a=multiprocessing.Process(target=runnn(1))
# b=multiprocessing.Process(target=runnn(2))
# c=multiprocessing.Process(target=runnn(3))


# print("end")



# def lopp():
#     x=0
#     while True:
#         x=x^1
# if __name__=='__main__':
    # po=Pool(10)
    # for i in range(1,11):
    #     po.apply(runnn,(i,))
    # print('start-----')
    # po.close()
    # po.join()
    # print('cloae_____')

    # tst=time.time()
    # print('start')
    # for i in range(1,11):
    #     t=threading.Thread(target=runnn,args=(i,))
    #     t.start()
        
    # tsp=time.time()
    # print('结束，耗时%d'%(tsp-tst)
    # print(multiprocessing.cpu_count())
import requests
import json
import re
import jieba

def translateen(kw):
    url="https://fanyi.baidu.com/sug"
    headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36",
    'Referer':'https://fanyi.baidu.com/',
    'Cookie': 'BIDUPSID=1AD6827A4B3F0EF2FD06478BAD4A7086; PSTM=1635161285; __yjs_duid=1_42122f133753019e8e99ab0ba93acc031635161741437; _ga=GA1.2.1226368305.1635161743; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=44D8A4DEB389635A1514A23BA96E9FC4:FG=1; BAIDUID_BFESS=44D8A4DEB389635A1514A23BA96E9FC4:FG=1; __bid_n=18402e81d44dd580b24207; BDUSS=jI2ZklQTTBCVndhektMa0JwODZ-ZGNBeDN6dm0xREhNUWJhY3ppQXFyakJzb0pqSVFBQUFBJCQAAAAAAQAAAAEAAADwv3gcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMElW2PBJVtjZ; BDUSS_BFESS=jI2ZklQTTBCVndhektMa0JwODZ-ZGNBeDN6dm0xREhNUWJhY3ppQXFyakJzb0pqSVFBQUFBJCQAAAAAAQAAAAEAAADwv3gcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMElW2PBJVtjZ; BAIDU_WISE_UID=wapp_1668065396176_118; ZFY=91kEiLIuHK41zw8uHd8OpllxJ6BME7w9tCxfCwVb8SA:C; FEID=v10-ea5ab6c02c83539d4b81b94c69d54912df3de7a2; __xaf_fpstarttimer__=1671697669553; __xaf_thstime__=1671697669879; __xaf_fptokentimer__=1671697669945; FPTOKEN=wm71ME6p1GnUz7AW/jbvTshfK5jWbiwAYSFy6pMN78Iaa16eb6wh9/pZ/lmqtTLZo04RmAH+hWZ0u7NaDfhw0qGnWRadz1FHd0j6JrkBLHPlWirKGls6Oa9CwGgsrvimp8TKgpwZnnEXGg3R5OSDZfFQCkjk7q/7YXmFJxMrecIViOB7doHqr8h/1mEUoWJVeVdAN/49vuxT105gm1YOcvkdRjXvBgoZW6l+NBN9bzo85Kx3NR4ni2+XkDvqi5S0qXU/IAL6skj7SrsKEdxjBREQjKlsp00d7dzo8GEpOa+bah3sBguyOqJnRhhdKctz+Y5Z2WrlAK5onjVS/popCNVNls2UFnVqG7hFfUnK+qoKR6fMzjRmeQa7yslojvJ28RBBsvCSdKqfPjw5VWiaALxHaPAYPI0+RF3ScbIk2oHq4SY7uuS5D0SJlQXdkweO|I9pUKhi+8Av9xYr2d/LtZUvJyeQ4EML7F+RLM/x+l8k=|10|c20f340dc3834e5187449be31c931802; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1682088249; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1682089314; ab_sr=1.0.1_NGY2ZGU3NzE5MGNkMDhjZmJmZjU1OGUwZTU3NDUyMWE2YTQ4YWFlOTFkYzA5OWE0NTEzZGQ2MzRhYzc1MGQ5ODA0MjIyMTFiZDU3Nzc3MDBkMzQ1YzZkNWIwYzU0MWZkMjM2MTAzOGMzMTIzMGQ0ZTFiMGNhOTkxNjc1NGUxNmJiZjc1YjE0NTAyMTZmNDBlMjJlM2EzYzM2YWI5NzJkOWZhZDg1ZmRjYzdjNDZlNzEzYjczMDE4OTdjYmViZjky'
    }
    datas={
    # 'from': 'zh',
    # 'to': 'en',
    # 'query': kw,
    # 'transtype': 'translang',
    # 'simple_means_flag': 3,
    # 'sign': 424354.170643,
    # 'token': 'f01df6aac7af497999f418af0c82e8e1',
    # 'domain': 'common'
   'kw':kw
}
    response=requests.post(url=url,headers=headers,data=datas)
    dicc=json.loads(response.content)
    # print(dicc)
    
    try:
        a=' '+dicc['data'][0]['v']+' '
       # print(a)
        ret=re.search(r'[^\（\u4e00-\u9fa5]([\u4e00-\u9fa5]+)[^\）\u4e00-\u9fa5]',a,re.I)
        print(ret.group(1))
        return ret.group(1)
    except:
        pass

def translatezh(kw):
    url="https://fanyi.baidu.com/sug"
    headers={
    'user-agent':"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.95 Safari/537.36",
    'Referer':'https://fanyi.baidu.com/',
    'Cookie': 'BIDUPSID=1AD6827A4B3F0EF2FD06478BAD4A7086; PSTM=1635161285; __yjs_duid=1_42122f133753019e8e99ab0ba93acc031635161741437; _ga=GA1.2.1226368305.1635161743; REALTIME_TRANS_SWITCH=1; SOUND_SPD_SWITCH=1; HISTORY_SWITCH=1; FANYI_WORD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=44D8A4DEB389635A1514A23BA96E9FC4:FG=1; BAIDUID_BFESS=44D8A4DEB389635A1514A23BA96E9FC4:FG=1; __bid_n=18402e81d44dd580b24207; BDUSS=jI2ZklQTTBCVndhektMa0JwODZ-ZGNBeDN6dm0xREhNUWJhY3ppQXFyakJzb0pqSVFBQUFBJCQAAAAAAQAAAAEAAADwv3gcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMElW2PBJVtjZ; BDUSS_BFESS=jI2ZklQTTBCVndhektMa0JwODZ-ZGNBeDN6dm0xREhNUWJhY3ppQXFyakJzb0pqSVFBQUFBJCQAAAAAAQAAAAEAAADwv3gcAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMElW2PBJVtjZ; BAIDU_WISE_UID=wapp_1668065396176_118; ZFY=91kEiLIuHK41zw8uHd8OpllxJ6BME7w9tCxfCwVb8SA:C; FEID=v10-ea5ab6c02c83539d4b81b94c69d54912df3de7a2; __xaf_fpstarttimer__=1671697669553; __xaf_thstime__=1671697669879; __xaf_fptokentimer__=1671697669945; FPTOKEN=wm71ME6p1GnUz7AW/jbvTshfK5jWbiwAYSFy6pMN78Iaa16eb6wh9/pZ/lmqtTLZo04RmAH+hWZ0u7NaDfhw0qGnWRadz1FHd0j6JrkBLHPlWirKGls6Oa9CwGgsrvimp8TKgpwZnnEXGg3R5OSDZfFQCkjk7q/7YXmFJxMrecIViOB7doHqr8h/1mEUoWJVeVdAN/49vuxT105gm1YOcvkdRjXvBgoZW6l+NBN9bzo85Kx3NR4ni2+XkDvqi5S0qXU/IAL6skj7SrsKEdxjBREQjKlsp00d7dzo8GEpOa+bah3sBguyOqJnRhhdKctz+Y5Z2WrlAK5onjVS/popCNVNls2UFnVqG7hFfUnK+qoKR6fMzjRmeQa7yslojvJ28RBBsvCSdKqfPjw5VWiaALxHaPAYPI0+RF3ScbIk2oHq4SY7uuS5D0SJlQXdkweO|I9pUKhi+8Av9xYr2d/LtZUvJyeQ4EML7F+RLM/x+l8k=|10|c20f340dc3834e5187449be31c931802; APPGUIDE_10_0_2=1; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1682088249; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1682089314; ab_sr=1.0.1_NGY2ZGU3NzE5MGNkMDhjZmJmZjU1OGUwZTU3NDUyMWE2YTQ4YWFlOTFkYzA5OWE0NTEzZGQ2MzRhYzc1MGQ5ODA0MjIyMTFiZDU3Nzc3MDBkMzQ1YzZkNWIwYzU0MWZkMjM2MTAzOGMzMTIzMGQ0ZTFiMGNhOTkxNjc1NGUxNmJiZjc1YjE0NTAyMTZmNDBlMjJlM2EzYzM2YWI5NzJkOWZhZDg1ZmRjYzdjNDZlNzEzYjczMDE4OTdjYmViZjky'
    }
    datas={
    # 'from': 'zh',
    # 'to': 'en',
    # 'query': kw,
    # 'transtype': 'translang',
    # 'simple_means_flag': 3,
    # 'sign': 424354.170643,
    # 'token': 'f01df6aac7af497999f418af0c82e8e1',
    # 'domain': 'common'
   'kw':kw
}
    response=requests.post(url=url,headers=headers,data=datas)
    dicc=json.loads(response.content)
    # print(dicc)
    try:
        a=dicc['data'][0]['v']
        #print(a)
        ret=re.search(r'([a-z]+)',a,re.I)
        print(ret.group(1))
        return ret.group(1)
    except:
        pass

while True:
    print('-----反复翻译------')
    try:
        kw=input('输入中文文本(exit退出):')
        times=int(input('输入翻译次数:'))
    except:
        print('输入戳误')
        continue
    if kw=='exit':
        print('-----end------')
        break

    for i in range(times):
        rett=[]
        kwlist=jieba.cut(kw)
        for keywzh in kwlist:
            if keywzh==' ':
                continue
            try:
                w=translatezh(keywzh)
                if w == None:
                    continue
                else:
                    rett.append(w)
            except:
                w=translatezh(keywzh)
                if w == None:
                    continue
                else:
                    rett.append(w)
        #print(rett)
        kw=' '.join(rett)
        print(kw)
        rett=[]
        kwlist=jieba.cut(kw)
        for keywen in kwlist:
            try:
                w=translateen(keywen)
                if w == None:
                    continue
                else:
                    rett.append(w)
            except:
                w=keywen
                if w == None:
                    continue
                else:
                    rett.append(w)
        #print(rett)
        kw=''.join(rett)

        print('已重复翻译完成%d次，结果为%s'%(i+1,kw))