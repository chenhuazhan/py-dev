import cv2 
import smtplib
import sys
import os
import time
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


smtpserver  = 'smtp.163.com'         # smtp服务器
username    = '18476923540@163.com'    # 发件邮箱账号
password    = '131718abc'            # 邮箱登录密码
sender      = '18476923540@163.com'    # 发件人
addressee   = '2849380303@qq.com'     # 收件人
exit_count  = 5                      # 尝试联网次数
path        = os.getcwd()            #获取图片保存路径 

def getPicture():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if not cv2.imwrite(path + './person.jpg', frame):
        print('图片保存失败')
        exit()
    # 关闭摄像头
    cap.release()


# 判断网络是否联通,成功返回0，不成功返回1
# linux中ping命令不会自动停止，需要加入参数 -c 4，表示在发送指定数目的包后停止。
def isLink():
    # return os.system('ping -c 4 www.baidu.com')
    return os.system('ping www.baidu.com')  

def main():
    reconnect_times = 0
    while isLink():
        time.sleep(10)
        reconnect_times += 1
        if reconnect_times == exit_count:
            sys.exit()

    getPicture()

main()
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
# print(path+'\person.jpg')
#cv2.imwrite(path+'\person.jpg', frame)


