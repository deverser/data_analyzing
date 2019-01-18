from die import Die
import pygal


# Создание двух кубиков D6 и D10
die_1 = Die()
die_2 = Die()

# Моделирование серии бросков с сохранением результатов в списке
results = [die_1.roll() * die_2.roll() for roll_num in range(50000)]

# print(results)
# Анализ результатов
max_result = die_1.num_sides * die_2.num_sides
frequencies = [results.count(value) for value in range(1, max_result+1)]

# print(frequencies)
# Визуализация результатов
hist = pygal.Bar()
dice = 'D' + str(die_1.num_sides) + ' * ' + 'D' + str(die_2.num_sides)
hist.title = 'Results of rolling ' + dice + ' 50,000 times'
hist.x_labels = [str(x) for x in range(1, max_result+1)]
hist.x_title = 'Result'
hist.y_title = 'Frequency of result'

hist.add(dice, frequencies)
hist.render_to_file('dice_visual.svg')
