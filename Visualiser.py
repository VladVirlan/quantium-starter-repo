from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("./data/output.csv")
df.columns = ["Sales", "Date", "Region"]

df["Sales"] = pd.to_numeric(df["Sales"])
df["Date"] = pd.to_datetime(df["Date"])

df_monthly = df.groupby(
    [pd.Grouper(key="Date", freq="MS"), "Region"]
)["Sales"].sum().reset_index()

fig = px.line(df_monthly, x="Date", y="Sales", color="Region", title="Monthly Sales by Region", markers=True)

fig.update_layout(
    template="plotly_white",
    xaxis_title="Date",
    yaxis_title="Sales",
    legend_title="Region",
    hovermode="x unified"
)

fig.add_shape(
    type="line",
    x0="2021-01-15",
    x1="2021-01-15",
    y0=0,
    y1=1,
    xref="x",
    yref="paper",
    line=dict(color="red", width=3, dash="dash")
)

fig.add_vrect(
    x0="2021-01-15",
    x1=df["Date"].max(),
    fillcolor="red",
    opacity=0.1,
    line_width=0
)

app.layout = html.Div(children=[
    html.H1(children="Soul Foods"),

    html.Div(children="""
        Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?
    """),

    dcc.Graph(id='line-graph', figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True)