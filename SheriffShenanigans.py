import time

print("---------------------------------------------------------")
time.sleep(2)
print("Before we start,")
time.sleep(1)
name = input("Enter your name: ")
time.sleep(2)
print("Enjoy playing my first Python Program!")
time.sleep(3)
print("Loading... (not really loading i just want to:)")
time.sleep(4)
print("---------------------------------------------------------")

def case_description1():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("*Crime Description:*")
    time.sleep(2)
    print("*A valuable diamond necklace was stolen from a high-end*")
    print("*jewelry store during business hours. The security camera footage is unclear,*") 
    print("*and there were several people in the store at the time.*")
    time.sleep(1)
    print("*Suspects:*")
    time.sleep(1)
    print("1. 'suspect1' - Claims she was at the library reading a book.")
    time.sleep(1)
    print("2. 'suspect2' - Says he was at the gym working out.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was at a friend's house.")
    time.sleep(1)
    print("4. 'suspect4' - States he was at the cinema watching a movie.")
    option = input("These are the crime case details, Sheriff " +name+ ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " +name+ ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Produces a library receipt, but it has no timestamp.")
            case_description1()
        elif option == "suspect2":
            print("suspect2: Provides a gym entry record,") 
            print("but it only shows his arrival time.")
            case_description1()
        elif option == "suspect3":
            print("suspect3: Has a text message conversation with her friend,")
            print("but no direct alibi.")
            case_description1()
        elif option == "suspect4":
            print("suspect4: Shows a movie ticket stub,")
            print("but it could have been bought for someone else.")
            time.sleep(2)
            print("You caught the criminal Sheriff " +name+ "! Good job.")
            main()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description1()


def case_description2():
    suspects = ["suspect1", "suspect2",  "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A luxury car was found vandalized in a quiet residential neighborhood.")
    print("The incident occurred late at night,")
    print("and several people were seen in the area around that time.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Says she was shopping at the mall.")
    time.sleep(1)
    print("2. 'suspect2' - Claims he was at home cooking dinner.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was visiting her grandmother.")
    time.sleep(1)
    print("4. 'suspect4' - States he was jogging in the park.")
    option = input("These are the crime case details, Sheriff " +name+ ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " +name+ ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Provides shopping receipts, but they are from earlier in the day.")
            time.sleep(2)
            print("You caught the criminal Sheriff " +name+ "! Good job.")
            main()
        elif option == "suspect2":  
            print("suspect2: Shows a half-cooked meal as evidence.")
            case_description2()
        elif option == "suspect3":
            print("suspect3: Has a call log with her grandmother, but it's inconclusive.")
            case_description2()
        elif option == "suspect4":
            print("suspect4: Wears jogging attire but has no witness to confirm his run.")
            case_description2()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description2()

def case_description3():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("An office was broken into over the weekend, and important documents were stolen.")
    print("The security system was disabled, suggesting inside knowledge.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Says she was having dinner at a restaurant.")
    time.sleep(1)
    print("2. 'suspect2' - Claims he was attending a concert.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was watching TV at home.")
    time.sleep(1)
    print("4. 'suspect4' - States he was out of town on a business trip.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Provides a restaurant receipt, but no one remembers seeing her.")
            case_description3()
        elif option == "suspect2":
            print("suspect2: Shows a concert ticket, but the venue was crowded.")
            case_description3()
        elif option == "suspect3":
            print("suspect3: Her TV was found on standby, suggesting she was not watching it at the time of the break-in.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect4":
            print("suspect4: Provides hotel receipts and travel tickets.")
            case_description3()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description3()

def case_description4():
    suspects = ["suspect1", "suspect2", "suspect3", "suspect4"]
    print("Crime Description:")
    time.sleep(2)
    print("A priceless painting was stolen from a private gallery during an exclusive event.")
    print("The thief was careful not to leave any traces behind.")
    time.sleep(1)
    print("Suspects:")
    time.sleep(1)
    print("1. 'suspect1' - Says she was walking her dog.")
    time.sleep(1)
    print("2. 'suspect2' - Claims he was at a friend's party.")
    time.sleep(1)
    print("3. 'suspect3' - Insists she was at a yoga class.")
    time.sleep(1)
    print("4. 'suspect4' - States he was at a café writing.")
    option = input("These are the crime case details, Sheriff " + name + ".")
    while option not in suspects:
        print("Choose the correct suspect Sheriff " + name + ": ")
        option = input()
        if option == "suspect1":
            print("suspect1: Has a photo of her walking her dog, but it lacks a timestamp.")
            case_description4()
        elif option == "suspect2":
            print("suspect2: No one at the party remembers seeing him there.")
            time.sleep(2)
            print("You caught the criminal Sheriff " + name + "! Good job.")
            main()
        elif option == "suspect3":
            print("suspect3: Shows a yoga class sign-in sheet.")
            case_description4()
        elif option == "suspect4":
            print("suspect4: Has a receipt from the café.")
            case_description4()
        else:
            print("That suspect doesn't exist Sheriff")
            case_description4()
            
def main():
    print("Hello Sheriff " +name+ "! We need you to investigate some crime cases")
    time.sleep(2)
    crime_cases = ["case1", "case2", "case3", "case4"]
    choice = input()
    while choice not in crime_cases:
        print("Choose the first crime case you would like to solve Sheriff: case1, case2, case3, or case4")
        time.sleep(1)
        choice = input()
        if choice == "case1":
            case_description1()
        elif choice == "case2":
            case_description2()
        elif choice == "case3":
            case_description3()
        elif choice == "case4":
            case_description4()
        else:
            print("That crime case doesn't exist Sheriff")

main()