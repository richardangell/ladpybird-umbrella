import pandas as pd
import ipywidgets as widgets



def column_select_widget(df):
    '''Function to create selector widget to choose column in df.'''

    if not type(df) is pd.DataFrame:

        raise TypeError('df must be a pd.DataFrame')

    widget = widgets.Select(
        options = df.columns.values,
        value = df.columns.values[0],
        rows = 2,
        description = 'Column:',
        disabled = False
    )

    return widget

