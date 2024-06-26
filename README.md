### [on going App repo](https://github.com/Talen-520/Django_Project
)

### [WEBSITE](http://fullstack.techtaohu.com/)

# littlelemon
 https://github.com/Talen-520/littlelemon/assets/63370853/299d54d5-77f8-45cd-a05b-6ee2785d7f37

### make sure run app on virtual environment then activate it by 

windows:

> /bin/activate

MacOS:

> source bin/activate
 
### runserver:

> python manage.py runserver

### install pakcages:

pip install -r requirements.txt


# EC2 server deployment setup

security group inbound:

SSH - IPv4
HTTP - IPv4
HTTP - IPv6


```
sudo apt-get update
sudo apt-get upgrade
```
### virtual environment
```
sudo apt-get install python3-venv
python3 -m venv env
```
### active venv
```
source env/bin/activate
```

### install Django
```
pip3 install django
```

then clone this repo, make sure your project setting contains EC2 IP

### install nginx
```
sudo apt-get install -y nginx
```

### install gunicorn, 

used for django app to communicate web server and hence bridge connection 

```
pip3 install gunicorn
```
check package installed
```
pip list
```
### install supervisor to run app in backend
```
sudo apt-get install supervisor
```
### head to gunicorn configuration file
```
cd /etc/supervisor/conf.d/
sudo touch gunicorn.conf
sudo nano gunicorn.conf
```
### edit configuration file
- replace littlelemon to your root directory
- replace littleLemon to your projectname

example
```
[program:gunicorn]
directory=/home/ubuntu/rootdirectory
command=/home/ubuntu/env/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/rootdirectory/app.sock projectname.wsgi:application
```
```
[program:gunicorn]
directory=/home/ubuntu/littlelemon
command=/home/ubuntu/env/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/littlelemon/app.sock littleLemon.wsgi:application
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log

[group:guni]
programs:gunicorn
```
ctrl + o save file and ctrl x quit

### create log file for error
```
sudo mkdir /var/log/gunicorn
```
### add process group
```
sudo supervisorctl reread
sudo supervisorctl update
sudo supervisorctl status
```
> if status shows not running, here is couple bugs happened too me,
> supervisor: couldn't chdir to /home/ubuntu/littleLemon: ENOENT
> supervisor: child process was not spawned
> solution: check directory path name, case sensitive
>
>   File "/home/ubuntu/littlelemon/littleLemon/wsgi.py", line 12, in <module>
>    from django.core.wsgi import get_wsgi_application
> ModuleNotFoundError: No module named 'django'
> [2023-09-19 03:39:01 +0000] [22217] [INFO] Worker exiting (pid: 22217)
>
> Django does not installed in virtual env
> it show be displayed as following:
> 
> guni:gunicorn                    RUNNING   pid 22574, uptime 0:02:05

### go to nginx directory 
```
cd ..
cd ..
cd nginx or cd /etc/nginx/
sudo nano nginx.conf
```
at top change user to root, inorder avoid permission issue
```
user root;
```
### create django configuration file
```
cd sites-available/ or cd /etc/nginx/sites-available
sudo touch django.conf
sudo nano django.conf
```
### Collect static files from multiple apps into a single path
By copying them from inside the individual apps into a single folder, you can point your frontend web server (e.g. nginx) to that single folder STATIC_ROOT and serve static files from a single location, rather than configure your web server to serve static files from multiple paths.
```
python3 manage.py collectstatic
```

### modify server name and app path
```
server{

	listen 80;
	server_name 0.0.0.0;
	#or server_name littlelemon.techtaohu.com; #which is your domain
	
	
	location / {

		include proxy_params;
		proxy_pass http://unix:/home/ubuntu/littlelemon/app.sock;

	}
	#static file location
	location /static/ {
    		alias /home/ubuntu/littlelemon/static/;
	}


}
```
### test configuration
```
sudo nginx -t
```
sample output
> nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
> nginx: configuration file /etc/nginx/nginx.conf test is successful


```
### get your site alive
sudo ln django.conf /etc/nginx/sites-enabled
sudo service nginx restart
```
### optional debug:
restart gunicorn
find current process

```
 ps aux | grep gunicorn

```

end process

```
sudo kill <pid>
```

restart process:

```
kill -HUP <PID>
```
