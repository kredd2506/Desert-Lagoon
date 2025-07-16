# Gradio Chat App

A lightweight Gradio front-end for interacting with the NRP chat endpoint via LiteLLM.

---

## 🚀 Features

- **Zero-configuration** chat UI powered by Gradio
- **Pluggable** LiteLLM models with function-calling support
- **Secure** handling of secrets via environment variables

---

## 📦 Prerequisites

- **Python 3.8+**
- **Git**
- (Optional) Virtual environment tool: `venv`, `virtualenv`, or similar

For NRP and Nautilus users, log in with your `.edu` email at:  
[NRP AI Documentation](https://nrp.ai/documentation/userdocs/ai/llm-managed/)

---

## 🔧 Installation

1. **Clone the repository**  
   ```bash
   git clone git@github.com:yourusername/gradio-chat-app.git
   cd gradio-chat-app
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**  
   ```bash
   cp .env.example .env
   ```
   Open `.env` in a text editor and set the following:  
   ```dotenv
   MODEL=gemma3                # LiteLLM model alias
   API_TOKEN=<your_key>        # Your LiteLLM API key
   ENDPOINT=https://llm.nrp-nautilus.io/
   ```

---

## 🔑 Obtaining Your LiteLLM API Key

1. Sign up or log in to your LiteLLM provider portal.
2. Generate a new API key.
3. Copy the key and paste it into the `API_TOKEN` field in your `.env` file.

---

## ▶️ Usage

Run the application:  
```bash
python app.py
```

A Gradio UI will launch locally (default: [http://localhost:7860](http://localhost:7860)). Open the URL in your browser and start chatting!

---

## 🤖 Supported Models

| Alias          | LiteLLM Identifier                                    | Key Features                                          |
|----------------|-------------------------------------------------------|-------------------------------------------------------|
| deepseek-r1    | RedHatAI/DeepSeek-R1-0528-quantized.w4a16            | 685B params, INT4 quantization, 131K tokens, tool calling, Claude/o3 performance |
| gemma3         | google/gemma-3-27b-it                                | 27B params, 131K tokens, agentic workflows, 140+ languages |
| llama3         | meta-llama/Llama-3.2-90B-Vision-Instruct             | 90B params, multimodal (vision), 131K tokens         |
| llama3-sdsc    | meta-llama/Llama-3.3-70B-Instruct                    | 70B params, 8 languages, 131K tokens, tool use      |
| embed-mistral  | intfloat/e5-mistral-7b-instruct                      | 7B params, embeddings                               |
| gorilla        | gorilla-llm/gorilla-openfunctions-v2                 | Function calling                                    |
| llava-onevision | llava-hf/llava-onevision-qwen2-7b-ov-hf             | Vision                                              |
| olmo           | allenai/OLMo-2-0325-32B-Instruct                     | 32B params, open source                             |
| phi3           | microsoft/Phi-3.5-vision-instruct                    | Vision                                              |
| watt           | watt-ai/watt-tool-8B                                 | Function calling                                    |

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
```
