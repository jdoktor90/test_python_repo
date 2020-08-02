from sda_exercises_oop_1_mz.cat import Cat


def cat_creator() -> list:
    cats = []
    cat1 = Cat("Filemon")
    cat2 = Cat("Puszek")
    cat1.eat_mause()
    cats.append(cat1)
    cats.append(cat2)
    return cats


def main():
    # cat = Cat("Mruczek")
    # print(cat.make_sound())
    cats = cat_creator()
    for cat in cats:
        print(cat.make_sound())
        cat.eat_mause()


if __name__ == "__main__":
    main()
