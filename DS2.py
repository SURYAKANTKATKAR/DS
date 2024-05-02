import seaborn as sns
import matplotlib.pyplot as plt

# Load the Titanic dataset
titanic_data = sns.load_dataset('titanic')

# Display the first few rows of the dataset
print(titanic_data.head())

# Visualize survival rate based on gender
plt.figure(figsize=(8, 6))
sns.countplot(x='survived', hue='sex', data=titanic_data)
plt.title('Survival Count by Gender')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# Visualize survival rate based on passenger class
plt.figure(figsize=(8, 6))
sns.countplot(x='survived', hue='class', data=titanic_data)
plt.title('Survival Count by Passenger Class')
plt.xlabel('Survived')
plt.ylabel('Count')
plt.show()

# Visualize survival rate based on age
plt.figure(figsize=(10, 6))
sns.histplot(x='age', hue='survived', data=titanic_data, bins=30, kde=True, palette='muted')
plt.title('Survival Distribution by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

#Plot histogram of ticket prices
plt.figure(figsize=(10, 6))
sns.histplot(titanic_data['fare'], bins=20, kde=True, color='skyblue')
plt.title('Distribution of Ticket Prices')
plt.xlabel('Fare')
plt.ylabel('Frequency')
plt.show()
