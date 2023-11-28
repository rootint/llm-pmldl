# NeuraLearn

## Introduction
Our project aims to enhance the knowledge base and accessibility of Large Language Models (LLMs) for Machine Learning engineers. We wanted to solve the following downsides of modern LLMs:

The free version of ChatGPT has a very early cutoff (2021), so you can’t ask about any modern research papers. Our models were fine-tuned on the latest research papers, and mitigate that issue.
The next downside is the accessibility. The best models are expensive (GPT-4 is ~2000 rubles per month, good luck paying for it with a Russian card). Also, all the state-of-the-art LLMs require using a VPN to access the websites, making the models even less accessible. Our solution can be run locally on almost any machine and provide GPT-3.5-like results for free with no internet or VPN.
The last downside is the customizability. You can’t fine-tune any of the mainstream models, like GPT and Claude because they are closed-source (well, you can, but it costs a lot and you will have to send your data to a third party). The models we are using are easily fine-tunable on consumer-grade GPUs and thanks to LoRa, you can easily change the model’s purpose by changing the adapter weights. (LoRa weights are 15MB, while the entire model is 14GB)


## How to use

1. Download any model you would like from [my HF Repo](https://huggingface.co/RNDRandoM/neuralearn-qlora-ft-7b/tree/main) (The recommended one is llama2_v2.gguf)
2. Put the downloaded model into the models/ folder
3. If you have downloaded the llama2_v2 model, skip the next step:
4. Change the model_path on line 67 in [server.py](./production/server.py)
5. Run the [server.py](./production/server.py). It's going to launch a web server on http://localhost:1337. You can use the model via the /chain endpoint or use the Flutter app, putting your URL into the lib/message_provider.dart.

## Contributions
**Daria Lebedeva:**
Developed a comprehensive and diverse dataset for Machine Learning (ML) by initially utilizing the Stanford Question Answering Dataset (SQuAD), then generating new data using ChatGPT and Wikipedia for topics in ML, Deep Learning, and Neural Networks. Then, expanded this dataset by incorporating questions from recent ML research papers, mining ML interviews for insights, and finally, enriching it with industry-relevant questions through web scraping, notably from "Top 100 Interview Questions on Artificial Intelligence" by M.K. Jeeva Rajan.

**Danil Timofeev:**
Experimented with 7 billion parameter LLaMa 2-based models, starting with the baseline LLaMa 2 model, effective in general ML topics but not the latest research. Encountered limitations using the HonestLLaMa 2 7B due to its lack of LoRa fine-tuning support. Tested the Orca 2 7B model, but it showed performance issues. Ultimately, achieved the best results by fine-tuning the base LLaMa 2 7B model on the custom dataset. Quantized the models for M1 GPU deployment and implemented a RAG approach to enhance outputs.


## Special Thanks
- [llama.cpp](https://github.com/ggerganov/llama.cpp) project for a simplified process of quantization
- [This Github Gist](https://gist.github.com/python273/563177b3ad5b9f74c0f8f3299ec13850) for how to stream models' output in a webserver