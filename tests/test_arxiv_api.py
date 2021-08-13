#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from backend.arxiv_api import ArxivApiClass
import pdb


class TestArxivApiClass:
    class TestCallApi:
        @pytest.fixture
        def api_class(self):
            api_class = ArxivApiClass()
            return api_class

        def test_APIをコールしjsonを受け取る(self, api_class):
            assert api_class.check_arxiv_api_call()