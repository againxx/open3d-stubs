"""
This type stub file was generated by pyright.
"""

class SemSegRandomSampler:
    """Random sampler for semantic segmentation datsets."""
    def __init__(self, dataset) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def initialize_with_dataloader(self, dataloader): # -> None:
        ...
    
    def get_cloud_sampler(self): # -> Generator[Any, None, None]:
        ...
    
    @staticmethod
    def get_point_sampler(): # -> (**kwargs: Unknown) -> tuple[Unknown, ndarray[Unknown, Unknown] | Unknown, Unknown]:
        ...
    

