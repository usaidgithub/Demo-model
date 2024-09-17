import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report


csv_path = r'Your csv file path here'
df = pd.read_csv(csv_path)

print("First few rows of the dataset:")
print(df.head())
print("Columns in the dataset:")
print(df.columns)

if 'FloodRisk' not in df.columns:
    print("Creating synthetic target column 'FloodRisk' for demonstration purposes.")
    df['FloodRisk'] = [0] * len(df)  
X = df[['Latitude', 'Longitude']]
y = df['FloodRisk']  
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Model accuracy: {accuracy * 100:.2f}%")
print("Classification report:")
print(report)

def predict_glof():
    try:
        latitude = float(input("Enter Latitude: "))
        longitude = float(input("Enter Longitude: "))
        
        user_input = pd.DataFrame([[latitude, longitude]], columns=['Latitude', 'Longitude'])
        
        user_input_scaled = scaler.transform(user_input)
        
        prediction = model.predict(user_input_scaled)
        
        if prediction[0] == 1:
            print("Prediction: There is a risk of a Glacial Lake Outburst Flood (GLOF) at this location.")
        else:
            print("Prediction: There is no significant risk of a GLOF at this location.")
    
    except ValueError:
        print("Invalid input. Please enter numerical values for latitude and longitude.")

predict_glof()
