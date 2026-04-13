from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd

app = Dash()

colors = {
    "bg": "#F7FAF7",
    "card": "#FFFFFF",
    "text": "#2D2D2D",
    "accent": "#FFABD5",
    "muted": "#A8BFA8"
}

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
    hovermode="x unified",
    plot_bgcolor=colors["card"],
    paper_bgcolor=colors["card"],
    font=dict(color=colors["text"]),
    margin=dict(l=40, r=40, t=60, b=40)
)

fig.update_traces(line=dict(width=3))

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

app.layout = html.Div(
    style={
        "backgroundColor": colors["bg"],
        "fontFamily": "Segoe UI, sans-serif",
        "padding": "40px"
    },
    children=[

        html.H1(
            "Soul Foods",
            style={
                "textAlign": "center",
                "color": colors["text"],
                "marginBottom": "5px"
            }
        ),

        html.P(
            "Were sales higher before or after the Pink Morsel price increase on 15 Jan 2021?",
            style={
                "textAlign": "center",
                "color": colors["muted"],
                "marginBottom": "30px",
                "fontSize": "18px"
            }
        ),

        html.Div(
            dcc.Graph(id="line-graph", figure=fig),
            style={
                "backgroundColor": colors["card"],
                "padding": "25px",
                "borderRadius": "16px",
                "boxShadow": "0 6px 20px rgba(0,0,0,0.08)",
                "marginBottom": "30px"
            }
        ),

        html.Div(
            [
                html.P(
                    "Filter by Region",
                    style={
                        "fontWeight": "600",
                        "marginBottom": "10px",
                        "color": colors["text"]
                    }
                ),

                dcc.RadioItems(
                    id="region-radio",
                    options=[
                        {"label": "All", "value": "all"},
                        {"label": "North", "value": "north"},
                        {"label": "East", "value": "east"},
                        {"label": "South", "value": "south"},
                        {"label": "West", "value": "west"},
                    ],
                    value="all",
                    inline=True,
                    labelStyle={
                        "marginRight": "20px",
                        "cursor": "pointer"
                    }
                )
            ],
            style={
                "backgroundColor": colors["card"],
                "padding": "20px",
                "borderRadius": "16px",
                "boxShadow": "0 6px 20px rgba(0,0,0,0.08)",
                "maxWidth": "500px",
                "margin": "0 auto"
            }
        )
    ]
)

@app.callback(
    Output("line-graph", "figure"),
    Input("region-radio", "value")
)
def update_graph(selected_region):
    if selected_region == "all":
        filtered_df = df_monthly
    else:
        filtered_df = df_monthly[df_monthly["Region"] == selected_region]

    fig = px.line(
        filtered_df,
        x="Date",
        y="Sales",
        color="Region",
        title="Monthly Sales by Region",
        markers=True
    )

    fig.update_layout(
        template="plotly_white",
        hovermode="x unified",
        plot_bgcolor=colors["card"],
        paper_bgcolor=colors["card"],
        font=dict(color=colors["text"]),
        margin=dict(l=40, r=40, t=60, b=40)
    )

    fig.update_traces(line=dict(width=3))

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

    return fig

if __name__ == "__main__":
    app.run(debug=True)