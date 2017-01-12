# udic nlp API[![Build Status](https://travis-ci.org/UDICatNCHU/PTT_KCM_API.svg?branch=master)](https://travis-ci.org/UDICatNCHU/PTT_KCM_API)


udic nlp API of web version, you can call the url directly and will cache the result in server.  
Now three languages are available:
* Chinese
* English
* Thai


### API usage and Results

APIʹ�÷�ʽ��������������api��URL pattern��  
(Usage of API (pattern written below is URL pattern))��

##### parameter

* `keyword`��the word you want to query.
* `lang`��Language you use. below are available language version��
  * `cht`������
  * `eng`��English `Still working on it`
  * `thai`��Thai `Still working on it`
* `num`(optional)��The amount of result you want to get (Default��`10`)
* `kcm`, `kem`��Used by `kcem`, you can customarily adjust these two parameter which will get different `kcem` performance.

##### url pattern

1. *`/api/kcm/?keyword=<>&lang=<>&num=<>`*  
  ȡ���P�I�ֵ�`���P���~` (Get `correlation terms` of a keyword)
  * ���� (Example)��`http://api.udic.cs.nchu.edu.tw/api/kcm/?keyword=���d��W&lang=cht`

  ```
  [
    ["��W",58],
    ["�_��",52],
    ["���I",36],
    ["����",33],
    ["���̌WԺ",22],
    ["�W��",19],
    ["�о���",19],
    ["�r�WԺ",19],
    ["�_��ʡ��",16],
    ["�������d��W",15]
  ]
  ```

2. *`/api/kem/?keyword=<>&lang=<>&num=<>`*  
ȡ���P�I�ֵ�`ͬ�x��` (Get `synonym` by keyword)
  * ���� (Example)��`http://api.udic.cs.nchu.edu.tw/api/kem/?keyword=������L&lang=cht`

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

3. *`/api/kcem/?keyword=<>&lang=<>&num=<>`*  
ȡ���P�I�ֵ�`���w�g֮�Č��P` (Get `is-a relationship` of a keyword)
  * ���� (Example)��`http://api.udic.cs.nchu.edu.tw/api/kcem/?keyword=�ܽ܂�&lang=cht&num=10&kcm=5&kem=100`

  ```
  [
    ["����","0.5800000000000003"],
    ["��݋","0.5500000000000003"],
    ["���","0.3900000000000002"],
    ["����","0.34000000000000014"],
    ["�_��","0.34000000000000014"],
    ["�ݳ���",0.17],
    ["����",0.17],
    ["�Ӱ",0.15],
    ["����",0.08],
    ["��Ŀ",0.08]
  ]
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
