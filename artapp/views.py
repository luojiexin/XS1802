from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    #  请求路径和请求方法
    # print(request.path, request.method)
    #  请求头信息 和 GET请求参数
    print('1', request.GET.get("page", request.GET.get('tag')))
    #  POST请求参数
    print('2', request.POST)
    return render(request, 'art/list.html',
                  context={'name': '杨斌', 'age': '250'})