from django.http import HttpResponseRedirect
from django.shortcuts import render,HttpResponse,redirect
#存在内存的文件
from io import BytesIO
from app01 import models
from django import forms
from app01.static.codeimg.pillow_test import check_code
from django.urls import reverse

from .md51 import md51
from .bootstrem import BootStrapForm

from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')


class Log_form(BootStrapForm):
    """用Form组件将数据库的数据返回前端"""
    name = forms.CharField(label='请输入您的用户昵称',
                           widget=forms.TextInput,
                           required=True,
                               )
    password = forms.CharField(label='请输入您的密码',
                               widget=forms.PasswordInput,
                               required=True,
                               )
    code = forms.CharField(
                            label='请输入验证码',
                               widget=forms.TextInput,
                               required=True
                               )
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md51(pwd)

def login(request):
    forms_u = Log_form()
    if request.method == "GET":
        return render(request,"login.html",{"forms":forms_u})
    '''
    将POST传来的用户名和密码与数据库中的比较，
     {{ form.name}}：通过传入HTML
    '''
    form_da = Log_form(data=request.POST)
    if form_da.is_valid():
        '''验证成功'''
        print(form_da.cleaned_data)
        #从返回的数据中取出并在保存sessio到数据库之前踢出img_code
        user_input_code = form_da.cleaned_data.pop('code')
        #从后端取出正确的image_code
        code = request.session.get('image_code','')
        #与用户输入的image_code进行校验
        if code.upper() != user_input_code.upper():
            return HttpResponse("验证码输入错误！")
        #将前端返回的字段对应数据库中的数据并取出
        admin_object = models.Users.objects.filter(**form_da.cleaned_data).first()
        print(admin_object)
        #如果改对象为空，说明数据库中没有用户输入的字段
        if not admin_object:
            # form_da.add_error("name",'输入错误')
            # forms_u.add_error("name","用户名或密码错误")
            return HttpResponse("用户名或密码错误")

        # 如果输入用户名和密码正确
        #网站生成随机字符串，写道用户的cookie中，并写道数据库的session中
        #并返回到首页
        request.session['info'] = {'id':admin_object.id,'name':admin_object.name}
        request.session.set_expiry(60*60*24*7)
        return render(request,"index.html")
    return render(request,"login.html",{"forms":forms_u})



def img_code(request):
    '''生成图片验证码'''
    img,code_string = check_code()
    print(code_string)
    stream = BytesIO()
    img.save(stream, 'png')
    #写入到session中，以便校验验证码
    request.session['image_code'] = code_string
    #设置session过期时间
    request.session.set_expiry(60)
    return HttpResponse(stream.getvalue())

class Uform(forms.ModelForm):
    """ModeForm组件的用户数据结构：username  pasword"""
    class Meta:
        model = models.Users
        fields = ["name","password"]
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md51(pwd)


def register(request):
    # return redirect('register.html')
    form = Uform()
    if request.method == "GET":

        return render(request,'register.html',{"form":form})
    #用户post提交的数据
    #获取页面提交的数据
    # username = request.POST.get("username")
    # passwd = request.POST.get("password")
    # user_dat_list = models.Users.objects.all()
    re_data = Uform(data=request.POST)
    if re_data.is_valid():
        print(re_data)
        re_data.save()
        return render(request,'login.html')
    # for d_user in user_dat_list:
    #     print("d_user是",d_user)
    #     if username == d_user.name:
    #         return HttpResponse("已经注册")
    #     else:
    #         models.Users.objects.create(name=username,password=md51(passwd))
    #         return redirect('/login/')
    return render(request,'register.html',{"form":form})


def loginout(request):
    '''退出登录'''
    request.session.claer()
    return render(request,'login.html')

def my_music(request):
    return render(request,'my_music.html')

def music_hall(request):
    return render(request,'musi_halll.html')

def about(request):
    return render(request,'about.html')


def info_lisrt(request):
    #获取数据库中所有用户信息
    userlist = models.Users.objects.all()
    return render(request,'user_info.html',{'userlist':userlist})

def delete(request):
    nid = request.GET.get('nid')
    models.Users.objects.filter(id=nid).delete()
    userlist = models.Users.objects.all()
    return render(request,'user_info.html',{'userlist':userlist})

def music_search(request):

    return render(request,'music_search.html')
