# python:alpine is 3.{latest}
FROM python:alpine 

LABEL maintainer="yangqinjiang"
WORKDIR /src
COPY  requirements.txt ./

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple


COPY src .

CMD ["gunicorn", "start:app", "-c", "./gunicorn.conf.py"]