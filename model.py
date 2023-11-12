import datetime
import json
import os


class NoteBook:
    def __init__(self):
        try:
            with open(f"JSON/id", "r") as f:
                num = int(f.read())
        except:
            with open(f"JSON/id", "w") as f:
                f.write("1")
                num = 0
        self.id = num  # при создании редактора заметок начинается нумерация самих заметок

    def create_note(self, title, text):
        self.id += 1
        note = Note(self.id, title, text)  # создадим заметку
        # создаем json файл
        self.__save_note(note)
        self.__save_state()
        print("Заметка создана")

    def __save_note(self, note):
        # сохраняется заметка
        with open(f"JSON/note_{note.get_id()}.json", "w") as write_file:
            data = {'title': note.get_title(),
                    'text': note.get_text(),
                    'date': str(note.get_date())}
            json.dump(data, write_file)
    # json.dums(note.get_title(), write_file)
    # json.dump(note.get_text(), write_file)
    # json.dump(str(note.get_date()), write_file)

    def read_note(self, id):
        with open(f"JSON/note_{id}.json", "r") as read_file:
            data = json.load(read_file)
            for k in data:
                print(f"{k}: {data[k]}")

    def update_note(self, id, title, text):
        try:
            os.remove(f"JSON/note_{id}.json")
            self.note_id_list.pop(id)
            note = Note(id, title, text)  # создадим заметку
            # создаем json файл
            self.__save_note(note)
            print("Заметка обновлена")
        except:
            print("Нет такой заметки")

    def delete_note(self, id):
        try:
            os.remove(f"JSON/note_{id}.json")
            self.note_id_list.pop(id)
            print("Заметка удалена")
        except:
            print("Нет такой заметки")

    def __save_state(self):
        os.remove(f"JSON/id")  # удаляем старый файл с сохраненным id
        with open(f"JSON/id", "w") as f:
            f.write(str(self.id))  # записываем новый максимальный id заметки

    # делать выборку по дате
    def print_notes_by_date(self):
        pass

    # выводить на экран весь список записок
    def print_all_notes(self):
        pass

    # При чтении списка заметок реализовать фильтрацию по дате


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
