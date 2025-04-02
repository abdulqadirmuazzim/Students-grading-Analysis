# #️⃣Introduction
Welcome to the **students Performance analysis** where we interprete the data of the **Students performance dataset** in order to discover patterns and ways in which students are able to achieve good grades and high scores. We'll search for correlations between features as well as other relationships that will help us achieve our goal. In this project we'll of course handle missing values, sort out the biases in the data and normalize skewed distrubutions (if any)

-------------------------
## 🎯Project goal
Investigate patterns as to how and why students are able to achieve good performance based on certain features like hours of study or sleep, attendance, class participation, extracurriculars and so on.

-------------------------
## 📊Analysis
Here we'll analyse, clean, visualize and draw insightful conclusions on the data, in our analysis we'll sort out the various biases that come with the data like how the `Grade` column doesn't refleact the academic performance of a student and so on.

-------------------------
## 💾Data
This dataset is real data of 5,000 records collected from a private learning provider.
The dataset includes key attributes necessary for exploring patterns, correlations, and insights related to academic performance. Dataset contains some missing values, bias in some features and imbalanced distribution.


| <h1>Columns</h1>              |   <h1>Information</h1>                 |
| -----------                   | -----------------                      |
| Student_ID                    |     Unique identifier for each student.|
| First_Name                    |     Student’s first name.              
| Last_Name                     |     Student’s last name.
| Email                         |     Contact email (can be anonymized).
| Gender                        |     Male, Female, Other.
| Age                           |     The age of the student.
| Department                    |     Student's department (e.g., CS, Engineering, Business).
| Attendance (%)                |     Attendance percentage (0-100%).
| Midterm_Score                 |     Midterm exam score (out of 100).
| Final_Scor                    |     Final exam score (out of 100).
| Assignments_Avg               |     Average score of all assignments (out of 100).
| Quizzes_Avg                   |     Average quiz scores (out of 100).
| Participation_Score           |     Score based on class participation (0-10).
| Projects_Score                |     Project evaluation score (out of 100).
| Total_Score                   |     Weighted sum of all grades.
| Grade                         |     Letter grade (A, B, C, D, F).
| Study_Hours_per_Week          |     Average study hours per week.
| Extracurricular_Activities    |     Whether the student participates in extracurriculars (Yes/No).
| Internet_Access_at_Home       |     Does the student have access to the internet at home? (Yes/No).
| Parent_Education_Level        |     Highest education level of parents (None, High School, Bachelor's, Master's, PhD).
| Family_Income_Level           |     Low, Medium, High.
| Stress_Level (1-10)           |     Self-reported stress level (1: Low, 10: High).
| Sleep_Hours_per_Night         |     Average hours of sleep per night.



-------------------------------------
## 🤔Questions:
- What factors contribute most to high student performance?
- Does family background influence academic success?
- How does gender relate to scores?
- Do extracurricular activities impact grades?
- Do stress levels negatively impact academic performance?
- Are students with more sleep performing better?
- Is the any **significant** difference in the average scores of various departments?

----
# Conclusion
1. What factors contribute most to high student performance?
    - Although there were biases regarding Total_Score and Grade, we refined our analysis by engineering features that better reflect performance, with features such as Participation_Score, Assignments_Avg, Quizzes_Avg, Projects_Score, Midterm_Score, and Final_Score.

2. Does family background influence academic success?
    - No. Both visualizations and hypothesis tests indicate no significant difference in performance among students from different family backgrounds.

3. How does gender relate to scores?
    - Gender has no correlation with Total_Score, as confirmed through statistical tests.

4. Do extracurricular activities impact grades?
    - No. Although participation in extracurricular activities varies among students, there is no statistically significant difference in academic performance between those who participate and those who do not.

5. Do stress levels negatively impact academic performance?
    - Stress levels do not significantly affect overall performance. Students who reported high stress and those with low stress had similar average scores, as confirmed by hypothesis testing.

6. Are students with more sleep performing better?
    - No strong relationship was found between sleep hours and academic performance.

7. Is there a significant difference in the average scores across departments?
    - No. There is no significant variation in average scores among the four departments.