# импорт необходимых библиотек и файлов
import unittest
import logging
import rt_with_exceptions as rr

# Желательно basicConfig указывать после импортов до написания кода программы
# basicConfig настроен на  параметры:
#     Уровень - INFO
#     Режим - запись с заменой('w')
#     Название файла - runner_tests.log
#     Кодировка - UTF-8
#     Формат вывода - на своё усмотрение, обязательная информация: уровень логирования, сообщение логирования.
logging.basicConfig(level=logging.INFO, filemode='w',
                    filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s | %(levelname)s | %(message)s')


class RunnerTest1(unittest.TestCase):

    # метод test_walk
    def test_walk(self):
        # блок try проверяет код на наличие исключений
        try:
            # объект класса Runner с произвольным именем
            walk_ = rr.Runner('man', -5)
            # вызов метода walk у этого объекта 10 раз
            for _ in range(10):
                walk_.walk()
            # методом assertEqual сравниваем distance этого объекта со значением 50
            self.assertEqual(walk_.distance, 50)
            # логирование INFO
            logging.info('"test_walk" выполнен успешно')
            # вывод на консоль если все правильно
            # print ('Test "walk" OK')
        # блок except выполняется, если в блоке try нашлась ошибка значения переменной
        except ValueError as e:
            # логирование на уровне WARNING
            logging.warning(f'Неверная скорость для Runner. \n{e}')

    # метод test_run
    def test_run(self):
        # блок try проверяет код на наличие исключений
        try:
            # объект класса Runner с произвольным именем
            run_ = rr.Runner(5)
            # вызов метода run у этого объекта 10 раз
            for _ in range(10):
                run_.run()
            # методом assertEqual сравниваем distance этого объекта со значением 100
            self.assertEqual(run_.distance, 100)
            # логирование INFO
            logging.info('"test_run" выполнен успешно')
            # вывод на консоль если все правильно
            # print('Test "run" OK')
        # блок except выполняется, если в блоке try нашлась ошибка типа переменной
        except TypeError as e:
            # логирование на уровне WARNING
            logging.warning(f'Неверный тип данных для объекта Runner. \n{e}')


    # # метод test_challenge
    # def test_challenge(self):
    #     # создаются 2 объекта класса Runner с произвольными именами
    #     challenge1 = rr.Runner('man_R', 10)
    #     challenge2 = rr.Runner('man_W', 5)
    #     # 10 раз у объектов вызываются методы run и walk соответственно
    #     for _ in range(10):
    #         challenge1.run()
    #         challenge2.walk()
    #     # метод assertNotEqual, чтобы убедится в неравенстве результатов
    #     self.assertNotEqual(challenge1.distance, challenge2.distance)
    #     # вывод на консоль если все правильно
    #     print('Test "challenge" OK')

if __name__ == '__main__':
    unittest.main()    