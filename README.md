# Court Data Fetcher — MVP

**Court chosen:** Faridabad District Court (https://districts.ecourts.gov.in/faridabad)

## Overview
This is a simple Flask web application that allows a user to enter:
- Case Type
- Case Number
- Filing Year

It then scrapes the Faridabad District Court public portal to fetch:
- Parties' names
- Filing date
- Next hearing date
- Most recent order/judgment PDF link(s)

All searches are logged into a local SQLite database (`queries.db`).

---

## Features
- Simple HTML form for input.
- Scrapes court data using `requests` + `BeautifulSoup`.
- Displays results in browser with clickable PDF download links.
- Logs each query and raw HTML response in SQLite.
- Error handling for invalid cases or site downtime.

---

## How to Run (Windows)

1. **Clone the repository**
   ```powershell
   git clone https://github.com/Sharvanibathini9/courtfetcher.git
   cd courtfetcher
