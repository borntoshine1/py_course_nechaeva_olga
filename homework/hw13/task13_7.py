def solution(string, ending):
    return string.endswith(ending)

print(solution("abc", 'bc'))
print(solution("abc", 'b'))
print(solution("abcde", ''))

#Завершите решение так, чтобы оно возвращало true,
# если первый переданный аргумент (строка) заканчивается вторым аргументом (также строкой).