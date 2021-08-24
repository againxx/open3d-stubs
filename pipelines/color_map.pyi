from typing import List
from .. import geometry, camera

class NonRigidOptimizerOption:
    def __init__(
        self,
        number_of_vertical_anchors: int = 16,
        non_rigid_anchor_point_weight: float = 0.316,
        maximum_iteration: int = 0,
        maximum_allowable_depth: float = 2.5,
        depth_threshold_for_visibility_check: float = 0.03,
        depth_threshold_for_discontinuity_check: float = 0.1,
        half_dilation_kernel_size_for_discontinuity_map: int = 3,
        image_boundary_margin: int = 10,
        invisible_vertex_color_knn: int = 3,
        debug_output_dir: str = "",
    ) -> None: ...

class RigidOptimizerOption:
    def __init__(
        self,
        maximum_iteration: int = 0,
        maximum_allowable_depth: float = 2.5,
        depth_threshold_for_visibility_check: float = 0.03,
        depth_threshold_for_discontinuity_check: float = 0.1,
        half_dilation_kernel_size_for_discontinuity_map: int = 3,
        image_boundary_margin: int = 10,
        invisible_vertex_color_knn: int = 3,
        debug_output_dir: str = "",
    ) -> None: ...

def run_non_rigid_optimizer(
    arg0: geometry.TriangleMesh,
    arg1: List[geometry.RGBDImage],
    arg2: camera.PinholeCameraTrajectory,
    arg3: NonRigidOptimizerOption,
) -> geometry.TriangleMesh: ...

def run_rigid_optimizer(
    arg0: geometry.TriangleMesh,
    arg1: List[geometry.RGBDImage],
    arg2: camera.PinholeCameraTrajectory,
    arg3: RigidOptimizerOption,
) -> geometry.TriangleMesh: ...
