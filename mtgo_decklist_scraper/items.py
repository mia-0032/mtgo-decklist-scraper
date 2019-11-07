# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import dataclasses
import scrapy

from typing import List, Optional


@dataclasses.dataclass(frozen=True)
class Card:
    name: str
    number: int
    card_type: Optional[str]


@dataclasses.dataclass()
class Board:
    card_list: List[Card] = dataclasses.field(default_factory=list)


class Deck(scrapy.Item):
    deck_id = scrapy.Field()
    player = scrapy.Field()
    mainboard = scrapy.Field()
    sideboard = scrapy.Field()
