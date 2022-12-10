
from PySide6.QtGui import QBrush, QColor
from pony.orm import db_session

def get_health_color(item):
    # if item.type != 'pc' and item.encounter.get_option('groupOf') > 1:
    #     hp = sum(item.encounter.get_option('groupHP')) / \
    #              item.encounter.get_option('groupOf')
    # else:
    hp = item.dbObj.hp
    if hp <= 0:
        hp = 0
        (red,green,blue)=(255,255,255)
        return (red,green,blue)
    else:
        maxhp = item.dbObj.max_hp
        green = int(255 * (float(hp) / float(maxhp)))
        #print "green1=%s"%green
        green = green if green > 0 else 0
        green = green if green < 255 else 255
        #print "green2=%s"%green
        red =  255 - green
        #print "red=%s"% red
        blue = 0
        return (red,green,blue)

@db_session
def update_text(item, db):
    if item.type == 'pc':
        # reaquire state from db. Pony implementation requires this.
        item.dbObj = db.Active[item.dbObj.id]
        item.setToolTip(item.dbObj.description)
        item.setText("%s | %s | hp:%s | %s%s%s%s" % (
                item.dbObj.initiative,
                item.dbObj.name,
                item.dbObj.hp,
                # These are the various types of indicators I have.
                u'\u2716' * item.dbObj.death_save_fail,
                u'\u2714' * item.dbObj.death_save_success,
                u'\u2605' * item.dbObj.black_star,
                u'\u2606' * item.dbObj.white_star))
        (red,green,blue) = get_health_color(item)
        #print "red=%s,green=%s,blue=%s"% (red,green,blue)
        painter = QBrush(QColor(red,green,blue))
        item.setBackground(painter)
        # painter = QBrush(QColor(Qt.blue))
        # item.setForeground(painter)
    else:
        update_text_for_non_players(item)

@db_session
def update_text_for_non_players(item):
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
        item.setText("%s | %s | hp:%s | %s%s%s%s" % (
                item.encounter.get_option('initiative'),
                item.encounter.get_option('name'),
                item.encounter.get_option('hp'),
                u'\u2716' * item.encounter.get_option('DSF'),
                u'\u2714' * item.encounter.get_option('DSS'),
                u'\u2605' * item.encounter.get_option('bs'),
                u'\u2606' * item.encounter.get_option('ws')))
        (red,green,blue) = get_health_color(item)
        #print "red=%s,green=%s,blue=%s"% (red,green,blue)
        painter = QBrush(QColor(red,green,blue))
        item.setBackground(painter)
        # painter = QBrush(QColor(Qt.blue))
        # item.setForeground(painter)
    if item.encounter.get_option('type') != 'pc':
        item.setToolTip("%s" % item.encounter.to_string())
