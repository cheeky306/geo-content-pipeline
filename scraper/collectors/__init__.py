"""
Collectors package for fetching content from various sources.
"""
from .base_collector import BaseCollector
from .url_collector import URLCollector
from .document_collector import DocumentCollector

__all__ = ['BaseCollector', 'URLCollector', 'DocumentCollector']
