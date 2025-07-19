from color import Color
from ray import Ray
from vector import Vector

class Phong:

    @staticmethod
    def phong_illumination(hit_point, normal, view_dir, material, scene_lights, objects):
        ka = material.ka
        kd = material.kd
        ks = material.ks
        ns = material.ns 

        N = normal.normalize()
        V = view_dir.normalize()

        ambient_intensity = Vector(*scene_lights.ambient)
        color = ka * (ambient_intensity / 255)

        for light in scene_lights.lights:
            #Direção da Luz 
            L = (light.position - hit_point).normalize()
            
            #Direção do Observador
            R = ((N * 2 * N.dot(L)) - L).normalize()

            shadow_origin = hit_point + N * 1e-3
            shadow_ray = Ray(shadow_origin, L)
            in_shadow = any(
                (inter := obj.intersect(shadow_ray)) and inter.t > 1e-3
                for obj in objects
            )
            if in_shadow:
                continue

            light_intensity = Vector(*light.intensity)

            diff = max(N.dot(L), 0)
            diffuse = kd * (light_intensity / 255) * diff

            spec = max(V.dot(R), 0) ** ns
            specular = ks * (light_intensity / 255) * spec

            color += diffuse + specular

        final_r = min(max(int(color.x * 255), 0), 255)
        final_g = min(max(int(color.y * 255), 0), 255)
        final_b = min(max(int(color.z * 255), 0), 255)

        return Color(final_r, final_g, final_b)