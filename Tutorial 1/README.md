# Working with the basics - Ollama to run an LLM on your computer

Following the installation of [Ollama](https://ollama.com/) in [Tutorial 0](https://github.com/howardcheung/workshop-Interactive-AI-Agent/tree/main/Tutorial%200), you should have your Ollama ready in your computer. Let's see what you can do with it.

## Check your setup

To see what you have inside your *Ollama* installion, open any terminal window. For windows, you can do "Search" -> "cmd" and type this comman

```cmd
ollama --version
```

It will show you the version of *Ollama* on your computer. Following that, run

```cmd
ollama list
```

You should see the list of large language models on your computer. Following [Tutorial 0](https://github.com/howardcheung/workshop-Interactive-AI-Agent/tree/main/Tutorial%200), you should find *llama3.2:3b* that we will use in this workshop.

## Try it on terminal

Large language models can act as chatbots in the terminal windows too. Let's use *llama3.2:3b* for illustration. In the terminal window, first run

```cmd
ollama serve
```

If the operation is successful, you should be able to see log records of the operation. Then, leave this terminal window up and open another terminal window to continue.

If you encounter an error, no worries! *Ollama* should be running in the background. Let's continue.

Run the following command:

```cmd
ollama run llama3.2:3b
```

It will ask you to write something to start the conversation with the local LLM. Try it now!

To exit, simply write

```
/bye
```

in the conversation.

## Wanna try another LLM?

To use another LLM, visit [Ollama](https://ollama.com/) and look for other models in the top search bar. You can use some common LLM names like *mistral*, *deepseek*, *qwen* to start. 

As a general rule, for computers without GPU (*Graphical User Unit*), it is better not to download models with high parameters. Limit the ones you download under *4B* parameters would be a good place to start.

Once you have identified a model you want, in your terminal, type

```cmd
ollama pull {name of your model}
```

to download the model. For example, if you want the model *gemma3:1b*, run

```cmd
ollama pull gemma3:1b
```

Once the progress bar reaches 100%, run the model in your terminal using

```cmd
ollama run {name of your model}
```

and you can try another model to see what you will have differently!