values = {"J": 11, "Q": 12, "K": 13, "A": 14}


def dict_counter(card_collection: list[tuple], index: int) -> dict:
    counter_dict = {card[index]: 0 for card in card_collection}

    for card in card_collection:
        counter_dict[card[index]] += 1

    return counter_dict


def create_valued_list(card_collection: list[tuple]) -> list[tuple]:
    valued_card_collection = [
        (values.get(card[0]), card[1])
        if values.get(card[0]) is not None
        else (int(card[0]), card[1])
        for card in card_collection
    ]
    return valued_card_collection


def sort_all_cards_asc(valued_card_collection: list[tuple]):
    sorted_list = sorted(valued_card_collection, key=lambda x: x[0])
    return sorted_list
