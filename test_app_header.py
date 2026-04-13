def test_header_present(dash_duo):
    from Visualiser import app

    dash_duo.start_server(app)

    header = dash_duo.find_element("h1")
    assert header is not None
    assert header.text == "Soul Foods"
