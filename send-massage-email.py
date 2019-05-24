# 发送邮件库
import smtplib
#邮件文本
from email.mime.text import MIMEText

#SMTP 服务器
SMTPserver = "smtp.163.com"
#发邮件 的地址   账号
Sender = "suncksunck@163.com"
#发送者邮箱授权密码   密码
passwd = "1234567890a"

#邮件内容
message = "您好 这是第一个邮件"
#字符转成邮件文本
msg = MIMEText(message)
#标题
msg["Subject"] = "来自帅哥的问候"
#发送者
msg["From"] = Sender

#创建SMTP服务器   邮件25 端口号
mailServer = smtplib.SMTP(SMTPserver, 25)

#登录邮箱
mailServer.login(Sender, passwd)
#发送邮件  msg.as_string() 转换邮件
mailServer.sendmail(Sender,["xxxxxx@163.com", "xxxxxxx@163.com"], msg.as_string())

#退出邮件
mailServer.quit()







# 账户注册：请通过该地址开通账户http://sms.ihuyi.com/register.html
import http.client
import urllib

host = "106.ihuyi.com"
sms_send_uri = "/webservice/sms.php?method=Submit"

# 用户名是登录用户中心->验证码短信->产品总览->APIID
account = "C79343041"
# 密码 查看密码请登录用户中心->验证码短信->产品总览->APIKEY
password = "5a51b73518a48dcd5395d7f38085f8ca"


def send_sms(text, mobile):
    params = urllib.parse.urlencode(
        {'account': account, 'password': password, 'content': text, 'mobile': mobile, 'format': 'json'})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    conn = http.client.HTTPConnection(host, port=80, timeout=30)
    conn.request("POST", sms_send_uri, params, headers)
    response = conn.getresponse()
    response_str = response.read()
    conn.close()
    return response_str


if __name__ == '__main__':
    mobile = "156xxxxxxxx"
    text = "您的验证码是：121254。请不要把验证码泄露给其他人。"

    print(send_sms(text, mobile))




