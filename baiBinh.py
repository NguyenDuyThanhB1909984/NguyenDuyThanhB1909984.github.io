import streamlit as st
from itertools import combinations

def find_combinations(hand):
    comb = list(combinations(hand,3))
    return comb

def exclude_combination(card_list, comb):
    return [x for x in card_list if x not in comb[0]]

def sort_combinations(combs):
    comb_with_sum = [(sum(comb),comb) for comb in combs]
    return sorted(comb_with_sum, key=lambda x: x[0], reverse=True)

st.title("Card Combination Finder")
cards = list(range(1,14))
selected_cards = st.multiselect("Select 6 cards from the following: ", cards)
if len(selected_cards) != 6:
    st.write("Please select 6 cards")


else:
    combs = find_combinations(selected_cards)
    comb_with_sum = sort_combinations(combs)

    for comb in combs:
        comb2 = exclude_combination(selected_cards, combs)
        
        st.write(comb2, " ", comb)
        st.write(sum(comb2)%10, " ",sum(comb)%10 )

    st.write("3 best combinations:")
    for sum, comb in comb_with_sum[:3]:
        st.write("Sum: ", sum)
        st.write("Combination: ", comb)
