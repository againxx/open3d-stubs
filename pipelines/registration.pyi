from typing import overload, List, Union, Iterable, Optional
from numpy import float64, int32
from numpy.typing import NDArray
from .. import geometry, utility

class Feature:
    data: NDArray[float64]
    def __init__(self, *args, **kwargs) -> None: ...
    def dimension(self) -> int: ...
    def num(self) -> int: ...
    def resize(self, dim: int, n: int) -> None: ...

class RobustKernel:
    def __init__(self, *args, **kwargs) -> None: ...
    def weight(self, residual: float) -> float: ...

class CauchyLoss(RobustKernel):
    k: float
    def __init__(self, *args, **kwargs) -> None: ...

class GMLoss(RobustKernel):
    k: float
    def __init__(self, *args, **kwargs) -> None: ...

class HuberLoss(RobustKernel):
    k: float
    def __init__(self, *args, **kwargs) -> None: ...

class L1Loss(RobustKernel):
    def __init__(self, *args, **kwargs) -> None: ...

class L2Loss(RobustKernel):
    def __init__(self, *args, **kwargs) -> None: ...

class TukeyLoss(RobustKernel):
    k: float
    def __init__(self, *args, **kwargs) -> None: ...

class CorrespondenceChecker:
    require_pointcloud_alighment_: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def Check(
        self,
        source: geometry.PointCloud,
        target: geometry.PointCloud,
        corres: utility.Vector2iVector,
        transformation: NDArray[float64],
    ) -> bool: ...

class CorrespondenceCheckerBasedOnDistance(CorrespondenceChecker):
    distance_threshold: float
    def __init__(self, *args, **kwargs) -> None: ...

class CorrespondenceCheckerBasedOnEdgeLength(CorrespondenceChecker):
    similarity_threshold: float
    def __init__(self, *args, **kwargs) -> None: ...

class CorrespondenceCheckerBasedOnNormal(CorrespondenceChecker):
    normal_angle_threshold: float
    def __init__(self, *args, **kwargs) -> None: ...

class ICPConvergenceCriteria:
    max_iteration: int
    relative_fitness: float
    relative_rmse: float
    @overload
    def __init__(self, other: ICPConvergenceCriteria) -> None: ...
    @overload
    def __init__(
        self,
        relative_fitness: float = 1e-06,
        relative_rmse: float = 1e-06,
        max_iteration: int = 30,
    ) -> None: ...

class PoseGraphEdge:
    confidence: float
    information: NDArray[float64]
    source_node_id: int
    target_node_id: int
    transformation: NDArray[float64]
    uncertain: bool
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PoseGraphEdge) -> None: ...
    @overload
    def __init__(
        self,
        source_node_id: int = -1,
        target_node_id: int = -1,
        transformation: NDArray[float64] = ...,
        information: NDArray[float64] = ...,
        uncertain: bool = False,
        confidence: float = 1.0,
    ) -> None: ...

class PoseGraphEdgeVector:
    def __init__(self, *args, **kwargs) -> None: ...
    def __getitem__(self, key) -> PoseGraphEdge: ...
    def __setitem__(self, key, value: PoseGraphEdge) -> PoseGraphEdgeVector: ...
    def append(self, x: float) -> None: ...
    def clear(self) -> None: ...
    def extend(self, L: Union[PoseGraphEdgeVector, Iterable]) -> None: ...
    def insert(self, i: int, x: PoseGraphEdge) -> None: ...
    def pop(self, i: Optional[int]) -> PoseGraphEdge: ...

class PoseGraphNode:
    pose: NDArray[float64]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: PoseGraphNode) -> None: ...
    @overload
    def __init__(
        self,
        pose: NDArray[float64],
    ) -> None: ...

class PoseGraphNodeVector:
    def __init__(self, *args, **kwargs) -> None: ...
    def __getitem__(self, key) -> PoseGraphNode: ...
    def __setitem__(self, key, value: PoseGraphNode) -> PoseGraphNodeVector: ...
    def append(self, x: float) -> None: ...
    def clear(self) -> None: ...
    def extend(self, L: Union[PoseGraphNodeVector, Iterable]) -> None: ...
    def insert(self, i: int, x: PoseGraphNode) -> None: ...
    def pop(self, i: Optional[int]) -> PoseGraphNode: ...

class PoseGraph:
    edges: List[PoseGraphEdge]
    nodes: List[PoseGraphNode]
    def __init__(self, *args, **kwargs) -> None: ...

class FastGlobalRegistrationOption:
    decrease_mu: bool
    division_factor: float
    iteration_number: int
    maximum_correspondence_distance: float
    maximum_tuple_count: float
    tuple_scale: float
    use_absolute_scale: bool
    @overload
    def __init__(self, other: FastGlobalRegistrationOption) -> None: ...
    @overload
    def __init__(
        self: FastGlobalRegistrationOption,
        division_factor: float = 1.4,
        use_absolute_scale: bool = False,
        decrease_mu: bool = False,
        maximum_correspondence_distance: float = 0.025,
        iteration_number: int = 64,
        tuple_scale: float = 0.95,
        maximum_tuple_count: int = 1000,
    ) -> None: ...

class RANSACConvergenceCriteria:
    confidence: float
    max_iteration: int
    @overload
    def __init__(self, other: RANSACConvergenceCriteria) -> None: ...
    @overload
    def __init__(
        self, max_iteration: int = 100000, confidence: float = 0.999
    ) -> None: ...

class RegistrationResult:
    correspondence_set: NDArray[int32]
    fitness: float
    inlier_rmse: float
    transformation: NDArray[float64]
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, other: RegistrationResult) -> None: ...
