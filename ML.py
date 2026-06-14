import pandas as pd
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
    app.run(host='0.0.0.0', debug=True, port=5000)




"""
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