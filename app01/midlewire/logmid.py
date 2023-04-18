from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse,redirect

class AuthMid(MiddlewareMixin):
    '''自定义登录中间件
    主要实现：
        不让不登录的用户访问某些页面
    '''
    def process_request(self,request):
        #列出用户再不登录的情况下能访问的页面，出这些页面外，用户再不等的情况下都不能访问
        if request.path_info in ['/login/','/register/','/imagco/']:  #,'/favicon.ico/'
            return
        info_dict = request.session.get('info')
        if info_dict:
            return

        #没有登录过，返回登录页面
        return redirect('/login/')
