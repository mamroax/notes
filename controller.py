from model import NoteBook


class Controller:
    def __init__(self):
        self.flag = True
        self.notebook = NoteBook()

    def __istructions(self):
        print("create - создать заметку\n read - прочитать заметку\n"
              "update - изменить заметку\n delete - удалить заметку\n"
              "exit - выйти из программы")

    def run(self):
        while (self.flag):
            comand = input("Введите команду: \n")
            if comand == "create":
                title = input("Введите заголовок заметки:\n ")
                text = input("Введите текст заметки:\n ")
                self.notebook.create_note(title, text)
            elif comand == "read":
                id = input("Введите id заметки:\n ")
                self.notebook.read_note(id)
            elif comand == "update":
                id = input("Введите id заметки:\n ")
                title = input("Введите заголовок заметки:\n ")
                text = input("Введите текст заметки:\n ")
                self.notebook.update_note(id, title, text)
            elif comand == "delete":
                id = input("Введите id заметки:\n ")
                self.notebook.delete_note(id)
            elif comand == "exit":
                self.flag = False
            else:
                self.__istructions()
