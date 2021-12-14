def cards():
    suit_of_cards = 'diamonds, clubs, hearts, spades'.split(', ')
    list_of_cards = ['A', *range(2, 11), 'J', 'Q', 'K']
    for i in suit_of_cards:
        for j in list_of_cards:
            yield str(j) + ' ' + i

new_pack_of_cards = cards()
while new_pack_of_cards:
    print(next(new_pack_of_cards))