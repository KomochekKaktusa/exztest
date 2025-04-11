from music_recommendations import recommend_music
from community import get_community_info

def main():
    print("Добро пожаловать в музыкального бота-помощника!")
    
    while True:
        print("\nПожалуйста, выберите услугу:")
        print("1. Рекомендация музыки по жанру")
        print("2. Сообщество по настроению")
        print("3. Выход")
        
        choice = input("Введите номер услуги (1-3): ")
        
        if choice == "1":
            recommend_music()
        elif choice == "2":
            print("\nИнформация о сообществе:")
            print(get_community_info(as_markdown=False))
            input("\nНажмите Enter чтобы вернуться в меню...")
        elif choice == "3":
            print("До свидания! Возвращайтесь за новыми рекомендациями!")
            break
        else:
            print("Неверный ввод. Пожалуйста, введите число от 1 до 3.")

if __name__ == "__main__":
    main()