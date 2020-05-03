
# docker镜像的编译
`docker build -t yangqinjiang/mnist-dl-backend:latest . && docker run -it --rm --name test yangqinjiang/mnist-dl-backend:latest`
# 1,docker swarm 的使用
`docker swarm init`

# 2, 运行docker stack, mnist-app是stack名称
`docker stack deploy mnist-app -c docker-compose.yml --with-registry-auth`
# 3, 查询services的运行, mnist-app是stack名称
`docker stack services mnist-app`
# 4,查看程序的运行日志, mnist-app是docker-compose.yml 定义的services
`docker service logs -f mnist-app`
# 5,停止docker stack的运行, mnist-app是stack名称
`docker stack rm mnist-app `


# docker其它操作
"""
删除 带none的image 
docker rmi `docker images|grep none|awk '{print $3}'`
"""