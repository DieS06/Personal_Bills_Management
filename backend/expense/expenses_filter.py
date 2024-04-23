from django.db.models import Sum, Q
from .models import Expense
from users.models import User

def expenses_filter(user, init_date, end_date):
    expense = Expense.objects.filter(
        user = user,
        init = init_date,
        end = end_date,
    )

    #if categorias:
    #    expenses = gastos.filter(categoria__in=categorias)
    #return gastos

#def generar_grafico_por_dia(expenses):
    # Implementar la lógica para generar el gráfico por día
#    pass

#def generar_grafico_por_semana(expenses):
    # Implementar la lógica para generar el gráfico por semana
#   pass

#def generar_grafico_por_mes(expenses):
    # Implementar la lógica para generar el gráfico por mes
#   pass

#def generar_grafico_por_año(expenses):
    # Implementar la lógica para generar el gráfico por año
#    pass
