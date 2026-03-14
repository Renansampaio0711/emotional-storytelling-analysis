import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("C:/Users/scleber/OneDrive/Desktop/Projeto Análise de Dados/Movie and Emotional Attachment Survey.csv")

#DISTRIBUCTION BY GENDER

df["Gender"].value_counts()
df["Gender"].value_counts().plot(kind="bar")
plt.title("Distribuição por gênero")
plt.show()

#AUDIENCE ATTACHMENT SCORE MEAN

print('Audience Attachment Score Mean:')
print(df["Audience Attachment Score"].mean())

#EMOTIONAL STORYTELLING SCORE MEAN

print('Emotional Storytelling Score Mean:')
print(df["Emotional Storytelling Score"].mean())

#Emotional Storytelling Score X  Audience Attachment Score  

df = pd.read_csv("C:/Users/scleber/OneDrive/Desktop/Projeto Análise de Dados/Movie and Emotional Attachment Survey.csv")
# Emotional Storytelling Score X  Audience Attachment Score  
plt.scatter(df["Emotional Storytelling Score"], df["Audience Attachment Score"])
plt.xlabel("Storytelling")
plt.ylabel("Apego emocional")
plt.title("Storytelling vs Apego emocional")
plt.show()

#Correlation Matrix

corr_table = df.corr(numeric_only=True)
print(corr_table)

#Correlation between Emotional Storytelling Score  and Audience Attachment Score :
corr_scores = df[["Emotional Storytelling Score", "Audience Attachment Score"]].corr()
print(corr_scores) #here we can see that there is a strong correlation between Emotional Storytelling Score and Audience Attachment Score


# Questions most correlated with Emotional Storytelling Score

corr = df.corr(numeric_only=True)

corr_story = corr["Emotional Storytelling Score"].sort_values(ascending=False)

print(corr_story)


# Questions most correlated with Emotional Storytelling Score

corr = df.corr(numeric_only=True)

corr_story = corr["Audience Attachment Score"].sort_values(ascending=False)

print(corr_story)


# Correlation by Gender