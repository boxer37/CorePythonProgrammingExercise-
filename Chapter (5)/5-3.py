# _*_ coding:utf-8 _*_

# 5-3

def rank(score):
    if score>=90:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

def main():
    try:
        score = int(raw_input("Enter a score: "))
        if score in range(0,101):
            print rank(score)
        else:
            print "The score must in 0~100! "
            main()
    except:
        print "Something was wrong, please enter a number! "
        main()

if __name__ == "__main__":
    main()
