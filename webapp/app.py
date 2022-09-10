from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go

app = Dash(__name__)


def display_dropdown(id, options, value):
    return dcc.Dropdown(id=id, options=options, value=value, clearable=False)


app.layout = html.Div([
    html.Center(html.H4('Predict heart disease based on health indicators')),
    html.P("BMI:"),
    dcc.Input(id='bmi', value='Type here'),
    html.P("Smoker:"),
    display_dropdown("smoke", ["Yes", "No"], "No"),
    html.P("Alcohol drinker:"),
    display_dropdown("alcohol_drinker", ["Yes", "No"], "No"),
    html.P("Had stroke:"),
    display_dropdown("stroke", ["Yes", "No"], "No"),
    html.P("Physical health:"),
    dcc.Input(id='physical_health', value='Type here'),
    html.P("Mental health:"),
    dcc.Input(id='mental_health', value='Type here'),
    html.P("Walks differently:"),
    display_dropdown("diff_walking", ["Yes", "No"], "No"),
    html.P("Sex:"),
    display_dropdown("sex", ["Male", "Female"], "Male"),
    html.P("Age category:"),
    display_dropdown("age_category", ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 or older'], "18-24"),
    html.P("Race:"),
    display_dropdown("race", ['American Indian/Alaskan Native', 'Asian', 'Black', 'Hispanic', 'Other', 'White'], "White"),
    html.P("Diabetic:"),
    display_dropdown("diabetic", ['No', 'No, borderline diabetes', 'Yes', 'Yes (during pregnancy)'], "No"),
    html.P("Physical activity:"),
    display_dropdown("physical_activity", ["Yes", "No"], "No"),
    html.P("Gen health:"),
    display_dropdown("gen_health", ['Excellent', 'Fair', 'Good', 'Poor', 'Very good'], "Good"),
    html.P("Sleep time:"),
    dcc.Input(id='sleep_time', value='Type here'),
    html.P("Has asthma:"),
    display_dropdown("asthma", ["Yes", "No"], "No"),
    html.P("Has kidney disease:"),
    display_dropdown("kidney_disease", ["Yes", "No"], "No"),
    html.P("Has skin cancer:"),
    display_dropdown("skin_cancer", ["Yes", "No"], "No"),
    html.Div(id='hidden_div', style={'display': 'none'}),
    html.Center(html.Button('Submit health indicators', id='submit_button')),
])            

@app.callback(
    Output('hidden_div', 'children'),
    Input('bmi', 'value'))
def on_button_press(value):
    print("### -> " + value)


app.run_server(debug=True)