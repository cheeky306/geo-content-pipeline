#!/usr/bin/env python3
"""
Knowledge Ledger Agent - Main CLI application.

Processes URLs and documents into a structured knowledge ledger.
"""
import argparse
import sys
from pathlib import Path
from typing import List
from datetime import datetime

from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn

from models import Source, ProcessedContent, KnowledgeLedger, SourceType
from collectors import URLCollector, DocumentCollector
from processors import ContentCleaner, ContentChunker, TopicExtractor, AuthorityScorer, QAChecker
from generators import LedgerBuilder
from utils import generate_source_id, extract_references, clean_text


console = Console()


class KnowledgeLedgerAgent:
    """Main agent that orchestrates the knowledge ledger creation."""
    
    def __init__(self):
        self.url_collector = URLCollector()
        self.doc_collector = DocumentCollector()
        self.cleaner = ContentCleaner()
        self.chunker = ContentChunker()
        self.topic_extractor = TopicExtractor(max_topics=10)
        self.authority_scorer = AuthorityScorer()
        self.qa_checker = QAChecker()
        self.ledger_builder = LedgerBuilder()
    
    def process(self, urls: List[str] = None, folder: str = None) -> KnowledgeLedger:
        """
        Process sources and create knowledge ledger.
        
        Args:
            urls: List of URLs to process
            folder: Folder path containing documents
            
        Returns:
            KnowledgeLedger object
        """
        sources = []
        locations = []
        
        # Collect URLs
        if urls:
            locations.extend(urls)
        
        # Collect documents from folder
        if folder:
            folder_path = Path(folder)
            if folder_path.exists() and folder_path.is_dir():
                for ext in DocumentCollector.SUPPORTED_EXTENSIONS:
                    locations.extend(str(p) for p in folder_path.rglob(f'*{ext}'))
            else:
                console.print(f"[yellow]Warning: Folder not found: {folder}[/yellow]")
        
        if not locations:
            console.print("[red]Error: No URLs or documents to process[/red]")
            return KnowledgeLedger(sources=[], processed_contents=[], topics=[])
        
        # Process each source
        with Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            console=console,
        ) as progress:
            task = progress.add_task("Processing sources...", total=len(locations))
            
            for i, location in enumerate(locations):
                progress.update(task, description=f"Processing {i+1}/{len(locations)}: {location[:50]}...")
                
                # Collect content
                collector = self._get_collector(location)
                if not collector:
                    console.print(f"[yellow]Skipping unsupported source: {location}[/yellow]")
                    continue
                
                data = collector.collect(location)
                
                # Create source
                source_id = generate_source_id(len(sources) + 1)
                source_type = self.authority_scorer.classify_type(data['content'], data['metadata'])
                authority = self.authority_scorer.score(source_type, data['content'], data['metadata'])
                
                # Extract references
                references = extract_references(data['content'])
                
                source = Source(
                    id=source_id,
                    name=data['title'],
                    source_type=source_type,
                    authority_score=authority,
                    location=location,
                    content=data['content'],
                    title=data['title'],
                    metadata=data['metadata'],
                    references=references
                )
                
                sources.append(source)
                progress.advance(task)
        
        console.print(f"[green]✓[/green] Collected {len(sources)} sources")
        
        # Process content
        console.print("Processing content...")
        processed_contents = []
        
        for source in sources:
            # Clean content
            cleaned = self.cleaner.clean(source.content)
            
            # Chunk content
            chunks = self.chunker.chunk(cleaned)
            
            processed = ProcessedContent(
                source_id=source.id,
                chunks=chunks,
                cleaned_text=cleaned
            )
            processed_contents.append(processed)
        
        console.print(f"[green]✓[/green] Processed {len(processed_contents)} sources")
        
        # Extract topics
        console.print("Extracting topics...")
        topics = self.topic_extractor.extract_topics(processed_contents)
        console.print(f"[green]✓[/green] Extracted {len(topics)} topics")
        
        # Create knowledge ledger
        ledger = KnowledgeLedger(
            sources=sources,
            processed_contents=processed_contents,
            topics=topics
        )
        
        return ledger
    
    def _get_collector(self, location: str):
        """Get appropriate collector for a location."""
        if self.url_collector.can_handle(location):
            return self.url_collector
        elif self.doc_collector.can_handle(location):
            return self.doc_collector
        return None
    
    def generate_markdown(self, ledger: KnowledgeLedger) -> str:
        """Generate markdown from knowledge ledger."""
        console.print("Generating knowledge ledger...")
        markdown = self.ledger_builder.build(ledger)
        
        # Format markdown
        console.print("Formatting markdown...")
        markdown = self.qa_checker.format_markdown(markdown)
        
        # Run QA checks
        console.print("Running QA checks...")
        qa_results = self.qa_checker.check_all(markdown)
        
        # Report results
        has_errors = False
        
        # Structure errors
        if qa_results['structure_errors']:
            console.print("[red]Structure Errors:[/red]")
            for error in qa_results['structure_errors']:
                console.print(f"  - {error}")
            has_errors = True
            
        # Link errors
        if qa_results['link_errors']:
            console.print("[red]Link Errors:[/red]")
            for error in qa_results['link_errors']:
                console.print(f"  - {error}")
            has_errors = True
            
        # Lint errors
        if qa_results['lint_errors']:
            console.print("[yellow]Linting Issues:[/yellow]")
            # Limit output if too many
            for i, error in enumerate(qa_results['lint_errors']):
                if i >= 10:
                    console.print(f"  ... and {len(qa_results['lint_errors']) - 10} more")
                    break
                console.print(f"  - {error}")
        
        if not has_errors:
            console.print("[green]✓[/green] QA Checks passed")
        else:
            console.print("[yellow]⚠[/yellow] QA Checks completed with issues")
        
        return markdown
    
    def save_markdown(self, markdown: str, output_path: str):
        """Save markdown to file."""
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown)
        console.print(f"[green]✓[/green] Saved to: {output_path}")


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Knowledge Ledger Agent - Process URLs and documents into structured knowledge"
    )
    parser.add_argument(
        '--urls',
        nargs='+',
        help='URLs to process'
    )
    parser.add_argument(
        '--folder',
        help='Folder containing documents to process'
    )
    parser.add_argument(
        '--output',
        default='knowledge_ledger.md',
        help='Output markdown file (default: knowledge_ledger.md)'
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if not args.urls and not args.folder:
        console.print("[red]Error: Must provide --urls and/or --folder[/red]")
        parser.print_help()
        sys.exit(1)
    
    # Run agent
    console.print("\n[bold blue]Knowledge Ledger Agent[/bold blue]\n")
    
    agent = KnowledgeLedgerAgent()
    
    try:
        # Process sources
        ledger = agent.process(urls=args.urls, folder=args.folder)
        
        if not ledger.sources:
            console.print("[red]No sources were successfully processed[/red]")
            sys.exit(1)
        
        # Generate markdown
        markdown = agent.generate_markdown(ledger)
        
        # Save
        agent.save_markdown(markdown, args.output)
        
        # Summary
        console.print(f"\n[bold green]Summary:[/bold green]")
        console.print(f"  Sources: {len(ledger.sources)}")
        console.print(f"  Topics: {len(ledger.topics)}")
        console.print(f"  Output: {args.output}")
        
    except Exception as e:
        console.print(f"[red]Error: {str(e)}[/red]")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
