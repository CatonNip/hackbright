DUBLIN_TO_POWELL = 6.15
FRUITVALE_TO_UNION_CITY = 3.80
ORINDA_TO_RICHMOND = 3.35
HAYWARD_TO_CONCORD = 5.20
FREMONT_TO_COLMA = 6.60

def load_card(one,five,ten,twenty):
    clipper_card = (one*1) + (five*5) + (ten*10) + (twenty*20)
    
    print(clipper_card)
    return


def travel_to_destination(fare_price,card_value):
	if clipper_card >= fare_price:
		print"Welcome aboard, enjoy your trip."
    else:
        print"You need more money!"
    return

load_card(3,0,0,0):
travel_to_destination(FREMONT_TO_COLMA):
load_card(0,0,0,1):
travel_to_destination(HAYWARD_TO_CONCORD):
load_card(1,1,0,0):
travel_to_destination(DUBLIN_TO_POWELL):
load_card(2,0,1,0):
travel_to_destination(FRUITVALE_TO_UNION_CITY):