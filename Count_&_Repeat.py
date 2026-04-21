class Repeater:
    def repeat(self):
        word = input("Enter a word: ")
        rep = int(input("How many times? "))

        for i in range(rep):
            print(word)

rep = Repeater()
rep.repeat()