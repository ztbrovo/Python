# Comprehensive application -- Business Card Management System
# Frame construction
# card_main.py----Main operating cycle     cards_tools.py
import cards_tool
# while true to make the code executed always.
while True:
    # TODO to show menu
    cards_tool.show_menu()
    action_str = input("please choose one action")
    print("you chose 【%s】" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            cards_tool.new_card()
        elif action_str == "2":
            cards_tool.show_all()
        elif action_str == "3":
            cards_tool.search_card()
        # if don not want to write inner code, use pass.
        # pass
    elif action_str == "0":
        print("welcome to the cards management system")
        break
        # pass
    else:
        print("your input is wrong,please choose again.")
