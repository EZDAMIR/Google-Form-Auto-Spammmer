import requests
import random
import threading

GoogleURL = "https://docs.google.com/forms/d/e/1FAIpQLSeRk-OZGhqcIImy6aQdIvTd7_TOZB1HaUnazu1gFMUdRnD7aw"

urlResponse = GoogleURL + "/formResponse"
urlReferer = GoogleURL + "/viewForm"

form_data = {'entry.595221527': ['Очень Знакомо', 'Немного знакомо',
                                 'Не знакомо'],
             'entry.963201081': ['Очень большая пробелма', 'Своего рода проблема',
                                 'Не большая проблема'],
             'entry.244010941': ["Решительно поддерживаю",
                                 'Частично поддерживаю',
                                 'Нейтрально',
                                 'Скорее против',
                                 'Категорически против'],
             'entry.960844902': ['Очень обеспокоен', 'Немного обеспокоен',
                                 'Не обеспокоен'],
             'entry.1426285918': ['Повышение прозрачности', 'Сокращение возможностей для коррупции',
                                  'Без изменений',
                                  "Не уверен"],
             'entry.2049345275': ['Да', 'Нет']}

# Number of threads you want to run
num_threads = 5
chunks_per_thread = 100

threads = []


def submit_form(chunk):
    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    for _ in range(chunk):
        random_form_data = {key: random.choice(values) for key, values in form_data.items()}
        r = requests.post(urlResponse, data=random_form_data, headers=user_agent)
        print(random_form_data)


# create and start the threads
for _ in range(num_threads):
    thread = threading.Thread(target=submit_form, args=(chunks_per_thread,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed.")