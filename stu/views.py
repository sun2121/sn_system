from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from stu.models import Student


def index_view(request):

    #根据不同的请求方式处理不同的业务需求
    if request.method=='GET':
        return render(request,'register.html')
    else:
        # 1.接受请求参数
        uname = request.POST.get('uname','')
        pwd = request.POST.get('pwd','')
        # 2.非空判断
        if uname and pwd:
            # 3.创建模型对象
            student = Student(sname=uname,spwd=pwd)
            # 4.插入数据库
            student.save()

        # 5.页面响应
        return HttpResponse('注册成功！')
    return HttpResponse('注册失败！')


# def login_view(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     else:
#         #1.获取请求参数
#         uname = request.POST.get('uname')
#         pwd = request.POST.get('pwd')
#         #2.查询数据库
#         if uname and pwd:
#             c = Student.objects.filter(sname=uname,spwd=pwd).count()
#         #3.判断是否成功登录
#             if c == 1:
#                 return HttpResponse('登陆成功！')
#         return HttpResponse('登陆失败！')

def login_view(request):
    if request.method == 'GET':
        return render(request,'index.html')
    else:
        #1.获取请求参数
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        #2.查询数据库
        if uname and pwd:
            c = Student.objects.filter(sname=uname,spwd=pwd).count()
        #3.判断是否成功登录
            if c == 1:
                return HttpResponse('登陆成功！')
        return HttpResponse('登陆失败！')