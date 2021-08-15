import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from backend.arxiv_api import ArxivApiClass
from backend.extractor import Extractor

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

arxiv_api = ArxivApiClass()
extractor = Extractor()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/api/papers/")
def read_nlp_papers(num: int = 10):
    papers = arxiv_api.call_nlp_papers(max_results=num)
    papers = [arxiv_api.extract_title_and_summary_and_comment_from_paper(paper) for paper in papers]

    for paper in papers:
        paper.update({
            "task": extractor.extract_task(paper["summary"]),
            "ne": extractor.extract_ne(paper["summary"])
        })

    return {"papers": papers}


if __name__ == '__main__':
    uvicorn.run("app.main:app", host='0.0.0.0', port=8000,
                log_level="trace", debug=True)
