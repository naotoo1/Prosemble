from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from hybrid1 import Hybrid

# Data_set and scaling
scaler = StandardScaler()
X, y = load_iris(return_X_y=True)
X = X[:, 0:2]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
scaler.fit(X_train)
X_test = scaler.transform(X_test)
print(X_train.shape, y_train.shape)

# summary of prototype labels
proto_classes = [0, 1, 2]

# Transferred learned prototypes for glvq, gmlvq and celvq models respectively
new_prototypes_1 = (
    [[-1.1442775, 0.8578415], [-0.22741659, -1.3264811], [1.4355098, 0.14914764]])
new_prototypes_2 = (
    [[-0.9664123, 0.8180202], [-0.14138626, -0.7539766], [1.0968374, 0.0320867]])
new_prototypes_3 = (
    [[-1.601125, 1.136284], [0.22535476, - 1.4961139], [1.7082069 - 0.34369266]])

# object of the Hybrid Class
tryy_1 = Hybrid(new_prototypes_1, proto_classes, 3, omega_matrix=None, matrix='n')
tryy_2 = Hybrid(new_prototypes_2, proto_classes, 3, omega_matrix=None, matrix='n')
tryy_3 = Hybrid(new_prototypes_2, proto_classes, 3, omega_matrix=None, matrix='n')

# predictions with transfered learned prototypes of glvq, gmlvq and celvq
pred1 = tryy_1.predict(x_test=X_test)
pred2 = tryy_2.predict(x_test=X_test)
pred3 = tryy_3.predict(x_test=X_test)

all_pred = [pred1, pred2, pred3]

# predictions based on max votes
final_pred = tryy_1.pred_prob(x=X_test, y=all_pred)

# summary results of the accuracy
print(tryy_1.accuracy(y_test, final_pred))

# summary of prediction probability
print(tryy_1.prob(x=X_test, y=all_pred))
