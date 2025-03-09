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
        """
        Gera um raio que passa pelo pixel (i, j) da tela.
        
        O método calcula a posição exata do pixel no plano da câmera
        e determina a direção do raio a partir da posição da câmera.
        
        Parâmetros:
        i (int): Coordenada horizontal do pixel.
        j (int): Coordenada vertical do pixel.
        
        Retorna:
        Ray: Um objeto representando o raio gerado.
        """
        # Determina o centro do plano da tela no espaço 3D
        screen_center = self.position - (self.w * self.d)
        
        # Calcula a posição exata do pixel no plano da tela
        pixel_position = (screen_center +
                          self.u * ((i - self.h_res / 2) / self.h_res) +
                          self.v * ((j - self.v_res / 2) / self.v_res))
                          
        # Determina a direção do raio normalizando o vetor que parte da câmera para o pixel
        direction = (pixel_position - self.position).normalize()
        return Ray(self.position, direction)

