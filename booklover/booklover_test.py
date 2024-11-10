import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        """Add a book and test if it is in book_list."""
        books = BookLover("George", "george@gmail.com", "historical fiction")
        books.add_book("Frankenstein", 5)
        self.assertIn("Frankenstein", books.book_list['book_name'].values)

    def test_2_add_book(self):
        """Add the same book twice. Test if it's in book_list only once."""
        books = BookLover("George", "george@gmail.com", "historical fiction")
        books.add_book("Frankenstein", 5)
        books.add_book("Frankenstein", 4)
        self.assertEqual(len(books.book_list), 1)

    def test_3_has_read(self):
        """Pass a book in the list and test if the answer is True."""
        books = BookLover("George", "george@gmail.com", "historical fiction")
        books.add_book("Frankenstein", 5)
        self.assertTrue(books.has_read("Frankenstein"))

    def test_4_has_read(self):
        """Pass a book NOT in the list and use assert False to test if the answer is True."""
        books = BookLover("George", "george@gmail.com", "historical fiction")
        books.add_book("Frankenstein", 5)
        self.assertFalse(books.has_read("The Queen's Gambit"))

    def test_5_num_books_read(self):
        """Add some books to the list, and test num_books matches expected."""
        books = BookLover("George", "george@gmail.com", "historical fiction")
        books.add_book("Frankenstein", 5)
        books.add_book("The Queen's Gambit", 2)
        self.assertEqual(books.num_books_read(), 2)

    def test_6_fav_books(self):
        """Add some books with ratings to the list, making sure some of them have rating > 3."""
        books = BookLover("George", "george@gmail.com", "historical fiction")
        books.add_book("Frankenstein", 5)
        books.add_book("The Queen's Gambit", 2)
        books.add_book("Dune", 4)
        self.assertTrue(all(rating > 3 for rating in books.fav_books()['book_rating']))

        
if __name__ == '__main__':
    unittest.main(verbosity=3)

    
    
    
    
    