from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse
class M1(MiddlewareMixin):
    '''中间件M1'''
    def process_request(self,request):
        '''
        返回值可有可无
            无返回值继续向后走
            有返回值：如HTtpresponse，render（返回一个页面）
            或redired重定向(向用户返回一个地址，让用户向返回这个地址发起请求)
        '''
        print("M1开始进入中间件")
        return HttpResponse("无权访问")

    def process_response(self,request,response):
        print("M1走了")
        return response

class M2(MiddlewareMixin):
    '''中间件M2'''
    def process_request(self,request):
        print("M2开始进入中间件")

    def process_response(self,request,response):
        print("M2走了")
        return response