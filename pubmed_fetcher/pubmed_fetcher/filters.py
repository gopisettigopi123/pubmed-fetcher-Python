# pubmed_fetcher/filters.py

import re

def is_non_academic(affiliation: str) -> bool:
    academic_keywords = ["university", "college", "school", "department", "institute", "lab"]
    pharma_keywords = ["pharma", "therapeutics", "biotech", "inc", "ltd", "gmbh", "corp", "co."]

    affiliation = affiliation.lower()
    if any(word in affiliation for word in academic_keywords):
        return False
    return any(word in affiliation for word in pharma_keywords)
