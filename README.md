# KCM_web_api[![Build Status](https://travis-ci.org/UDICatNCHU/PTT_KCM_API.svg?branch=master)](https://travis-ci.org/UDICatNCHU/PTT_KCM_API)

�W퓰��KCM api������ֱ�Ӻ��оWַ�õ��Y�����K�ҕ�cache��ԃ�^�ĽY��  
Ŀǰ֧Ԯ��
* ���İ�
* Ӣ�İ�
* ̩�İ�
KCM API of web version, you can call the url directly and will cache the result in server.  
Now three languages are available:
* Chinese
* English
* Thai


### API usage and Results

APIʹ�÷�ʽ��������������api��URL pattern��  
(Usage of API (pattern written below is URL pattern))��

1. ȡ���P�I�ֵ����P���~ (Get correlation terms of a keyword, put the KeyWord you want to query after `/?issue=`)�� `/api/kcmApi/?keyword={���}���Q}&lang={�Z�ԅ�������cht��eng��thai�����x}&num={�؂��Ć��֔�����Ոݔ�딵��}`
  * ��ԃ�Wַ (query url)��http://140.120.13.243:32785/api/kcmApi/?keyword=
  * ���� (Example)��`http://140.120.13.243:32785/api/kcmApi/?keyword=���d��W&lang=cht&num=10`
  * result��
  ```
  {
    "��W": 164,
    "��": 93,
    "�": 88,
    "��": 86,
    "����": 81,
    "�_��": 72,
    "���I": 66,
    "�W��": 55,
    "���̌WԺ": 55,
    "�r�WԺ": 50
  }
  ```

2. ȡ���P�I�ֵ����P���~ (Get correlation terms of a keyword, put the KeyWord you want to query after `/?issue=`)�� `/api/kemApi/?keyword={���}���Q}&lang={�Z�ԅ�������cht��eng��thai�����x}&num={�؂��Ć��֔�����Ոݔ�딵��}` (num�ą��������A�O���؂�10�������hʹ���@�Nģʽ������A�Ƚ���cache����t���Ҫ�Ⱥܾ�) (num parameter is not recommended to add, cause it takes time to query model. If num parameter is absent, will use num=10 in default.)
  * ��ԃ�Wַ (query url)��http://140.120.13.243:32785/api/kemApi/?keyword=
  * ���� (Example)��`http://140.120.13.243:32785/api/kemApi/?keyword=������L&lang=cht&num=10`
  * result��
  ```
  {
    "X��": "0.6915161609649658",
    "�b": "0.6872922778129578",
    "�ͳ���": "0.6902425289154053",
    "�ͳ�����": "0.7779505252838135",
    "�����Ăb": "0.7140904664993286",
    "֩����": "0.7551226615905762",
    "֩��b": "0.7653720378875732",
    "�����b": "0.7000312805175781",
    "ρ��": "0.7080279588699341",
    "׃�ν���": "0.7029522657394409"
  }
  ```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisities

1. OS��Ubuntu / OSX would be nice
2. environment��need python3 `sudo apt-get update; sudo apt-get install; python3 python3-dev`

### Installing

There are two choice��

* Install By Git��
  1. ���d (Download this project)��`git clone https://github.com/UDICatNCHU/KCM_web_api.git`
  2. ʹ��̓�M�h�� (Use virtualenv is recommended)��
    1. ����̓�M�h����ȡ������venv��`virtualenv venv`
    2. ���ӷ��� (How to activate virtualenv)
      1. for Linux��`. venv/bin/activate`
      2. for Windows��`venv\Scripts\activate`
  3. ���b (Install)��`make install`
* Install By Docker��
  1. ��ָ��������Dockerfile��Ŀ����� (You can only run this command in directory which has Dockerfile)��`sudo docker build -t kcm .`


## Running & Testing

## Run

Still has two choice to Run�� it depends on which installed method you used��

* By Git��
  1. �Ƚ���KCM model, lang����Ո����Ҫ�������Z��ģ�� (You need to build KCM model first, you can pass `cht` or `eng` to lang parameter)��`cd KCM; nohup make init lang={cht��eng} &`
  2. ����django�ŷ���(Open django Server)��`./manage.py runserver`
  3. �_���g�[�����z��һ��API�Ƿ������a��json�Y��(Open your browser and test whether it works or not.)
* By Docker��
  1. �ڱ�������container�K���chost��port��ͨ ()��`sudo docker run -d -P --name={container name} kcm`
  2. �M��docker container����KCM model(Enter docker container for building KCM model)��`sudo docker exec -it {container name} bash`
  3. ����KCM model, lang����Ո����Ҫ�������Z��ģ�� (You need to build KCM model first, you can pass `cht` or `eng` to lang parameter)��`cd KCM; nohup make init lang={cht��eng} &`
  4. �˳�container֮�ᣬ�_���g�[�����z��һ��API�Ƿ������a��json�Y��(Leave container and test whether it works or not.)


### Break down into end to end tests

### And coding style tests

Ŀǰ�]��coding style tests...  
There's no coding style tests yet.

## Deployment

Ŀǰֻ��һ��� **django** ��ʽ��ʹ��gunicorn����uwsgi���𼴿�  
It's just a normal django project, use gunicorn or uwsgi can deploy.

## Built With

* Django 1.10.2
* python3.5

## Versioning

For the versions available, see the [tags on this repository](https://github.com/david30907d/KCM/releases).

## Contributors

* **��̩�|** [david](https://github.com/david30907d)

## License

This project is licensed under the **MIT** License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

���xKCM���������� Thanks all Contributors of KCM
