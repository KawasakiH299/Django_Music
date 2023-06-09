# Django-
## 项目是由一部分vue作为前端+django作为后端+mysql作为数据库构成

#### 项目需要环境：
	- 1.python
	- 2.pycharm
	- 3.python中django包
		- pip install django
	- 4.mysql：
		- python和mysql交互需要mysqlclient模块支持，安装mysqlclient ：pip install mysqlclient 
		- mysql登录名和密码都必须为root，端口为默认端口：3306

#### 项目需要初始化才能运行：
		#初始化数据库并创建一个名为music的数据库：
		- 可参考文件夹	./安装包和安装步骤		
		#初始化迁移表：
		- python manage.py makemigrations --empty role 
		#创建数据迁移表
		- py ./manage.py makemigrations 
		#根据迁移表的操作将数据存入数据库
		- py ./manage.py migrate 
		（这些命令会在mysql中创建许多表，app01_users是保存用户昵称和密码的表）

#### 项目功能简介：
	- 首先是用户登录功能：
		- 登录地址为:http://127.0.0.1:8000/login/(本地服务器)
		- 登录用户在输入昵称和密码（后台设置本能为空），jango作为后端会将用户输入的昵称和密码
			- 与mysql中数据库为app01_users中的数据做对比，如果正确，登录成功，
			- 本地服务器会随机生成一个序列cookie返回给游览器，并作为session保存到mysql数据库
			中的django_session表中，session的有效时间是7天，7天之后用户需要再次访问，需要再次登录，并跳转到首页
		- 为了安全考虑，防止登录被爆破，添加了一个输入验证码的功能，
		- 验证码的图片是由pillow模块生成并保存在内存的二进制文件，结合字体文件可以形成有效时间为60秒的字母图片验证码，
		- 考虑到爬虫技术，爬虫可以利用一定的图像识别，由于数字的识别毕字母的识别简单，选择的是字母验证，并添加了干扰像素点
	- 用户注册功能：
		- 用户注册地址是：http://127.0.0.1:8000/register/（本地服务器）
		- 用户在填写完昵称和密码后会交给后端，jango会获取用户提交的昵称和密码的表单
			- 表单中昵称数据会作为字符串保存进mysql，密码会被非对称加密算法MD5，
			- 加密后成为一个一定长度的字符串保存到mysql中，这样即使数据库中的数据泄露，仍然看不到用户的真正密码，因为MD5加密是不可逆的加密算法，
			- 被加密后即使开发人员也不字段用户的真正密码
	- 用户搜索歌曲的功能：
		- 访问地址是首页的音乐库（可以自行更改）：http://127.0.0.1:8000/search/（本地服务器）
		- 搜索功能是vue实例化，和网易云ap实现
		- 搜索的歌曲信息由其他用户评论和视频，可自行下载喜欢的歌曲和视频（仅提供技术支持，不可作商业用途）
	- djago的后台管理：
		- 后台管理员登录地址：http://127.0.0.1:8000/admin/   (本地服务器)
		- 可以直接看到用户，并以用户界面的形式直接对网页的数据进行操作
		
		
