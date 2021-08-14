# arxiv-checker-backend
This is an API to return accepted papers related to natural language processing from arxiv.

## build
```Dockerfile
$ docker build -t arxiv_checker:latest .
$ docker run -d --rm --name arxiv_checker_debug -it -v ${PWD}:/projects -p 8000:8000 arxiv_checker
$ docker ps -a|grep arxiv_checker_debug
```

## test
`$ pytest`

### link
https://qiita.com/izuna385/items/749dd0c552c88534d5b3
 