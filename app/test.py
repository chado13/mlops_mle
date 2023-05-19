import joblib
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

X, y = load_iris(return_X_y=True, as_frame=True)

# X,y를 train, valid로 나누기
# random_state는 다시 호출 할 때 동일한 학습/평가 데이터 세트를 생성할 수 있도록 지정해주는 난수값
X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, random_state=2022)

# 데이터셋을 표준화하는 스케일러
scaler = StandardScaler()

# 데이터 표준화
scaled_X_train = scaler.fit_transform(X_train)
scaled_X_valid = scaler.transform(X_valid)

classifier = SVC()
classifier.fit(scaled_X_train, y_train)

train_pred = classifier.predict(scaled_X_train)
valid_pred = classifier.predict(scaled_X_valid)

train_acc = accuracy_score(y_true=y_train, y_pred=train_pred)
valid_acc = accuracy_score(y_true=y_valid, y_pred=valid_pred)


joblib.dump(scaler, "scaler.joblib")
joblib.dump(classifier, "classifier.joblib")
