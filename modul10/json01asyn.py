# модуль 10 практика 1.2
from threading import Thread, Event
from turtledemo.penrose import start

import requests
import queue
import pprint
import datetime

if __name__ == '__main__':
    ACCESS_TOKEN = 'CXyFeSBw2lAdG41xkuU3LS6a_nwyxwwCz2dCkUohw-rw0C49x2HqP__6_4is5RPx'
    RANDOM_GENRE_API_URL = 'https://binaryjazz.us/wp-json/genrenator/v1/genre'
    GENIUS_API_URL = 'https://api.genius.com/search'
    GENIUS_URL = 'https://api.genius.com'

    all_songs = []


    class GetGenre(Thread):
        def __init__(self, queue, stop_event):
            self.queue = queue
            self.stop_event = stop_event
            super().__init__()

        def run(self):
            while not stop_event.is_set():
                genre = requests.get(RANDOM_GENRE_API_URL).json()
                self.queue.put(genre)


    class Genius(Thread):
        def __init__(self, queue):
            self.queue = queue
            super().__init__()

        def run(self):
            genre = self.queue.get()
            data = requests.get(GENIUS_API_URL, params={'access_token': ACCESS_TOKEN, 'q': genre})
            data = data.json()
            try:
                song_id = data['response']['hits'][0]['result']['api_path']
                s = f"{GENIUS_URL}{song_id}/apple_music_player"
                # print(s)
                all_songs.append({"": genre, "song": s})
            except IndexError as e:
                self.run()


    start = datetime.datetime.now()
    queue = queue.Queue()
    stop_event = Event()

    genre_list = []
    genius_list = []
    for _ in range(3):
        t = GetGenre(queue, stop_event)
        t.start()
        genre_list.append(t)

    for _ in range(10):
        t = Genius(queue)
        t.start()
        genius_list.append(t)

    for t in genius_list:
        t.join()

    stop_event.set()

    for t in genre_list:
        t.join()

    print(queue.qsize())
    pprint.pprint(all_songs)
    print(len(all_songs))
    print(datetime.datetime.now() - start)

    # разработка не завершена
