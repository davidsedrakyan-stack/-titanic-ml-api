#input()-получение значения от пользователя
#print,sep-разделитель между значениями,\n-перевод на новую строку,end-указание конца строки,\-обозначает как обычный символ,\t-создает отпуск как будто нажал таб,
#min-находит минимальное значение,max-максимальное значение,abs-находит модуль числа,\\-округление,**-возведение в степень
#print("результат: ", 5,7, sep="'", end="?\n")
#print("fak \" \ny\no\nu")
#print("результат:", 5 * 5)
#print("результат:", max(3 ,4 ,4 ,4 ,2 ,2 ))
#input("введите число: ")
#del-удаление переменной
#boolean = true,false-тип данных правда или ложь
#fuk = 5 #int
#dijit = 7.12345678 #float
#word = "результат: " #string
#boolean = True #bool

#num1 = int(input("Введите первое число: "))

#num2 = int(input("Введите второе число: "))

#num1 += 5 - к переменной num1 я добавил число 5,также можно и +-*/

#print("Result:", num1 + num2)
#print("Result:", num1 * num2)
#print("Result:", num1 / num2)
#print("Result:", num1 - num2)
#print("Result:", num1 ** num2)
#print("Result:", num1 // num2)

#word= "молодец"

#print(word * 1)

#if 5==5:
#    print("yes")
 #   print("ура")


#user_data = int(input("Введите число:"))
#isHappy = True
#and, or- операторы
#if isHappy or user_data == 6:
#    print("user is happy")
#elif user_data == 7:
 #   print("namber is 7")
#elif user_data == 5:
#    print("namber is 5")
#else:
#    print("user is unhappy")
#data= input()
#number = 5 if data== "five" else 0 - тернарный оператор (сокращенный)
#if data == "five":
#    number=5
#else:
#
#print(number)
#range - диапазон
#range(x,y,z) x-начало диапазона y- конец диапазона z-колво отступов
#for i in range(1, 6,2):
  #  print(i)
#for i in ....это перебирание ,цикл
#count = 0

#word = "Hello world"
#for i in word:
#      if i == "l":
#          count += 1

#print("Count:", count)
#while более удобный цикл
#i = 5

#while i <= 15:
 #   print(i)
 #   i+=2
 #break- прервание цикла
#for i in range(1,11):
#    if i >= 5:
#        break

 #   print(i)


#found = None
#for i in "hello":
 #   if i == "r":
  #      found = True
 #       break
 #   else: found = False
#print(found)

#nums = []- это список

#nums = [5, 3 , 9, 3, True, "писька" ,[5, 7]]

#nums[0]= 50
#nums[4]= 1.01

#print(nums[1])
#numbers=[5, 4 ,7]


                          #СПИСКИ
#numbers.append(100)-прибавление в список нового элемента
#numbers.insert(1, True)- прибавление в список но с определенным местом
#numbers.extend([])-добавление в первоначальный список новый
#numbers.sort()-сортирование списка
#numbers.reverse()-переваричмвает порядок списка
#numbers.pop()-удаление последнего элемента списка
#numbers.clear()-удаление всех элементов списка
#numbers.pop(0)-удаление элемента списка по его индексу
#numbers.remove(7)-удаление определенного элемента списка
#numbers.count(7)-нахождение совпадений в списке с числом в скобках
#print(len(numbers))-нахождение длинны списка
#range(len(numbers))-в диапазоне длинны numbers
               #СТРОКИ
#word.upper()-переводит строку в верхний регистр
#word.isupper()-если вся строка будет в верхнем регистре то покажет True
#word.islower()-если вся строка будет в нижнем регистре то покажет True
#word.capitalize()-переводит первый синвол в верхний регистр
#word.find("p")-находит индекс синвола в скобках в строке
#word.split(", ")-создает список из слов разделенных синволом в скобках
#word.join()- объединение строки
#word[0:4:2]-срез строки по его индексу,0- это начальный идекс 4-это конечный 2-это шаг


#nums=[5, 2, 4, "50", False]

#for el in nums:
#    el*=2
#    print(el)

#n = int(input("Введите длинну списка: "))

#user_list = []

#i = 0
#while i < n:
#    string= "напишите элемент#"+ str(i+1)+ ": " #столько раз сколь напишем n
#    user_list.append(input(string))
#    i += 1


