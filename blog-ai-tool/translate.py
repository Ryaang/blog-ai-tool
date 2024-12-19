import os
from typing import Optional, Dict, List
from .base_processor import BaseProcessor

class TranslationProcessor(BaseProcessor):
    def __init__(self, api_key: str, base_url: str, model: str, config: dict, directory: str):
        super().__init__(api_key, base_url, model, config)
        self.source_directory = directory
        self.target_languages = config.get("translation", {}).get("target_languages", [])

    def get_target_directory(self, language_code: str) -> str:
        """Generate target directory path based on source directory and language code"""
        source_parent = os.path.dirname(self.source_directory)
        return os.path.join(source_parent, language_code)

    def translate_file(self, source_path: str, target_language: str, language_code: str) -> None:
        """Translate source file and save to target language directory"""
        # Calculate target file path
        rel_path = os.path.relpath(source_path, self.source_directory)
        target_path = os.path.join(self.get_target_directory(language_code), rel_path)

        # Read source file
        with open(source_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Generate translation prompt
        prompt = f"""Please translate the following content into {target_language}. 
Maintain any markdown formatting, special characters and frontmatter. Do not respond with anything else. Do not wrap the content with ```.

Content:
{content}"""

        # Get translation result
        translated_content = self._call_openai(prompt)

        # Ensure target directory exists
        os.makedirs(os.path.dirname(target_path), exist_ok=True)

        # Save translation result
        with open(target_path, 'w', encoding='utf-8') as f:
            f.write(translated_content)

    def process_directory(self) -> None:
        """Process all files in source directory for each target language"""
        for target_lang in self.target_languages:
            language = target_lang.get("language")
            code = target_lang.get("code")
            
            print(f"Processing translations for {language}...")
            
            for root, _, files in os.walk(self.source_directory):
                for file in files:
                    if file.endswith(('.md', '.markdown')):  # Only process markdown files
                        retry_count = self.config["system"]["retry_count"]
                        while retry_count > 0:
                            try:
                                source_path = os.path.join(root, file)
                                print(f"Translating {file} to {language}...")
                                self.translate_file(source_path, language, code)
                                break
                            except Exception as e:
                                print(f"Failed to translate {file}: {e}")
                                print(f"Attempts remaining: {retry_count-1}")
                                retry_count -= 1
            
            print(f"Completed translations for {language}")
            
def translate_blog_directory(directory: str, api_key: str, base_url: str, model: str, config: dict):
    processor = TranslationProcessor(api_key, base_url, model, config, directory)
    processor.process_directory()
