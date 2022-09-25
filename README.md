# django-demo
- python version: Python 3.7.3
- Django version: Django==1.11.17
## env setup
### setup venv 
```bash
mkdir ~/.pip
cat << EOF > ~/.pip/pip.conf
global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn
EOF
apt-get install python3-venv
python3 -m venv venv
```
### setup django project
```bash
source venv/bin/activate
pip install Django==1.11.17
django-admin startproject devops .
pip freeze > requirements.txt
```
### setup django db mysql
```bash
pip install PyMySQL
cat << EOF > devops/__init__.py
import pymysql
pymysql.install_as_MySQLdb()
EOF
pip freeze > requirements.txt
```
### start new django app
```bash
python manage.py startapp cmdb
python manage.py makemigrations cmdb
python manage.py migrate
```