#print(user_list)












#word = "football, basketball, tennis"

#word =("football, basketball, tennis ")

#hobby=word.split(", ")

#for i in range(len(hobby)):
 #   hobby[i]=hobby[i].capitalize()


#result = ", ".join(hobby)

#print(result)




#lis = [1, 3, 5, "stroka", True, -2.34]

#print(lis[0:6:2])


#piska = ("1|  2 |true| True")

#print(piska.split("| "))


                                           #КОРТЕЖИ
#data = (6, 3, 4 ,5 ,True, 2)-это кортеж,это тот же список но элементы нельзя менять
#new_data = tuple(nums)- преобразует список в кортеж

#print(data[:5])-

#print(data.count(6))

#print(len(data))


#data = (6, 3, "hello" ,5 ,True, 2)


#for el in data:
#    print(el)

#nums = [5, 6, 3]

#new_data = tuple(nums)
#word = tuple("Hello world")
#print(new_data)



                                           #СЛОВАРИ

#country = {4: 3}  #это словарь он отличается то списка тем что у каждого значения есть ключ
#print(country[4]) #чтобы получить число 3 мы обращаемся к его ключу тоесть числу 4

#country = {(4, 2): 3}  #так же ключом может быть КОРТЕЖ
#(country[(4, 2)])


#country = dict(code= "RU", name = "Russia")   #команда dict создает список причем ключ для этой строки является "......"
#print(country.get("code"))-обращение к ключу
#print(country["code"])
#print(country.keys())-получение только ключей
#print(country.values())-получение только значений
#["code"] = "None"-обновляем ключ


#print(country.items()) создаает список из кортежей
#for key , value in country.items():
 #   print(key, " - ", value)




                               #МНОЖЕСТВА


#data = set("hello")                    #-это тот же список но все синволы в множестве не могут повторятся и они размешанны
                                       #-функция set создает множества


#data = {5, 3, 5 ,6, 6, 2}              #-это множество
#data.add(42)                             #-добавление в множество новый элемент
#data.update(["gg", True, 7.3])           #-добавление во множество список
#data.remove(True)
#print(data)

#nums = [1, 2, 3,4 ,5, 6, 7, 3, 5 ,6, 6, 6]

#new_nums = set(nums)                   #-это удаление элементов из списка

#new_data = frozenset([5, 3, 5 ,6, 6, 2, "gg", True, 7.3])       #-это совмещение кортежа и множества

#print(new_data)


                                       #ФУНКЦИИ

#def test_funk(word):                                #-это функции которые мы пишем сами
 #   print(word, end="")                               #pass - означает что функция ничего не делает
 #   print("!")                                      #в скобнах мы задаем какой нибудь параметр
#
#test_funk("Hi")
#test_funk(5)
#test_funk(3.5)





#def summa(a, b):
#    word = a + b
 #   print("Result: ", word)
#
#summa(12, 3)
#summa("Hi", "!")


# summa(a, b):

#    return a+b                   #return означает выведенно будет только значение word

#word = summa(12, 3)
#summa("Hi", "!")
#print(word)



#def maximal(l):
#    max_ment = l[0]
#    for el in l:
#        if el > max_ment:       #нахождение максимального элемента
#            max_ment = el
#    print(max_ment)


#def minimal(l):
#   min_ment = l[0]
#    for el in l:                #нахождение минимального элемента
##        if el < min_ment:
 #           min_ment = el
#    print(min_ment)

#nums1 = [1, 2 ,3 ,4 ,6]
#maximal(nums1)
#minimal(nums1)


#nums2 = [1.2, 2.3,2.1 ,3 ,4 ,6]
#maximal(nums2)
#minimal(nums2)

#func = lambda a, b: a +b
#func2 = lambda a, b: a -b
#func3 = lambda a, b: a *b
#func4 = lambda a, b: a /b    #это анонимная функция


#res= func(3,5)
#print(res)






                                   #ФАЙЛЫ

#data = input("Enter a text: ")

#file = open("data/text.txt", "a")       #-открытие файла data c параметром text.txt
                                        #"a"-добавление нового в конец файла "w"чтобы переписать файл
#file.write(data + "\n")              #-добавление в файл




#file.close()                            #ОБЯЗАТЕЛЬНО ЗАКРЫВАТЬ ФАЙЛЫ



