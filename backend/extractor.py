from typing import List
import spacy
from backend.config import NLP_TASKS

class Extractor:
    def __init__(self, spacy_model: str = 'en_core_web_sm'):
        self.nlp = spacy.load(spacy_model)

    def extract_ne(self, sentence: str) -> List[str]:
        doc = self.nlp(sentence)
        return list(set([X.text for X in doc.ents if X.label_ not in ["CARDINAL", "PERCENT"]]))

    def extract_task(self, sentence: str) -> List[str]:
        return list(set([task for task in NLP_TASKS if task in sentence]))

