import pandas as pd
import matplotlib.pyplot as plt
# Load data
df = pd.read_csv("students.csv")
#total & average
df['Total'] = df[['Maths', 'Science', 'English']].sum(axis=1)
df['Average'] = df['Total']/3
#find topper
topper = df.loc[df['Total'].idxmax()]
print("Topper Details:")
print(topper)
#Add grades
def grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    else:
        return'C'
df['Grade'] = df['Average'].apply(grade)
print("\nSubject Toppers:")
print("Maths Topper:", df.loc[df['Maths'].idxmax()]['Name'])
print("Science Topper:", df.loc[df['Science'].idxmax()]['Name'])
print("English Topper:", df.loc[df['English'].idxmax()]['Name'])
#graph
plt.bar(df['Name'],df['Average'])
for i in range(len(df)):
    plt.text(i, df['Average'][i], round(df['Average'][i],2), ha='center')
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance")
plt.show()
#Save file
df.to_csv("result.csv", index=False)
#show final data
print("\nFinal Data:")
print(df.to_string(index=False))