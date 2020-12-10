#!/usr/bin/env python
# encoding: utf-8
import smtplib,socket,sys
from os import system
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from datetime import datetime
_NOME_ = sys.argv[1]
_IP_ = sys.argv[2]
_ADRESS_OS_ = '/etc/issue.net'
OS = open(_ADRESS_OS_).readlines()
for SYS in OS:
	_OS_ = SYS.replace('\n','')
_DATA_ = datetime.now()
_ANO_ = str(_DATA_.year)
_MES_ = str(_DATA_.month)
_DIA_ = str(_DATA_.day)
_HORA_ = str(_DATA_.hour)
_MINUTO_ = str(_DATA_.minute)
_SEGUNDO_ = str(_DATA_.second)
_MSG_ = MIMEMultipart('alternative')
_MSG_['Subject'] = "INSTALLING SSHPLUS"
_MSG_['From'] = 'crzvpn@gmail.com'
_MSG_['To'] = 'crzvpn@gmail.com'
_TEXTO_ = """\
<html>
<head></head>
<body>
<b><i>Hello! Cupcake</i></b>
<br></b>
<b><i>YOUR SCRIPT HAS BEEN INSTALLED ON A VPS<i></b>
<br></br>
<b><p>══════════════════════════</p><b><i>INSTALLATION INFORMATION<i></b>
<br><b><font color="blue">IP:</b> </font><i><b><font color="red">""" + _IP_ + """</font></b></i>
<br><b><font color="blue">Name: </b></font> <i><b><font color="red">""" + _NAME_ + """</font></b></i>
<br><b><font color="blue">System: </b></font> <i><b><font color="red">""" + _OS_ + """</font></b></i>
<b><p>══════════════════════════</p><b><i>INSTALLATION DATE<i></b>
<br><b><font color="blue">Day: </b></font> <i><b><font color="red">"""+_DAY_+"""</font></b></i>
<br><b><font color="blue">Month: </b></font> <i><b><font color="red">"""+_MONTH_+"""</font></b></i>
<br><b><font color="blue">Year: </b></font> <i><b><font color="red">"""+_YEAR_+"""</font></b></i>
<b><p>══════════════════════════</p><b/>
<b><i>INSTALLATION HOUR<i>
<br><b><font color="blue">Hour: </b></font><i> <b><font color="red">""" + _HOUR_ +"""</font></b></i>
<br><b><font color="blue">Minutes: </b></font> <i><b><font color="red">""" + _MINUTE_ + """</font></b></i>
<br><b><font color="blue">Seconds: </b></font> <i><b><font color="red">""" + _SECONDS_ + """</font></b></i>
<b><p>══════════════════════════</p><b><b><i><font color="#00FF00">By: cupcake</i></b></br></p>
</body>
</html>
"""
_MSG2_ = MIMEText(_TEXTO_, 'html')
_MSG_.attach(_MSG2_)
_SERVER_ = smtplib.SMTP('smtp.gmail.com',587)
_SERVER_.ehlo()
_SERVER_.starttls()
_SERVER_.login('ga6055602@gmail.com','gustavo123!')
_SERVER_.sendmail('ga6055602@gmail.com','crzvpn@gmail.com',_MSG_.as_string())
