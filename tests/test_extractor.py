#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
from backend.extractor import Extractor
import pdb

class TestExtractor:
    @pytest.fixture
    def extractor_class(self):
        extractor_class = Extractor()
        return extractor_class

    @pytest.fixture
    def sentence_example(self):
        sentence_example = 'We introduce a new language representation model called BERT, which stands ' \
                        'for Bidirectional Encoder Representations from Transformers. Unlike recent language ' \
                        'representation models, BERT is designed to pre-train deep bidirectional representations ' \
                        'from unlabeled text by jointly conditioning on both left and right context in all ' \
                        'layers. ' \
                        'As a result, the pre-trained BERT model can be fine-tuned with just one additional ' \
                        'output ' \
                        'layer to create state-of-the-art models for a wide range of tasks, such as question ' \
                        'answering and language inference, without substantial task-specific architecture ' \
                        'modifications. BERT is conceptually simple and empirically powerful. It obtains new ' \
                        'state-of-the-art results on eleven natural language processing tasks, including pushing ' \
                        'the GLUE score to 80.5% (7.7% point absolute improvement), MultiNLI accuracy to 86.7% ' \
                        '(4.6% absolute improvement), SQuAD v1.1 question answering Test F1 to 93.2 (1.5 ' \
                        'point absolute improvement) and SQuAD v2.0 Test F1 to 83.1 ' \
                        '(5.1 point absolute improvement).'

        return sentence_example

    class TestExtractNe:
        def test_nlp要素を含む複文からエンティティのリストを返却する(self, extractor_class, sentence_example):
            assert 'BERT' in extractor_class.extract_ne(sentence_example)

    class TestExtractTasks:
        def test_nlpタスクを含む複文からnlpタスクのリストを返却する(self, extractor_class, sentence_example):
            assert 'question answering' in extractor_class.extract_task(sentence_example)
