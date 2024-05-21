import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

app = Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP], title="Superstore Analysis")
server = app.server

sidebar = dbc.Col(
    children=[
        html.Div(
            dcc.Link(
                f"{page['name']}", 
                href=page["relative_path"], 
                className = 'link-info link-underline link-underline-opacity-0 link-opacity-75-hover'
            )
        ) for page in dash.page_registry.values()
    ],  
    className="bg-gradient rounded ms-3 p-4 h-100",
    style={"background-color": "#0e1525"},
)

app.layout = dbc.Container(
    children = dbc.Row(
        children = [
            dbc.Col(sidebar, width={"size" : 2}),
            dbc.Col(dash.page_container)
        ],
        class_name="w-100"
    ),
    className = 'bg-black min-vh-100 pt-2 pb-2',
    fluid=True
)

if __name__ == '__main__':
    app.run_server(debug=False, use_reloader = True, dev_tools_hot_reload = True, dev_tools_hot_reload_interval = 10, dev_tools_ui = True)