def test_graph_present(dash_duo):
    from Visualiser import app

    dash_duo.start_server(app)

    graph = dash_duo.find_element("#line-graph")
    assert graph is not None
