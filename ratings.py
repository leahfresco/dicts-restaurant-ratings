"""Restaurant rating lister."""
import sys
import random

def get_ratings(scores):
    """Returns Restaurant ratings in alphabetical order"""

    scores_file = open(scores)

    restaurant_ratings = {}
    for line in scores_file:
        line = line.rstrip()
        ratings = line.split(':')
        restaurant_ratings[ratings[0]] = ratings[1]
    return restaurant_ratings

def add_new_restaurant(restaurant_ratings):
    """ Adds new restaurant from user input """
    new_restaurant = raw_input("Restaurant name: ")
    
    valid_ratings = ['1', '2', '3', '4', '5']

    new_restaurant_score = raw_input("Restaurant score: ")

    while new_restaurant_score not in valid_ratings:
        print "That was not a valid score! Please select a number 1-5."
        new_restaurant_score = raw_input("Restaurant score: ")

    restaurant_ratings[new_restaurant] = new_restaurant_score
    
    return restaurant_ratings

def print_restaurant_ratings(restaurant_ratings):
    """ Prints restaurant ratings"""
    restaurant_ratings = sorted(restaurant_ratings.items())
    for restaurant, rating in restaurant_ratings:
        print "{} is rated at {}.".format(restaurant, rating)


def update_rating(restaurant_ratings, restaurant=None):
    if not restaurant:
        restaurant = random.choice(restaurant_ratings.keys())
    new_rating = raw_input("Choose a rating for {}, current rating is {}: "
        .format(restaurant, restaurant_ratings[restaurant]))
    restaurant_ratings[restaurant] = new_rating

    return restaurant_ratings

def show_menu():
    """ Shows user menu """
    print "1: Add new restaurant and rating"
    print "2: See all restaurant ratings"
    print "3: Modify random restaurant rating"
    print "4: Modify restaurant rating of your choice"
    print "q: Quit program"

restaurants = get_ratings(sys.argv[1])
choice = ''
show_menu()
while choice != 'q':
    choice = raw_input(">>> ")
    if choice == '1':
        restaurants = add_new_restaurant(restaurants)
    elif choice == '2':
        print_restaurant_ratings(restaurants)
    elif choice == '3':
        restaurants = update_rating(restaurants)
    elif choice == '4':
        update_restaurant = raw_input("Which restaurant would you like to update: ")
        restaurants = update_rating(restaurants, update_restaurant)
    elif choice =='q':
        print "Goodbye"
    else:
        show_menu()


