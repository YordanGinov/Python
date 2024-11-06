from typing import Optional

from project.user import User


class Library:
    def __init__(self) -> None:
        self.user_records: list[User] = []
        self.books_available: dict[str, list[str]] = {} # author: [list of books]
        self.rented_books: dict[str, dict[str, int]] = {} # user: [book name: days to return]]

    def get_book(self, author: str, book_name: str, days_to_return: int, user: User) -> str:
        if book_name in self.books_available[author] and author in self.books_available:
            user.books.append(book_name)
            self.books_available[author].remove(book_name)
            if user.username not in self.rented_books:
                self.rented_books[user.username] = {}
            self.rented_books[user.username][book_name] = days_to_return
            return f"{book_name} successfully rented for the next {days_to_return} days!"

        for username, book_date in self.rented_books.items():
            if book_name in self.rented_books[username]:
                return f'The book "{book_name}" is already rented and will be available in {book_date[book_name]} days!'

    def return_book(self, author: str, book_name: str, user: User) -> Optional[str]:
        if book_name in user.books:
            user.books.remove(book_name)
            self.books_available[author].append(book_name)
            del self.rented_books[user.username][book_name]
        return f"{user.username} doesn't have this book in his/her records!"
