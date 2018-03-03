#coding=utf-8
import requests as rs
import re
import os
u'''  
注：
    Agent error:[1]!
    IP和port都是正常的，但是访问返回值出错
    Agent error:[2]!
    ip和port出错
'''
def N_start(url,IPfile,num,oknum):
    file = []
    fileurl = re.sub(":","",re.sub("/","",re.sub("\?","",url)))
    print fileurl
    fp=open("D:\\pythonfile\\IP\\"+IPfile,'r')
    for i in fp.readlines():
        file.append(i.strip('\r\n'))
    fp.close()
    print len(file)
    N_ok=1
    for ii in xrange(num,len(file)):
        N_proxies = {"http":"http://"+str(file[ii])}
        headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'accept-language':'zh-CN,zh;q=0.9,en;q=0.8',
                    'cookie':'tt_webid=6522599707537360387; uuid="w:8805d604a47d41c0b9c75111cc3728d1"; UM_distinctid=16197413a68158-07274f021d2f1d-1781c36-100200-16197413a6b4ce; _ga=GA1.2.2024255764.1518661090; tt_webid=6522599707537360387; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6522599707537360387; login_flag=de2acfa225535eabc67c2838fa5606fe; sessionid=c0baa4837b800804c9aea8c45c3bf311; sid_tt=c0baa4837b800804c9aea8c45c3bf311; sso_login_status=1; uid_tt=19205dcaa3f7eea9092ae6867dc35ec0; sid_guard="c0baa4837b800804c9aea8c45c3bf311|1518972342|15552000|Fri\054 17-Aug-2018 16:45:42 GMT"; __tea_sdk__web_id=2028512914; __tea_sdk__user_unique_id=86728952843; __tea_sdk__ssid=-8888; CNZZDATA1259612802=2034571911-1518657930-https%253A%252F%252Fwww.baidu.com%252F%7C1519721136; __tasessionId=q20sxaqr01519721239773',
                    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        print N_proxies
        print "Test the "+str(ii)+" IP"
        try:
            fsession = open("D:\\pythonfile\\IP\\"+str(fileurl)+".nie",'w')
            fsession.write(str(ii))
            fsession.close()
        except:
            fsession.write(str(ii))
            fsession.close()
        try:
            r1 = rs.get(url,headers =headers,proxies = N_proxies,timeout = 3)

            if r1.ok:
                print r1.content
                print "-------------------------------------> "+str(N_ok)
                N_ok+=1
                if N_ok ==oknum:
                    break
            else:
                print "Agent error:[1]!"
        except:
            print "Agent error:[2]!"

if __name__=="__main__":
    url = "http://yoururl"#Enter an article link that you want to brush, and note that the protocol must be HTTP,if it is not to be changed to HTTP
    filepath = "D:\\pythonfile\\IP\\"+str(re.sub(":","",re.sub("/","",url)))+".nie"
    if os.path.exists(filepath):
        fs = open(filepath,'r')
        try:
            num = fs.readlines()[0]
            print "Loding session"
        except:
            num = 0
        fs.close()
    else:
        num = 0
    IPfile = "ip_1000.txt"
    N_start(url,IPfile,int(num),oknum=2500)
