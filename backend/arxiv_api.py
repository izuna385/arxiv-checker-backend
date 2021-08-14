import json
from typing import Dict, List
import arxiv
from backend.config import CONFERENCES, YEARS
import pdb
from arxiv import Result

class ArxivApiClass:
    '''
    arXiv APIを叩く部分を受け持つクラス
    '''
    def __init__(self, max_paper_num_per_call: int = 30):
        self.max_paper_num_per_call = max_paper_num_per_call
        self.conferences = self._nlp_conference_list_creator()

    def _nlp_conference_list_creator(self) -> List[str]:
        conferences = list()
        for conference in CONFERENCES:
            for year in YEARS:
                conferences.append(conference + str(year))
                conferences.append(conference + ' ' + str(year))

        return conferences

    def _encoding_conference_for_api_query(self, conference: str) -> str:
        return conference.replace(' ', '%20')

    def check_arxiv_api_call(self, query: str = "ACL2020", max_results: int = 10) -> List:
        '''
        arxiv apiを叩いて結果が返却されるかどうかを確認するメソッド。
        :param query:
        :param max_results:
        :return: ジェネレータをリストへ変換した、arxiv apiの返却結果
        '''
        return [paper for paper in arxiv.Search(query=query, max_results=max_results).results()]

    def call_nlp_papers(self, max_results: int = 20) -> List[Result]:
        '''
        arxiv apiを叩いて、コメントに自然言語処理国際学会を含む
        :param max_results:
        :return:
        '''
        search_query = '(' + ' OR '.join(["co=" + "'" + conference + "'" for conference in self.conferences]) + \
                       ') AND cat:cs.CL'
        return [paper for paper in arxiv.Search(query=search_query, max_results=max_results).results()]

    def extract_title_and_summary_and_comment_from_paper(self, paper: Result) -> Dict:
        '''
        Resultクラスから不要な情報を除き、title, abstract, commentのみを返却する
        :param paper:
        :return:
        '''
        return {
            "title": paper.title,
            "summary": paper.summary,
            "comment": paper.comment
        }
