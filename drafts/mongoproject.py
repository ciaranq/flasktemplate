import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
# MONGODB_URI="mongodb+srv://ciaran:Code2019@quote-vj3wf.mongodb.net/quote?retryWrites=true&w=majority"
DBS_NAME = "quote"
COLLECTION_NAME = "quote"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e


def get_record():
    print("")
    quoteNumber = input("Enter your quote number > ")
    # email = input("Enter email for quote > ")

    try:
        doc = coll.find_one({'quoteId': quoteNumber, })
    except:
        print("Error accessing the database")

    if not doc:
        print("")
        print("Error! No Quote found.")

    return doc


def show_menu():
    print("")
    print("1. Add a record")
    print("2. Find a record by name")
    print("3. Edit a record")
    print("4. Delete a record")
    print("6. Last Quote")
    print("5. Exit")

    option = input("Enter option: ")
    return option


def add_record():
    print("")
    # quoteId=add 1 to last quote ID
    newQuoteId = str(1+coll.count_documents({}))
    name = input("Enter your name > ")
    email = input("Enter your email > ")
    liveDate = input("Enter live date  > ")
    rankTime = input("Enter Time rank > ")
    rankQuality = input("Enter Quality rank > ")
    rankCost = input("Enter Cost rank > ")
    budget = input("Enter Budget > ")

    new_doc = {'quoteId': newQuoteId, 'name': name.title(), 'email': email, 'liveDate': liveDate,
               'rankTime': rankTime.upper(), 'rankQuality': rankQuality.upper(), 'rankCost':
               rankCost.upper(), 'budget': budget}

    try:
        coll.insert_one(new_doc)
        print("")
        print("Document inserted")
    except:
        print("Error accessing the database")


def find_record():
    doc = get_record()
    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())


def find_lastquoteno():
    lastQuote = coll.count_documents({})
    print(lastQuote)
    if lastQuote:
        print("goy ya")
        newQuote = lastQuote+1
        print(newQuote)
        nq = str(1+coll.count_documents({}))
        print(nq)


def edit_record():
    doc = get_record()
    if doc:
        update_doc = {}
        print("")
        for k, v in doc.items():
            if k != "_id":
                update_doc[k] = input(k.capitalize() + " [" + v + "] > ")

                if update_doc[k] == "":
                    update_doc[k] = v

        try:
            coll.update_one(doc, {'$set': update_doc})
            print("")
            print("Document updated")
        except:
            print("Error accessing the database")


def delete_record():

    doc = get_record()

    if doc:
        print("")
        for k, v in doc.items():
            if k != "_id":
                print(k.capitalize() + ": " + v.capitalize())

        print("")
        confirmation = input(
            "Is this the document you want to delete?\nY or N > ")
        print("")

        if confirmation.lower() == 'y':
            try:
                coll.remove(doc)
                print("Document deleted!")
            except:
                print("Document not deleted")


def main_loop():
    while True:
        option = show_menu()
        if option == "1":
            add_record()
        elif option == "2":
            find_record()
        elif option == "3":
            edit_record()
        elif option == "4":
            delete_record()
        elif option == "6":
            find_lastquoteno()
        elif option == "5":
            conn.close()
            break
        else:
            print("Invalid option")
        print("")


conn = mongo_connect(MONGODB_URI)
coll = conn[DBS_NAME][COLLECTION_NAME]

main_loop()
