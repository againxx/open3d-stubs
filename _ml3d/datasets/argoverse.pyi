"""
This type stub file was generated by pyright.
"""

from .base_dataset import BaseDataset
from .utils import BEVBox3D

log = ...
class Argoverse(BaseDataset):
    """This class is used to create a dataset based on the Agroverse dataset,
    and used in object detection, visualizer, training, or testing.
    """
    def __init__(self, dataset_path, info_path=..., name=..., cache_dir=..., use_cache=..., **kwargs) -> None:
        """Initialize the function by passing the dataset and other details.

        Args:
            dataset_path: The path to the dataset to use.
            info_path: The path to the file that includes information about the
                dataset. This is default to dataset path if nothing is provided.
            name: The name of the dataset.
            cache_dir: The directory where the cache will be stored.
            use_cache: Indicates if the dataset should be cached.

        Returns:
            class: The corresponding class.
        """
        ...
    
    @staticmethod
    def get_label_to_names(): # -> dict[int, str]:
        """Returns a label to names dictonary object.

        Returns:
            A dict where keys are label numbers and values are the corresponding
            names.
        """
        ...
    
    @staticmethod
    def read_lidar(path): # -> ndarray[Unknown, Unknown]:
        """Reads lidar data from the path provided.

        Returns:
            A data object with lidar information.
        """
        ...
    
    @staticmethod
    def read_label(bboxes): # -> list[Unknown]:
        """Reads labels of bound boxes.

        Returns:
            The data objects with bound boxes information.
        """
        ...
    
    def get_split(self, split): # -> ArgoverseSplit:
        """Returns a dataset split.

        Args:
            split: A string identifying the dataset split that is usually one of
            'training', 'test', 'validation', or 'all'.

        Returns:
            A dataset split object providing the requested subset of the data.
        """
        ...
    
    def get_split_list(self, split): # -> Any | dict[Unknown, Unknown]:
        """Returns a dataset split.

        Args:
            split: A string identifying the dataset split that is usually one of
            'training', 'test', 'validation', or 'all'.

        Returns:
            A dataset split object providing the requested subset of the data.

        Raises:
            ValueError: Indicates that the split name passed is incorrect. The
            split name should be one of 'training', 'test', 'validation', or
            'all'.
        """
        ...
    
    def is_tested(self): # -> None:
        """Checks if a datum in the dataset has been tested.

        Args:
            dataset: The current dataset to which the datum belongs to.
            attr: The attribute that needs to be checked.

        Returns:
            If the dataum attribute is tested, then resturn the path where the
            attribute is stored; else, returns false.
        """
        ...
    
    def save_test_result(self): # -> None:
        """Saves the output of a model.

        Args:
            results: The output of a model for the datum associated with the
            attribute passed.
            attr: The attributes that correspond to the outputs passed in results.
        """
        ...
    


class ArgoverseSplit:
    """This class is used to create a split for Agroverse dataset.

    Initialize the class.

    Args:
        dataset: The dataset to split.
        split: A string identifying the dataset split that is usually one of
            'training', 'test', 'validation', or 'all'.
        **kwargs: The configuration of the model as keyword arguments.

    Returns:
        A dataset split object providing the requested subset of the data.
    """
    def __init__(self, dataset, split=...) -> None:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def get_data(self, idx): # -> dict[str, Unknown]:
        ...
    
    def get_attr(self, idx): # -> dict[str, Unknown]:
        ...
    


class Object3d(BEVBox3D):
    """The class stores details that are object-specific, such as bounding box
    coordinates.
    """
    def __init__(self, center, size, yaw, name, box) -> None:
        ...
    
    def generate_corners3d(self):
        """This generates a Corners 3D representation for the object, and
        returns the corners in 3D, such as (8, 3) corners of a Box3D in camera
        coordinates.
        """
        ...
    

