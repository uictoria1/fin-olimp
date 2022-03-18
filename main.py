"""Task 1"""
# Вам дана функция 'task1', которая принимает массив с числами,
# верните сумму всех чисел в данном массиве.

def task1(arr: list) -> int:
  # пишите код здесь
  return sum(arr);


"""Task 2"""
# Вам дана функция 'task2', которая принимает массив с числами,
# верните первое положительное число в данном массиве

def task2(arr: list) -> int:
  # пишите код здесь
  for d in arr:
	  if(d > 0):
		  return d;

"""Task 3"""
# Вам дана функция 'task3', которая принимает массив с числами,
# верните сумму всех четных чисел

def task3(arr: list) -> int:
  # пишите код здесь
  sum = 0
  for i in arr:
	  if(i % 2 == 0):
		  sum += i
  return sum
  

"""Task 4"""
# Вам дана функция 'task4', которая принимает два числа,
# верните среднее арифметическое этих чисел

def task4(num1: int, num2: int) -> float:
  # пишите код здесь
  return (num1 + num2) / 2;
  

"""Task 5"""
# Вам дана функция 'task5', которая принимает строку,
# верните строку, прочитанную задом наперед. 
# Например:
# начальная строка -> "hello world"
# результат -> "dlrow olleh"

def task5(string: str) -> str:
  # пишите код здесь
  return string[::-1]
  

"""Task 6"""
# Вам дана функция 'task6', которая принимает строку,
# верните все числа из этой строки.
# Например:
# строка -> "Я родился в 2010 году, мне 12 лет"
# результат -> [2010, 12]

def task6(string: str) -> list:
  # пишите код здесь
  tokens = string.split(" ")
  for i in range(len(tokens)):
    tokens[i] = tokens[i].strip()
  numbers = []
  for word in tokens:
    if(word.isnumeric()):
      numbers.append(word)
  return numbers
  

"""Task 7"""
# Вам дана функция 'task7', которая принимает строку,
# выведите, является ли это строка палиндромом. 
# Палиндром - число, буквосочетание, слово или текст, одинаково читающееся в обоих направлениях. Например число 101, строка "топот" являются палиндромами.
# Регистр не должен учитываться. ("Топот" - палиндром)

def task7(string: str) -> bool:
  # пишите код здесь
  string = string.lower()
  size = len(string)
  for i in range(size // 2):
    if(string[i] != string[size - 1 - i]):
      return False
  return True


"""Task 8"""
# Вам дана функция 'task8', которая принимает массив чисел nums и число target. 
# Выведите индексы двух чисел в массиве nums, которые в сумме дают данное число target.

def task8(nums: list, target: int) -> list:
  # пишите код здесь
  left = []
  right = []
  for i in nums:
    if i not in left and i not in right:
      left.append(i)
      right.append(target - i)
    else:
      if i in left:
        # in left
        index = left.index(i)
        right_num = right[index]
        return [nums.index(i), nums.index(right_num)]
      else: 
        # in right
        index = right.index(i)
        left_num = left[index]
        return [nums.index(left_num), nums.index(i)]

"""Task 9"""
# Вам дана функция 'task9', которая принимает строку с хештегами в виде: "#hello#world"
# выведите список из всех хештегов без символа решетки
# результат: ["hello", "world"]

def task9(hashtags: str) -> list:
  # пишите код здесь
  l = []
  temp = ""
  for ch in hashtags:
    if ch == "#":
      if len(temp) > 0:
        l.append(temp)
        temp = ""
    else:
      temp += ch

  if len(temp) > 0:
    l.append(temp)
  return l

"""Task 10"""
# Вам дана функция 'task10', которая принимает массив из чисел,
# выведите, есть ли среди них повторяющиеся

def task10(arr: list) -> bool:
  # пишите код здесь
  unique = set(arr)
  return len(unique) != len(arr)