#file = open("data/text.txt", "r")

#print(file.read(11))                 #функцие для выявлени текта в файле

#for line in file:
#    print(line, end="")

#file.close()



                                               #ОБРАБОТЧИКИ ИСКЛЮЧЕНИЙ


#x = 0
#while x == 0:

 #  try:
 #   x = int(input("Введите число:"))      #при ошибке присходит другой код
#    x +=5
  #W print(x)
 #  except ValueError:
 #   print("Введи число блять!!! ")
 #  else: print("fuck")
 #  finally:                              # в лубом случае выполняет код
 #   print("молодец")


                                           #МЕНЕДЖЕР С....КАК

#try:
#    with open("text.txt", "r", encoding="utf-8")as file: #даже при ошибке файл закрывается
 #       print(file.read())
#except FileNotFoundError:
#    print("Вы лох")


                                      #МОДУЛИ

#import time

#time.sleep(3)                #модуль time выполняет действия с временем
                              #функция .sleep замораживает вре выполнения кода
#print("Hello Arman")





#import datetime as dt                   #

#print("дата сегодня: ",dt.datetime.now())


#import sys, os, platform
#from math import sqrt as s, ceil
#print(os.name)
#(ceil(s(100)))


#import mymodule as my

#print(my.name)


#from mymodule import add_three_numbers as add

#print(add(1, 2, 0))

#import cowsay as co

#co.cow("АРМАН ЛОХ")




                               #ООП

#то описание общих характеристик в одном месте


#class Cat:
 #   name = None              #в class мы указываем основные характеристики
 #   age = None
 #   isHappy = None
#
 #   def set_data(self, name, age, isHappy):
 ##       self. age = age
  #      self.isHappy = isHappy
 #   def get_data(self):
 #       print("Name:", self.name,"Age:", self.age,"isHappy:",self.isHappy)


#cat1 = Cat()
#cat1.set_data("Barsik", 3, True)

#cat2 = Cat()
#cat2.set_data("Piska", 2, False)

#cat3 = Cat()
#cat3.set_data("Ponos", 1, True)

#cat1.get_data()
#cat2.get_data()
#cat3.get_data()





#import webbrowser

##########


#def maximal(l): max_ment = l[0]
  #  for el in l:
#        if el > max_ment:       #нахождение максимального элемента
#            max_ment = el
#    print(max_ment)


#def minimal(l):
#   min_ment = l[0]
#    for el in l:                #нахождение минимального элемента
##        if el < min_ment:
 #           min_ment = el
#    print(min_ment)

#nums1 = [1, 2 ,3 ,4 ,6]
#maximal(nums1)
#minimal(nums1)




#def summa(a, b):
  #  res = (a + b)
  #  print("Result" , res)

#def minus(a, b):
  #  res = (a - b)
#    print("Result" , res)

#def multiplication(a, b):
 #   res = (a * b)
 #   print("Result" , res)

#def division(a, b):
  #  res = (a / b)
 #   print("Result" , res)


#






"""
from sklearn.datasets import load_iris
import pandas as pd

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target

print(df.head())


from sklearn.model_selection import train_test_split

x = df[iris.feature_names]
y = df['target']

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

from sklearn.neighbors import KNeighborsClassifier


model = KNeighborsClassifier(n_neighbors=3)
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)
print(f'Точночть модели: {accuracy * 100:.2f}%')

import numpy as np

example = np.array([[5.1, 3.5, 1.4, 0.2]])
print("Предсказание класс:",iris.target_names[[0]])

"""
"""                                          
from tkinter.scrolledtext import example"""
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
iris = load_iris()
x = iris.data
y = iris.target
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
model = LogisticRegression(max_iter=500)
model.fit(x_train, y_train)

accuracy = model.score(x_test, y_test)
print("Accuracy:", accuracy)

example=[[5.1, 3.5, 1.4, 0.2]]
prediction = model.predict(example)
print("Prediction:",iris.target_names[prediction][0])
"""

print("Hello")


"""
import numpy as np

X = np.array([
    [30, 1, 5, 10],
    [50, 2, 3, 7],
    [70, 3, 8, 5],
    [90, 3, 10, 3],
    [120, 4, 15, 2],
    [60, 2, 6, 8],
    [80, 3, 9, 4],
    [100, 4, 12, 3]
])

