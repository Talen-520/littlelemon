# on going App repo

https://github.com/Talen-520/Django_Project

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


### EC2 server deployment setup

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


