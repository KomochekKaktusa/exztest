Community_data = {
    "name": "Текстовый бот-помощник",
    "description": "Музыкальное сообщество по настроению. Подбери звучание под свои эмоции!",
    "link": "https://t.me/kkaktusa"
}

def get_community_info(as_markdown: bool = True) -> str:
    """Возвращает информацию о сообществе в указанном формате"""
    if as_markdown:
        text = (
            f"*{Community_data['name']}*\n\n"
            f"_{Community_data['description']}_\n\n"
            f"[Ссылка на сообщество]({Community_data['link']})"
        )
    else:
        text = (
            f"{Community_data['name']}\n\n"
            f"{Community_data['description']}\n\n"
            f"Ссылка на сообщество: {Community_data['link']}"
        )
    return text

# Тестирование функции
if __name__ == "__main__":
    print("Обычный текст:")
    print(get_community_info(as_markdown=False))
    
    print("\nMarkdown формат:")
    print(get_community_info(as_markdown=True))