y = np.array([50, 80, 120, 150, 220, 90, 130, 180])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.model_selection import GridSearchCV


from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', RandomForestRegressor())
])

params = {
    'model__n_estimators': [50, 100],
    'model__max_depth': [None, 5, 10]
}

grid = GridSearchCV(pipe, params, cv=3)
grid.fit(X_train, y_train)

best_model = grid.best_estimator_

print("Лучшие параметры:", grid.best_params_)


# квартира: 75 м², 3 комнаты, 7 этаж, 6 км до центра
price = best_model.predict([[112, 4, 2, 25]])
print("Цена:", price)

score = best_model.score(X_test, y_test)
print("R²:", score)

"""
"""
import numpy as np

X = np.array([
    [30, 1, 5, 10],
    [50, 2, 3, 7],
    [70, 3, 8, 5],
    [90, 3, 10, 3],
    [120, 4, 15, 2],
    [60, 2, 6, 8],
    [80, 3, 9, 4],
    [100, 4, 12, 3]
])

y = np.array([50, 80, 120, 150, 220, 90, 130, 180])

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', KNeighborsClassifier(n_neighbors=3))
])

params = {
    'model__n_estimators': [50, 100],
    'model__max_depth': [None, 5, 10]
}

grid = GridSearchCV(pipe, params, cv=3)
grid.fit(X_train, y_train)

best_model = grid.best_estimator_

print("Лучшие параметры:", grid.best_params_)


# квартира: 75 м², 3 комнаты, 7 этаж, 6 км до центра
price = best_model.predict([[74, 3, 7, 6]])
print("Цена:", price)
"""


# 1. загрузка
# 2. очистка
# 3. X / y
# 4. split
# 5. модель
# 6. обучение
# 7. оценка
''''
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_score, recall_score,accuracy_score


titanic = pd.read_csv('titanic.csv')

df =pd.DataFrame(titanic)

df.info()
df.isnsa.sum()

df['Age']=df['Age'].fillna(df['Age'].mean())

df=pd.get_dummies(df,colums=['Sex'])

df=df[['Pclass',
'Sex',
'Age',
'Fare',
'Survived']]

x = df[['Pclass','Age','Fare','Sex_female','Sex_male']]
y = df['Survived']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression(max_iter=200))
])

param = {
    'model__C': [0.1, 1, 10],
}

grid = GridSearchCV(pipeline, param, cv=5)
grid.fit(x_train, y_train)


accuracy = grid.score(x_test, y_test)
print("Accuracy",accuracy)

y_pred = grid.predict(x_test)

print("Precision:", precision_score(y_test, y_pred, zero_division=0))
print("Recall:", recall_score(y_test, y_pred, zero_division=0))
'''
"""


                                                        #   
                                                        #  TITANIC 
                                                        #


                                                                
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# 1. Загрузка данных
df = pd.read_csv("titanic.csv")

# 2. Выбор колонок
df = df[['Pclass', 'Sex', 'Age', 'Fare', 'SibSp', 'Parch', 'Embarked', 'Survived']]

# 3. Обработка пропусков
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

# 4. Encoding
df = pd.get_dummies(df, columns=['Sex', 'Embarked'])

# 5. X и y
X = df.drop('Survived', axis=1)
y = df['Survived']

# 6. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# 🔵 МОДЕЛЬ ДО отбора
# -------------------------

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc_before = accuracy_score(y_test, y_pred)

print("Accuracy BEFORE:", acc_before)

# -------------------------
# 🔥 Feature Importance
# -------------------------

importances = model.feature_importances_

print("\nFeature Importances:")
for name, score in zip(X.columns, importances):
    print(f"{name}: {score:.3f}")

# -------------------------
# 🔥 Выбор лучших признаков
# -------------------------

selected_features = [
    name for name, score in zip(X.columns, importances)
    if score > 0.05
]

print("\nSelected Features:", selected_features)

# -------------------------
# 🔵 МОДЕЛЬ ПОСЛЕ отбора
# -------------------------

X_train_sel = X_train[selected_features]
X_test_sel = X_test[selected_features]

model2 = RandomForestClassifier(random_state=42)
model2.fit(X_train_sel, y_train)

