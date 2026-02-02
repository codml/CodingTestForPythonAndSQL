def solution(phone_book):
    hash = set()
    phone_book.sort(key=len)
    for phone in phone_book:
        for i in range(len(phone)):
            if phone[:i+1] in hash:
                return False
        hash.add(phone)
    return True