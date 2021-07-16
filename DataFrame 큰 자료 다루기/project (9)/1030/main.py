import pandas as pd

df = pd.read_csv('data/enrolment_1.csv')

# 코드를 작성하세요.
df['status']='allowed'
df.loc[(df['year'] == 1 ) & (df['course name'] == 'information technology'), 'status'] = 'not allowed'
df.loc[(df['year'] == 4 ) & (df['course name'] == 'commerce'), 'status'] = 'not allowed'
allowed = df["status"] == "allowed"
course_counts = df.loc[allowed, "course name"].value_counts()
closed_courses = list(course_counts[course_counts < 5].index)
for course in closed_courses:
    df.loc[df["course name"] == course, "status"] = "not allowed"
# 정답 출력
df