y_pred2 = model2.predict(X_test_sel)
acc_after = accuracy_score(y_test, y_pred2)

print("\nAccuracy AFTER:", acc_after)

"""


"""
import pandas as pd

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df.head())
print(df.info())
print(df.isnull().sum())



# Заполняем Age
df["Age"] = df["Age"].fillna(df["Age"].median())

# Заполняем Embarked
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Кодируем категории
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Удаляем лишнее
df = df.drop(["Cabin", "Name", "Ticket"], axis=1)


# Размер семьи
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

# Один или нет
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

from sklearn.model_selection import train_test_split

X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

models = {
    "Logistic": LogisticRegression(max_iter=1000),
    "Tree": DecisionTreeClassifier(max_depth=5),
    "Forest": RandomForestClassifier(n_estimators=100)
}

for name, model in models.items():
    model.fit(X_train, y_train)
    print(name)
    print("Train:", model.score(X_train, y_train))
    print("Test:", model.score(X_test, y_test))
    print("------")


#Лучшая модель  RandomForestClassifier


"""
"""
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import recall_score, precision_score
import joblib
from flask import Flask, request

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

df = pd.read_csv(url)

print(df.head())
print(df.info())
print(df.isnull().sum())


df["Age"] = df["Age"].fillna(df["Age"].median())

df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

df = df.drop(["Cabin", "Name", "Ticket"], axis=1)
df = df.drop(["PassengerId"], axis=1)
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1

df["IsAlone"] = (df["FamilySize"] == 1).astype(int)



X = df.drop("Survived", axis=1)                                  #
y = df["Survived"]                                                     #
                                                                       #  РАЗДЕЛЕНИЕ ДАННЫХ
X_train, X_test, y_train, y_test = train_test_split(                   #
    X, y, test_size=0.2, random_state=42                        #
)


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


predictions = model.predict(X_test)
print("prediction accuracy:", model.score(X_test, y_test))
print("prediction recall", recall_score(y_test, predictions))
print("prediction precision", precision_score(y_test, predictions))


joblib.dump(model, 'model.pkl')

app = Flask(__name__)
@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    prediction = model.predict([list(data.values())])
    return {"survived": int(prediction[0])}

if __name__ == '__main__':
    app.run(debug=True)

"""


import requests

response = requests.post(
    "http://127.0.0.1:5000/predict",
    json={
        "Pclass": 3,
        "Sex": 0,
        "Age": 22,
        "SibSp": 1,
        "Parch": 0,
        "Fare": 7.25,
        "Embarked": 0,
        "FamilySize": 2,
        "IsAlone": 0
    }
)
print(response.json())





"""







import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score



url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"

df = pd.read_csv(url)

print(df.head())
print(df.info())
print(df.isnull().sum())

df["zn"] = df["zn"].fillna(df["zn"].mean())

df = df.drop(columns=["nox", "age", "ptratio", "b"])

x = df.drop(["medv"] , axis=1)
y = df["medv"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("regressor", LinearRegression())
])

pipeline.fit(x_train, y_train)

accuracy = pipeline.score(x_test, y_test)
print("Точность: ",(accuracy * 100), "%")

mean_squared_error = mean_squared_error(y_test, y_test * pipeline.predict(x_test))
print(mean_squared_error)

predictions = pipeline.predict(x_test)
print(predictions)

