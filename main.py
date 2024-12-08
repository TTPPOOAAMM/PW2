users = [
    {
        'username': 'user',
        'password': 'user',
        'role': 'user',
        'subscription_type': 'Premium',
        'history': ['Киндер Буэно', 'Judas'],
        'created_at': '2024-01-10'
    },
    {
        'username': 'admin_user',
        'password': 'adminpass',
        'role': 'admin'
    }
]

tracks = [
    {'title': '100 Barz', 'artist': 'Слава КПСС', 'genre': 'Рэп', 'rating': 9.8},
    {'title': 'Киндер Буэно', 'artist': 'Валентин Дядька', 'genre': 'Рэп', 'rating': 9.9},
    {'title': 'Blinding Lights', 'artist': 'The Weeknd', 'genre': 'Поп', 'rating': 9.5},
    {'title': 'Judas', 'artist': 'Lady Gaga', 'genre': 'Поп', 'rating': 9.2}
]

def authenticate():
    username = input("Введите логин: ")
    password = input("Введите пароль: ")
    for user in users:
        if user['username'] == username and user['password'] == password:
            return user
    print("Неверный логин или пароль.")
    return None

def update_profile(user):
    new_password = input("Введите новый пароль: ")
    user['password'] = new_password
    print("Пароль успешно обновлен.")

def view_tracks():
    print("\n--- Доступные треки ---")
    for track in tracks:
        print(f"- {track['title']} ({track['artist']}) - Жанр: {track['genre']}, Рейтинг: {track['rating']}")

def listen_to_track(user):
    view_tracks()
    track_title = input("Введите название трека для прослушивания: ")
    for track in tracks:
        if track['title'] == track_title:
            user.setdefault('history', []).append(track['title'])
            print(f"Вы слушаете: {track_title} от {track['artist']}.")
            return
    print("Трек не найден.")

def view_history(user):
    print("\n--- История прослушиваний ---")
    for track in user.get('history', []):
        print(f"- {track}")

def sort_and_filter_tracks():
    print("\n1. Сортировать по рейтингу")
    print("2. Фильтровать по жанру")
    choice = input("Выберите действие: ")

    if choice == '1':
        sorted_tracks = sorted(tracks, key=lambda x: x['rating'], reverse=True)
        for track in sorted_tracks:
            print(f"{track['title']} - Рейтинг: {track['rating']}")
    elif choice == '2':
        genre = input("Введите жанр для фильтрации: ")
        filtered_tracks = filter(lambda x: x['genre'].lower() == genre.lower(), tracks)
        for track in filtered_tracks:
            print(f"{track['title']} ({track['artist']}) - Жанр: {track['genre']}")
    else:
        print("Некорректный выбор.")

def add_track():
    title = input("Введите название трека: ")
    artist = input("Введите исполнителя: ")
    genre = input("Введите жанр: ")
    rating = float(input("Введите рейтинг трека: "))
    tracks.append({'title': title, 'artist': artist, 'genre': genre, 'rating': rating})
    print("Трек успешно добавлен.")

def delete_track():
    track_title = input("Введите название трека для удаления: ")
    global tracks
    tracks = [track for track in tracks if track['title'] != track_title]
    print("Трек успешно удален.")

def edit_track():
    track_title = input("Введите название трека для редактирования: ")
    for track in tracks:
        if track['title'] == track_title:
            track['artist'] = input("Введите нового исполнителя: ")
            track['genre'] = input("Введите новый жанр: ")
            track['rating'] = float(input("Введите новый рейтинг: "))
            print("Трек успешно обновлен.")
            return
    print("Трек не найден.")

def user_menu(user):
    while True:
        print("\n--- Меню пользователя ---")
        print("1. Просмотр доступных треков")
        print("2. Прослушивание трека")
        print("3. Просмотр истории прослушиваний")
        print("4. Сортировка и фильтрация треков")
        print("5. Обновление профиля")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            view_tracks()
        elif choice == '2':
            listen_to_track(user)
        elif choice == '3':
            view_history(user)
        elif choice == '4':
            sort_and_filter_tracks()
        elif choice == '5':
            update_profile(user)
        elif choice == '6':
            print("Выход из системы...")
            break
        else:
            print("Некорректный выбор.")

def admin_menu(admin):
    while True:
        print("\n--- Меню администратора ---")
        print("1. Добавление трека")
        print("2. Удаление трека")
        print("3. Редактирование трека")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_track()
        elif choice == '2':
            delete_track()
        elif choice == '3':
            edit_track()
        elif choice == '4':
            print("Выход из системы...")
            break
        else:
            print("Некорректный выбор.")

def main():
    print("Добро пожаловать в музыкальный сервис!")
    while True:
        user = authenticate()
        if user:
            if user['role'] == 'user':
                user_menu(user)
            elif user['role'] == 'admin':
                admin_menu(user)

main()
