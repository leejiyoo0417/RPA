import pandas as pd
#col-names = ['과목번호','과목명','강의실','시간수']
#list = list([['c1','인공지능개론','R1'3],
#['c2','웃음치료','R2',2],
#['c3','경영학','r3',3],
#['c4','3d디자인','r4',4],
#['c5','웃스포트경영','r2',2],
#['c6','예술의 세계','r3',1],
#])

#df = pd.Datafeame(list1, columns=col_names)
#print(df)
data = {

'과목번호'  : ['c1','c2','c3','c4','c5','c6'],
'과목명'  : ['인공지능개론','웃음치료','경영학','3d디자인','스포츠 경영학','예술의 세계'],
'강의실' : ['r1','r2','r3','r4','r5','r6'],
'시간수' : [3,2,3,4,2,1]
}
df = pd.Datafeame(data)
print(df,end='\n\n')

sr_no = df.loc[2]
print(sr_no,end='\n\n')

cell_name = df.loc[2]['과목명']
print(cell_name)

df.to_csv('file.csv', index=False)

print("#################################")

df['담당교수'] = ['홍길동','김펄수','이영희','박영수','최영희','김영수']
print(df, end='\n\n')

df.loc[6] = ['c7','통계학','r7',3,' 이철수']
print(df,end='\n\n')

df1 = df.drop(['강의실'],axis=1)
print(df1,end='\n\n')

df2 = df.drop([5],axis=0)
print(df2,end='\n\n')

print("#################################")

#범위찾기
#행 찾기
print(df.loc[0:2],end='\n\n')
print(df.loc[0:2],end='\n\n')
#열 찾기
print(df['과목명','담당교수']== '경영학', end='\n\n')
print(df.loc[:,'강의실,':'담당교수'], end='\n\n')


print("#################################")
#조건 찾ㄱㅣ
#행 찾기
print(df['과목명']== '경영학', end='\n\n')
print(df.loc['과목명']== '경영학', end='\n\n')
print([df['과목명'] > 2], end='\n\n')


#셀찾기 
print(df.loc[df['과목명']== '경영학']['담당교수'], end='\n\n')
print(df.loc[df['과목명']== '경영학']['담당교수'].valuse[0], end='\n\n')

#df.loc[3]['담당교수']='이경영'
df.loc[3,'담당교수']='이경영'
print(df,end='\n\n')

#df.loc[df['과목명'] == ' 경영학']['담당교수'] = '이경영'
df.loc[df['과목명'] == ' 경영학']['담당교수'] = '이경영'
print(df,end='\n\n')

print(df.loc[df['과목명']== '경영학','담당교수'].valuse[0], end='\n\n')









