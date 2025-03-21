from ray import Ray
import numpy as np

class Phong:
    
    @staticmethod
    def phong_illumination(hit_point, normal, view_dir, material, scene_lights, objects):

        color = material.ka * scene_lights.ambient

        for light in scene_lights.lights:
            light_dir = (light.position - hit_point).normalize()

            shadow_ray = Ray(hit_point + normal * 1e-4, light_dir)
            in_shadow = any(obj.intersect(shadow_ray) for obj in objects)

            if in_shadow:
                continue 

            diff_intensity = max(normal.dot(light_dir), 0)
            diffuse = material.kd * light.intensity * diff_intensity

            reflect_dir = ((normal * normal.dot(light_dir) * 2) - light_dir).normalize()
            spec_intensity = max(view_dir.dot(reflect_dir), 0) ** material.eta
            specular = material.ks * light.intensity * spec_intensity

            color += diffuse + specular

        return np.clip(color, 0, 255).astype(np.uint8)
