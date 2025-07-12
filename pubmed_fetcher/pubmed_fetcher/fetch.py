# pubmed_fetcher/fetch.py

import requests
from typing import List, Dict, Optional
from xml.etree import ElementTree as ET

API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/"

def search_pubmed(query: str, max_results: int = 100) -> List[str]:
    response = requests.get(f"{API_URL}esearch.fcgi", params={
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    })
    response.raise_for_status()
    return response.json()["esearchresult"]["idlist"]

def fetch_details(pubmed_ids: List[str]) -> List[Dict]:
    if not pubmed_ids:
        return []

    ids_str = ",".join(pubmed_ids)
    response = requests.get(f"{API_URL}efetch.fcgi", params={
        "db": "pubmed",
        "id": ids_str,
        "retmode": "xml"
    })
    response.raise_for_status()

    root = ET.fromstring(response.text)
    return [parse_article(article) for article in root.findall(".//PubmedArticle")]

def parse_article(article) -> Dict:
    from pubmed_fetcher.filters import is_non_academic

    title = article.findtext(".//ArticleTitle", default="N/A")
    pmid = article.findtext(".//PMID", default="N/A")
    date = article.findtext(".//PubDate/Year") or article.findtext(".//PubDate/MedlineDate", default="N/A")
    authors = article.findall(".//Author")

    non_academic_authors, affiliations, emails = [], set(), set()

    for author in authors:
        affs = author.findall(".//AffiliationInfo/Affiliation")
        for aff in affs:
            aff_text = aff.text or ""
            if is_non_academic(aff_text):
                affiliations.add(aff_text)
                lastname = author.findtext("LastName") or ""
                initials = author.findtext("Initials") or ""
                non_academic_authors.append(f"{lastname} {initials}".strip())
                if "@" in aff_text:
                    emails.add(aff_text.split()[-1])

    return {
        "PubmedID": pmid,
        "Title": title,
        "Publication Date": date,
        "Non-academic Author(s)": "; ".join(non_academic_authors),
        "Company Affiliation(s)": "; ".join(affiliations),
        "Corresponding Author Email": "; ".join(emails)
    }
