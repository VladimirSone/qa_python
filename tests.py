from main import BooksCollector

# тест 1
# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # проверяю метод добавления новой книги и получаем жанр книги по её имени
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # тест 1 - проверяю добавление книги
    # строка 29 ошибка выводится
    @pytest.mark.parametrize('name', ['Оно', 'Война и мир'])
    def test_add_new_book_added_book(self, name):
        collector = BooksCollector()
        collector.add_new_book('Оно', 'Война и мир')
        assert name in collector.book_genre

    # тест 2 - проверяю присвоение книге жанра
    @pytest.mark.parametrize('name', ['Оно'])
    def test_set_book_genre_not_book_genre(self, name):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        assert collector.books_genre[name] == 'Ужасы'

    # тест 3 - проверяю,что книга соответсвует жанру
    def test_get_book_genre_book_corresponds_genre(self):
        collector = BooksCollector()
        collector.book_genre = {'Оно': 'Ужасы'}
        assert collector.get_book_genre('Оно') == 'Ужасы'

    # тест 4
    # проверить, что выводится список книг с определенным жанром
    def test_get_books_with_specific_genre_book_info(self):
        result = ['Оно']
        collector = BooksCollector()
        collector.book_genre = {'Оно': 'Ужасы'}
        assert collector.get_books_with_specific_genre('Ужасы') == result

    # тест 5 проверка, что можно получить данные по словарю
    @pytest.mark.parametrize('dictionare', [{'Оно', 'Война и мир'}])
    def test_get_books_genre_conclusion(self, dictionare):
        collector = BooksCollector
        collector.books_genre = {'Оно', 'Война и мир'}
        assert collector.get_books_genre() == dictionare

    # Тест 6 - проверяю, что выводятся детские книги
    def test_get_books_for_children_book(self):
        collector = BooksColector()
        collector.add_new_book('Три медведя')
        collector.add_new_book('Челюсти')
        collector.set_book_genre('Три медведя', 'Мультфильм')
        collector.set_book_genre('Челюсти', 'Ужасы')
        assert collector.get_books_for_children() == ['Три медведя']

    # тест 7 -  позитивная проверка добавления книги в избранный список
    def test_add_book_in_favorites_final(self):
        result = ['Оно']
        collector = BooksCollector()
        collector.books_genre = {'Оно'}
        collector.add_book_in_favorites('Оно')
        assert collector.get_list_of_favorites_books('Оно') == result

    # тест 8 - проверяем удаление книги из избранного списка книг
    @pytest.mark.parametrize('name', ['Оно', 'Война и мир'])
    def test_delete_book_from_favorites_exactly_deletes(self, name):
        collector = BooksCollector()
        collector.favorites = ['Оно']
        collector.delete_book_from_favorites('Оно')
        assert name not in collector.favorites

    # тест 9 проверить, что получаем список избранных книг
    @pytest.mark.parametrize('dictionare', ['Оно', 'Война и мир'])
    def test_get_list_of_favorites_books_bring_out_list(self, dictionare):
        collector = BooksCollector
        collector.favorites = ['Оно', 'Война и мир']
        assert collector.get_list_of_favorites_books() == dictionare
