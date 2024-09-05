# Импорт библиотеки для создания оконного приложения  
from tkinter import *
from tkinter import messagebox
 
def sort_colors(set_of_objects):
    """Сортирует объекты по цветам.

    Входные данные:
    set_of_objects (str): Строка, содержащая объекты, помеченные цветами ('С' - синий, 
                          'К' - красный, 'З' - зеленый).

    Возвращает:
    str: Отсортированная строка объектов, где сначала идут зеленые, 
         затем синие, и в конце красные объекты, или None,
         если в наборе есть непомеченные объекты.
    """
    
    # Устанавливаем начальные значения счетчиков для объектов разных цветов
    amount_of_red = 0    # Счетчик объектов из класса КРАСНЫЙ
    amount_of_green = 0  # Счетчик объектов из класса ЗЕЛЕНЫЙ
    amount_of_blue = 0   # Счетчик объектов из класса СИНИЙ

    # Перебор набора и подсчет количества объектов каждого цвета
    for obj in set_of_objects:
        if obj == "С":
            amount_of_blue += 1
        elif obj == "К":
            amount_of_red += 1
        elif obj == "З":
            amount_of_green += 1
        else:
            return None
    
    # Формируем упорядоченный список объектов
    sorted_objects = (amount_of_green * 'З') + (amount_of_blue * 'С') + (amount_of_red * 'К')
    
    return sorted_objects

def test_sort_color():
    """Проверяет корректность работы функции сортировки.

    Возвращает:
    int: 0, если все тесты пройдены, 1, если есть ошибки в тестах.
    """
    
    flag = 0 # Флаг, для отслеживания правильности работы функции сортировки: 0 - все правильно, 1 - есть ошибки

    # Тест 1. Обычный набор
    if sort_colors('СКЗКСЗКСЗКСЗКССЗКЗКСЗККЗ') != 'ЗЗЗЗЗЗЗЗСССССССККККККККК':
        flag = 1
        messagebox.showinfo('Тest 1', f'Failed!')
    # Тест 2. Уже отсортированный
    if sort_colors('ЗЗЗСССССССККККК') != 'ЗЗЗСССССССККККК':
        flag = 1
        messagebox.showinfo('Тest 2', f'Failed!')
    # Тест 3. Состоящий из одного обьекта
    if sort_colors('С') != 'С':
        flag = 1
        messagebox.showinfo('Тest 3', f'Failed!') 
    # Тест 4. Пустой ввод
    if sort_colors('') != '':
        flag = 1
        messagebox.showinfo('Тest 4', f'Failed!')
    # Тест 5. Содержащий непомеченный обьект
    if sort_colors('СЗКЗСКЗСКЗКСаСКСЗКСКЗ') != None:
        flag = 1
        messagebox.showinfo('Тest 5', f'Failed!')
    # Тест 6. Смешанный случай
    if sort_colors('СЗКЗСКЗСКЗКСаСКСЗКСКЗCRPRPCRPСКЗСЗККЗСЗКСЗКСЗКЗКСЗКЗскскс') != None:
        flag = 1
        messagebox.showinfo('Тest 6', f'Failed!')
    
    return (flag) # Возвращает флаг, указывающий на наличие или отсутствие ошибки

def main():
    
    """Основная функция, обрабатывающая ввод пользователя."""
    if test_sort_color() == 0:

        """Функция для ввода данных от пользователя и вывода результатов сортировки"""
        set_of_objects = clr_set_tf.get()

        # Обработка объектов
        sorted_output = sort_colors(set_of_objects)
        if sorted_output is not None:  # Проверяем результат сортировки на наличие ошибок
            messagebox.showinfo('Отсортированные обьекты:', f'{sorted_output}                             ')
        else:
            messagebox.showinfo('ОШИБКА', f'В наборе есть обьект, непомеченный цветом!')
    else:
        messagebox.showinfo('ОШИБКА', f'Функция сортировки работает неправильно!')

# Создаем оконное приложение
window = Tk()
window.title('Сортировщик цветных обьектов V 1')
window.geometry('500x250')

# Шаблон формы  
frame = Frame(
   window,
   padx=10,
   pady=10
)
frame.pack(expand=True)
 
# Заголовки формы
clr_set_lb = Label(
   frame,
   text="""Введите набор обьектов, помеченных цветом, например 'СКККСЗЗЗСКСЗС', где:

   С - обьект,помеченный синим цветом,
   К - обьект, помеченный красным цветом,
   З - обьект, помеченный зеленым цветом.
   """
)
clr_set_lb.grid(row=4, column=1)

# Поле ввода для набора обьектов
clr_set_tf = Entry(
   frame,
)
clr_set_tf.grid(row=5, column=1, pady=5)

# Кнопка для запуска сортировки
srt_btn = Button(
   frame,
   text="Сортироать!",
   command=main
)
srt_btn.grid(row=6, column=1)

# Запуск основного цикла приложения
window.mainloop()
