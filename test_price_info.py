from price_info import cost_of_fruits, total_cost_shopping

def test_cost_of_fruit():  
    result = cost_of_fruits('apple', 10)
    assert  result == 12.0
    
def test_total_cost_shopping():
    price_list={'apple' : 1.20, 'orange':1.40, 'watermelon': 6.50, 'pineapple': 2.70, 'pear' : 0.90, 'papaya': 2.95, 'pomegranate': 4.95 }

    quantity_list= {'apple': 5, 'orange':5, 'watermelon': 1, 'pineapple': 2, 'pear' : 10, 'papaya': 1, 'pomegranate': 2}
    
    result = total_cost_shopping(price_list, quantity_list)
    assert result == 46.75