import streamlit as st
from itertools import combinations

def find_combinations(hand):
    comb = list(combinations(hand,3))
    return comb

def exclude_combination(card_list, comb):
    return [x for x in card_list if x not in comb]



def sort_combinations(combs,comb2s):
    comb_with_sum = []
    for comb, comb2 in zip(combs,comb2s):
        temp = (comb, comb2)
        if temp not in comb_with_sum:
            comb_with_sum.append((sum(comb)%10 + sum(comb2)%10,temp))
    return sorted(comb_with_sum, key=lambda x: x[0], reverse=True)



st.title("Card Combination Finder")
st.write("Vì bài binh chỉ dựa trên nút, nên cần nhập nút của lá bài. ")
st.write("Lá bài ách( trên bài là chữ A) là 1 ")
st.write("3 lá tây( trên bài là chữ J,Q,K) là 10 ")


cards = ['chọn',1,2,3,4,5,6,7,8,9,10]

selected_cards =[]

col1, col2 = st.columns(2)

with col1:
    selected_cards.append(st.selectbox("Lá bài 1 ", cards, key='cards1'))
    selected_cards.append(st.selectbox("Lá bài 2 ", cards, key='cards2'))
    selected_cards.append(st.selectbox("Lá bài 3 ", cards, key='cards3'))

with col2:
    selected_cards.append(st.selectbox("Lá bài 4 ", cards,  key='cards4'))
    selected_cards.append(st.selectbox("Lá bài 5 ", cards,  key='cards5'))
    selected_cards.append(st.selectbox("Lá bài 6 ", cards,  key='cards6'))


if 'chọn' in selected_cards:
    st.write("Vui lòng chọn 6 lá")



else:
    combs = find_combinations(selected_cards)
    comb2s = [exclude_combination(selected_cards, comb) for comb in combs]
    comb_with_sum = sort_combinations(combs,comb2s)
    comb_with_sum = sorted(comb_with_sum, key=lambda x: x[0], reverse=True)
    

    
    for i in range(len(comb_with_sum)):
        
        st.markdown("""
        <style>
        .big-font {
            font-size:30px !important;
        }
        </style>
        """, unsafe_allow_html=True)
     
        st.markdown(f'<p class="big-font">Kết quả: {sum(comb_with_sum[i][1][0])%10} - {sum(comb_with_sum[i][1][1])%10}</p>', unsafe_allow_html=True)
        st.markdown(f'<p font-size= "25px"> Cách sắp xếp: {comb_with_sum[i][1][0]} - {tuple(comb_with_sum[i][1][1])}</p>', unsafe_allow_html=True)
        st.write()
        