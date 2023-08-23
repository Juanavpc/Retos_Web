def cost_parking(day_of_week, parking_time):
    rate = 0

    if (day_of_week == 'Lunes' or day_of_week == 'Martes' or day_of_week == 'Miercoles'):
        rate = 2.00
    elif (day_of_week == 'Jueves' or day_of_week == 'Viernes'):
        rate = 2.50
    elif (day_of_week == 'Sabado' or day_of_week == 'Domingo'):
        rate = 3.00
    else:
        print('Día de la semana incorrecto')
        return
    
    hour = int(parking_time)
    minutes = int((parking_time - hour) * 60)

    if minutes > 0:
        hour += 1
    
    total_cost = rate * hour
    return total_cost

day = input('Ingrese el día de la semana: ')
time = float(input('Ingrese el tiempo estacionado: '))

cost = cost_parking(day, time)
if cost > 0:
    print(f'El costo de estacionamiento es: ${cost: .2f}')