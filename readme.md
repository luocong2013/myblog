## 一、创建myblog项目
* django-admin startproject myblog

## 二、运行myblog项目
* cd myblog

* myblog>python manage.py runserver 5000
## 三、创建blog应用
* cd myblog

* myblog>python manage.py startapp blog

* 添加应用名到settings.py中的INSTALLED_APPS里
## 四、配置url
* myblog下的urls.py是总路径，应用blog下的urls.py是在总路径下的分路径