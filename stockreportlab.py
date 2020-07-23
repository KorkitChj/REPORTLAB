from reportlab.pdfgen import canvas
#load thai font
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
#colors
from reportlab.lib import colors
#auto open pdf
from subprocess import Popen
# set A4
from reportlab.lib.pagesizes import A4 #210 x 297 mm
# import unit แปลงเป็นระยะหน่วย mm
from reportlab.lib.units import mm
# stock data
from uncleengineer import thaistock
# datetime
from datetime import datetime


pdfmetrics.registerFont(TTFont('F1','angsana.ttc'))

def Text(c,x,y,text,font='F1',size=30,color=colors.black):
    c.setFillColor(color)
    c.setFont(font,size)
    c.drawString(x,y,text)

dtf = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
c = canvas.Canvas('stock - {}.pdf'.format(dtf),pagesize=A4)


c.setFont('F1',30)
c.setFillColor(colors.black)
c.drawCentredString(105 * mm,280 * mm,'ราคาหุ้น (+)')
c.drawCentredString(105 * mm,180 * mm,'ราคาหุ้น (-)')
c.drawCentredString(105 * mm,80 * mm,'ราคาหุ้น (0)')
# ใส่ข้อความแบบ list

textlines = [] #ราคาบวก
textlines2 = [] #ราคาลบ
textlines3 = [] #ไม่เปลี่ยนแปลง

mystock = ['SCB','TMB','KBANK','KTB','CPALL','CPN','GULF','PTT','BBL']

for st in mystock:
    check = thaistock(st)
    txt = 'Stock: {} Price: {} Baht Change: {}'.format(st,check[1],check[2])
    if check[2][0] == '+':
        textlines.append(txt)
    elif check[2][0] == '-':
        textlines2.append(txt)
    else:
        textlines3.append(txt)

#Zone1
text = c.beginText(40 * mm, 260 * mm)
text.setFont('F1',25)
text.setFillColor(colors.green)
for line in textlines:
    text.textLine(line)
c.drawText(text)

#Zone2
text = c.beginText(40 * mm, 160 * mm)
text.setFont('F1',25)
text.setFillColor(colors.red)
for line in textlines2:
    text.textLine(line)
c.drawText(text)

#Zone3
text = c.beginText(40 * mm, 60 * mm)
text.setFont('F1',25)
text.setFillColor(colors.black)
for line in textlines3:
    text.textLine(line)
c.drawText(text)


dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

Text(c,150*mm,285*mm,dt,size=15)

c.showPage()
c.save()

Popen('stock - {}.pdf'.format(dtf),shell=True)




