import streamlit as st
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Iris Flower Predictor",
    page_icon="🌸",
    layout="centered"
)

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    iris = load_iris()

    df = pd.DataFrame(
        iris.data,
        columns=iris.feature_names
    )

    df['species'] = iris.target

    return df, iris.target_names

df, target_names = load_data()

# ---------------- TRAIN MODEL ----------------
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(df.iloc[:, :-1], df['species'])

# ---------------- TITLE ----------------
st.title("🌸 Iris Flower Species Predictor")
st.markdown(
    "Predict Iris flower species using a Machine Learning model."
)

# ---------------- SIDEBAR ----------------
st.sidebar.header("🌿 Input Flower Features")

sepal_length = st.sidebar.slider(
    "Sepal Length (cm)",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max()),
    float(df['sepal length (cm)'].mean())
)

sepal_width = st.sidebar.slider(
    "Sepal Width (cm)",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max()),
    float(df['sepal width (cm)'].mean())
)

petal_length = st.sidebar.slider(
    "Petal Length (cm)",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max()),
    float(df['petal length (cm)'].mean())
)

petal_width = st.sidebar.slider(
    "Petal Width (cm)",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max()),
    float(df['petal width (cm)'].mean())
)

# ---------------- INPUT DATA ----------------
input_data = np.array([
    [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]
])

# ---------------- PREDICTION ----------------
prediction = model.predict(input_data)
prediction_proba = model.predict_proba(input_data)

predicted_species = target_names[prediction][0]

# ---------------- DISPLAY RESULT ----------------
st.subheader("🔍 Prediction Result")

st.success(f"Predicted Species: **{predicted_species.upper()}**")

# ---------------- CONFIDENCE ----------------
st.subheader("📊 Prediction Confidence")

confidence_df = pd.DataFrame(
    prediction_proba,
    columns=target_names
)

st.bar_chart(confidence_df.T)

# ---------------- USER INPUT DISPLAY ----------------
st.subheader("📝 User Input Features")

input_df = pd.DataFrame(
    input_data,
    columns=df.columns[:-1]
)

st.dataframe(input_df)

# ---------------- DATASET PREVIEW ----------------
with st.expander("📂 View Dataset"):
    st.dataframe(df.head())

# ---------------- MODEL INFO ----------------
with st.expander("🤖 Model Information"):
    st.write("""
    - Model Used: Random Forest Classifier
    - Dataset: Iris Dataset
    - Library: Scikit-learn
    """)

# ---------------- FOOTER ----------------
st.markdown("---")
st.markdown(
    "Built with ❤️ using Streamlit and Scikit-learn"
)