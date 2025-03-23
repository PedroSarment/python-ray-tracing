from color import Color
from phong import Phong
from ray import Ray
import numpy as np

class Render: 
    @staticmethod
    def render(ray, objects, lights, depth=0, max_depth=3) -> Color:
        if depth > max_depth:
            return Color(0, 0, 0)

        closest_t = float('inf')
        hit_result = None

        for obj in objects:
            hit = obj.intersect(ray)
            if hit and hit.t < closest_t:
                closest_t = hit.t
                hit_result = hit

        if hit_result is None:
            return Color(0, 0, 0)

        view_dir = (ray.origin - hit_result.hit_point).normalize()

        local_color = Phong.phong_illumination(
            hit_point=hit_result.hit_point,
            normal=hit_result.normal,
            view_dir=view_dir,
            material=hit_result.material,
            scene_lights=lights,
            objects=objects
        )

        reflected_color = Color(0, 0, 0)
        if hit_result.material.kr.magnitude() > 0:
            reflect_dir = ray.direction - hit_result.normal * (2 * ray.direction.dot(hit_result.normal))
            reflect_ray = Ray(hit_result.hit_point + hit_result.normal * 1e-4, reflect_dir.normalize())
            reflected_color = Render.render(reflect_ray, objects, lights, depth + 1, max_depth)
            reflected_color = reflected_color * hit_result.material.kr

        refracted_color = Color(0, 0, 0)
        if hit_result.material.kt.magnitude() > 0:
            ior_i = 1.0
            ior_t = getattr(hit_result.material, "ni", 1.5)
            n = hit_result.normal
            cosi = -ray.direction.dot(n)

            if cosi < 0:
                cosi = -cosi
                n = n * -1
                ior_i, ior_t = ior_t, ior_i

            eta = ior_i / ior_t
            k = 1 - eta ** 2 * (1 - cosi ** 2)
            if k >= 0:
                refract_dir = ray.direction * eta + n * (eta * cosi - np.sqrt(k))
                refract_ray = Ray(hit_result.hit_point - n * 1e-4, refract_dir.normalize())
                refracted_color = Render.render(refract_ray, objects, lights, depth + 1, max_depth)
                refracted_color = refracted_color * hit_result.material.kt

        final_color = (local_color + reflected_color + refracted_color).clip()
        return final_color