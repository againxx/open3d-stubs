from typing import Dict
from numpy import float32
from numpy.typing import NDArray
from .. import geometry

class MaterialRecord:
    absorption_color: NDArray[float32]
    absorption_distance: float
    albedo_img: geometry.Image
    anisotropy_img: geometry.Image
    ao_img: geometry.Image
    ao_rough_metal_img: geometry.Image
    aspect_ratio: float
    base_anisotropy: float
    base_clearcoat: float
    base_clearcoat_roughness: float
    base_color: NDArray[float32]
    base_metallic: float
    base_reflectance: float
    base_roughness: float
    clearcoat_img: geometry.Image
    clearcoat_roughness_img: geometry.Image
    generic_imgs: Dict[str, geometry.Image]
    generic_params: Dict[str, NDArray[float32]]
    gradient: Gradient
    ground_plane_axis: float
    has_alpha: bool
    line_width: float
    metallic_img: geometry.Image
    normal_img: geometry.Image
    point_size: float
    reflectance_img: geometry.Image
    roughness_img: geometry.Image
    sRGB_color: bool
    scalar_max: float
    scalar_min: float
    shader: str
    thickness: float
    transmission: float
    def __init__(self) -> None: ...
