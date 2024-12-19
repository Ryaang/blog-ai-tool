import os
import argparse
import tomli
from .blog_seo import process_blog_directory

def load_config(config_path: str = "blog-ai-tool.toml") -> dict:
    """Load configuration from TOML file"""
    try:
        with open(config_path, "rb") as f:
            return tomli.load(f)
    except FileNotFoundError:
        print(f"Config file not found: {config_path}")
        print("Please create a config file, you can get the example from https://github.com/Ryaang/blog-ai-tool")
        exit(1)

def main():
    parser = argparse.ArgumentParser(description='Process Hugo blog markdown files')
    parser.add_argument('--config', '-c', help='Path to config file', default='blog-ai-tool.toml')
    parser.add_argument('--directory', '-d', help='Directory containing markdown files')
    parser.add_argument('--api-key', '-k', help='OpenAI Compatible API key')
    parser.add_argument('--base-url', '-b', help='OpenAI Compatible Base URL')
    parser.add_argument('--model', '-m', help='OpenAI Compatible Model')
    parser.add_argument('--language', '-l', help='Language')

    args = parser.parse_args()
    
    # Load config from file
    config = load_config(args.config)
    
    # Command line arguments override config file
    api_key = args.api_key or os.environ.get("OPENAI_API_KEY") or config["openai"]["api_key"]
    if not api_key:
        raise ValueError("OpenAI API key must be provided via config file, --api-key, or OPENAI_API_KEY environment variable")
    
    directory = args.directory or config["blog"]["directory"]
    base_url = args.base_url or os.environ.get("OPENAI_BASE_URL") or config["openai"]["base_url"]
    model = args.model or config["openai"]["model"]
    language = args.language or config["blog"]["language"]
    
    process_blog_directory(
        directory=directory,
        api_key=api_key,
        base_url=base_url,
        model=model,
        language=language,
        config=config
    )

if __name__ == '__main__':
    main()