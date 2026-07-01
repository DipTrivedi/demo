from sklearn.linear_model import LinearRegression

x=[[1],[2],[3],[4],[5]]
y=[40,50,60,70,80]

model=LinearRegression()

model.fit(x,y)

hours=float(input("enter how many hours you studied..:"))

predicted_mark=model.predict([[hours]])

print(f"Based on hours {hours} you may score around {predicted_mark}")