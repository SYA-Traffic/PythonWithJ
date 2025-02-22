import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

# Data preparation
data = {
    "TAZ": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Trips_by_HHs": [3860, 13338, 4043, 6468, 2434, 4578, 9519, 8861, 9337, 3920],
    "Vehicles": [427, 1187, 710, 672, 373, 527, 931, 929, 743, 571]
}
df = pd.DataFrame(data)

# Regression Model
X = df[['Vehicles']]  # Predictor
y = df['Trips_by_HHs']  # Response
model = LinearRegression()
model.fit(X, y)

# Prediction
y_pred = model.predict(X)


# Plotting
plt.figure(figsize=(10, 6))
plt.scatter(X, y, color='blue', label='Actual data')
plt.plot(X, y_pred, color='red', label=f'Regression line (R^2={r2_score(y, y_pred):.2f})')
plt.title('Regression Analysis of Trips by Households vs. Vehicles')
plt.xlabel('Vehicles')
plt.ylabel('Trips by Households')
plt.legend()
plt.grid(True)
plt.show()
