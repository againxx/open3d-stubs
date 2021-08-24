from enum import Enum
from typing import overload
from numpy import float64
from numpy.typing import NDArray
from .. import geometry, camera, utility

class TSDFVolumeColorType(Enum):
    Gray32 = ...
    NoColor = ...
    RGB8 = ...

class TSDFVolume:
    color_type: TSDFVolumeColorType
    sdf_trunc: float
    voxel_length: float
    def __init__(self, *args, **kwargs) -> None: ...
    def extract_point_cloud(self) -> geometry.PointCloud: ...
    def extract_triangle_mesh(self) -> geometry.TriangleMesh: ...
    def integrate(
        self,
        image: geometry.RGBDImage,
        intrinsic: camera.PinholeCameraIntrinsic,
        extrinsic: NDArray[float64],
    ) -> None: ...
    def reset(self) -> None: ...

class ScalableTSDFVolume(TSDFVolume):
    @overload
    def __init__(self, other: ScalableTSDFVolume) -> None: ...
    @overload
    def __init__(
        self,
        voxel_length: float,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
        volume_unit_resolution: int = 16,
        depth_sampling_stride: int = 4,
    ) -> None: ...
    def extract_voxel_point_cloud(self) -> geometry.PointCloud: ...

class UniformTSDFVolume(TSDFVolume):
    length: float
    resolution: int
    @overload
    def __init__(self, other: UniformTSDFVolume) -> None: ...
    @overload
    def __init__(
        self,
        length: float,
        resolution: int,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
    ) -> None: ...
    @overload
    def __init__(
        self,
        length: float,
        resolution: int,
        sdf_trunc: float,
        color_type: TSDFVolumeColorType,
        origin: NDArray[float64],
    ) -> None: ...
    def extract_volume_color(self) -> utility.Vector3dVector: ...
    def extract_volume_tsdf(self) -> utility.Vector2dVector: ...
    def extract_voxel_grid(self) -> geometry.VoxelGrid: ...
    def extract_voxel_point_cloud(self) -> geometry.PointCloud: ...
