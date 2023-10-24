from restaurantData import *
from linkedlist import LinkedList

#intro graphic
print("**************************************")
print("***                                ***")
print("***     Welcome to Food Nation!    ***")
print("***   Your friendly neighborhood   ***")
print("*** restaurant recommendation tool.***")
print("***                                ***")
print("**************************************")

# Insert food types into a linkedlist. The data is in restaurantData.py.
def insert_cuisine():
    cuisine_list = LinkedList()
    for cuisine in types:
        cuisine_list.insert_beginning(cuisine)
    return cuisine_list

# Insert restaurant data into a LinkedList of LinkedLists. The data is in restaurantData.py.
def insert_restaurant_data():
    restaurant_data_list = LinkedList()
    for cuisine in types:
        restaurant_sublist = LinkedList()
        for restaurant in restaurant_data:
            if restaurant[0] == cuisine:
                restaurant_sublist.insert_beginning(restaurant)
        restaurant_data_list.insert_beginning(restaurant_sublist)
    return restaurant_data_list

my_cuisine_list = insert_cuisine()
my_restaurant_list = insert_restaurant_data()

#print(my_cuisine_list.getCount())

#cuisines = my_cuisine_list.stringify_list()
#restaurants = my_restaurant_list.stringify_list()

#print(cuisines)
#print(my_restaurant_list)

run = True
while run:
    # Write code for user interaction here
    print("Let's get started finding you somewhere to eat!")

    cuisine_input = ""

    while len(cuisine_input) == 0:
        cuisine_first_letter = str(input("Please type the first letter of the cuisine for which you would like a recommendation.")).lower()
    
        # Search for user_input in food types data structure here
        matching_cusine = []
        cuisine_list_head = my_cuisine_list.get_head_node()
        while cuisine_list_head is not None:
            if str(cuisine_list_head.get_value()).startswith(cuisine_first_letter):
                matching_cusine.append(cuisine_list_head.get_value())
            cuisine_list_head = cuisine_list_head.get_next_node()

        # print list of matching food types
        for cuisine in matching_cusine:
            print(cuisine)

        #check if no cuisine was found    
        if len(matching_cusine) == 0:
            print("I'm sorry, we do not have a cuisine that matches that letter.")
    
        # Check if only one type of restaurant was found, ask user if they would like to select this type
        elif len(matching_cusine) == 1:
            print("The only matching cuisine is " + str(matching_cusine) + ".")
            list_restaurants = input("Would you like to see the restaurant recommendations for this cuisine? Type Y for yes and N for no.")
            if list_restaurants.upper() == "N":
                run = False
            else:
                #code for retrieving restaurant data
                selected_cuisine = matching_cusine[0]
                restaurant_list_head = my_restaurant_list.get_head_node()
                while restaurant_list_head.get_next_node() is not None:
                    sublist_head = restaurant_list_head.get_value().get_head_node()
                    if sublist_head.get_value()[0] == selected_cuisine:
                        while sublist_head.get_next_node() is not None:
                            print("--------------------------")
                            print("Name: " + sublist_head.get_value()[1])
                            print("Price: " + sublist_head.get_value()[2] + "/5")
                            print("Rating: " + sublist_head.get_value()[3] + "/5")
                            print("Address: " + sublist_head.get_value()[4])
                            print("--------------------------\n")
                            sublist_head = sublist_head.get_next_node()
                    restaurant_list_head = restaurant_list_head.get_next_node()
            
        else:
            print("The following cuisines match your request: ")
            for cuisine in matching_cusine:
                print(cuisine)
            cuisine_choice = input("Please enter the place number in the list of the cuisine you would like recommendations for. For example, if you would like African cuisine and the list reads 'American, African' type '2'.")
            
            #code for retrieving restaurant data
            selected_cuisine = matching_cusine[int(cuisine_choice) - 1]
            restaurant_list_head = my_restaurant_list.get_head_node()
            while restaurant_list_head.get_next_node() is not None:
                sublist_head = restaurant_list_head.get_value().get_head_node()
                if sublist_head.get_value()[0] == selected_cuisine:
                    while sublist_head.get_next_node() is not None:
                        print("--------------------------")
                        print("Name: " + sublist_head.get_value()[1])
                        print("Price: " + sublist_head.get_value()[2] + "/5")
                        print("Rating: " + sublist_head.get_value()[3] + "/5")
                        print("Address: " + sublist_head.get_value()[4])
                        print("--------------------------\n")
                        sublist_head = sublist_head.get_next_node()
                restaurant_list_head = restaurant_list_head.get_next_node()


        # Ask user if they would like to search for other types of restaurants
        restart = input("If you would like to conduct another search, please enter Y for yes. Otherwise, please enter N for no.")
        if restart.upper == "N":
            run = False
            print("Thank you for using Food Nation!")
