# django-demo
## debian dev evn setup
python version: Python 3.7.3
Django version: Django==1.11.17
### python3 venv setup
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
source venv/bin/activate
pip install Django==1.11.17
pip freeze > requirements.txt
```
