# arxiv-checker-backend

## build
```Dockerfile
$ docker build -t arxiv_checker:latest .
$ docker run -d --rm --name arxiv_checker_debug -it arxiv_checker
$ docker ps -a|grep arxiv_checker_debug
```