"""
This type stub file was generated by pyright.
"""

from .base_dataset import BaseDatasetSplit

log = ...
class InferenceDummySplit(BaseDatasetSplit):
    def __init__(self, inference_data) -> None:
        ...
    
    def __len__(self): # -> Literal[1]:
        ...
    
    def get_data(self, idx):
        ...
    
    def get_attr(self, idx): # -> dict[str, Unknown]:
        ...
    

