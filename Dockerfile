# 引用镜像
FROM yangqinjiang/alpine-python3-numpy-flask:latest

LABEL maintainer="yangqinjiang"

WORKDIR /src
COPY src .

ENTRYPOINT ["python"]
CMD ["main.py"]
