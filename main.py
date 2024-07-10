import view, model, controller

print("""
b - вылет самолетиков
m - включить маршрутизатор
  клавиши влево/вправо/вверх/вниз на NumPad - движение выделенной точки
  + на NumPad - добавление новой точки
  0 - удалить все точки
  s - запуск самолетика по маршруту
  
TAB - режим отладки
""")

while True:
    view.risovanie()
    controller.control()