"""
"""
| Команда       | Для чего нужна              | Пример                                                                      |
| ------------- | --------------------------- | --------------------------------------------------------------------------- |
| `SELECT`      | Получить данные             | `SELECT * FROM users;`                                                      |
| `FROM`        | Указать таблицу             | `SELECT * FROM users;`                                                      |
| `WHERE`       | Фильтрация строк            | `SELECT * FROM users WHERE age > 18;`                                       |
| `ORDER BY`    | Сортировка                  | `SELECT * FROM users ORDER BY age DESC;`                                    |
| `LIMIT`       | Ограничить количество строк | `SELECT * FROM users LIMIT 5;`                                              |
| `DISTINCT`    | Уникальные значения         | `SELECT DISTINCT country FROM users;`                                       |
| `COUNT()`     | Подсчет строк               | `SELECT COUNT(*) FROM users;`                                               |
| `AVG()`       | Среднее значение            | `SELECT AVG(age) FROM users;`                                               |
| `SUM()`       | Сумма                       | `SELECT SUM(price) FROM orders;`                                            |
| `MIN()`       | Минимум                     | `SELECT MIN(age) FROM users;`                                               |
| `MAX()`       | Максимум                    | `SELECT MAX(age) FROM users;`                                               |
| `GROUP BY`    | Группировка данных          | `SELECT sex, AVG(age) FROM users GROUP BY sex;`                             |
| `HAVING`      | Фильтр после группировки    | `SELECT country, COUNT(*) FROM users GROUP BY country HAVING COUNT(*) > 5;` |
| `JOIN`        | Объединение таблиц          | `SELECT * FROM users JOIN orders ON users.id = orders.user_id;`             |
| `LEFT JOIN`   | Все строки из левой таблицы | `SELECT * FROM users LEFT JOIN orders ON users.id = orders.user_id;`        |
| `INNER JOIN`  | Только совпадающие строки   | `SELECT * FROM users INNER JOIN orders ON users.id = orders.user_id;`       |
| `AS`          | Переименование столбца      | `SELECT AVG(age) AS mean_age FROM users;`                                   |
| `IN`          | Проверка в списке           | `SELECT * FROM users WHERE country IN ('USA', 'France');`                   |
| `BETWEEN`     | Диапазон значений           | `SELECT * FROM users WHERE age BETWEEN 18 AND 30;`                          |
| `LIKE`        | Поиск по шаблону            | `SELECT * FROM users WHERE name LIKE 'D%';`                                 |
| `IS NULL`     | Проверка на NULL            | `SELECT * FROM users WHERE age IS NULL;`                                    |
| `IS NOT NULL` | Проверка не NULL            | `SELECT * FROM users WHERE age IS NOT NULL;`                                |
| `AND`         | Логическое И                | `SELECT * FROM users WHERE age > 18 AND country = 'USA';`                   |
| `OR`          | Логическое ИЛИ              | `SELECT * FROM users WHERE country = 'USA' OR country = 'France';`          |
| `NOT`         | Отрицание                   | `SELECT * FROM users WHERE NOT country = 'USA';`                            |

"""


"""import pandas as pd
import sqlite3
from sklearn.linear_model import LinearRegression

conn = sqlite3.connect("shop.db")

query = """
#SELECT
 #   age,
  #  salary,
  #  spending
#FROM customers
"""

df = pd.read_sql(query, conn)

X = df[["age", "salary"]]
y = df["spending"]

model = LinearRegression()
model.fit(X, y)

print("Model trained")"""



"""python -c "
import requests
data = {'Pclass': 1, 'Sex': 1, 'Age': 28, 'SibSp': 0, 'Parch': 0, 'Fare': 100.0, 'Embarked': 1, 'FamilySize': 1, 'IsAlone': 1}
response = requests.post('http://127.0.0.1:5000/', json=data)
print(response.json())
"""







"""import pandas as pd
import joblib
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Загрузка данных
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
df = pd.read_csv(url)

# Обработка пропусков
df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Кодирование категориальных признаков
df["Sex"] = df["Sex"].map({"male": 0, "female": 1})
df["Embarked"] = df["Embarked"].map({"S": 0, "C": 1, "Q": 2})

# Удаление ненужных колонок
df = df.drop(
    ["PassengerId", "Cabin", "Name", "Ticket"],
    axis=1
)

# Feature Engineering
df["FamilySize"] = df["SibSp"] + df["Parch"] + 1
df["IsAlone"] = (df["FamilySize"] == 1).astype(int)

# Разделение данных
X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Подбор гиперпараметров
params = {
    "n_estimators": [100, 200],
    "max_depth": [5, 10, None],
    "min_samples_split": [2, 5]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    params,
    cv=5,
    scoring="f1"
)

grid.fit(X_train, y_train)

model = grid.best_estimator_

# Оценка
predictions = model.predict(X_test)

print("Best params:", grid.best_params_)
print("Accuracy :", accuracy_score(y_test, predictions))
print("Precision:", precision_score(y_test, predictions))
print("Recall   :", recall_score(y_test, predictions))
print("F1 Score :", f1_score(y_test, predictions))

# Сохранение модели
joblib.dump(model, "model.pkl")

print("Model saved as model.pkl")

from flask import Flask, request, jsonify, render_template
import pandas as pd
import joblib

