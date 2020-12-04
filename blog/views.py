from django.shortcuts import render
from django.http import JsonResponse
import pymysql
import json
# Create your views here.
video_list = [
    {
        'name': '天选之子--卡卡',
        'video_src': 'https://3g.163.com/v/video/VU68ARR5V.html'
    },

]
def get_db():
    db = pymysql.connect(host='localhost', user='root', password='', database='mysite_db_mysql', charset='utf8')
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
    return cursor


def login(request):
    if request.method == 'POST':
        print(6666, json.loads(request.body))
        parm = json.loads(request.body)
        user = parm['username']
        password = parm['password']
        cursor = get_db()
        cursor.execute("select id from user where username='%s' and password='%s'" % (user, password))
        row = cursor.fetchall()
        print(6666, row)
        cursor.close()
        if len(row):
            request.session['username'] = user
            return JsonResponse({'user_id': row[0]['id'], 'success': 'Ok', 'video_list': video_list}, safe=False)
        else:
            if request.session.get('username'):
                del request.session['username']
            return JsonResponse({'success': 'None'}, safe=False)