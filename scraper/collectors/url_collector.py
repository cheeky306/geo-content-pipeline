"""
URL collector using Firecrawl MCP or direct scraping.
"""
import re
from typing import Dict, Any
from .base_collector import BaseCollector
import requests
from bs4 import BeautifulSoup


class URLCollector(BaseCollector):
    """Collects content from URLs."""
    
    def __init__(self, use_firecrawl: bool = False):
        """
        Initialize URL collector.
        
        Args:
            use_firecrawl: Whether to use Firecrawl MCP (requires MCP integration)
        """
        self.use_firecrawl = use_firecrawl
    
    def can_handle(self, location: str) -> bool:
        """Check if this is a URL."""
        return location.startswith('http://') or location.startswith('https://')
    
    def collect(self, location: str) -> Dict[str, Any]:
        """
        Collect content from a URL.
        
        Args:
            location: URL to scrape
            
        Returns:
            Dictionary with content, title, and metadata
        """
        if self.use_firecrawl:
            return self._collect_with_firecrawl(location)
        else:
            return self._collect_with_requests(location)
    
    def _collect_with_firecrawl(self, url: str) -> Dict[str, Any]:
        """
        Collect using Firecrawl MCP.
        Note: This requires MCP integration which is handled at a higher level.
        For now, this is a placeholder that falls back to requests.
        """
        # TODO: Integrate with Firecrawl MCP when available in the main agent
        return self._collect_with_requests(url)
    
    def _collect_with_requests(self, url: str) -> Dict[str, Any]:
        """Collect using direct HTTP requests and BeautifulSoup."""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
            }
            response = requests.get(url, headers=headers, timeout=30)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'lxml')
            
            # Extract title
            title = self._extract_title(soup)
            
            # Extract main content
            content = self._extract_content(soup)
            
            # Extract metadata
            metadata = self._extract_metadata(soup, url)
            
            return {
                'content': content,
                'title': title,
                'metadata': metadata
            }
            
        except Exception as e:
            return {
                'content': f'Error fetching URL: {str(e)}',
                'title': url,
                'metadata': {'error': str(e), 'url': url}
            }
    
    def _extract_title(self, soup: BeautifulSoup) -> str:
        """Extract title from HTML."""
        # Try <title> tag
        if soup.title and soup.title.string:
            return soup.title.string.strip()
        
        # Try <h1>
        h1 = soup.find('h1')
        if h1:
            return h1.get_text().strip()
        
        # Try og:title
        og_title = soup.find('meta', property='og:title')
        if og_title and og_title.get('content'):
            return og_title['content'].strip()
        
        return 'Untitled'
    
    def _extract_content(self, soup: BeautifulSoup) -> str:
        """Extract main content from HTML."""
        # Remove script and style elements
        for element in soup(['script', 'style', 'nav', 'footer', 'header']):
            element.decompose()
        
        # Try to find main content area
        main_content = None
        
        # Look for common content containers
        for selector in ['article', 'main', '[role="main"]', '.post-content', '.article-content']:
            main_content = soup.select_one(selector)
            if main_content:
                break
        
        # If no main content found, use body
        if not main_content:
            main_content = soup.body
        
        if not main_content:
            return soup.get_text()
        
        # Extract text with some structure preservation
        text_parts = []
        
        for element in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'li', 'blockquote']):
            text = element.get_text().strip()
            if text:
                # Add heading markers
                if element.name in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
                    level = int(element.name[1])
                    text = '#' * level + ' ' + text
                text_parts.append(text)
        
        content = '\n\n'.join(text_parts)
        
        # Fallback to simple text extraction
        if not content:
            content = main_content.get_text()
        
        return content.strip()
    
    def _extract_metadata(self, soup: BeautifulSoup, url: str) -> Dict[str, Any]:
        """Extract metadata from HTML."""
        metadata = {'url': url}
        
        # Extract author
        author = soup.find('meta', attrs={'name': 'author'})
        if author and author.get('content'):
            metadata['author'] = author['content']
        
        # Extract description
        description = soup.find('meta', attrs={'name': 'description'})
        if description and description.get('content'):
            metadata['description'] = description['content']
        
        # Extract publish date
        pub_date = soup.find('meta', property='article:published_time')
        if pub_date and pub_date.get('content'):
            metadata['published_date'] = pub_date['content']
        
        return metadata
