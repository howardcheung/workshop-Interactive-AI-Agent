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
<img src="/Tutorial%203/figures/plotting.png" alt="Automatic Plotting of 100 Random Numbers" width="500">
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
* Numpy