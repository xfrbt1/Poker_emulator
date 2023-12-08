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


def sort_all_cards_asc(valued_card_collection: list[tuple]) -> list[tuple]:
    sorted_list = sorted(valued_card_collection, key=lambda x: x[0])
    return sorted_list


def uniq_cards_collection(valued_card_collection: list[tuple], index: int = 0) -> list[tuple]:
    uniq_collection = []
    for _ in valued_card_collection:
        if not is_in_list(uniq_collection, _[index], index):
            uniq_collection.append(_)
    return uniq_collection


def is_in_list(collection: list, value: int, index: int) -> bool:
    for _ in collection:
        if value == _[index]:
            return True
    return False
