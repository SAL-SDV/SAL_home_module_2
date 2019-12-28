from django.http.response import HttpResponse
from django.shortcuts import render
from datetime import datetime
import MySQLdb.cursors


def getConnection():
    return MySQLdb.connect(host='localhost',
                           user='user',
                           password='user',
                           db='sal',
                           charset='utf8',
                           cursorclass=MySQLdb.cursors.DictCursor
                           )


def setting(request):
    table = []
    connection = getConnection()
    with connection.cursor() as cursor:
        sql = "SELECT * FROM sal.sensorlist "
        cursor.execute(sql)
        for row in cursor.fetchall():
            table.append(row)
        connection.close()

    for t in table:
        if request.GET.get(t["id"] + '_update') == None or request.GET.get(t["id"] + '_update') == '':
            print(t["id"] + 'はnullですよ')
            print(t["Name"])
        else:
            print(t["id"] + 'のNameを' +
                  request.GET.get(t["id"] + '_update') + 'に変更しました。')
            sql = "UPDATE sal.sensorlist SET Name = '" + \
                request.GET.get(t["id"] + '_update') + \
                "' WHERE ID = '" + t["id"] + "'; "

            connection = getConnection()
            with connection.cursor() as cursor:
                cursor.execute(sql)
                connection.commit()
                print(sql)
                # 更新
                sql = "SELECT * FROM sal.sensorlist "
                cursor.execute(sql)
                print(sql)
                table = []
                for row in cursor.fetchall():
                    table.append(row)
                connection.close()

    d = {
        'table': table,
    }
    return render(request, 'setting.html', d)


def home(request):
    # sqlに接続
    connection = getConnection()
    # select文 よりスマートな方法があるはず
    with connection.cursor() as cursor:
        sql = "SELECT path FROM sal.imagelist WHERE id = (SELECT MAX(id) FROM sal.imagelist)"
        cursor.execute(sql)
        result = cursor.fetchone()
        path = result["path"]

        sql = "SELECT imagedata FROM sal.imagelist WHERE id = (SELECT MAX(id) FROM sal.imagelist)"
        cursor.execute(sql)
        result = cursor.fetchone()
        data = result["imagedata"]
        print(data)

        sql = "SELECT id FROM sal.imagelist WHERE id = (SELECT MAX(id) FROM sal.imagelist)"
        cursor.execute(sql)
        result = cursor.fetchone()
        Sid = result["id"]
        Sid=int(Sid)%2+1
        sql = "SELECT Name FROM sal.sensorlist WHERE id = " + str(Sid)
        cursor.execute(sql)
        result = cursor.fetchone()
        name = result["Name"]

    # sqlから切断
    connection.close()
    d = {
        'path': path,
        'data': data,
        'Name': name,
    }

    return render(request, 'home.html', d)


def logs(request):
    connection = getConnection()
    logs = []
    with connection.cursor() as cursor:

        sql = "SELECT * FROM sal.imagelist ORDER BY id desc"
        cursor.execute(sql)
        for row in cursor.fetchall():
            logs.append(row)
        connection.close()
    d = {
        'logs': logs,
    }
    print(logs[1])
    return render(request, 'logs.html', d)

def sensorlogs(request):
    connection = getConnection()
    slogs = []
    with connection.cursor() as cursor:
        sql = "SELECT * FROM sal.imagelist inner join sal.sensorlist ON sal.imagelist.cameraID = sal.sensorlist.id"
        cursor.execute(sql)
        for row in cursor.fetchall():
            slogs.append(row)
        connection.close()
    d = {
        'slogs':slogs,
    }
    print(slogs[1])
    return render(request, 'sensorlogs.html', d)
