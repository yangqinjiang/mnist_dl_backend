# 引用镜像
FROM yangqinjiang/alpine-python3-numpy-flask:latest

LABEL maintainer="yangqinjiang"

WORKDIR /src
COPY src .

EXPOSE 8000
CMD ["/usr/bin/gunicorn","-c","gun.py", "main:app"]


# ENTRYPOINT ["python"]
# CMD ["main.py"]
