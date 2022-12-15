from django.urls import reverse
from rest_framework.test import APITestCase
from django.test import TestCase


class MatrixTests(APITestCase):
    def test1_matrix_correct(self):

        url = reverse(viewname='c_vec')
        response = self.client.get(url, data={'size': 2, 'matrix': '-1_-6*2_6'})
        self.assertEqual(response.data, {
            "size": 2,
            "matrix": [[-1.0, -6.0], [2.0, 6.0]],
            "count": [2.0, 3.0],
            "vec": [[-0.894, 0.832], [0.447, -0.555]]
        })
    def test2_matrix_correct(self):

        url = reverse(viewname='c_vec')
        response = self.client.get(url, data={'size': 2, 'matrix': '-1_-6*2_6'})
        self.assertEqual(response.data, {
            "size": 2,
            "matrix": [[-1.0, -6.0], [2.0, 6.0]],
            "count": [2.0, 3.0],
            "vec": [[-0.894, 0.832], [0.447, -0.555]]
        })
