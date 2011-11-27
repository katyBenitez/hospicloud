# -*- coding: utf-8 -*-
from haystack import indexes
from laboratory.models import Examen

class ExamenIndex(indexes.SearchIndex, indexes.Indexable):
    
    text = indexes.CharField(document=True, use_template=True)
    
    def get_model(self):
        
        return Examen
