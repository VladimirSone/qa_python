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

    # тест 1.1 негативная проверка длины имени книги
    # строка 29 ошибка выводится
    @pytest.mark.parametrize('negative_test', [' ', 'TheGreenEarThisthepromisedpointofreturnEa', 'TheGreenEarThisthepromisedpointofreturnEar'])
    def test_add_new_book_negative_quantity(self, negative_test):
        collector = BooksCollector()
        collector.add_new_book(negative_test)
        assert collector.get_book_genre() == {}

    # тест 2
    def test_set_book_genre_not_book_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()
        # создаём книгу и жанр
        set_book_genre_not_book_genre['Роман'] = 'Война и мир'
        # указываем, что есть список жанров
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        # книга с жанром ['Роман'] = 'Война и мир' сравниваем со списоком genre
        collector.set_book_genre_not_book_genre = self.genre
        # проверяем, что данный жанр есть в списке genre
        assert set_book_genre_not_genre in self.genre

    # тест 3
    def test_get_book_genre_new_name_book(self):
        collector = BooksCollector()
        # создаем переменную с новой книгой
        collector.new_name_book = 'Гордость и предубеждение и зомби'
        # проверяем, что получаем жанр по имени книги
        assert new_name_book == self.books_genre.get(name)

    # тест 4
    # проверить, что выводится список книг с определенным жанром
    def test_get_books_with_specific_genre_book_info(self):
        collector = BooksCollector
        # проверяем, что будем выводить жанр детективы([2])
        collector.book_info[2] = self.genre
        assert collector.book_info([]) != self.genre

    # тест 5 проверка, что словарь работает и мы получаем данные
    def test_get_books_genre_conclusion(self):
        collector = BooksCollector
        collector.conclusion = get_books_genre
        assert len(collector.conclusion()) == {}

    # тест 6 - проверить, что выводятся только детские жанры
    def test_get_books_for_children_not_limit(self):
        collector = BooksColector()
        collector.not_limit = self.genre_age_raiting
        assert collector.not_limit == []

    # тест 7 - выводится ошибка в строке 69
    # создал список книг в избранном
    add_book_in_favorites = ['Война и мир', 'Оно', 'Чебурашка']

    @pytest.mark.parametrize('add_book_in_favorites', add_book_in_favorites)
    def test_add_book_in_favorites_list(self, add_book_in_favorites):
        assert add_book_in_favorites_list(add_book_in_favorites)

    # тест 7.1 позитивная проверка добавлени книги в избранный список
    def test_add_book_in_favorites_final(self):
        collector = BooksCollector
    # переменная создание новой книги
        collector.add_new_book('Точка невозврата')
    # переменная добавление книги в список избранных
        collector.add_new_book_in_favorites('Точка невозврата')
        assert collector.get_list_of_favorites_books() == ['Точка']

    # тест 7.2 - негативная проверка добавление книги в избранное
    def test_add_book_in_favorites_negative(self):
        collector = BooksCollector
    # переменная избранные книги
        collector.add_book_in_favorites('Точка возврата')
        assert len(collector.get_list_of_favorites_books()) == 1

    # тест 8
    # проверяем удаление книги из избранного списка книг
    def test_delete_book_from_favorites_exactly_deletes(self):
        collector = BooksCollector()
    # переменная с новой книгой
        collector.add_new_book('Оно')
    # список избранных с книгой
        collector.add_book_in_favorites('Оно')
    # уделение книги из списка избранных
        collector.delete_book_from_favorites('Оно')
        assert collector.get_list_of_favorites_books() == []

    # тест 9 проверить, что получаем список избранных книг
    def test_get_list_of_favorites_books_bring_out_list(self):
        collector = BooksCollector
        collector.arg = get_list_of_favorites_books
        assert len(collector.arg()) == 'No list'
