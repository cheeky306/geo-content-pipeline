"""
Utility functions for the Knowledge Ledger Agent.
"""
import re
from typing import List
from pathlib import Path


def generate_source_id(index: int) -> str:
    """Generate a source ID like SOURCE-001."""
    return f"SOURCE-{index:03d}"


def sanitize_filename(name: str) -> str:
    """Sanitize a string to be used as a filename."""
    # Remove or replace invalid characters
    name = re.sub(r'[<>:"/\\|?*]', '', name)
    # Replace spaces with underscores
    name = name.replace(' ', '_')
    # Limit length
    return name[:100]


def extract_domain(url: str) -> str:
    """Extract domain from URL."""
    pattern = r'https?://(?:www\.)?([^/]+)'
    match = re.search(pattern, url)
    return match.group(1) if match else url


def is_high_authority_domain(domain: str) -> bool:
    """Check if a domain is high authority (.edu, .gov, etc.)."""
    high_authority_tlds = ['.edu', '.gov', '.ac.uk', '.org']
    return any(domain.endswith(tld) for tld in high_authority_tlds)


def clean_text(text: str) -> str:
    """Basic text cleaning."""
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    # Remove excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text)
    # Trim
    return text.strip()


def extract_references(text: str) -> List[str]:
    """Extract references/citations from text."""
    references = []
    
    # Look for common reference patterns
    # Pattern 1: [1], [2], etc.
    numbered_refs = re.findall(r'\[\d+\][^\[]*?(?=\[\d+\]|$)', text)
    references.extend(numbered_refs)
    
    # Pattern 2: References section
    ref_section = re.search(r'(?:References|Bibliography|Citations)[:\n]+(.*?)(?:\n\n|$)', 
                            text, re.IGNORECASE | re.DOTALL)
    if ref_section:
        # Split by newlines to get individual references
        refs = [ref.strip() for ref in ref_section.group(1).split('\n') if ref.strip()]
        references.extend(refs)
    
    # Pattern 3: URLs as references
    urls = re.findall(r'https?://[^\s<>"{}|\\^`\[\]]+', text)
    references.extend(urls)
    
    # Remove duplicates while preserving order
    seen = set()
    unique_refs = []
    for ref in references:
        ref_clean = ref.strip()
        if ref_clean and ref_clean not in seen:
            seen.add(ref_clean)
            unique_refs.append(ref_clean)
    
    return unique_refs


def format_markdown_table(headers: List[str], rows: List[List[str]]) -> str:
    """Format a markdown table."""
    lines = []
    
    # Header
    lines.append('| ' + ' | '.join(headers) + ' |')
    
    # Separator
    lines.append('|' + '|'.join(['---' for _ in headers]) + '|')
    
    # Rows
    for row in rows:
        lines.append('| ' + ' | '.join(str(cell) for cell in row) + ' |')
    
    return '\n'.join(lines)


def ensure_directory(path: str) -> Path:
    """Ensure a directory exists."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def read_file_content(filepath: str) -> str:
    """Read content from a text file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except UnicodeDecodeError:
        # Try with different encoding
        with open(filepath, 'r', encoding='latin-1') as f:
            return f.read()
