# record all cards dictionary
card_list = []


def show_menu():
    print("*" * 50)
    print("welcome to the card management system V 1.0")
    print("")
    print("1. add new card")
    print("2. show all")
    print("3. search card")
    print("")
    print("0. equip the system")
    print("*" * 50)


def new_card():
    print("-" * 50)
    print("add new card")

    name_str = input("input name_str")
    phone_str = input("input phone_str number")
    qq_str = input("input qq_str")
    email_str = input("input email_str")

    card_dict = {"name_str": name_str,
                 "phone_str": phone_str,
                 "qq_str": qq_str,
                 "email_str": email_str}

    card_list.append(card_dict)

    print(card_list)
    print("success to add the card %s" % name_str)


def show_all():
    print("-" * 50)
    print("show all")

    if len(card_list) == 0:
        print("there's no record,please add the new one")
        return
    # return ---- the following code can't be executed.

    for name in ["name", "phone", "qq", "email"]:
        print(name, end="\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name_str"],
                                        card_dict["phone_str"],
                                        card_dict["qq_str"],
                                        card_dict["email_str"]
                                        ))


def search_card():
    print("-" * 50)
    print("search card")

    find_name = input("please input the name: ")
    for card_dict in card_list:
        if card_dict["name_str"] == find_name:
            print("found it!")
            print("name\t\tphone\t\tqq\t\temail")
            print("=" * 50)
            print("%s\t\t%s\t\t%s\t\t%s" % (card_dict["name_str"],
                                            card_dict["phone_str"],
                                            card_dict["qq_str"],
                                            card_dict["email_str"]
                                            ))
            deal_card(card_dict)
            break
    else:
        print("sorry, can't find it")


def input_card_info(dict_value, tip_message):
    """

    :param dict_value: Original key
    :param tip_message: input
    :return:if input return message; if not, return original key.
    """
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value


def deal_card(find_dict):
    print(find_dict)

    action_str = input("please choose one:"
                       "1.edit 2.delete 3.back to main menu")
    if action_str == "1":
        find_dict["name_str"] = input_card_info(find_dict["name_str"], "name: ")
        find_dict["phone_str"] = input_card_info(find_dict["phone_str"], "phone: ")
        find_dict["qq_str"] = input_card_info(find_dict["qq_str"], "qq: ")
        find_dict["email_str"] = input_card_info(find_dict["email_str"], "email: ")
        print("edit the card")

    elif action_str == "2":
        card_list.remove(find_dict)
        print("delete the card")
