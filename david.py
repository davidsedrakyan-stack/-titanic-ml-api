#import random
from mimetypes import guess_type

#secret = random.randint(1, 20)

#while True:
 #   guess = int(input("угадай число от одного до двадцати: "))
 #   if guess > secret:
  #      print("слишком большое чило")
 #   elif guess < secret:
 #       print("слишком маленькое чило")
 #   elif guess == secret:
 #       print("Ты угадал")
 #       print("!!!!!!!!!!!!")



"""import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 6, 8, 10])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print(predictions)

score = model.score(X_test, y_test)
print(score)

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)"""


from sklearn.linear_model import LinearRegression
import numpy as np
"""from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)   #обучение с помощью Pipeline

pipe.fit(X_train, y_train)
pred = pipe.predict(X_test)

"""
"""
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import matplotlib.pyplot as plt

# 1. Загрузка (пример: house prices)
df = pd.read_csv("house-price-prediction.csv")

# -------------------------
# 2. Очистка данных
# -------------------------

# оставим только числовые признаки
df = df.select_dtypes(include=[np.number])

# заполним пропуски
df = df.fillna(df.mean())

# -------------------------
# 3. Target (цена)
# -------------------------

y = df['price']
X = df.drop('price', axis=1)

# -------------------------
# 4. Логарифмирование target 🔥
# -------------------------

y = np.log1p(y)

# -------------------------
# 5. Split
# -------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# 6. МОДЕЛИ
# -------------------------

models = {
    "LinearRegression": Pipeline([
        ('scaler', StandardScaler()),
        ('model', LinearRegression())
    ]),

    "RandomForest": RandomForestRegressor(),

    "GradientBoosting": GradientBoostingRegressor()
}

results = {}

# -------------------------
# 7. Обучение и сравнение
# -------------------------

for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    results[name] = (mae, mse)

    print(f"\n{name}")
    print("MAE:", mae)
    print("MSE:", mse)

# -------------------------
# 8. График (предсказание vs реальность)
# -------------------------

best_model = models["RandomForest"]
y_pred = best_model.predict(X_test)

plt.scatter(y_test, y_pred)
plt.xlabel("True values")
plt.ylabel("Predictions")
plt.title("True vs Predicted")
plt.show()

"""
"""
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)



df['target'] = iris.target

X = df[iris.feature_names]
y = df['target']

# split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

# scaling
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
                                                             #iris
# модель
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

# оценка
accuracy = knn.score(X_test, y_test)
print(f"Точность: {accuracy * 100:.2f}%")

# предсказание
example = np.array([[5.1, 3.5, 1.4, 0.2]])
example = scaler.transform(example)

prediction = knn.predict(example)
print("Предсказанный класс:", iris.target_names[prediction[0]])

"""















