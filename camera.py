from ray import Ray


class Camera:
    def __init__(self, position, look_at, up_vector, d, h_res, v_res):
        self.position = position
        self.look_at = look_at
        self.up_vector = up_vector.normalize()
        self.d = d
        self.h_res = h_res
        self.v_res = v_res
        
        self.w = (position - look_at).normalize()
        self.u = self.up_vector.cross(self.w).normalize()
        self.v = self.w.cross(self.u)

    def get_ray(self, i, j):
        screen_center = self.position - (self.w * self.d)
        pixel_position = (screen_center +
                          (i - self.h_res / 2) * (self.u / self.h_res) +
                          (j - self.v_res / 2) * (self.v / self.v_res))
        direction = (pixel_position - self.position).normalize()
        return Ray(self.position, direction)
