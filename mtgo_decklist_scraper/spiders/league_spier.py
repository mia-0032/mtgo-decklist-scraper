# -*- coding: utf-8 -*-

import scrapy

from bs4 import BeautifulSoup

from mtgo_decklist_scraper.items import Board, Card, Deck


class LeagueSpider(scrapy.Spider):
    name = 'league'

    def __init__(self, url=None, *args, **kwargs):
        self.url = url
        self.identifier = url.split('/')[-1]
        super().__init__(*args, **kwargs)

    def start_requests(self):
        yield scrapy.Request(url=self.url, callback=self.parse)

    def parse(self, response):
        soup = BeautifulSoup(response.text, 'lxml')

        decklists = soup.find('div', class_='decklists')
        deck_groups = decklists.find_all('div', class_='deck-group')

        for idx, deck_group in enumerate(deck_groups):
            deck = Deck()
            deck['deck_id'] = idx + 1

            player_name = deck_group.find('h4').get_text().replace(' (5-0)', '')
            deck['player'] = player_name

            mainboard_container = deck_group.find('div', class_='sorted-by-overview-container')
            main_card_lists = mainboard_container.find_all('div')
            mainboard = Board()

            for main_card_list in main_card_lists:
                card_type = main_card_list.find('h5')
                if card_type is None:
                    continue
                card_type = card_type.get_text().split(' ')[0]

                for row in main_card_list.find_all('span', class_='row'):
                    card_name = row.find('span', class_='card-name').get_text()
                    num = row.find('span', class_='card-count').get_text()
                    card = Card(name=card_name, number=int(num), card_type=card_type)
                    mainboard.card_list.append(card)

            deck['mainboard'] = mainboard

            sideboard_container = deck_group.find('div', class_='sorted-by-sideboard-container')
            sideboard = Board()

            if sideboard_container is not None:
                for row in sideboard_container.find_all('span', class_='row'):
                    card_name = row.find('span', class_='card-name').get_text()
                    num = row.find('span', class_='card-count').get_text()
                    card = Card(name=card_name, number=int(num), card_type=None)
                    sideboard.card_list.append(card)

            deck['sideboard'] = sideboard

            yield deck
