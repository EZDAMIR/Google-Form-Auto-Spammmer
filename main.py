import requests
import random
import threading


#URL of google form page
GoogleURL = "https://docs.google.com/forms/d/e/1FAIpQLSeRk-OZGhqcIImy6aQdIvTd7_TOZB1HaUnazu1gFMUdRnD7aw"

urlResponse = GoogleURL + "/formResponse"
urlReferer = GoogleURL + "/viewForm"

#IDs of entries can be found in console after sumbitting the form.
#Example of data that will be entered
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
             'entry.2049345275': ['Да', 'Нет'],}

# Number of threads you want to run(Do not use too many thread)
num_threads = 60
chunks_per_thread =10000

threads = []

count = 0


def submit_form(chunks_per_thread):
    global count
    user_agent = {'Referer': urlReferer,
                  'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
    for _ in range(chunks_per_thread):
        random_form_data = {key: random.choice(values) for key, values in form_data.items()}
        r = requests.post(urlResponse, data=random_form_data, headers=user_agent)
        count+=1
        print(count)


# create and start the threads
for _ in range(num_threads):
    thread = threading.Thread(target=submit_form, args=(chunks_per_thread,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("All threads completed.")