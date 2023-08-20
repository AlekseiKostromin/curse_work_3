import utils
import os


# создаем путь к json файлу
PATH = os.path.join('data', 'operations.json')


def main():
    """
    Основная функция
    :return:возвращает результат
    """
    # задаем переменную для массива данных
    operation_list = utils.load_json(PATH)

    # задаем переменную для  5 последних выполненных операций
    executed_list = utils.get_list_executed(operation_list)

    # задаем переменную для  экземпляров класса
    class_list = utils.get_list_class(executed_list)

    # задаем цикл для вывода операций
    for operation in class_list:
        print(f'{operation.formate_date()} {operation.description}\n'
              f'{operation.mask_from()} -> {operation.mask_to()}\n'
              f'{operation.amount} {operation.currency}\n'
              f'')


if __name__ == '__main__':
    main()