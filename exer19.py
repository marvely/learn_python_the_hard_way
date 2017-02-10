def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses." % cheese_count
    print "You have %d boxes_of_crackers." % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket. \n"

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "Or, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10+20, 5+6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)


# +++++++++++++++++++ my own function +++++++++++++++++++ #

def buy_kitchen_towels(current_amount, wanted_to_have_at_home):
    if current_amount >= wanted_to_have_at_home:
        print "We already have enough!\n"
    else:
        print "That's what we have at home: %d rolls of kitchen towels." % current_amount
        print "If we want to have %d rolls, we need to buy %d from Costco today.\n" % (wanted_to_have_at_home, wanted_to_have_at_home - current_amount)

buy_kitchen_towels(0, 30)

buy_kitchen_towels(50, 0)

current_rolls = int(raw_input("What is the current number of rolls that we have at home? >"))
wanted_stock = int(raw_input("How many do we need at home? >"))

buy_kitchen_towels(current_rolls, wanted_stock)
# break, and continue only works in a "for loop" or "while loop"!!!!
