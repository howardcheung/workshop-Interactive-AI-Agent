# An Agentic AI-assited writer for various topics

Let's try to have an agentic AI with a PocketFlow example of a topic writer [here](https://github.com/The-Pocket/PocketFlow/tree/main/cookbook/pocketflow-workflow) in a web-browser based interface with [Streamlit](https://streamlit.io/) to start the day!

## How it works

To run the Agentic AI interface for a topic writer, please finish the setup under [Tutorial 0](https://github.com/howardcheung/workshop-Interactive-AI-Agent/tree/main/Tutorial%200). Once you have done that, do the following

1. Start Anaconda Prompt
2. Build a virtual environment in the prompt window using
   ```
   conda create -n pocketflow python=3.10 pip jupyter pandas   
   ```
   Note that you only need to do this once.
3. Start the virtual environment and prepare it using the following commands:
   ```
   conda activate pocketflow
   pip install streamlit pocketflow openai
   ```
   Note that you only need to run *pip install streamlit pocketflow openai* once only. You only need to run *conda activate pocketflow* the next time you would like to run this again.
4. Move the current working directory of the promt to this directory with the *cd* command. To check it, type
   ```
   pwd
   ```
   and copy the path to replace the following example path and run it:
   ```
   cd "C:\Users\abc\Documents\workshop-Interactive-AI-Agent\Tutorial Example"
   ```
5. Run *Streamlit* with the following command:
   ```
   streamlit run app.py --server.port 8081
   ```
6. Enjoy the writer with any topic you can think of!

<p align="center">
<img src="/Tutorial%20Example/figures/running.png" alt="Interface with an article under processing" width="500">
</p>
