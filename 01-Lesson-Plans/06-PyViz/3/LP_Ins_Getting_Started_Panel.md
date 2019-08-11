### 4. Instructor Do: Getting Started with Panel (10 mins)

Students will receive a small demo on how to use Panel at a high level.

**Files:**

* [getting_started_panel.ipynb](Activities/04-Ins_Getting_Started_Panel/Solved/getting_started_panel.ipynb)

Open the solved file, and give students a high level run down of how Panel works. Begin by showing students how to prep **Panel** within Jupyter Lab:

* Panel can be imported into Python using the import command.

    ```python
    import panel as pn
    ```

* Panel comes equipped with its own set of libraries, functions, and widgets. An example library is the `panel.interact` library.

    ```python
    from panel.interact import interact
    from panel import widgets
    ```

* When working with Panel in Jupyter Lab, the Jupyter Lab Panel plugin is required. The plugin can be activated using the `extension` command. If the extension is not activated, Panel objects will not render in Jupyter Lab.

    ```python
    pn.extension()
    ```

Walk students through how the `interact` function is used to create quick and easy widget UI controls:

* A commonly used **Panel** function is `panel.interact`. `interact` allows users to create widget UI controls to manipulate function parameters.

  * These parameter widgets provide a convenient and easy way for users to change the values populating the visual, which is extremely handy when completing impact analysis.

  * The **Panel** parameter widget bar will only appear if a function was passed that accepts parameters. If a function without parameters is passed to the `interact` function, the `interact` function will execute, but it will not provide the widget bar.

  * It's important to note that this parameter widget is an added benefit provided by Panel. Not all dashboarding technologies provide this convenient feature.

    ![interact_data_struct.gif](Images/interact_data_struct.gif)

* Most Panel interact function accepts other functions as arguments. This is because the **interact** widget was designed from a functional programming point of view. This approaches heavily relies on developers passing functions to functions, which allows Panel to dynamically render content and plots based off of user input/interaction.

  * Imagine creating a dashboard reporting on housing sales by city across 10 years. Instead of having all 10 years of data for every city shown on a plot, you might want to limit the data to a specific year. A **Panel** select list could be used to select the year to report on.

    ```python
      # Define function to choose a year
      def choose_year(year):
          return year
    ```

    ```python
    # Declare one list of years to be used in a Panel select list
    list_of_years = ['2019','2018','2017','2016','2015']
    interact(chooseYear, x=list_of_years)
    ```

    ```python
    # Declare a second list of years to be used in a Panel select list
    list_of_years_2 = ['2014','2013','2012','2011','2010']
    interact(chooseYear, x=list_of_years)
    ```

    ![interact_data_struct_2.gif](Images/interact_data_struct_2.gif)

In addition to Python data structures, the `interact` function can be used with plots. Discuss how **Panel** can be used with plots.

* When used with plots, `interact` will still need to be passed a function that will render the plot.

* **Panel** will then create UI widgets to allow users to dynamically change parameters. An example would be plotting housing transactions data where the number of records plotted is parameterized. The `interact` function will create a widget that allows users to change configure the number of records being plotted.

    ```python
    # Define function to create plot
    def plot_housing_tx(number_of_sales):
        housing_transactions = pd.DataFrame({
        "years": np.random.randint(2010,2019,number_of_sales),
        "sales": np.random.randint(53,500,number_of_sales),
        "foreclosures": np.random.randint(10,147,number_of_sales)}).sort_values(['years','sales'])

        return housing_transactions.hvplot.scatter(x='sales',
                                        y='foreclosures',
                                        c='years',
                                        colormap='viridis',
                                                title='Alleghany, PA Housing Transactions')

    # Render plot with Panel interactive widget
    interact(plot_housing_tx, number_of_sales=100)
    ```

    ![interact_plot.gif](Images/interact_plot.gif)
