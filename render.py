from color import Color
from phong import Phong
from ray import Ray
import numpy as np
from vector import Vector

class Render: 
    @staticmethod
    def render(ray, objects, lights, ior_i=1.0, depth=0, max_depth=3) -> Color:
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
        material_kr = Render.calc_kr(hit_result.material, ior_i)
        if material_kr.magnitude() > 0:
            reflect_dir = ray.direction - hit_result.normal * (2 * ray.direction.dot(hit_result.normal))
            reflect_ray = Ray(hit_result.hit_point + hit_result.normal * 1e-4, reflect_dir.normalize())
            reflected_color = Render.render(reflect_ray, objects, lights, ior_i, depth + 1, max_depth)
            reflected_color = reflected_color * material_kr

        refracted_color = Color(0, 0, 0)
        material_kt =  Render.calc_kt(hit_result.material, ior_i)
        if material_kt.magnitude() > 0:
            ior_t = hit_result.material.ni
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
                refracted_color = Render.render(refract_ray, objects, lights, ior_i, depth + 1, max_depth)
                refracted_color = refracted_color * material_kt

        final_color = (local_color + reflected_color + refracted_color).clip()
   
        return final_color
    
    @staticmethod
    def calc_kr(material, ior):
        # Fresnel
        reflectance = min(max(((ior - material.ni) / (ior + material.ni)) ** 2, 0), 1)
        return material.ks * reflectance

    def calc_kt(material, ior):
        transmission = max(0.0, 1.0 - material.d)
        reflectance = ((ior - material.ni) / (ior + material.ni)) ** 2
        kt_scalar = max(0.0, transmission - reflectance)
        
        return Vector(kt_scalar, kt_scalar, kt_scalar)