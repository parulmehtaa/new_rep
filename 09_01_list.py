def wish(names,wishes):
    for i in range(0, len(names),1):
        for j in range(0,len(wishes),1):
            print(f"{wishes[j]} {names[i]}" )


def main():
    names=["Parul", "XXXX", "YYYY", "ZZZZ"]
    wishes=["Good Morning", "Good Evening", "Good Night"]
    wish(names,wishes)

main()
