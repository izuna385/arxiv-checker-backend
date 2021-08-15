# arxiv-checker-backend
This is an API to return accepted papers related to natural language processing from arxiv.

## build
```Dockerfile
$ docker build -t arxiv_checker_backend:latest .
$ docker run -d --rm --name arxiv_checker_backend_debug -it -v ${PWD}:/projects -p 8000:8000 arxiv_checker_backend
$ docker ps -a|grep arxiv_checker_debug
```

## test
`$ pytest`

## example
`$ curl http://localhost:8000/api/papers/?num=2`

```
{
    "papers": [
        {
            "title": "Survey on Publicly Available Sinhala Natural Language Processing Tools and Research",
            "summary": "Sinhala is the native language of the Sinhalese people who make up the\nlargest ethnic group of Sri Lanka. The language belongs to the globe-spanning\nlanguage tree, Indo-European. However, due to poverty in both linguistic and\neconomic capital, Sinhala, in the perspective of Natural Language Processing\ntools and research, remains a resource-poor language which has neither the\neconomic drive its cousin English has nor the sheer push of the law of numbers\na language such as Chinese has. A number of research groups from Sri Lanka have\nnoticed this dearth and the resultant dire need for proper tools and research\nfor Sinhala natural language processing. However, due to various reasons, these\nattempts seem to lack coordination and awareness of each other. The objective\nof this paper is to fill that gap of a comprehensive literature survey of the\npublicly available Sinhala natural language tools and research so that the\nresearchers working in this field can better utilize contributions of their\npeers. As such, we shall be uploading this paper to arXiv and perpetually\nupdate it periodically to reflect the advances made in the field.",
            "comment": "null",
            "task": [],
            "ne": [
                "Sri Lanka",
                "English",
                "Sinhala",
                "Chinese",
                "Natural Language Processing\n",
                "Indo-European",
                "Sinhalese"
            ]
        },
        {
            "title": "Infusing Finetuning with Semantic Dependencies",
            "summary": "For natural language processing systems, two kinds of evidence support the\nuse of text representations from neural language models \"pretrained\" on large\nunannotated corpora: performance on application-inspired benchmarks (Peters et\nal., 2018, inter alia), and the emergence of syntactic abstractions in those\nrepresentations (Tenney et al., 2019, inter alia). On the other hand, the lack\nof grounded supervision calls into question how well these representations can\never capture meaning (Bender and Koller, 2020). We apply novel probes to recent\nlanguage models -- specifically focusing on predicate-argument structure as\noperationalized by semantic dependencies (Ivanova et al., 2012) -- and find\nthat, unlike syntax, semantics is not brought to the surface by today's\npretrained models. We then use convolutional graph encoders to explicitly\nincorporate semantic parses into task-specific finetuning, yielding benefits to\nnatural language understanding (NLU) tasks in the GLUE benchmark. This approach\ndemonstrates the potential for general-purpose (rather than task-specific)\nlinguistic supervision, above and beyond conventional pretraining and\nfinetuning. Several diagnostics help to localize the benefits of our approach.",
            "comment": "TACL 2021",
            "task": [],
            "ne": [
                "today",
                "GLUE",
                "NLU",
                "Koller",
                "Ivanova",
                "Peters",
                "Tenney",
                "Bender"
            ]
        }
    ]
}
```

### link
https://qiita.com/izuna385/items/749dd0c552c88534d5b3
 