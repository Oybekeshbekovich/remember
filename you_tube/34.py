#MAGIC methods->sehrli usullar ular Dunder usullar orqali ular pythonning ko'plab o'rnatilgan operatsiyalari tomonidan
#avtomatik ravishda chaqiriladi.Ular ishlab chiqaruvchilarga obektlarning xatti harakatlarini aniqlash
#yoki sozlash imkonini beradi
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f'Title: {self.title}\nAuthor: {self.author}\nPages: {self.pages}'
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    def __lt__(self, other):
        return self.pages < other.pages
    def __gt__(self, other):
        return self.pages > other.pages
    def __add__(self, other):
        return f'{self.pages+other.pages}'
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key== 'pages':
            return self.pages
        elif key== 'title':
            return self.title
        elif key== 'author':
            return self.author
        else:
            return f'Key {key} was not found'
book1=Book("Dunyoning ishlari","O'tkir hoshimov",215)
book2=Book("Jimjitlik","Said Ahmad",306)
book3=Book("Shaytanat","Toxir Malik",512)
print(book1 ['audio'])
print(book2 ['title'])
print(book3 ['title'])