app = Flask(__name__)
model = joblib.load("model.pkl")                  #загружаем уже сохраненую модель


@app.route('/', methods=['GET', 'POST'])                # декоратор который говорит "Если передет на адрес / то выполняется функция"
def predict():
    if request.method == 'GET':
        return render_template ("david.html")

    data = request.get_json()                                            #Делаем запрос
    if not data:
        return jsonify({'error': 'No input data provided'}), 400  #если дата пустой то ошибка

    try:
        df = pd.DataFrame([data])                                           # превращаем дату в датафрэйм и делаем предсказание с помощью уже обученной модели
        prediction = model.predict(df)
        return jsonify({'survival_prediction': int(prediction[0])}), 200        #возращаем результат 1 или 0
    except Exception as e:
        return jsonify({'error': str(e)}), 500        # если какая нибудь любая ошибка то выводим ошибку 

if __name__ == '__main__':
    app.run(debug=True, port=5000)




Браузер открыл страницу (GET)
        ↓
Flask отдаёт HTML форму
        ↓
Пользователь заполнил форму и нажал кнопку
        ↓
JavaScript собрал данные и отправил POST-запрос
        ↓
Flask получил JSON → превратил в DataFrame
        ↓
Модель сделала предсказание → [0] или [1]
        ↓
Flask вернул JSON-ответ
        ↓
JavaScript показал результат на странице
"""


#docker run -d -p 80:80 docker/getting-started



"""| Команда                              | Что делает                                 | Пример                               |
| ------------------------------------ | ------------------------------------------ | ------------------------------------ |
| `docker --version`                   | Показывает версию Docker                   | `docker --version`                   |
| `docker info`                        | Информация о Docker                        | `docker info`                        |
| `docker images`                      | Список локальных образов                   | `docker images`                      |
| `docker ps`                          | Показывает запущенные контейнеры           | `docker ps`                          |
| `docker ps -a`                       | Показывает все контейнеры                  | `docker ps -a`                       |
| `docker pull IMAGE`                  | Скачать образ                              | `docker pull python:3.12`            |
| `docker run IMAGE`                   | Запустить контейнер                        | `docker run python:3.12`             |
| `docker run -it IMAGE`               | Запустить контейнер в интерактивном режиме | `docker run -it python:3.12`         |
| `docker run -d IMAGE`                | Запустить контейнер в фоне                 | `docker run -d nginx`                |
| `docker run -p HOST:CONTAINER IMAGE` | Пробросить порт                            | `docker run -p 5000:5000 flask-app`  |
| `docker run --name NAME IMAGE`       | Запустить контейнер с именем               | `docker run --name my_app nginx`     |
| `docker start ID`                    | Запустить остановленный контейнер          | `docker start my_app`                |
| `docker stop ID`                     | Остановить контейнер                       | `docker stop my_app`                 |
| `docker restart ID`                  | Перезапустить контейнер                    | `docker restart my_app`              |
| `docker rm ID`                       | Удалить контейнер                          | `docker rm my_app`                   |
| `docker rmi IMAGE`                   | Удалить образ                              | `docker rmi python:3.12`             |
| `docker exec -it ID bash`            | Зайти внутрь контейнера                    | `docker exec -it my_app bash`        |
| `docker logs ID`                     | Посмотреть логи контейнера                 | `docker logs my_app`                 |
| `docker logs -f ID`                  | Смотреть логи в реальном времени           | `docker logs -f my_app`              |
| `docker inspect ID`                  | Подробная информация о контейнере          | `docker inspect my_app`              |
| `docker cp SRC DEST`                 | Копировать файлы                           | `docker cp app.py my_app:/app/`      |
| `docker build -t NAME .`             | Собрать образ из Dockerfile                | `docker build -t ml-api .`           |
| `docker tag IMAGE NEW_NAME`          | Создать новый тег образа                   | `docker tag ml-api myrepo/ml-api:v1` |
| `docker push IMAGE`                  | Загрузить образ в реестр                   | `docker push myrepo/ml-api:v1`       |
| `docker pull IMAGE`                  | Скачать образ из реестра                   | `docker pull myrepo/ml-api:v1`       |
| `docker system prune`                | Очистить неиспользуемые ресурсы            | `docker system prune`                |
"""
