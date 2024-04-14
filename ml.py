import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Load the data
df = pd.read_csv('peak_data_01.csv')

# Split the features and target variables for both models
x1 = df[['X-Kulma', 'Y-Kulma', 'Z-Kulma']]
x2 = df[['X-Kulma2', 'Y-Kulma2', 'Z-Kulma2']]
y1 = df['Phi']
y2 = df['Phi2']

# Split the data into training and testing sets for both models
x1_train, x1_test, y1_train, y1_test = train_test_split(x1, y1, test_size=0.1)
x2_train, x2_test, y2_train, y2_test = train_test_split(x2, y2, test_size=0.1)

# Initialize and train the first model
model1 = DecisionTreeRegressor()
model1.fit(x1_train, y1_train)

# Initialize and train the second model
model2 = DecisionTreeRegressor()
model2.fit(x2_train, y2_train)

# Make predictions for both models
prediction1 = model1.predict(x1_test)
prediction2 = model2.predict(x2_test)

# Calculate Mean Squared Error for both models
mse1 = mean_squared_error(y1_test, prediction1)
mse2 = mean_squared_error(y2_test, prediction2)

print("Mean Squared Error for Phi:", mse1)
print("Mean Squared Error for Phi2:", mse2)
