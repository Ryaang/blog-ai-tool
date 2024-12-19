# 🤖 Blog AI tool
[![PyPI - Version](https://img.shields.io/pypi/v/blog-ai-tool)](https://pypi.org/project/blog-ai-tool/) [![PyPI - License](https://img.shields.io/pypi/l/blog-ai-tool)](https://pypi.org/project/blog-ai-tool/)   [![Static Badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-8A2BE2)](README-Zh.md) [![Static Badge](https://img.shields.io/badge/English-blue)](README.md)

🌟 Useful ai tools for blog framework like Hexo, Hugo, etc, as long as you manage your blog with markdown format. [简体中文](README-Zh.md)

## ✨ Features
- 🎯 Generate seo content (title, **description**, keywords) for blog posts in markdown format
- 📝 Generate ai summary for blog posts
- 🌍 Translate blog posts to multiple languages
- 🛠️ Support blog framework like Hexo, Hugo, etc.
- 🌐 Support multiple language
- 🧠 Support multiple AI model like OpenAI, Qwen, Llama, etc. As long as the model provides openai-compatible API.

## 🛠️ Installation

```bash
pip install blog-ai-tool
```

## 🚀 Usage

### Command Line

```bash
# Using default config file
blog-ai-tool

# if the above command is not working, try to use this following command instead
python -m blog_ai_tool

# Using custom config file
blog-ai-tool --config my-config.toml

# Override specific settings
blog-ai-tool --directory content/posts --model gpt-4
```

Disclaimer: AI may destory your blog, please use git to **backup** your blog before use. Also, its not recommended to use this tool without **reviewing** the generated content. Always check the generated content before publishing. The best time to use this tool is right after you have written the blog post, before publishing.

### Python API

```python
from blog_ai_tool import HugoBlogProcessor, load_config

# Load configuration
config = load_config("blog-ai-tool.toml")

# Initialize processor
processor = HugoBlogProcessor(
    api_key="your-api-key",
    base_url="https://api.openai.com/v1",
    model="gpt-4",
    language="auto",
    config=config
)

# Process a single file
processor.process_markdown("path/to/post.md")
```

## 📚 Configuration

Download the [example config file](blog-ai-tool.toml) and modify it to your needs. Put the config file in your blog root directory (the same level as as your blog config file), then run the command.

## 🤝 Development

We sincerely welcome any contributions to this project. Please feel free to submit your ideas and suggestions.

## 📝 License

MIT