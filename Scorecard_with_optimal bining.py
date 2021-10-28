import pandas as pd
from optbinning import Scorecard, BinningProcess
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from optbinning.scorecard.plots import plot_ks, plot_auc_roc



df_application = pd.read_csv('/train_cleaned.csv', low_memory=True)
df_application.set_index('A', inplace=True)
df_application_train, df_application_test, y_train, y_test = train_test_split(
    df_application, df_application.TARGET, test_size=0.2, random_state=42)
list_features = df_application_train.drop(columns=['TARGET']).columns.values
list_categorical = df_application_train.select_dtypes(include=['object', 'category']).columns.values
selection_criteria = {"iv": {"min": 0.02, 'max':1, "strategy": "highest"}}
logreg = LogisticRegression(C=3, max_iter=1000, random_state=42)
%%time
scaling_method = "pdo_odds"
scaling_method_data = {"pdo": 20, "odds": 50, "scorecard_points": 600}

scorecard = Scorecard(
    target='TARGET',
    binning_process=binning_process,
    estimator=logreg,
    scaling_method=scaling_method,
    scaling_method_params=scaling_method_data,
    intercept_based=False,
    reverse_scorecard=True,
)

scorecard.fit(df_application_train)

df_application_test.loc[:,"predict_proba"] = scorecard.predict_proba(df_application_test)[:, 1]
df_application_test.loc[:,"score"] = scorecard.score(df_application_test)

plot_ks(df_application_test.TARGET, df_application_test.score, savefig=True, fname='scorecard_ks_plot.jpeg', dpi=100)
plot_ks(df_application_test.TARGET, df_application_test.predict_proba)
plot_auc_roc(df_application_test.TARGET, df_application_test.score, savefig=True, fname='scorecard_rocauc_plot.jpeg', dpi=100)
plot_auc_roc(df_application_test.TARGET, df_application_test.predict_proba)

import pickle

with open('scorecard_model.pickle', 'wb') as pfile:
   pickle.dump(scorecard, pfile)
   
with open("scorecard_model.pickle", 'rb') as scorecard_pickle:
	scorecard_production = pickle.load(scorecard_pickle)
print(scorecard_production)


# For a few samples
scorecard_production.score(df_application_test.iloc[0:3, :])