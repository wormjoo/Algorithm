def first_check(s):
    if "a" in s or "e" in s or "i" in s or "o" in s or "u" in s:
        return True
    else:
        return False


def second_check(s):
    v_cnt = 0
    c_cnt = 0

    for x in s:
        if x in ["a", "e", "i", "o", "u"]:
            v_cnt += 1
            c_cnt = 0
        else:
            c_cnt += 1
            v_cnt = 0
        if v_cnt == 3 or c_cnt == 3:
            return False

    return True


def third_check(s):
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            if s[i] != "e" and s[i] != "o":
                return False
    return True


while 1:
    case = input()
    if case == "end":
        break
    if first_check(case) and second_check(case) and third_check(case):
        print("<" + case + ">", "is acceptable.")
    else:
        print("<" + case + ">", "is not acceptable.")
