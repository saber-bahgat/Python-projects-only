my_books=[]
new_books=input("Write the name of a book you own: ")
my_books.append(new_books)
new_books=input("Write the name of another book you own or (Enter to skip): ")
if new_books:
  my_books.append(new_books)
  print("Your library:")
  print(my_books)
else:
  print("Your library:")
  print(my_books)
wish_books=[]
wish_book=input("Write the name of a book you wish to have in the future: ")
wish_books.append(wish_book)
wish_book=input("Write the name of another book you wish to have in the future or (Enter to skip): ")
if wish_book:
  wish_books.append(wish_book)
  print("Your wish list: ")
  print(wish_books)
else:
  print("Your wish list:")
  print(wish_books)
acquired_books=input("Write the name of a book from your wish list that you've acquried or (Enter to skip): ")
if acquired_books in wish_books:
  my_books.append(acquired_books)
  wish_books.remove(acquired_books)
  print("Updated library: ")
  print(my_books)
  print("Updated wish list:")
  print(wish_books)
else:
  print("Updated library: ")
  print(my_books)
  print("Updated wish list:")
  print(wish_books)
donated_books=input("Write the name of a book from your library you wish to donate or (Enter to skip): ")
if donated_books in my_books:
  my_books.remove(donated_books)
  print("Final library after donations:", my_books)
else:
  print("Final library after donations:", my_books)