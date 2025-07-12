# cli.py

import argparse
import sys
from pubmed_fetcher.fetch import search_pubmed, fetch_details
from pubmed_fetcher.utils import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic author affiliations.")
    parser.add_argument("query", type=str, help="PubMed search query")
    parser.add_argument("-f", "--file", help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    try:
        ids = search_pubmed(args.query)
        if args.debug:
            print(f"[DEBUG] Found {len(ids)} PubMed IDs.")

        details = fetch_details(ids)

        if args.file:
            save_to_csv(details, args.file)
            print(f"[INFO] Results saved to {args.file}")
        else:
            for paper in details:
                print(paper)

    except Exception as e:
        print(f"[ERROR] {str(e)}", file=sys.stderr)
        sys.exit(1)
