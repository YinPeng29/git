# -*-coding:utf-8-*-
#!/usr/bin/env python

import sys
from NoteBook_Progarme.notebook import Note,Notebook
#这里不可以使用,相对导入语句导入,因为我们还没有把我们的代码放到一个包里,仅仅是放在了一个文件夹里

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1":self.show_notes,
            "2":self.search_notes,
            "3":self.add_note,
            "4":self.modify_note,
            "5":self.quit
        }

    def display_menu(self):
        print("""
            Notebook Menu:
            1. Show all Notes
            2. Search Notes
            3. Add Note
            4. Modify note
            5. Quit
            """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)   # action 实际上指向一个特定的方法
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))

    def show_notes(self,notes=None):
        if not notes:
            notes = self.notebook.notes
            if not notes:
                print("Sorry don't have any notes!")
        for note in notes:
            print("id:{0}\ntag:{1}\nmemo:{2}".format(note.id,note.tags,note.memo))


    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        if not notes:
            print("Can't search any notes,may be it is empty ")
        else:
            self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        tags = input("Enter a tags: ")
        self.notebook.new_note(memo,tags=tags)
        print("Your notes has been added.")


    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter a tags: ")
        if memo:
            self.notebook.modify_memo(id,memo)
        if tags:
            self.notebook.modify_tags(id,tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__=='__main__':
    Menu().run()


