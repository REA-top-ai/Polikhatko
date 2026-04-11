import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler

# Пример данных о дронах (можно заменить на реальные данные)
data = {
    'Масса (кг)': [1.2, 3.5, 0.8, 5.0, 2.1, 4.0, 1.5, 6.0, 0.5, 7.0],
    'Дальность полета (км)': [5, 20, 2, 50, 10, 30, 7, 100, 1, 150],
    'Скорость полета (км/ч)': [40, 60, 30, 80, 50, 70, 45, 90, 25, 100],
    'Время полета (мин)': [30, 45, 20, 60, 35, 50, 40, 90, 15, 120],
    'Грузоподъемность (кг)': [0.5, 2.0, 0.2, 5.0, 1.0, 3.0, 0.8, 10.0, 0.1, 15.0],
    'Применение': ['Разведка', 'Доставка', 'Разведка', 'Военный', 'Наблюдение', 'Доставка', 'Наблюдение', 'Военный',
                   'Разведка', 'Военный']
}

# Создаем DataFrame
df = pd.DataFrame(data)

# Разделяем данные на признаки (X) и целевую переменную (y)
X = df.drop('Применение', axis=1)
y = df['Применение']

# Разделяем данные на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Масштабируем данные
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Обучаем модель (Random Forest)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Предсказываем на тестовых данных
y_pred = model.predict(X_test_scaled)

# Оцениваем точность
accuracy = accuracy_score(y_test, y_pred)
print(f'Точность модели: {accuracy:.2f}')


# Функция для классификации нового дрона
def classify_drone():
    print("\nВведите параметры дрона для классификации:")
    mass = float(input("Масса (кг): "))
    distance = float(input("Дальность полета (км): "))
    speed = float(input("Скорость полета (км/ч): "))
    flight_time = float(input("Время полета (мин): "))
    payload = float(input("Грузоподъемность (кг): "))

    # Создаем DataFrame для нового дрона
    new_drone = pd.DataFrame([[mass, distance, speed, flight_time, payload]],
                             columns=['Масса (кг)', 'Дальность полета (км)', 'Скорость полета (км/ч)',
                                      'Время полета (мин)', 'Грузоподъемность (кг)'])

    # Масштабируем данные
    new_drone_scaled = scaler.transform(new_drone)

    # Предсказываем класс
    prediction = model.predict(new_drone_scaled)
    print(f"\nРекомендуемое применение дрона: {prediction[0]}")


# Пример использования
if __name__ == "__main__":
    classify_drone()