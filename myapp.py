from music_recommendations import recommend_music

def main():
    print("Добро пожаловать в музыкального бота-помощника!")
    
    while True:  # Основной цикл для возврата к выбору услуги
        print("\nПожалуйста, выберите услугу:")
        print("1. Рекомендация музыки по жанру")
        print("2. Выход")
        
        choice = input("Введите номер услуги (1 или 2): ")
        
        if choice == "1":
            recommend_music()
        elif choice == "2":
            print("До свидания! Возвращайтесь за новыми рекомендациями!")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите 1 или 2.")

if __name__ == "__main__":
    main()