import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr, spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import statsmodels.api as sm

# Шаг 1: Загрузка данных
data = pd.read_csv('./db/statistics/dataBreath.csv')
data= data.fillna(data.mean())

time = 'exhalationTime'
frequency = 'exhalationFrequency'

# Шаг 2: Корреляционный анализ
# Корреляция Пирсона
pearson_corr, pearson_p = pearsonr(data[time].dropna(), data[frequency].dropna())
print(f'Pearson correlation: {pearson_corr}, p-value: {pearson_p}')

# Шаг 3: Регрессионный анализ
# Линейная регрессия
X = data[time].values.reshape(-1, 1)
y = data[frequency].values

# Модель линейной регрессии
regressor = LinearRegression()
regressor.fit(X, y)
y_pred = regressor.predict(X)

# Визуализация результатов регрессии
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue')
plt.plot(X, y_pred, color='red')
plt.title('Линейная регрессия: Длительность выдоха и Пульс на выдоха')
plt.xlabel('Длительность выдоха')
plt.ylabel('Пульс на выдоха')
plt.show()

# Коэффициент детерминации (R^2)
r2 = r2_score(y, y_pred)
print(f'Determination coefficient (R^2) {r2}')

# Шаг 4: Статистическая значимость
# Оценка значимости коэффициентов регрессии
X = sm.add_constant(X)  # Добавление константы для расчета интерсепта
model = sm.OLS(y, X).fit()
print(model.summary())
