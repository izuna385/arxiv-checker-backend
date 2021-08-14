#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from backend.arxiv_api import ArxivApiClass
import pdb
from arxiv import Result

class TestArxivApiClass:
    @pytest.fixture
    def api_class(self):
        api_class = ArxivApiClass()
        return api_class

    class TestCallApi:
        def test_APIをコールしjsonを受け取る(self, api_class):
            assert api_class.check_arxiv_api_call()

    class TestNlpConferencesList:
        def test_表記ゆれを含めた直近のNLP国際会議リストを返却する(self, api_class):
            assert [conference for conference in api_class._nlp_conference_list_creator()]

    class TestCallNlpPapers:
        def test_NLP関連国際学会の論文リストを指定した件数受け取る(self, api_class):
            max_results = 10
            assert len([paper for paper in api_class.call_nlp_papers(max_results=max_results)]) == 10

    class TestExtractTitleAndAbstractFromPaper:
        def test_文章からtitleとsummaryとcommentのみを抽出する(self, api_class):
            nlp_papers = api_class.call_nlp_papers(max_results=100)
            for nlp_paper in nlp_papers:
                paper_infomation = api_class.extract_title_and_summary_and_comment_from_paper(nlp_paper)
                assert "title" in paper_infomation and "summary" in paper_infomation and "comment" in paper_infomation