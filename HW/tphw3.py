import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Creating DataFrame with your data
data = {
    'Vehicles': [427, 1187, 710, 672, 373, 527, 931, 929, 743, 571],
    'Trips_by_HHs': [3860, 13338, 4043, 6468, 2434, 4578, 9519, 8861, 9337, 3920]
}
df = pd.DataFrame(data)

# Setting up the linear regression model
model = LinearRegression()
X = df[['Vehicles']]  # Predictor variable
y = df['Trips_by_HHs']  # Response variable
model.fit(X, y)

# Generating predictions for the regression line
df['Predicted'] = model.predict(X)

# Calculating R-squared value
r_squared = r2_score(y, df['Predicted'])

# Coefficients
intercept = model.intercept_
slope = model.coef_[0]

# Plotting the regression analysis
plt.figure(figsize=(10, 6))
plt.scatter(df['Vehicles'], df['Trips_by_HHs'], color='blue', label='Actual Data')
plt.plot(df['Vehicles'], df['Predicted'], color='red', label='Regression Line')
plt.title('Regression Analysis')
plt.xlabel('Vehicles')
plt.ylabel('Trips by Households (HHs)')
plt.legend()
plt.grid(True)
plt.show()
