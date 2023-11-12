import datetime
import json
import os


class NoteBook:
    def __init__(self):
        self.id = 0  # при создании редактора заметок начинается нумерация самих заметок
        self.note_id_list = []

    def create_note(self, title, text):
        self.id += 1
        self.note_id_list.append(self.id)
        note = Note(self.id, title, text)  # создадим заметку
        # создаем json файл
        self.__save_note(note)
        print("Заметка создана")

    def __save_note(self, note):
        # сохраняется заметка
        with open(f"JSON/note_{note.get_id()}.json", "w") as write_file:
            json.dump(note.get_title() + ";", write_file)
            json.dump(note.get_text() + ";", write_file)
            json.dump(str(note.get_date()) + ";", write_file)

    def read_note(self, id):
        if int(id) in self.note_id_list:
            with open(f"JSON/note_{id}.json", "r") as read_file:
                data = json.load(read_file)
                print(data)
        else:
            print("Нет такой заметки")


    def update_note(self, id, title, text):
        if int(id) in self.note_id_list:
            os.remove(f"JSON/note_{id}.json")
            self.note_id_list.pop(id)
            note = Note(id, title, text)  # создадим заметку
            # создаем json файл
            self.__save_note(note)
            print("Заметка обновлена")
        else:
            print("Нет такой заметки")


    def delete_note(self, id):
        if int(id) in self.note_id_list:
            os.remove(f"JSON/note_{id}.json")
            self.note_id_list.pop(id)
            print("Заметка удалена")
        else:
            print("Нет такой заметки")


class Note:
    def __init__(self, id, title, text):
        self.__id = id
        self.__title = title
        self.__text = text
        self.__date = datetime.datetime.now()

    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_text(self):
        return self.__text

    def get_date(self):
        return self.__date

    def set_title(self, title):
        self.__title = title

    def set_text(self, text):
        self.__text = text

    def set_date(self):
        self.__date = datetime.datetime.now()
