from utils import to_lines, group_lines


def part_1(lines):
    decks = parse(lines)
    (winner, decks) = combat(decks)
    return winner_score(winner, decks)


def parse(lines):

    if isinstance(lines, str):
        lines = to_lines(lines)

    lines = group_lines(lines)

    decks = [player[1:] for player in lines]
    decks = [[int(card) for card in deck] for deck in decks]
    return decks


def combat(decks):

    while (len(decks[0]) > 0) and (len(decks[1]) > 0):

        player1 = decks[0].pop(0)
        player2 = decks[1].pop(0)

        winner = 1 if (player1 > player2) else 2

        cards_for_winner = (player1, player2) if (winner == 1) else (player2, player1)
        decks[winner - 1].extend(cards_for_winner)

    winner = 1 if (len(decks[1]) == 0) else 2
    return winner, decks


def winner_score(winner, decks):
    winner_deck = decks[winner - 1]
    return sum(card * (i + 1) for (i, card) in enumerate(reversed(winner_deck)))


def part_2(lines):
    decks = parse(lines)
    (winner, decks) = recursive_combat(decks)
    return winner_score(winner, decks)


def recursive_combat(decks):

    seen = set()

    while True:

        if (len(decks[0]) == 0) or (len(decks[1]) == 0):
            winner = 1 if (len(decks[1]) == 0) else 2
            return winner, decks

        deck_state = (tuple(decks[0]), tuple(decks[1]))
        if deck_state in seen:
            return 1, decks
        else:
            seen.add(deck_state)

        player1 = decks[0].pop(0)
        player2 = decks[1].pop(0)

        if (len(decks[0]) >= player1) and (len(decks[1]) >= player2):
            (winner, _) = recursive_combat([decks[0][:player1], decks[1][:player2]])

        else:
            winner = 1 if (player1 > player2) else 2

        cards_for_winner = (player1, player2) if (winner == 1) else (player2, player1)
        decks[winner - 1].extend(cards_for_winner)
