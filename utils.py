
import json


#Открыть JSON файл
def read_json_file(data_json):
    with open(data_json, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data


#Функция поиска постов по слову
def load_posts(search_word, all_posts):
    posts = []
    for i in all_posts:
        if search_word in i["content"]:
            posts.append(i)
    return posts


#Функция добавления нового поста в JSON файл
def load_new_post(load_data_json, data_js, file_json):
    data_js.append(load_data_json)
    with open(file_json, 'w', encoding='utf-8') as f:
        json.dump(data_js, f, ensure_ascii=False, indent=4)


#Функция проверки расщирения файла
def check_extension(array_extension, extension):
    if extension.lower() in array_extension:
        return True
    return False


