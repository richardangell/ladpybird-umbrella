import pandas as pd
import altair as alt
import panel as pn
import param



def df_viewer(df, response, height = 400):
    '''Function to produce interactive viewer in jupyter notebook to inspect
    columns in pandas DataFrame.

    User is able to select columns to display from a drop down box, which updates a
    scatter plot of the response by the particular column.

    This is used to supply the data and other items to DataFrameViewer class. Could 
    not find a way to pass them in an init() for the class.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the data to plot.
    response : str
        Name of response column in df.
    height : int
        Height of the panel output in notebook cell.

    Returns
    -------
    panel.layout.Row
        Panel to be rendered in jupyter notebook. Contains drop down to select column to 
        plot and plot which is updated which column selection is changed.

    '''

    class DataFrameViewer(param.Parameterized):
        '''Class to (scatter) plot response by column from pandas DataFrame.
        
        Particular column to plot response by is selected in a drop down box.

        Inspried by examples from;
        https://examples.pyviz.org/gapminders/gapminders.html#gallery-gapmindersInboxx.    
        '''

        column_selector = param.ObjectSelector(
            default = response, 
            objects = df.columns.values
        )

        def get_data(self):

            return df
    
        def altair_view(self):

            data  = self.get_data()

            title = f'{response} by {self.column_selector}'
            xlabel = self.column_selector
            ylabel = response

            plot  = alt.Chart(data).mark_circle().encode(
                alt.X(
                    self.column_selector, 
                    axis = alt.Axis(
                        title = xlabel
                    )
                ),
                alt.Y(
                    response, 
                    axis = alt.Axis(
                        title = ylabel
                    )
                )
            ).properties(title = title).interactive()

            return plot

    if not type(df) is pd.DataFrame:

        raise TypeError('df must be a pd.DataFrame')

    if not type(response) is str:

        raise TypeError('response must be a str')
      
    if not response in df.columns.values:

        raise ValueError(f'response {response} is not in df')

    if not type(height) is int:

        raise TypeError('height must be an int')
    
    viewer = DataFrameViewer()

    panel_with_viewer = pn.Row(
        viewer.param, 
        viewer.altair_view, 
        height = height
    )

    return panel_with_viewer


