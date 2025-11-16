# Setup procedure

Wanna try this tutorial? This is the place to start!

## Anaconda

First you need to install Anaconda. Follow this [link](https://www.anaconda.com/download) to download the most up-to-date Anaconda version and install it!

## Ollama

You will also need to have a large language model (LLM) on your computer. To do so, we use [Ollama](https://ollama.com/download/). Similar to the previous case, first you need to download it and install it.

After that, follow the instructions below:

1. Open a terminal
2. Run the command below to make sure that you have it installed and is callable. If not, restart your computer
   ```
   ollama --version
   ```
3. Run the following to download the LLM we will be using throughout the tutorials:
   ```
   ollama pull llama3.2:3b
   ```
4. Run the following command to start the ollama if it is not automatically done by your ollama installation:
   ```
   ollama serve
   ```
   
## What else?

The rest of the procedures would be listed in separate tutorials. Go ahead and start to have fun at [Tutorial Example](https://github.com/howardcheung/workshop-Interactive-AI-Agent/tree/main/Tutorial%20Example)!
