import frontmatter
import os
from typing import Dict
from .base_processor import BaseProcessor

class HugoBlogProcessor(BaseProcessor):
    def __init__(self, api_key: str, base_url: str, model: str, language: str, config: dict):
        super().__init__(api_key, base_url, model, config)
        self.language = language
        if self.config["blog"]["language"] == "auto":
            self.language = "the same as the blog content"

    def generate_metadata(self, content: str) -> Dict[str, str]:
        """Generate metadata using OpenAI based on content"""
        metadata_config = self.config["metadata"]
        ai_summary_config = metadata_config["ai_summary"]
        if ai_summary_config:
            ai_summary_task = f"""4. Based on the following blog content, generate a summary (max {metadata_config['ai_summary_length']} words with plain text)"""
        else:
            ai_summary_task = ""
        prompt = f"""Based on the following blog content, generate:
1. A concise title (max {metadata_config['max_title_length']} words)
2. A brief description (max {metadata_config['max_description_length']} words)
3. {metadata_config['keyword_count']} relevant keywords (space-separated)
{ai_summary_task}
The language should be {self.language}.

Content:
{content}

Format response as JSON with keys: title, description, keywords{", summary" if ai_summary_config else ""}"""

        response = self._call_openai(prompt)
        return self._extract_json(response)

    def process_markdown(self, file_path: str) -> None:
        """Process markdown file and update its front matter"""
        with open(file_path, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
        
        content = post.content
        metadata = post.metadata

        # Check for missing metadata
        needs_update = False
        if not metadata.get('title') or not metadata.get('description') or not metadata.get('keywords'):
            print(f"Generating metadata for {file_path}")
            generated = self.generate_metadata(content)
            needs_update = True

            # Only update missing fields
            if not metadata.get('title'):
                metadata['title'] = generated['title']
            if not metadata.get('description'):
                metadata['description'] = generated['description']
            if not metadata.get('keywords'):
                metadata['keywords'] = generated['keywords']
            if generated.get("summary") and not metadata.get('summary'):
                metadata['summary'] = generated['summary']


        if needs_update:
            # Create new post with updated metadata
            new_post = frontmatter.Post(content, **metadata)
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(new_post))

def metadata_blog_directory(directory: str, api_key: str, base_url: str, model: str, language: str, config: dict):
    """Process all markdown files in the directory"""
    processor = HugoBlogProcessor(api_key, base_url, model, language, config)
    retry_count = config["system"]["retry_count"]
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                attempts = retry_count
                while attempts > 0:
                    try:
                        file_path = os.path.join(root, file)
                        processor.process_markdown(file_path) 
                        break
                    except Exception as e:
                        print(f"Failed to process {file_path}: {e}")
                        print(f"Attempts remaining: {attempts-1}")
                        attempts -= 1
