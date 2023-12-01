from src.game_state.list_transformations import dict_counter


def is_royal_flush(sorted_card_collection: list[tuple]) -> bool:
    if not is_flush(sorted_card_collection):
        return False

    counter_suits = dict_counter(sorted_card_collection, 1)
    max_suit = max(counter_suits, key=counter_suits.get)
    new_collection = [card for card in sorted_card_collection if card[1] == max_suit]

    return bool(is_straight(new_collection) and new_collection[-1][1] == 14)


def is_straight_flush(sorted_card_collection: list[tuple]) -> bool:
    if not is_flush(sorted_card_collection):
        return False

    counter_suits = dict_counter(sorted_card_collection, 1)
    max_suit = max(counter_suits, key=counter_suits.get)
    new_collection = [card for card in sorted_card_collection if card[1] == max_suit]

    return bool(is_straight(new_collection) or is_wheel(new_collection))


def is_four_of_a_kind(sorted_card_collection: list[tuple]) -> bool:
    counter_card_values = dict_counter(sorted_card_collection, 0)
    if 4 in counter_card_values.values():
        return True
    return False


def is_full_house(sorted_card_collection: list[tuple]) -> bool:
    pair = False
    three = False
    counter_card_values = dict_counter(sorted_card_collection, 0)

    for k, v in counter_card_values.items():
        if v >= 3:
            three = True
        if v == 2:
            pair = True

    return bool(three and pair)


def is_flush(sorted_card_collection: list[tuple]) -> bool:
    counter_card_suit = dict_counter(sorted_card_collection, 1)
    for k, v in counter_card_suit.items():
        if v >= 5:
            return True
    return False


def is_straight(sorted_card_collection: list[tuple]) -> bool:
    counter = 1

    for i in range(len(sorted_card_collection) - 1):
        if sorted_card_collection[i][0] + 1 == sorted_card_collection[i + 1][0]:
            counter += 1
        elif sorted_card_collection[i][0] - sorted_card_collection[i + 1][0] > 1:
            counter = 1

    return counter >= 5


def is_wheel(sorted_card_collection: list[tuple]) -> bool:
    for i in (14, 2, 3, 4, 5):
        if i not in set(card[0] for card in sorted_card_collection):
            return False
    return True


def is_three_of_a_kind(sorted_card_collection: list[tuple]) -> bool:
    counter_card_values = dict_counter(sorted_card_collection, 0)
    if 3 in counter_card_values.values():
        return True
    return False


def is_two_pairs(sorted_card_collection: list[tuple]) -> bool:
    counter_card_values = dict_counter(sorted_card_collection, 0)
    return bool(sum(1 for value in counter_card_values.values() if value >= 2) >= 2)


def is_pair(sorted_card_collection: list[tuple]) -> bool:
    counter_card_values = dict_counter(sorted_card_collection, 0)
    if 2 in counter_card_values.values():
        return True
    return False
