from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

# Create your views here.

def vector(request):
    size = request.GET.get('size', None)

    if size is None:
        return HttpResponse('Размер не указан')

    try:
        size = int(size)
    except:
        return HttpResponse('Размер не число')

    if size <= 0:
        return HttpResponse('Размер меньше или равен 0')

    matrix = request.GET.get('matrix', None)

    if matrix is None:
        return HttpResponse('Матрица не указана')

    matrix = matrix.split('*')

    new_matrix = []

    if len(matrix) != size:
        return HttpResponse('Матрица неверного размера')

    for row in matrix:
        try:
            row = list(map(float, row.split('_')))
        except:
            return HttpResponse('В матрице содержатся недопустимые значения')

        if len(row) != size:
            return HttpResponse('Неверный размер строки в матрице')

        new_matrix.append(row)

    new_matrix = np.array(new_matrix)
    r, b = np.linalg.eig(new_matrix)


    new_matrix = '<br/><br/>'.join(['","&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(map(str, row)) for row in new_matrix])
    '''b = '<br/><br/>'.join(['&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'.join(map(str, row)) for row in b])
    b = '<p style=\"font-size:13pt;\">' + b + '</p>' '''
    new_matrix = '<p style=\"font-size:13pt;\">'+new_matrix+'</p>'
    new_matrix = '<h2 style="color:#551e67" ><center> Результаты: </center></h1>' + new_matrix + '<h4><center> Куваков Темир (ИНБО-07-20) </center></h4>'

    return HttpResponse('<br>'f"Собсвтенные числа: {r}"'<br/>'
                        '<br>'f"Собственные векторы: {b}"'<br/>')
