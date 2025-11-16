# Working with the intermediates 1 - Streamlit for the interface

Welcome to Tutorial 3! This tutorial would guide you through ways to create interaction functions with users with a web interface based on [Streamlit](https://streamlit.io/).

## Beginning

To start, let's use the virtual environment we created in [Tutorial Example](https://github.com/howardcheung/workshop-Interactive-AI-Agent/tree/main/Tutorial%20Example). In "Anaconda Prompt", run

```cmd
conda activate pocketflow
streamlit run app.py --server.port 8081
```

You should be able to see an automatic plot with random numbers generated using the basic plotting example from *Streamlit*. 

<p align="center">
<img src="/Tutorial%203/figures/plotting.png" alt="Automatic Plotting ofs Random Numbers" width="500">
</p>


Using the above command, you are instructing

* *Streamlit*, a python library, to host a *Streamlit* application at the port of your local computer port 8081
* Your web browser to open a web application being hosted at the local computer port 8081
* The *Streamlit* application to run following the instructions in *app.py*

This web hosting operation creates a default front-end for your computer user to interact with using your web browser.

## What is being done in *app.py*

Now let's look at app.py in details. In the beginning, we have

```python
import streamlit as st
import numpy as np
import time
```

These lines import the required Python libraries for the operation later. This includes

* Streamlit - the library that creates the web interfaces
* Numpy - the library that does numerical functions like vector addition, matrix multiplication and random number generation
* time - the default Python library that does applications with time like countdown and time recording

The second batch of codes

```python
st.title("Plotting Demo")
st.caption("""
This demo illustrates a combination of plotting and animation with Streamlit. We're generating a bunch of random numbers in a loop for around 5 seconds. Enjoy!
"""
)

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.rand(1, 1)
chart = st.line_chart(last_rows)
```
sets up the streamlit interface, including

* the title of the web interface as "Plotting Demo"
* the caption of the web interface
* the sidebar with a progress bar at 0% and an empty text
* a line chart with one random number from the standard normal distribution

Now let's look at the next batch

```python
for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text(f"{i}% complete")
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)
```

This instructs Python to iterate 100 times of the following procedure

* Create a vector of 5 random numbers from the standard normal distribution
* Create another set of numbers using the previous 5 numbers and their cumulative sums (i.e. sum functions with previous entries repeatedly in Excel)
* Add these numbers to the previously created random number vector to create a new random number vector with 5 new entries
* Add the new vector into the plot with the old random numbers
* Renew the text in the sidebar progress bar for the completion rate
* Update the progress bar with the new percentage of completion
* Prepare the new vector for the addition in the next iteration
* Ask Python to wait for 0.05 seconds before next iteration

and have the chart updated accordingly.

Finally, once you finish the plot, *Streamlit* is asked to

```python
progress_bar.empty()
st.button("Rerun")
```

empty the sidebar progress bar and prepare a "Rerun" button for you to rerun the above procedure.

## Your own trial!

Based on the above, can you try

* change the plot into a bar chart?
* create a new button to choose what chart you would like to run after an initial run?

Try to explore [Streamlit Documentation](https://docs.streamlit.io/develop/api-reference) to figure them out!

<p align="center">
<img src="/Tutorial%203/figures/ans.png" alt="Try it!" width="500">
</p>
