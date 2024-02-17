import requests
import pygame
import sys
import os
import asyncio
import aiohttp
import math

class MapParams(object):
    def __init__(self):
        self.lat = 55.75482
        self.lon = 37.62169
        self.zoom = 16
        self.type = "map"
        self.my_step = 0.003
        self.marker_file = None
        self.markers_updated = False

    def update(self, event):
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

    def ll(self):
        return str(self.lon) + "," + str(self.lat)

    def update_marker_file(self, marker_file):
        self.marker_file = marker_file
        self.markers_updated = True

def load_map(mp):
    map_request = f"http://static-maps.yandex.ru/1.x/?ll={mp.ll()}&z={mp.zoom}&l={mp.type}"
    if mp.marker_file:
        map_request += f"&pt={mp.ll()},pm2rdm~{mp.ll()},pm2grm"
    response = requests.get(map_request)
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

async def add_markers(mp):
    red_square_coordinates = get_coordinates_by_address('Москва, Красная площадь')
    if red_square_coordinates:
        marker_request = f"&pt={red_square_coordinates[0]},{red_square_coordinates[1]},pm2rdm"
        map_request = f"http://static-maps.yandex.ru/1.x/?ll={mp.ll()}&z={mp.zoom}&l={mp.type}{marker_request}"
        async with aiohttp.ClientSession() as session:
            async with session.get(map_request) as response:
                content = await response.read()
                map_file = "map_with_marker.png"
                with open(map_file, "wb") as file:
                    file.write(content)
                mp.update_marker_file(map_file)

    metro_stations = ['Библиотека имени Ленина', 'Арбатская', 'Тверская', 'Маяковская', 'Пушкинская']
    for station in metro_stations:
        coordinates = get_coordinates_by_address(f'Москва, метро {station}')
        if coordinates:
            marker_request = f"&pt={coordinates[0]},{coordinates[1]},pm2grm"
            map_request = f"http://static-maps.yandex.ru/1.x/?ll={mp.ll()}&z={mp.zoom}&l={mp.type}{marker_request}"
            async with aiohttp.ClientSession() as session:
                async with session.get(map_request) as response:
                    content = await response.read()
                    map_file = f"map_with_marker_{station.replace(' ', '_')}.png"
                    with open(map_file, "wb") as file:
                        file.write(content)
                    mp.update_marker_file(map_file)

def get_coordinates_by_address(address):
    api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"
    geocode_url = 'https://geocode-maps.yandex.ru/1.x/'


    params = {
        'apikey': api_key,
        'format': 'json',
        'geocode': address
    }

    response = requests.get(geocode_url, params=params)
    data = response.json()

    if 'response' in data and 'GeoObjectCollection' in data['response']:
        features = data['response']['GeoObjectCollection']['featureMember']
        if features:
            coordinates_str = features[0]['GeoObject']['Point']['pos']
            return tuple(map(float, coordinates_str.split()))

    return None

def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 450))
    mp = MapParams()
    clock = pygame.time.Clock()
    FPS = 60
    map_file = None
    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
                break
            elif event.type == pygame.KEYDOWN:
                mp.update(event)

        if mp.markers_updated:
            asyncio.run(add_markers(mp))
            mp.markers_updated = False

        map_file = load_map(mp)
        screen.blit(pygame.image.load(map_file), (0, 0))
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    if map_file is not None:
        os.remove(map_file)

if __name__ == '__main__':
    main()
