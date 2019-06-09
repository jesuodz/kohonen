import numpy as np
import itertools

class SOM:
    def __init__(self, h, w, dim):
        """
            Construccion de una SOM rellena de zeros.
            h, w, dim: Construye una (h, w, dim) SOM.
        """
        self.shape = (h, w, dim)
        self.som = np.zeros((h, w, dim))

        # Parametros de entrenamiento
        self.L0 = 0.0
        self.lam = 0.0
        self.sigma0 = 0.0

    def train(self, data, l0, lam, sigma0, initializer=np.random.rand):
        """
            Procedimiento de entrenamiento para una SOM.
            data: matriz N*d, N el numero de ejemplos,
                  d lo mismo que dim=self.shape[2].
            L0, lam, sigma0: parametros de entrenamiento.
        """
        self.l0 = l0
        self.lam = lam
        self.sigma0 = sigma0

        self.som = initializer(*self.shape)

        for t in itertools.count():
            if self.sigma(t) < 1.0: break

            i_data = np.random.choice(range(len(data)))

            bmu = self.find_bmu(data[i_data])
            self.update_bmu(bmu, data[i_data], t)
        self.data = data

    def find_bmu(self, input_vec):
        """
            Encuentra el BMU dado un vector de entrada.
            input_vec: un d=dim=self.shape[2] vector de entrada.
        """
        list_bmu = []
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                dist = np.linalg.norm((input_vec-self.som[y,x]))
                list_bmu.append(((y,x), dist))
        list_bmu.sort(key=lambda x: x[1])
        return list_bmu[0][0]

    def update_som(self, bmu, input_vector, t):
        """
            Llama la regla de actualizacion para cada celula.
            bmu: (y, x) coordenadas.
            input_vector: vector de entrada actual.
            t: tiempo actual.
        """
        for y in range(self.shape[0]):
            for x in range(self.shape[1]):
                dist_to_bmu = np.linalg.norm((np.array(bmu) - np.array((y, x))))
                self.update_cell((y, x), dist_to_bmu, input_vector, t)

    def update_cell(self, cell, dist_to_bmu, input_vector, t):
        """
            Computa la regla de actualizacion en una celula.
            cell: (y, x) coordenadas
            dist_to_bmu: L2 distancia de la celula al bmu.
            input_vector: vector de entrada actual.
            t: tiempo actual.
        """
        self.som[cell] += self.N(dist_to_bmu, t) * self.L(t) * (input_vector-self.som[cell])

    def N(self,dist_to_bmu, t):
        """
            Computa la penalizacion vecina
            dist_to_bmu: L2 distancia al bmu.
            t: tiempo actual.
        """
        curr_sigma = self.sigma(t)
        return np.exp(-(dist_to_bmu**2) / (2*curr_sigma**2))

    def sigma(self, t):
        """
            Formula de radio vecino.
            t: tiempo actual.
        """
        return self.sigma0*np.exp(-t/self.lam)

    def update_bmu(self, bmu, input_vector, t):
        """
            Actualiza la regla para el BMU.
            bmu: Coordenadas (y, x)
            input_vector: vector de data actual
            t: tiempo actual
        """
        self.som[bmu] += self.L(t) * (input_vector-self.som[bmu])

    def L(self, t):
        """
            Formula de ratio de aprendizaje
            t: tiempo actual
        """
        return self.L0*np.exp(-t/self.lam)

    def quant_err(self):
        """
            Computa el error cuatizado de la som.
            Usa la data del ultimo entrenamiento
        """
        bmu_dists = []
        for input_vector in self.data:
            bmu = self.find_bmu(input_vector)
            bmu_feat = self.som[bmu]
            bmu_dists.append(np.linalg.norm(input_vector - bmu_feat))
        return np.array(bmu_dists).mean()

# square_data = np.random.rand(5000, 2)
# som_square = SOM(20, 20, 2)
# som_square.train(square_data, l0=0.8, lam=1e2, sigma0=10)

color_data = np.random.rand(3,3)
som_color = SOM(40, 40, 3)
som_color.train(color_data, l0=0.8,lam=1e2, sigma0=20)
print(som_color.som)
