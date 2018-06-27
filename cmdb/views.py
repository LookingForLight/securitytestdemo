
from django.shortcuts import render
from django.shortcuts import HttpResponse
from cmdb.models import UserInfo
from django.http import JsonResponse
# Create your views here.

from django.db import connection
from django.utils.safestring import mark_safe
msg = []
def index(request):
	result = []
	# return HttpResponse("Hello world!")
	if request.method == "POST":

		userId = request.POST.get("userId",None)
		# password = request.POST.get("password",None)

		#执行自定义SQL
		# cursor = connection.cursor()
		with connection.cursor() as cursor:
			qsql = "select username,sex from cmdb_userinfo WHERE id ='%s'" % (userId)
			#qsql = """select username from cmdb_userinfo WHERE username= '%s' AND  password = '%s'""" % (username, password)
			print("查询语句："+qsql)
			cursor.execute(qsql)
			row = cursor.fetchall()
			#将元组转换为list
			listrow = list(row)

			result = convertResult(listrow)
			print(result)
		return render(request,'index.html',{'info':result})

	if request.method == "GET":
		return render(request, "index.html")



def comment(request):

    if request.method == "GET":
        xsstest = request.GET.get("xsstest")
        if xsstest:
	        safexss=mark_safe(xsstest)
	        return HttpResponse(safexss)

        return render(request,'comment.html',{'msg':msg})
    else:
        v = request.POST.get('content')

        if "script11" in v:
            return render(request,'comment.html',{'error': '小兔崽子还想黑我'})
        else:
            with connection.cursor() as cursor:
                insertsql = 'insert into cmdb_commentinfo(comment) VALUES ("%s")' % (v)
                print("插入语句：" + insertsql)
                cursor.execute(insertsql)

            return render(request,'comment.html',{'success':'提交成功'})



def showlist(request):
	if request.method == "GET":
		comments=[]
		with connection.cursor() as cursor:
			commemtsql = 'select id,comment from cmdb_commentinfo'
			print("查询语句：" + commemtsql)
			cursor.execute(commemtsql)
			res_list = cursor.fetchall()
			res_dict = dict(res_list)
			for values in res_dict.values():
				comments.append(values)

		return render(request,'showcomment.html',{'res_dict':comments})


def test(request):

	temp = "<a href='http://www.ly.com'>同程旅游</a>"
	newtemp = mark_safe(temp)
	msg.append(temp)
	return render(request,'test.html',{'temp':newtemp})

def result(request):

    return render(request,'result.html')

#将列表元组（tuple）转换成列表对象(dict)
def convertResult(param):
	result = []

	if not isinstance(param,list):
		print("参数应该是数据")
	else:
		for tup in param:
			dict = {}
			if isinstance(tup, tuple):
				for j in range(len(tup)):
					if j == 0:
						dict['name'] = tup[j]
					elif j == 1:
						dict['sex'] = tup[j]

			result.append(dict)
	return result
