import numpy as np

def game_core_v3(number: int = 1) -> int:
    count = 1
    min_number = 1
    max_number = 100
    predict = (max_number + min_number) // 2  # начальное предположение
    
    while number != predict:
        count += 1
        if number > predict: 
            min_number = predict + 1
        else: 
            max_number = predict - 1
        predict = (max_number + min_number) // 2
        
    return count

def score_game(random_predict) -> int:
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Алгоритм угадывает число в среднем за: {score} попыток")
    return score

# Тестируем
print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
