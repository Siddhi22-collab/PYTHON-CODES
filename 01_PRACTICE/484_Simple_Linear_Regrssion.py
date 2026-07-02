class LinearRegression:

    def __init__(self):
        self.m = 0
        self.c = 0

    def mean(self, data):
        return sum(data)/len(data)

    def fit(self, X, Y):

        x_mean = self.mean(X)
        y_mean = self.mean(Y)

        numerator = 0
        denominator = 0

        for i in range(len(X)):
            numerator += (X[i]-x_mean)*(Y[i]-y_mean)
            denominator += (X[i]-x_mean)**2

        self.m = numerator/denominator
        self.c = y_mean - self.m*x_mean

    def predict(self, x):
        return self.m*x + self.c


X = [1,2,3,4,5,6,7,8,9,10]
Y = [3,4,5,6,8,9,11,12,13,15]

model = LinearRegression()

model.fit(X,Y)

print("Slope =",model.m)
print("Intercept =",model.c)

print("Prediction for X=12")
print(model.predict(12))