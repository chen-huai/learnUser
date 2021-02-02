# 学习Django

### 新建项目
* 在所需位置终端输入`django-admin.py startproject 项目名称`
  ```
  $ 目录位置 项目名称
  $ tree
  .
  |-- HelloWorld（项目名称）
  |   |-- __init__.py
  |   |-- asgi.py
  |   |-- settings.py
  |   |-- urls.py
  |   `-- wsgi.py
  `-- manage.py
  ```
* django自带服务器运行
```
# 该方式只能在本机使用
python manage.py runserver
# 浏览器输入http://127.0.0.1:8000/
```
```
# 该方式可以在同一域名下，输入运行电脑：域名IP:8000/
python manage.py runserver 0.0.0.0:8000
```

### 新建app

* django-admin.py startapp app名称
* settings.py 中找到INSTALLED_APPS这一项，如下：
  ```
    INSTALLED_APPS = (
      'django.contrib.admin',
      'django.contrib.auth',
      'django.contrib.contenttypes',
      'django.contrib.sessions',
      'django.contrib.messages',
      'django.contrib.staticfiles',
      'app名称',  # 添加新的app             
      )
  ```

### 数据库
#### 选择数据库类型--MySQL
* 在项目project中的setting.py里修改为MySQL数据库
```
DATABASES = {
     'default':
        {
            'ENGINE': 'django.db.backends.mysql',    # 数据库引擎
            'NAME': 'tuv_inventory', # 数据库名称
            'HOST': '127.0.0.1', # 数据库地址，本机 ip 地址 127.0.0.1
            'PORT': 3306, # 端口
            'USER': 'root',  # 数据库用户名
            'PASSWORD': '123456', # 数据库密码
            'OPTIONS': {
                            'charset': 'utf8',
                            'autocommit': True,
                           'init_command': 'SET sql_mode="STRICT_TRANS_TABLES"',
                   }
        }
}
```
* 在项目project中的__init__.py里
```
import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
```
#### 数据库模型建立
* 在对应app的model.py里
```
from django.db import models
from django.conf import settings
# 一个类对应一张表 
class Supplier(models.Model):
    # 一个变量代表一个字段，字段可选类型、默认值和显示名称等等
    supplierName = models.CharField(max_length=100, verbose_name="供应商")
    address = models.CharField(max_length=100, blank=True, verbose_name="地址")
    phone = models.CharField(max_length=32, blank=True, verbose_name="电话")
    email = models.CharField(max_length=32, blank=True, verbose_name="邮件")
    remark = models.CharField(max_length=500, blank=True, verbose_name="备注")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")   
    # 用于显示
    def __str__(self):             
        return self.supplierName
    # 用于给本表指定一个别名
    class Meta():
        verbose_name_plural = "供应商"
```
#### 生成数据库
* 创建表结构
`python manage.py migrate`
* 让 Django 知道我们在我们的模型有一些变更
`python manage.py makemigrations app名称`
* 创建表结构
`python manage.py migrate app名称`
#### 显示数据库
* 在对应app的admin.py里
: 主要是为了django自带的admin模块，高效开发
```
from django.contrib import admin
from base.models import *
# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    # 显示字段
    list_display = ('supplierName','address','phone','email','remark','is_delete')
    # address字段显示别名为'地址'
    address.short_description = '地址'
    # 搜索字段
    search_fields = ('supplierName',)
    # 显示页面
    list_per_page = 20
    # 排序，可多个
    ordering = ('supplierName',)
    # 可编辑字段（不美观）
    # list_editable = ["address",'phone','email','remark','is_delete']
admin.site.register(Supplier, SupplierAdmin)
```
```
    # 当字段为多对多类型时，显示操作
    def users(self,obj):
        # 原理：查找全部并循环显示
        return [bt.username for bt in obj.user.all()]
```
```
# 任何一个app中的admin
admin.site.site_header = "库存后台管理"
admin.site.site_title = '库存后台管理'
```
### 创建数据库超级管理员
* 创建超级用户
`python manage.py createsuperuser`
输入用户名，密码，邮件等信息后，可登入admin界面，方便操作
* 输入`http:/127.0.0.1:8000/admin`即可访问django自带的admin模块，能高效开发
* 更换admin界面，如：simpleui。
```
# 项目setting.py中添加
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'laboratory',
    'base',
    'invoicing',
]
```
```
# 项目setting.py中添加

# simpleui设置
# 取消simpleui的开发信息
SIMPLEUI_HOME_INFO = False
# 更换后台界面的logo
SIMPLEUI_LOGO = 'https://www.tuvsud.cn/images/logo-100.png'# TUV logo
# 更改对应名称的表图标
SIMPLEUI_ICON = {
	'入库': 'fas fa-archive',
}
```
