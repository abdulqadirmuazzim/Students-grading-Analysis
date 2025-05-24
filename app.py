import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
from matplotlib import pyplot as plt
import pandas as pd


st.title("Students Performance Analysis")
st.divider()
welcome = """
    Welcome to the **Students Performance Analysis Dashboard**! 🚀  

This **Streamlit** dashboard was built as a powerful complement to the **Jupyter Notebook analysis**, designed to provide an interactive and dynamic way to explore students’ performance data. This tool lets you visualize insights effortlessly.  

Navigate through different sections to explore **summary statistics**, detailed graphical representations, and data-driven observations. From **gender distribution** to performance comparisons across departments, everything you need is at your fingertips!  

Uncover meaningful patterns and insights—happy exploring! 🎉  

    """

st.write(welcome)

df = pd.read_csv("Cleaned_student_data.csv")

st.subheader("Summary Statistics")
dtype = st.selectbox("Select a data type", options=["Numerical", "Categorical"])

dtype = "number" if dtype == "Numerical" else "object"

st.dataframe(df.describe(include=dtype))


univariate, bivariate = st.columns(2)

# get the ID fields
id_fields = ["Student_ID", "First_Name", "Last_Name", "Email"]


@st.fragment
def uni_plots():
    # drop them and select the categorical columns
    categorical_cols = (
        df.drop(columns=id_fields).select_dtypes(include="object").columns
    )

    plot_type = st.selectbox(
        "Select a Plot Type", options=["Population based", "Score based"]
    )

    if plot_type == "Population based":
        column = st.selectbox(label="Choose a Feature", options=categorical_cols)

        # The first chart is for columns with more than 3 unique values
        def bar_plot():
            # get the mean Final_Scores for each unique value in the column
            counts = df[column].value_counts()
            # plot a bar chart
            st.bar_chart(counts)

        # The first chart is for columns with 3 or less unique values
        def pie_plot():

            feature = df[column].value_counts()
            fig = go.Figure(
                data=[
                    go.Pie(
                        labels=feature.index,
                        values=feature,
                    )
                ]
            )
            st.plotly_chart(fig)

        if df[column].nunique() <= 3:
            pie_plot()
        else:
            bar_plot()

    else:
        column = st.selectbox(label="Choose a Feature", options=categorical_cols)

        chart_space = st.empty()
        # get the mean Final_Scores for each unique value in the column
        data = df.groupby(column).Final_Score.mean()
        # plot a bar chart
        st.bar_chart(data)


@st.fragment
def bi_plots():
    data = df.drop(columns=id_fields + ["Unnamed: 0"])

    x = st.selectbox(label="X-Axis", options=data.columns.to_list())
    y = st.selectbox(label="Y-Axis", options=data.columns.to_list())
    # So we got 3 possibilities:
    # - Either there are 2 categorical variables
    #   + use multiple bar charts
    #   + use a stacked bar chart
    # - Either there are 2 numerical variables
    #   + we use a scatter plot
    #   + we use a density plot
    # - Either they are categorical and numerical variables
    #   + use multiple box plots

    # numerical cols
    num_cols = data.select_dtypes(include="number")

    # categorical cols
    cat_cols = data.select_dtypes(include="object")
    chart_space = st.empty()

    if (x in cat_cols) and (y in cat_cols):
        # create a cross tab
        xtab = pd.crosstab(data[x], data[y])
        # instantiate the plotly figure
        fig = go.Figure()
        # loop over the columns
        for col in xtab.columns:
            # add the bar to the figure
            fig.add_trace(go.Bar(x=xtab.index, y=xtab[col], name=col))

        fig.update_layout(barmode="relative", title=f"Bar plot for {x} against {y}")

        chart_space.plotly_chart(fig)

    if (x in num_cols) and (y in num_cols):
        chart_space.scatter_chart(data=data, x=x, y=y)

    if (x in cat_cols) and (y in num_cols):
        mean = st.checkbox("Compare averages?")
        if mean:
            y_vals = data.groupby(x)[y].mean()
            fig = px.bar(x=data[x].unique(), y=y_vals)
            chart_space.plotly_chart(fig)
        else:
            fig = px.box(data, x=x, y=y)
            chart_space.plotly_chart(fig)

    elif (x in num_cols) and (y in cat_cols):
        mean = st.checkbox("Compare averages?")
        if mean:
            y_vals = data.groupby(y)[x].mean()
            fig = px.bar(x=data[y].unique(), y=y_vals)
            chart_space.plotly_chart(fig)
        else:
            fig = px.box(data, x=y, y=x)
            chart_space.plotly_chart(fig)


with univariate:
    st.write("Univariate Analysis")
    with st.container(border=True, height=500):
        uni_plots()


with bivariate:
    st.write("Bivariate Analysis")
    with st.container(border=True, height=500):
        bi_plots()


st.write("Multivariate Analysis")
with st.container(border=True):
    data = df.drop(columns=id_fields + ["Unnamed: 0"])
    # numerical cols
    num_cols = data.select_dtypes(include="number")

    # categorical cols
    cat_cols = data.select_dtypes(include="object")

    @st.fragment()
    def multi_plots():
        x = st.selectbox(label="X-axis", options=num_cols.columns.to_list())
        y = st.selectbox(label="Y-axis", options=num_cols.columns.to_list())
        color = st.selectbox(label="Color", options=cat_cols.columns.to_list())
        size = st.selectbox(label="Size", options=[None] + num_cols.columns.to_list())

        st.scatter_chart(
            data=df.sample(frac=0.3, replace=False),
            x=x,
            y=y,
            color=color,
            size=size,
        )

    multi_plots()


st.write(
    "If there are any tweaks needed you can open an issue at the [github reop](https://github.com/abdulqadirmuazzim/Students-grading-Analysis/issues)!"
)
