import pandas as pd
import utility


def make_df(data):
    hands, bids = [], []
    for line in data:
        hand, bid = line.split(' ')[0], line.split(' ')[1]
        hands.append(hand)
        bids.append(bid)
    df = pd.DataFrame({'hands': hands, 'bids': bids})
    return df


def check_for_multiples(values, n_repeats):
    for val in values:
        if values.count(val) == n_repeats:
            return True
    return False


def categorise_hands_no_jokers(values, unique):
    if len(unique) == 5:
        return 'high_card'
    if len(unique) == 4:
        return 'pair'
    if len(unique) == 3:
        result = check_for_multiples(values, 3)
        if result:
            return 'three_oak'
        else:
            return 'two_pair'
    if len(unique) == 2:
        result = check_for_multiples(values, 4)
        if result:
            return 'four_oak'
        else:
            return 'full_house'
    if len(unique) == 1:
        return 'five_oak'


def categorise_hands_with_jokers(values, unique):
    if len(unique) == 5:
        return 'pair'
    if len(unique) == 4:
        return 'three_oak'
    if len(unique) == 3:
        result = check_for_multiples(values, 3)
        if result:
            return 'four_oak'
        else:
            return 'full_house'
    if len(unique) == 2:
        result = check_for_multiples(values, 4)
        if result:
            return 'five_oak'
        else:
            return 'four_oak'
    if len(unique) == 1:
        return 'five_oak'


def categorise_hands(hand, joker=False):
    values = [char for char in hand]  # split into characters (all str)
    unique = list(set(values))
    if joker and 'J' in unique:
        result = categorise_hands_with_jokers(values, unique)
    else:
        result = categorise_hands_no_jokers(values, unique)

    return result


def get_ranks(df, joker=False):
    start_rank = 1  # starting value
    ranked_hands = ['high_card', 'pair', 'two_pair', 'three_oak', 'full_house', 'four_oak', 'five_oak']  # low to high

    if joker:  # J is lowest
        ranked_values = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    else:
        ranked_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']

    for hand in ranked_hands:
        hand_df = df[df['category'] == hand].copy()
        hand_df['ranks'] = hand_df['hands'].apply(lambda x: tuple(ranked_values.index(c) + 1 for c in x)).rank(method='dense').astype(int) + start_rank - 1
        df.loc[df['category'] == hand, 'ranks'] = hand_df['ranks']
        start_rank += len(hand_df)

    df['bids'], df['ranks'] = df['bids'].astype(int), df['ranks'].astype(int)
    df = df.sort_values(by='ranks').reset_index(drop=True)
    return df


def get_total_winnings(data):
    df = data.copy()
    df['category'] = df['hands'].apply(categorise_hands)
    df = get_ranks(df)
    df['winnings'] = df['bids'] * df['ranks']
    return df['winnings'].sum()


def get_total_winnings_with_joker(df):
    df['category'] = df['hands'].apply(categorise_hands, joker=True)
    df = get_ranks(df, joker=True)
    df['winnings'] = df['bids'] * df['ranks']
    return df['winnings'].sum()


def solve_d7(data_path):
    data = utility.read_file(data_path)
    df = make_df(data)
    q1_answer = get_total_winnings(df)
    q2_answer = get_total_winnings_with_joker(df)
    print(q1_answer)
    print(q2_answer)


if __name__ == '__main__':
    path = "C:\\Users\\bmvan\PycharmProjects\\aoc_2023\data\d7.txt"
    solve_d7(path)