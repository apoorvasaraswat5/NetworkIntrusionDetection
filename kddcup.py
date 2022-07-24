from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix

np.random.seed(0)



df = pd.read_csv('kddcup.txt', sep=",", header=None)
df.columns = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment", "urgent", "hot", "num_failed_logins", "logged in", "num_compromised", "root_shell", "su_attempted", "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds", "is_host_login", "is_guest_login", "count", "srv_count","serror_rate", "srv_serror_rate", "rerror_rate","srv_rerror_rate","same_srv_rate", "diff_srv_rate", "srv_diff_host_rate", "dst_host_count","dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate", "dst_host_same_src_port_rate","dst_host_srv_diff_host_rate", "dst_host_serror_rate","dst_host_srv_serror_rate","dst_host_rerror_rate", "dst_host_srv_rerror_rate", "clss"]

features = df.columns[:41]


df["protocol_type"] = pd.factorize(df.protocol_type)[0]
df["service"] = pd.factorize(df.service) [0]
df["flag"] = pd.factorize(df.flag) [0]
df["clss"] = pd.factorize(df.clss) [0]
print(df.head(5))

df['is_train'] = np.random.uniform(0,1, len(df)) <= .75
train, test = df[df['is_train']==True], df[df['is_train']==False]
print('Number of observations in training data: ', len(train))
print('Number of observations in test data: ', len(test))

y = train.clss

clf = RandomForestClassifier(n_jobs=2, random_state=0)
clf.fit(train[features],y)
predictions = clf.predict(test[features])

print('CONFUSION MATRIX>>>>')
#print(confusion_matrix(test['clss'],predictions))
print(pd.crosstab(test['clss'], predictions, rownames=['Actual Class'], colnames=['Predicted Class']))

print('Train Accuracy: ', accuracy_score(train['clss'], clf.predict(train[features])))
print('Test Accuracy: ', accuracy_score(test['clss'], predictions))

print('List of importance of features: ')
print(list(zip(train[features], clf.feature_importances_)))





