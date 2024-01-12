class MapParams(object):
    def __init__(self):
        self.lat = 61.665279  # Координаты центра карты на старте. Задал координаты университета
        self.lon = 50.813492
        self.zoom = 16  # Масштаб карты на старте. Изменяется от 1 до 19
        self.type = "map"  # Другие значения "sat", "sat,skl"
        self.my_step = 0.003

    def update(self, event):
        print(event.key)
        if event.key == 1073741899 and self.zoom < 19:  # Page_UP
            self.zoom += 1
        elif event.key == 1073741902 and self.zoom > 2:  # Page_DOWN
            self.zoom -= 1
        elif event.key == 1073741904:  # LEFT_ARROW
            self.lon -= self.my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 1073741903:  # RIGHT_ARROW
            self.lon += self.my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 1073741906 and self.lat < 85:  # UP_ARROW
            self.lat += self.my_step * math.pow(2, 15 - self.zoom)
        elif event.key == 1073741905 and self.lat > -85:  # DOWN_ARROW
            self.lat -= self.my_step * math.pow(2, 15 - self.zoom)

    # Преобразование координат в параметр ll, требуется без пробелов, через запятую и без скобок
    def ll(self):
        return str(self.lon) + "," + str(self.lat)


# Создание карты с соответствующими параметрами.
def load_map(mp):
    map_request = "http://static-maps.yandex.ru/1.x/?ll={ll}&z={z}&l={type}".format(ll=mp.ll(), z=mp.zoom, type=mp.type)
    response = requests.get(map_request)
    if not response:
        print("Ошибка выполнения запроса:")
        print(map_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)

    # Запись полученного изображения в файл.
    map_file = "map.png"
    try:
        with open(map_file, "wb") as file:
            file.write(response.content)
    except IOError as ex:
        print("Ошибка записи временного файла:", ex)
        sys.exit(2)
    return map_file


def main():
  # Инициализируем pygame
  pygame.init()
  screen = pygame.display.set_mode((600, 450))
  mp = MapParams()
  # создание объекта Clock
  clock = pygame.time.Clock()

  # установка FPS
  FPS = 60
  map_file = None
  while True:
      events = pygame.event.get()
      for event in events:
          if event.type == pygame.QUIT: # Выход из программы
              break
          elif event.type == pygame.KEYDOWN: # Обрабатываем различные нажатые клавиши.
              mp.update(event)
              map_file = load_map(mp)

      if map_file is not None:
          # Рисуем картинку, загружаемую из только что созданного файла.
          screen.blit(pygame.image.load(map_file), (0, 0))
          pygame.display.update()

      clock.tick(FPS) # Ограничение FPS

  pygame.quit()
  # Удаляем файл с изображением.
  if map_file is not None:
      os.remove(map_file)



import requests

class MapParams:
   # Your class implementation here

def get_map(params):
   map_request = f"http://static-maps.yandex.ru/1.x/?ll={params.ll()}&z={params.zoom}&l={params.type}"
   response = session.get(map_request)
   if not response:
       print("Ошибка выполнения запроса:")
       print(map_request)
       print("Http статус:", response.status_code, "(", response.reason, ")")
       sys.exit(1)

   map_file = "map.png"
   try:
       with open(map_file, "wb") as file:
           file.write(response.content)
   except IOError as ex:
       print("Ошибка записи временного файла:", ex)
       sys.exit(2)
   return map_file

if __name__ == '__main__':
   session = requests.Session()
   mp = MapParams()
   print(get_map(mp))