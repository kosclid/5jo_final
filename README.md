1. 가상환경 설치
python -m venv venv
venv\Scripts\activate
    mac---
    python3 -m venv ./venv
    source venv/bin/activate

2. 라이브러리 설치
python -m pip install "django==4.1.0“
python -m pip install "django~=4.1"
python -m pip install --upgrade pip
python -m pip install wheel

pip install django-bootstrap5
pip install Mysqlclient
pip install Pillow
pip install scipy
pip install opencv-python
pip install pandas
pip install tensorflow
pip install -U scikit-learn
pip install mediapipe
pip install hangul-utils

3. migrate

3-1 마이그래이션 하기전에 accounts, dictionary폴더에 migrations폴더 들어가서
__init__.py외에 다른 파일(0001_initial.py같은)있는지 확인하고 있으면 삭제하세요
__init__.py은 지우면 안되요!!!

3-2 mysql 데이터 베이스는 밀어야 합니다...모델 다시 수정 했어요..

    mac ---
    pip install pymysql
    설치 후 settings에 
    import pymysql
    pymysql.install_as_MySQLdb()

이후 마이그래이션 진행하면 됩니다.
python manage.py makemigrations
python manage.py migrate

데이터베이스 슈퍼계정(관리자) 만들기
python manage.py createsuperuser

이후 데이터 베이스가 잘 연결되어 있다면 powershell에서 아래코드가 실행됩니다.
python manage.py load_initial_ganada
python manage.py load_initial_article
차례대로 실행 (데이터 베이스에 데이터 저장하는 과정)

    이름 확인 잘 해
    python manage.py load_ganada
    python manage.py load_article

이후에 run하시면 됩니다. python manage.py runserver

pip install cryptography