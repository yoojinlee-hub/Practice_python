import pandas as pd
import numpy as np

df = pd.read_csv('data/enrolment_2.csv')
studentnumlist = df['course name'].value_counts()
# 코드를 작성하세요.
auditoriumclasslist = list(studentnumlist[studentnumlist > 80].index)
mediumroomclasslist = list(studentnumlist[(studentnumlist <= 80) & (studentnumlist > 40)].index)
largeroomclasslist = list(studentnumlist[(studentnumlist <= 40) & (studentnumlist > 15)].index)

notassignedboolseries = df['status'] == 'not allowed'
auditoriumboolseries = df['course name'].isin(auditoriumclasslist)
largeroomboolseries = df['course name'].isin(largeroomclasslist)
mediumroomboolseries = df['course name'].isin(mediumroomclasslist)

df['room assignment'] = np.where(notassignedboolseries, 'not allowed', 
                        np.where(auditoriumboolseries, "Auditorium", 
                        np.where(largeroomboolseries, "Large room", 
                        np.where(mediumroomboolseries, "Medirum room", "Small room"))))
# 정답 출력
df