import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('peak_data_01.csv')


# Split the features and target variables for both models
y1 = df['Massa[GeV]']
x1 = df.drop(columns=['Tapahtuma', 'Tapahtuma.1', 'Massa[GeV]', 'Tyyppi1', 'Tyyppi2', 'Massa(kg)', 'Phi(deg)', 'Phi2(deg)'])

# Split the data into training and testing sets for both models
x1_train, x1_test, y1_train, y1_test = train_test_split(x1.values, y1, test_size=0.1)

# Initialize and train the first model
model1 = DecisionTreeRegressor()
model1.fit(x1_train, y1_train)


# Make predictions for both models
prediction1 = model1.predict(x1_test)

print(model1.predict([[4, 3, 100, 41, 5, 2, -5, 1, 25, -2, -10, 27, 10, 2, -1, 1]]))

# Calculate Mean Squared Error for both models
mse1 = mean_squared_error(y1_test, prediction1)

print("Mean Squared Error for Phi:", mse1)
