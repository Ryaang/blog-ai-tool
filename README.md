# Blog AI tool
Genertate seo content for static blog post with AI, support blog framework like Hexo, Hugo, etc.

## Features
- Generate seo content (title, **description**, keywords) for blog in markdown format
- Support blog framework like Hexo, Hugo, etc.
- Support multiple language
- Support multiple AI model like OpenAI, Qwen, Llama, etc. As long as the model provides openai-compatible API.

## Installation

```bash
pip install blog-ai-tool
```

## Usage

### Command Line

```bash
# Using default config file
blog-ai-tool

# Using custom config file
blog-ai-tool --config my-config.toml

# Override specific settings
blog-ai-tool --directory content/posts --model gpt-4
```

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

## Configuration

Download the [example config file](blog-ai-tool.toml) and modify it to your needs. Put the config file in your blog root directory, then run the command.

## License

MIT