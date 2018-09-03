# mini-mvc
一个居于flask的mvc框架

# 简单用法
（1）安装依赖（查看根目录下的requirement.txt文件）
（2）运行 run_dbg_server.bat (linux输入命令 sh run_dbg_server.sh)  
（3）在浏览器输入 http://127.0.0.1:5000/login?phone=13522144567&password=123456  
（4）浏览器如果正常输出，运行成功 

# 代码说明
│  main.py  
│  manager.py  
│  db_create.py  
│  mini-mvc.ini  
│  restart_uwsgi.py  
│  run_dbg_server.bat  
│  run_dbg_server.sh  
│  requirement.txt  
│  
├─common  通用代码  
│      middlewares.py  
│      render.py  
│      utils.py  
│      
├─conf  配置文件  
│      settings.py  
│  
├─controller  控制器代码（mvc的c部分）  
│      controller_base.py  
│      login_controller.py  
│  
├─dbs  模型代码（mvc的m部分）  
│     models.py  
│     
└─views  视图代码（mvc的v部分）  
  login_views.py  
  view_base.py  
        
