
table_foods = ["apples", "oranges", "cherries", "banana"]
table_Hosts = ["Alice", "Bob", "Carol", "David"]
table_pets = ["dogs", "cats", "moose", "goose"]


def printTable(tableData, leftWidth, RightWidth):
    print("Jenny's Gathering".center(leftWidth + RightWidth, "*"))
    for k1, v in tableData.items():
        print(k1.ljust(leftWidth, "-") + str(v).rjust(RightWidth))
        
alltable_gathering = {"Alice": [ "apple", 5, "dog", 1 ],
                      "Bob": [ "oranges", 8, "cats", 3 ], 
                      "Carol": [ "cherries", 24, "moose", 1 ], 
                      "David": [ "banana", 4, "goose", 2 ]}

printTable(alltable_gathering, 20, 20)