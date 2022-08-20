import numpy as np
def random_predict(number: int = 1) -> int:
    """Компьютер угадывает рандомное число
    Args:
        number (int, optional): Загаданное число Defaults to 1.
    Returns:
        int: Число попыток
    """
    predict_number = np.random.randint(1, 101) # Задаём рандомное число, в диапазоне от 1 до 100
    count = 0 # Переменная счетчик, в которую сохраняем количество попыток
    min = 1 # Минимальное значение диапазона
    max = 100 # Максимальное значение диапазона
    
    
    while True:
        count += 1
        
        if number < predict_number:
            max = predict_number - 1
            predict_number = (min + max) // 2 # Уменьшаем диапозон поиска
        
            
        elif number > predict_number:
            min = predict_number + 1
            predict_number = (min + max) // 2 # Увеличиваем диапазон поиска
            
        else:
            break # Число найдено, прерываем цикл
        
    return(count)

def score_game(random_predict) -> int:
    """ За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм
    Args:
        random_predict ([type]): функция угадывания
    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    for number in random_array:
        count_ls.append(random_predict(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    
if __name__ == "__main__":
    
     score_game(random_predict)