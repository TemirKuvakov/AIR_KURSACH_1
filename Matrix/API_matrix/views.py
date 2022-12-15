from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import MatrixVector
from .serializers import MatrixSerializer
from drf_spectacular.utils import extend_schema, OpenApiParameter, OpenApiExample



# Create your views here.
class MatrixVectorView(APIView):

    @extend_schema(
        request={400: str, 200: MatrixSerializer},
        responses={400: str, 200: MatrixSerializer},
        methods=["GET"]
    )
    @extend_schema(
        parameters=[
            OpenApiParameter(name='size', location=OpenApiParameter.QUERY,
                             description='matrix size', required=True, type=int),
            OpenApiParameter(name='matrix', location=OpenApiParameter.QUERY,
                             description='matrix', required=True,
                             examples=[OpenApiExample('2x2 matrix', value='1_2*3_4'),
                                       OpenApiExample('3x3 matrix', value='1_2_3*4_5_6*9_4_2')])
        ],
        description='Calculates inverse matrix',
        examples=[OpenApiExample('2x2 matrix',
                                 value=MatrixSerializer(
                                     instance=MatrixVector(2, [[1, 2], [2, 1]], [1, 2], [[-0.33, 0.66], [0.66, -0.33]])).data,
                                 response_only=True,
                                 status_codes=[200]
                                 ),
                  OpenApiExample('No size',
                                 value='Размер не указан',
                                 response_only=True,
                                 status_codes=[400]
                                 ),
                  OpenApiExample('Invalid matrix',
                                 value='Матрица неверного размера',
                                 response_only=True,
                                 status_codes=[400]
                                 )
                                ]
    )
    def get(self, request):
        size = request.GET.get('size', None)

        if size is None:
            return Response('Размер не указан', 400)

        try:
            size = int(size)
        except:
            return Response('Размер не число', 400)

        if size <= 0:
            return Response('Размер меньше или равен 0', 400)

        matrix = request.GET.get('matrix', None)

        if matrix is None:
            return Response('Матрица не указана', 400)

        matrix = matrix.split('*')

        new_matrix = []

        if len(matrix) != size:
            return Response('Матрица неверного размера', 400)

        for row in matrix:
            try:
                row = list(map(float, row.split('_')))
            except:
                return Response('В матрице содержатся недопустимые значения', 400)

            if len(row) != size:
                return Response('Неверный размер строки в матрице', 400)

            new_matrix.append(row)

        new_matrix = np.array(new_matrix)

        try:
            r, b = np.linalg.eig(new_matrix)
        except np.linalg.LinAlgError as e:
            return Response("Определитель матрицы равен нулю", 400)

        for row in b:
            for i in range(len(row)):
                row[i] = round(row[i], 3)

        matrixVector = MatrixVector(size, new_matrix, r, b)
        serializer_for_request = MatrixSerializer(instance=matrixVector)
        return Response(serializer_for_request.data, 200)

