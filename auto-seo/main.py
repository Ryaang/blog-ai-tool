import os
import argparse
from blog_seo import process_blog_directory

def main():
    parser = argparse.ArgumentParser(description='Process Hugo blog markdown files')
    parser.add_argument('--directory', '-d', help='Directory containing markdown files')
    parser.add_argument('--api-key', '-k', help='OpenAI Compatible API key', 
                       default=os.environ.get('OPENAI_API_KEY'))
    parser.add_argument('--base-url', '-b', help='OpenAI Compatible Base URL', 
                       default=os.environ.get('OPENAI_BASE_URL'))
    parser.add_argument('--model', '-m', help='OpenAI Compatible Model', 
                       default='gpt-4o-mini')
    parser.add_argument('--language', '-l', help='Language', 
                       default='the same as the blog content')

    
    args = parser.parse_args()
    
    if not args.api_key:
        raise ValueError("OpenAI API key must be provided either via --api-key or OPENAI_API_KEY environment variable")
    
    process_blog_directory(args.directory, args.api_key, args.base_url, args.model, args.language)

if __name__ == '__main__':
    main() 