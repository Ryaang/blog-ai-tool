# 🤖 博客 AI 工具
[![PyPI - Version](https://img.shields.io/pypi/v/blog-ai-tool)](https://pypi.org/project/blog-ai-tool/) [![PyPI - License](https://img.shields.io/pypi/l/blog-ai-tool)](https://pypi.org/project/blog-ai-tool/)   [![Static Badge](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-8A2BE2)](README-Zh.md) [![Static Badge](https://img.shields.io/badge/English-blue)](README.md)

🌟 适用于 Hexo、Hugo 等博客框架的 AI 工具，只要你使用 markdown 格式管理博客即可使用。[English](README.md)

## ✨ 特性
- 🎯 为 markdown 格式的博客文章生成 SEO 内容（标题、**描述**、关键词）
- 📝 为博客文章生成 AI 摘要
- 🌍 将博客文章翻译成多种语言
- 🛠️ 支持 Hexo、Hugo 等博客框架
- 🌐 支持多语言
- 🧠 支持 OpenAI、Qwen、Llama 等多种 AI 模型，只要该模型提供兼容 OpenAI 的 API 即可

## 🛠️ 安装

```bash
pip install blog-ai-tool
```

## 🚀 使用方法

### 命令行

```bash
# 使用默认配置文件
blog-ai-tool

# 如果上述命令不起作用，请尝试使用以下命令
python -m blog_ai_tool

# 使用自定义配置文件
blog-ai-tool --config my-config.toml

# 覆盖特定设置
blog-ai-tool --directory content/posts --model gpt-4
```

免责声明：AI 可能会破坏你的博客，使用前请使用 git **备份**你的博客。同时，不建议在**未审核**生成内容的情况下使用此工具。发布前务必检查生成的内容。使用此工具的最佳时机是在你刚写完博客文章后、发布前。

### Python API

```python
from blog_ai_tool import HugoBlogProcessor, load_config

# 加载配置
config = load_config("blog-ai-tool.toml")

# 初始化处理器
processor = HugoBlogProcessor(
    api_key="your-api-key",
    base_url="https://api.openai.com/v1",
    model="gpt-4",
    language="auto",
    config=config
)

# 处理单个文件
processor.process_markdown("path/to/post.md")
```

## 📚 配置

下载[示例配置文件](blog-ai-tool.toml)并根据需要修改。将配置文件放在博客根目录（与博客配置文件同级），然后运行命令。

## 🤝 开发

我们诚挚欢迎对这个项目的任何贡献。请随时提交你的想法和建议。

## 📝 许可证

MIT
