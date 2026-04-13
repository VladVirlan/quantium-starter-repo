def test_radio_present(dash_duo):
    from Visualiser import app

    dash_duo.start_server(app)

    radio = dash_duo.find_element("#region-radio")
    assert radio is not None


def test_radio_options(dash_duo):
    from Visualiser import app

    dash_duo.start_server(app)

    options = dash_duo.find_elements("input[type='radio']")
    assert len(options) == 5
