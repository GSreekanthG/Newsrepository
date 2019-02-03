from django.shortcuts import render

# Create your views here.
def index(request):
    return  render(request,'newsapp/index.html')
def moviesinfo(request):
    head_msg='Latest Movies Information'
    msg1='sonali slowly getting cured'
    msg2='salman going to marry soon'
    msg3='narendra modi is going to act in some movie'
    my_dict={'head_msg':head_msg,'msg1':msg1,'msg2':msg2,'msg3':msg3}
    return  render(request,'newsapp/news.html',context=my_dict)
def sportsinfo(request):
    head_msg = 'Latest sports Information'
    msg1 = 'sonali slowly getting cured'
    msg2 = 'salman going to marry soon'
    msg3 = 'narendra modi is going to act in some movie'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return  render(request,'newsapp/news.html',context=my_dict)
def politicsinfo(request):
    head_msg = 'Latest politics Information'
    msg1 = 'sonali slowly getting cured'
    msg2 = 'salman going to marry soon'
    msg3 = 'narendra modi is going to act in some movie'
    my_dict = {'head_msg': head_msg, 'msg1': msg1, 'msg2': msg2, 'msg3': msg3}
    return  render(request,'newsapp/news.html',context=my_dict)