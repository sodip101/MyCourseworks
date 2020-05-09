def displaybooklist(List):# function to display book list that takes 2D list as paramter
    for item in List:
        print("|",item[0]," "*(4-len(item[0])),"|",
              "|",item[1]," "*(20-len(item[1])),"|",
              "|",item[2]," "*(13-len(item[2])),"|",
              "|",item[3]," "*(8-len(str(item[3]))),"|",
              "|",item[4]," "*(8-len(item[4])),"|",)
