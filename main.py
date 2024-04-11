def words(text):
    return len(text.split())

def letters(text):
    d = {}
    l = []
    for i in text:
        d[i.lower()] = d.get(i.lower(),0) + 1
    for k,v in d.items():
        if k.isalpha():
            l.append({"letter":k,"count":v})
    return l

def sort_on(d):
    return d['count']


if __name__ == "__main__":
    with open("books/frankenstein.txt", "r") as f:
        file_contents = f.read()
        print("--- Begin report of books/frankenstein.txt ---")
        w = words(file_contents)
        print(f"{w} words found in the document")
        l = letters(file_contents)
        l.sort(reverse=True, key=sort_on)
        for i in l:
            print(f"the '{i['letter']}' character was found {i['count']} times")
    