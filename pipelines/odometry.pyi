from typing import Tuple
from numpy import float64
from numpy.typing import NDArray
from .. import geometry, camera, utility

class OdometryOption:
    iteration_number_per_pyramid_level: utility.IntVector
    max_depth: float
    max_depth_diff: float
    min_depth: float
    def __init__(
        self,
        iteration_number_per_pyramid_level: utility.IntVector = ...,
        max_depth_diff: float = 0.03,
        min_depth: float = 0.0,
        max_depth: float = 4.0
    ) -> None: ...

class RGBDOdometryJacobian:
    def __init__(self, *args, **kwargs) -> None: ...

class RGBDOdometryJacobianFromColorTerm(RGBDOdometryJacobian):
    def __init__(self, *args, **kwargs) -> None: ...

class RGBDOdometryJacobianFromHybridTerm(RGBDOdometryJacobian):
    def __init__(self, *args, **kwargs) -> None: ...

def compute_rgbd_odometry(
    rgbd_source: geometry.RGBDImage,
    rgbd_target: geometry.RGBDImage,
    pinhole_camera_intrinsic: camera.PinholeCameraIntrinsic = ...,
    odo_init: NDArray[float64] = ...,
    jacobian: RGBDOdometryJacobian = RGBDOdometryJacobianFromHybridTerm(),
    option: OdometryOption = ...,
) -> Tuple[bool, NDArray[float64], NDArray[float64]]: ...
