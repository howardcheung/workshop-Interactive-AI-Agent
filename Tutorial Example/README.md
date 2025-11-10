
Install Anaconda

Install Ollama at [here](https://ollama.com/download/)

ollama serve

ollama pull llama3.2:3b

Run Anaconda Prompt

cd to current directory

conda create -n pocketflow python=3.10 pip jupyter pandas

conda activate pocketflow

pip install streamlit pocketflow openai

git clone https://github.com/The-Pocket/PocketFlow.git
cd PocketFlow
pip install -e .

streamlit run app.py --server.port 8081