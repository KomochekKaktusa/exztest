Community_data = {
    "name:" "Текстовый бот-помощник",
    "description:" "Музыкальное сообщество по настроению. Подбери звучание под свои эмоции!",
    "link:" "https://t.me/kkaktusa"
}

def get_community_info(as_markdown: bool = True) -> str:
    text = f"{Community_data['name']} \n {Community_data['description']} \n\n Ссылка на сообщество - {Community_data['link']}"

print(get_community_info(as_markdown = False))
