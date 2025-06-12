from dash import Dash, dcc, html
import plotly.graph_objs as go
import numpy as np

app = Dash(__name__)

def generate_dummy_drift_data():
    dates = np.arange(30)
    drift_scores = np.random.rand(30)
    return dates, drift_scores

dates, scores = generate_dummy_drift_data()

app.layout = html.Div([
    html.H2("Feature Data Drift Monitoring"),
    dcc.Graph(
        id="drift-graph",
        figure={
            "data": [
                go.Scatter(
                    x=dates,
                    y=scores,
                    mode="lines+markers",
                    name="Drift Score"
                )
            ],
            "layout": go.Layout(
                yaxis={"title": "Drift Metric"},
                xaxis={"title": "Days"},
                hovermode="closest",
            ),
        },
    ),
])

if __name__ == "__main__":
    app.run_server(debug=False, host="0.0.0.0", port=8050)
