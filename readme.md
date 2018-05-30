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
* 在blog应用下创建urls.py文件

* myblog下的urls.py是总路径，应用blog下的urls.py是在总路径下的分路径
## 五、Django Template
* 在blog应用下创建templates目录，再创建一些html文件，在views.py中return render(request, 'index.html', {'hello': 'hello, hello, hello'})

* 为了避免多个应用的情况下找不到url，最好将html文件放到对应应用名下
## 六、Models
* 编写Models，在应用下的models.py下创建字段

* 生成数据表
    * 命令行中进入manage.py同级目录

    * 执行 python manage.py makemigrations app名(可选)

    * 再执行 python manage.py migrate

    * Django会自动在app/migrations/目录下生成移植文件

    * 执行 **python manage.py sqlmigrate 应用名 文件id** 查看SQL语句

* 页面呈现数据
    * views.py中import models

    * article = models.Article.objects.get(pk=1)