# Python连接数据库
import mysql.connector

STEM = "甲乙丙丁戊己庚辛壬癸"
BRANCH = "子丑寅卯辰巳午未申酉戌亥"
ZODIAC = "鼠牛虎兔龙蛇马羊猴鸡狗猪"


def stembranch(year):
    return STEM[(year - 4) % 10] + BRANCH[(year - 4) % 12]


def zodiac(year):
    return ZODIAC[(year - 4) % 12]


def leap(year):
    return "闰年" if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else "平年"


conn = mysql.connector.connect(user='root', password='', database='db')
cursor = conn.cursor()
# cursor.execute('create table demo(year integer, stembranch char(2), zodiac char(1), leap char(2))')
# for i in range(2100):
#    cursor.execute("insert into demo values(%s, %s, %s, %s)", (i, stembranch(i), zodiac(i), leap(i)))
cursor.execute('select * from demo')
result = cursor.fetchall()
for i in result:
    print(i)
conn.commit()
conn.close()
cursor.close()

# cursor.execute('SELECT * FROM employee')
# values = cursor.fetchall()
# for i in values:
#     print(i)
# cursor.close()
# conn.close()
