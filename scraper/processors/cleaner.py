"""
Content cleaning and normalization.
"""
import re
from typing import List, Optional, Dict, Any


class ContentCleaner:
    """Cleans and normalizes text content."""
    
    def clean(self, text: str) -> str:
        """
        Clean and normalize text while preserving structure.
        
        Args:
            text: Raw text to clean
            
        Returns:
            Cleaned text
        """
        if not text:
            return ""
        
        # Fix common encoding issues
        text = self._fix_encoding(text)
        
        # Normalize whitespace but preserve paragraph breaks
        text = self._normalize_whitespace(text)
        
        # Fix markdown formatting if present
        text = self._fix_markdown(text)
        
        # Remove excessive blank lines (more than 2 consecutive)
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        return text.strip()
    
    def _fix_encoding(self, text: str) -> str:
        """Fix common encoding issues."""
        # Replace common problematic characters
        replacements = {
            '\u2019': "'",  # Right single quotation mark
            '\u2018': "'",  # Left single quotation mark
            '\u201c': '"',  # Left double quotation mark
            '\u201d': '"',  # Right double quotation mark
            '\u2013': '-',  # En dash
            '\u2014': '--', # Em dash
            '\u2026': '...', # Ellipsis
            '\xa0': ' ',    # Non-breaking space
        }
        
        for old, new in replacements.items():
            text = text.replace(old, new)
        
        return text
    
    def _normalize_whitespace(self, text: str) -> str:
        """Normalize whitespace while preserving paragraph structure."""
        # Replace tabs with spaces
        text = text.replace('\t', '    ')
        
        # Remove trailing whitespace from each line
        lines = [line.rstrip() for line in text.split('\n')]
        
        # Join back
        text = '\n'.join(lines)
        
        # Replace multiple spaces with single space (except at line start for indentation)
        lines = []
        for line in text.split('\n'):
            # Preserve leading whitespace, normalize the rest
            leading_space = len(line) - len(line.lstrip())
            rest = re.sub(r' {2,}', ' ', line.lstrip())
            lines.append(' ' * leading_space + rest)
        
        return '\n'.join(lines)
    
    def _fix_markdown(self, text: str) -> str:
        """Fix common markdown formatting issues."""
        # Ensure space after heading markers
        text = re.sub(r'^(#{1,6})([^ #])', r'\1 \2', text, flags=re.MULTILINE)
        
        # Ensure blank line before headings (except at start)
        text = re.sub(r'\n([#]{1,6} )', r'\n\n\1', text)
        text = re.sub(r'^\n+', '', text)  # Remove leading blank lines
        
        return text
