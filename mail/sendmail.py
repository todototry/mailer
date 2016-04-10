from email import encoders
from email.header import Header
from email.mime.multipart import MIMEBase, MIMEMultipart
from email.mime.message import MIMEMessage
from email.mime.audio import MIMEAudio
from email.mime.image import MIMEImage
from email.mime.text import MIMEText, MIMENonMultipart
from email.utils import parseaddr, formataddr
import smtplib


class SendMail(object):
    def __init__(self, server, port):
        self.server = smtplib.SMTP(server, port)

        self.sender =""
        self.pwd =""

        self.receivers = ""
        self.cc = ""

        self.contentType=""  #1.plain  2.html  3.multipart
        self.encrypt = False  # server.starttls()
        self.contentTemplate = None  #use jinjia2 to render template.
        self.contentDict = None
        self.attachments = None    #use dict, with index. such as {"1":"firstpath.png","":"second_path.png"}


    def set_sender(self, sender, pwd):
        self.sender = sender
        self.pwd = pwd
        return self

    def set_receiver_cc(self, receivers, cc, bcc=""):

        return self

    def set_encrypt(self, use_tls):
        self.encrypt = use_tls
        return self

    def set_content(self, content_type="plain", content="Hello there!", **tpl_or_data_dict):
        # support raw string, template, data_for_render and attachments in dict() type.

        return self


    def send(self):
        # 邮件对象:
        msg = MIMEMultipart()
        msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
        msg['To'] = _format_addr('管理员 <%s>' % to_addr)
        msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

        # 邮件正文是MIMEText:
        msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))

        # 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        with open('/Users/michael/Downloads/test.png', 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'png', filename='test.png')
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename='test.png')
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)