class Analyzer:
    @staticmethod
    def get_combination(player_cards: list[tuple], table_cards: list[tuple]):
        all_cards = player_cards + table_cards

        valued_list = Analyzer.create_valued_list(all_cards)
        sorted_valued_list = Analyzer.sort_all_cards_asc(valued_list)

        counter_values = Analyzer.dict_counter(all_cards, 0)
        counter_suits = Analyzer.dict_counter(all_cards, 1)

        if Analyzer._is_royal_flush():
            return 10

        if Analyzer._is_straight_flush():
            return 9

        if Analyzer._is_four_of_a_kind():
            return 8

        if Analyzer._is_full_house():
            return 7

        if Analyzer._is_flush():
            return 6

        if Analyzer._is_straight():
            return 5

    @staticmethod
    def dict_counter(card_collection: list[tuple], index: int) -> dict:
        counter_dict = {card[index]: 0 for card in card_collection}

        for card in card_collection:
            counter_dict[card[index]] += 1

        return counter_dict

    @staticmethod
    def create_valued_list(card_collection: list[tuple]) -> list[tuple]:
        valued_card_collection = [
            (values.get(card[0]), card[1])
            if values.get(card[0]) is not None
            else (int(card[0]), card[1])
            for card in card_collection
        ]
        return valued_card_collection

    @staticmethod
    def sort_all_cards_asc(valued_card_collection: list[tuple]):
        sorted_list = sorted(valued_card_collection, key=lambda x: x[0])
        return sorted_list

    @staticmethod
    def _is_royal_flush():
        ...

    @staticmethod
    def _is_straight_flush():
        ...

    @staticmethod
    def _is_four_of_a_kind():
        ...

    @staticmethod
    def _is_full_house():
        ...

    @staticmethod
    def _is_flush():
        ...

    @staticmethod
    def _is_straight():
        ...


combinations = {
    1: "HIGH CARD",
    2: "ONE PAIR",
    3: "TWO PAIRS",
    4: "THREE OF A KIND",
    5: "STRAIGHT",
    6: "FLUSH",
    7: "FULL HOUSE",
    8: "FOUR OF A KIND",
    9: "STRAIGHT FLUSH",
    10: "FLUSH ROYAL",
}

values = {"J": 11, "Q": 12, "K": 13, "A": 14}
