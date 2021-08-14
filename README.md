# arxiv-checker-backend

## build
```Dockerfile
$ docker build -t arxiv_checker:latest .
$ docker run -d --rm --name arxiv_checker_debug -it -v ${PWD}:/projects -p 8000:8000 arxiv_checker
$ docker ps -a|grep arxiv_checker_debug
```

### check
 