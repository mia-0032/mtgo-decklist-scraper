# mtgo-decklist-scraper
MTGO Decklist Scraper

## Usage

You can run it with Python or Docker.

### Python

```bash
pip install -r requirements.txt
scrapy crawl league -a url=https://magic.wizards.com/en/articles/archive/mtgo-standings/pioneer-league-2019-10-28
```

### Docker

```bash
docker-compose build
docker-compose run scrapy crawl league -a url=https://magic.wizards.com/en/articles/archive/mtgo-standings/pioneer-league-2019-10-28
```
