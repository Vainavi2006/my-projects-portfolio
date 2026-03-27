import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("students.csv")

# Step 5: Total & Average
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = df['Total'] / 3

# Step 6: Find topper
topper = df.loc[df['Total'].idxmax()]
print("Topper Details:")
print(topper)

# Step 7: Add grades
def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    else:
        return 'C'

df['Grade'] = df['Average'].apply(grade)
print("\nFinal Student Data:\n")
print(df.to_string(index=False))

# Step 8: Graph
plt.bar(df['Name'], df['Average'])
for i in range(len(df)):
    plt.text(i, df['Average'][i], round(df['Average'][i],2), ha='center')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance")
plt.show()


# Step 9: Save file
df.to_csv("result.csv", index=False)

# Show final data
print("\nFinal Student Data:\n")
print(df.to_string(index=False))
