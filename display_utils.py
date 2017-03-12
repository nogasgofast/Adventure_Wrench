from PyQt4.QtGui import *
from PyQt4.QtCore import *

def get_health_color(item):
    if item.encounter.get_option('groupOf') > 1:
        hp = sum(item.encounter.get_option('groupHP')) / \
                 item.encounter.get_option('groupOf')
    else:
        hp = item.encounter.get_option('hp')
    if hp <= 0:
        hp = 0
        (red,green,blue)=(255,255,255)
        return (red,green,blue)
    else:
        maxhp = item.encounter.get_option('maxHP') 
        green = int(255 * float(hp) / float(maxhp))
        print "green1=%s"%green
        green = green if green > 0 else 0
        print "green2=%s"%green 
        red =  255 - green
        print "red1=%s"%green
        blue = 0
        return (red,green,blue) 

def update_text(item):
    if item.encounter.get_option('groupOf') > 1:
        format = "%s | %s | %s left with hp Sum: %s High: %s Low: %s" % (
                item.encounter.get_option('initiative'),
                item.encounter.get_option('name'),
                item.encounter.get_option('groupOf'),
                sum(item.encounter.get_option('groupHP')),
                max(item.encounter.get_option('groupHP')),
                min(item.encounter.get_option('groupHP')))
        item.setText(format)
        (red,green,blue) = get_health_color(item)
        painter = QBrush(QColor(red,green,blue))
        item.setBackground(painter)
        # painter = QBrush(QColor(Qt.blue))
        # item.setForeground(painter)
    else:
        item.setText("%s | %s | hp:%s" % (
                item.encounter.get_option('initiative'),
                item.encounter.get_option('name'),
                item.encounter.get_option('hp')))
        (red,green,blue) = get_health_color(item)
        #print "red=%s,green=%s,blue=%s"% (red,green,blue)
        painter = QBrush(QColor(red,green,blue))
        item.setBackground(painter)
        # painter = QBrush(QColor(Qt.blue))
        # item.setForeground(painter)


 
