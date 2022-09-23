import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# input dataset
wbreastcancer_route = "data.csv"
df_wbreastcancer = pd.read_csv(wbreastcancer_route)

# change M, B to 1, 0
df_wbreastcancer["diagnosis"] = df_wbreastcancer["diagnosis"].replace(["M", "B"], [1, 0])

# divide the features
feature_mean_corr, feature_se_corr, feature_worst_corr = ["diagnosis"], ["diagnosis"], ["diagnosis"]
feature_mean, feature_se, feature_worst = [], [], []
for i in df_wbreastcancer.columns:
    if "mean" in i:
        feature_mean.append(i)
        feature_mean_corr.append(i)
    elif "se" in i:
        feature_se.append(i)
        feature_se_corr.append(i)
    elif "worst" in  i:
        feature_worst.append(i)
        feature_worst_corr.append(i)

# streamlit
st.title("Wisconsin Breast Cancer Diagnostic dataset")
result1 = st.button('aim?')
result2 = st.button('the correlation between attibutes')
result3 = st.button('the density plots of perimeter and concave, and why the?')
result4 = st.button('any result?')
if result1:
    st.write("""
    how to estimate whether the cancer is benign or maliganant by its attribute?
    """)
if result2:
    fig, axis = plt.subplots(1, 3, figsize=(30, 8))
    # mean
    axis[0] = sns.heatmap(df_wbreastcancer[feature_mean_corr].corr(), cmap="viridis", annot=True, ax=axis[0])
    # se
    axis[1] = sns.heatmap(df_wbreastcancer[feature_se_corr].corr(), annot=True, ax=axis[1], cmap="viridis")
    # worst
    axis[2] = sns.heatmap(df_wbreastcancer[feature_worst_corr].corr(), annot=True, ax=axis[2], cmap="viridis")
    axis[0].set_title("mean")
    axis[1].set_title("se")
    axis[2].set_title("worst")
    st.pyplot(fig)
if result3:
    st.write("the two highest correlation with diagnosis is perimeter_mean anc concave point mean")
    a = sns.displot(data=df_wbreastcancer, x="concave points_mean", kind="kde", hue="diagnosis")
    b = sns.displot(data=df_wbreastcancer, x="perimeter_mean", kind="kde", hue="diagnosis")
    c = sns.displot(data=df_wbreastcancer, x="concave points_mean", y="perimeter_mean", hue="diagnosis", kind="kde")
    st.pyplot(a)
    st.pyplot(b)
    st.pyplot(c)

if result4:
    st.write("""We found, most malignants' concave points and perimeter are higher than benign's.
    we can distinguish part of benigns and part of malignant. But we cannot distinguish them from the overapping area.
    """)
