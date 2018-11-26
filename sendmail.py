# -*- coding: utf-8 -*-

import configparser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.audio import MIMEAudio
from email.mime.application import MIMEApplication
import mimetypes
import os
from testdata.getpath import GetConfigFile


class MyMail():
    def __init__(self, mail_config_file):
        config = configparser.ConfigParser()
        # config.read(GetConfigFile('mail.conf'))
        config.read(mail_config_file)
        self.smtp = None
        mail = config['SMTP']
        self.login_user = mail.get('login_user')
        self.login_pwd = mail.get('login_pwd')
        self.from_addr = mail.get('from_addr')
        self.to_addrs = mail.get('to_addrs')
        self.host = mail.get('host')
        self.port = mail.get('port')

    # 连接到服务器
    def connect(self):
        # self.smtp.set_debuglevel(True)
        # self.smtp.starttls()
        self.smtp = smtplib.SMTP_SSL(self.host, self.port)
        self.smtp.ehlo()

    # 登陆邮件服务器
    def login(self):
        try:
            self.smtp.login(self.login_user, self.login_pwd)
        except Exception as e:
            print('%s' % e)

    # 发送邮件
    def send_mail(self, mail_subject, mail_content, attachment_path_set):
        # 构造MIMEMultipart对象做为根容器
        msg = MIMEMultipart()
        msg['From'] = self.from_addr
        # msg['To'] = self.to_addrs
        msg['To'] = ';'.join(eval(self.to_addrs))
        msg['Subject'] = mail_subject
        # 注意，这里的msg['To']只能为逗号分隔的字符串，形如 'sdxx@163.com', 'xdflda@126.com' msg['Subject'] = mail_subject
        # 添加邮件内容
        content = MIMEText(mail_content, "html", _charset='utf-8')
        # 说明 这里charset必须为gbk 和# -*- coding: GBK -*-一致 否则邮件内容乱码

        msg.attach(content)
        for attachment_path in attachment_path_set:
            if os.path.isfile(attachment_path):
                type, coding = mimetypes.guess_type(attachment_path)
                if type == None:
                    type = 'application/octet-stream'
                major_type, minor_type = type.split('/', 1)
                with open(attachment_path, 'rb') as file:
                    if major_type == 'text':
                        attachment = MIMEText(file.read(), _subtype=minor_type, _charset='GB2312')
                    elif major_type == 'image':
                        attachment = MIMEImage(file.read(), _subtype=minor_type)
                    elif major_type == 'application':
                        attachment = MIMEApplication(file.read(), _subtype=minor_type)
                    elif major_type == 'audio':
                        attachment = MIMEAudio(file.read(), _subtype=minor_type)
                # 修改附件名称
                attachment_name = os.path.basename(attachment_path)
                attachment.add_header('Content-Disposition', 'attachment', filename=('gbk', '', attachment_name))
                # 说明 这里的('gbk','',attachment_name) 解决了附件为中文名称时 显示不对的问题

                msg.attach(attachment)
        # 得到格式化后的完整文本
        full_text = msg.as_string()

        # 发送邮件
        self.smtp.sendmail(self.from_addr, eval(self.to_addrs), full_text)

    # 退出
    def quit(self):
        self.smtp.quit()


if __name__ == '__main__':
    msg = """
    <table width="800" border="0" cellspacing="0" cellpadding="4">
        <tr>
            <td bgcolor="#CECFAD" height="20" style="font-size:20px">接口自动化测试报告<a href="http://127.0.0.0:8000"> 更多内容>></a></td>
        </tr><br><br>
        <tr>
            <td bgcolor="#EFEBDE" height="100" style="font-size:23px">
                1)测试用例总数：<font color=red>%(yonglizongshu)</font><br><br>
                2)通过用例总数：<font color=red>%(tongguoyongli)</font><br><br>
                3)失败用例总数：<font color=red>%(shibeiyongli)</font><br><br>
                4)通过率：<font color=red>%(tongguolv)</font><br><br>
                5)接口请求地址：<font color=red>%(test_net)</font><br><br>
                6)测试时间：<font color=red>%(time_now)</font><br><br>
                            详细内容查看附件：<font color=red>%(neirong)</font><br><br>
            </td>
        </tr>
    """
    mail = MyMail(GetConfigFile('mail.conf'))
    mail.connect()
    mail.login()
    # mail_content = 'Hi 附件为接口测试报告，请查阅'
    mail_content = msg
    mail_title = '【测试报告】接口测试报告'
    attachment = set(['./testreport/2018-11-18-23-41-55-TestReport.xls'])
    mail.send_mail(mail_title, mail_content, attachment)
    mail.quit()
