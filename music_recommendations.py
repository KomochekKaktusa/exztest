# База данных рекомендаций по жанрам
music_database = {
    "хардкор панк": [
        "Fugazi - Blueprint",
        "OFF! - What's Next",
        "Black Flag - My War",
        "Descendents - Hope"
    ],
    "построк": [
        "ЖЩ - 2000 ярдов",
        "Slint - Breadcrumb trail",
        "Swans - Helpless Child",
        "Godspeed you! Black Emperor - Sleep"
    ],
    "матрок": [
        "Tiny Moving Parts - Always Focused",
        "Toe - Goodbye",
        "Delta Sleep - Sultans of Ping",
        "Feed Me Jack - Defenitely You"
    ],
    "эмо": [
        "Chinese Football - Electronic girl",
        "Modern Baseball - Tears Over Beers",
        "American Football - Never Meant",
        "Sunny Day Real Estate - In Сircles"
    ]
}

def recommend_music():
    while True:  # Цикл для возможности повторного выбора жанра
        print("\nДоступные музыкальные жанры:")
        genres = list(music_database.keys())
        
        # Выводим жанры через запятую
        print(", ".join(genre.capitalize() for genre in genres))
        print("Или введите 'назад' для возврата в меню")
        
        selected_genre = input("\nВведите название жанра: ").lower()
        
        if selected_genre == 'назад':
            print("\nВозвращаемся в главное меню...\n")
            return  # Выходим из функции и возвращаемся в главное меню
        
        if selected_genre in music_database:
            print(f"\nРекомендуемые {selected_genre} треки:")
            for track in music_database[selected_genre]:
                print(f"- {track}")
            
            # Предлагаем продолжить или вернуться
            print("\nХотите получить другие рекомендации?")
            choice = input("1 - Да, выбрать другой жанр\n2 - Нет, вернуться в меню\nВыбор: ")
            
            if choice == '2':
                print("\nВозвращаемся в главное меню...\n")
                return
            elif choice != '1':
                print("Неверный ввод, возвращаемся в главное меню...\n")
                return
        else:
            print("Жанр не найден. Пожалуйста, введите один из доступных жанров или 'назад'")