from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connection_decorator(func):
    """Makes sure code doesn`t fall with an exceprion and prints what exception did you get if you got one"""
    def wrapper(*args):
        try:
            client = MongoClient( # connecting to database
                "", # insert your connection string
                server_api=ServerApi("1"),
            )

            db = client.book
            return func(*args, db)
        except Exception as e:
            print(e)

    return wrapper


# TEST DATA

# result_many = db.cats.insert_many([
# {
#     "name": "Барсик",
#     "age": 3,
#     "features": ["ходить у капці", "дає себе гладити", "рудий"],
# },

# {
#     "name": "Мурзик",
#     "age": 2,
#     "features": ["любить грати з м'ячиком", "нявкає вранці", "чорний з білими плямами"],
# },

# {
#     "name": "Васька",
#     "age": 4,
#     "features": ["лазить по деревах", "спить на підвіконні", "сірий"],
# },

# {
#     "name": "Рижик",
#     "age": 1,
#     "features": ["грає з дітьми", "ловить мишей", "рудий з білими лапками"],
# },

# {
#     "name": "Тигра",
#     "age": 5,
#     "features": ["стрибає високо", "любить воду", "смугастий"],
# },

# {
#     "name": "Сніжок",
#     "age": 2,
#     "features": ["спить на подушках", "п'є тільки з чашки", "білий"],
# },

# {
#     "name": "Кузя",
#     "age": 3,
#     "features": ["гавкає на незнайомців", "грає з іграшками", "коричневий"],
# },

# {
#     "name": "Лео",
#     "age": 4,
#     "features": ["ходить на повідку", "дружить з собаками", "рудий"],
# },

# {
#     "name": "Мурчик",
#     "age": 1,
#     "features": ["ловить мишей", "спить у коробці", "смугастий"],
# },

# {
#     "name": "Буся",
#     "age": 2,
#     "features": ["бігає по дому", "любить ласку", "чорна"],
# },

# {
#     "name": "Маркіз",
#     "age": 3,
#     "features": ["грає з клубком ниток", "спить на ліжку", "білий з чорними плямами"],
# }
# ])


@connection_decorator
def find_cats(db):
    """Prints each cat from the database if there are any"""
    cats = db.cats.find({})
    if cats:
        for cat in cats:
            print(cat)
    else:
        print("No cats")


def cat_exists(name, db):
    """Checks if cat with this name is in the database"""
    return db.cats.find_one({"name": name})


@connection_decorator
def find_cat(name, db):
    """Prints the cat with a certain name from the database if there is one"""
    cat = cat_exists(name, db)
    if cat:
        print(cat)
    else:
        print(f"No cats named {name}")


@connection_decorator
def change_age(name, new_age, db):
    """Changes cat`s age if such cat is in the database"""
    if cat_exists(name, db):
        db.cats.update_one({"name": name}, {"$set": {"age": new_age}}) 
        print(f"{name} is now {new_age} years old")
    else:
        print(f"No cats named {name}")


@connection_decorator
def add_feature(name, new_feature, db):
    """Adds a new feature to cat`s list if such cat is in the database"""
    if cat_exists(name, db):
        db.cats.update_one({"name": name}, {"$push": {"features": new_feature}})
        print(f"{name} now has a new feature")
    else:
        print(f"No cats named {name}")


@connection_decorator
def delete_cat(name, db):
    """Deletes the cat with a certain name from the database if there is one"""
    if cat_exists(name, db):
        db.cats.delete_one({"name": name})
        print(f"{name} was deleted")
    else:
        print(f"No cats named {name}")


@connection_decorator
def clear(db):
    """Removes all cats from the database"""
    db.cats.delete_many({})
    print("No cats now")


# find_cats()
# find_cat('Васька')
# change_age("Васька", 10)
# add_feature('Васька', 'Погано пахне')
# delete_cat('Маркіз')
# clear()
