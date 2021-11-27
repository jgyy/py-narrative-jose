"""
Overview of Regular Expressions
"""
from re import search, findall, finditer, compile as rcompile


def main():
    """
    main function
    """
    text = "The agent's phone number is 408-555-1234. Call soon!"
    print("phone" in text)
    pattern = "phone"
    print(search(pattern, text))
    pattern = "NOT IN TEXT"
    print(search(pattern, text))
    pattern = "phone"
    match = search(pattern, text)
    print(match)
    print(match.span())
    print(match.start())
    print(match.end())
    text = "my phone is a new phone"
    match = search("phone", text)
    print(match.span())
    matches = findall("phone", text)
    print(matches)
    print(len(matches))
    for match in finditer("phone", text):
        print(match.span())
    print(match.group())
    text = "My telephone number is 408-555-1234"
    phone = search(r"\d\d\d-\d\d\d-\d\d\d\d", text)
    print(phone.group())
    print(search(r"\d{3}-\d{3}-\d{4}", text))
    phone_pattern = rcompile(r"(\d{3})-(\d{3})-(\d{4})")
    results = search(phone_pattern, text)
    print(results.group())
    print(results.group(1))
    print(results.group(2))
    print(results.group(3))
    print(search(r"man|woman", "This man was here."))
    print(search(r"man|woman", "This woman was here."))
    print(findall(r".at", "The cat in the hat sat here."))
    phrase = "there are 3 numbers 34 inside 5 this sentence."
    print(findall(r"[^\d]", phrase))
    print(findall(r"[^\d]+", phrase))
    test_phrase = "This is a string! But it has punctuation. How can we remove it?"
    print(findall("[^!.? ]+", test_phrase))
    clean = " ".join(findall("[^!.? ]+", test_phrase))
    print(clean)
    text = "Only find the hypen-words in this sentence. But you do not know how long-ish they are"
    print(findall(r"[\w]+-[\w]+", text))
    text = "Hello, would you like some catfish?"
    texttwo = "Hello, would you like to take a catnap?"
    textthree = "Hello, have you seen this caterpillar?"
    print(search(r"cat(fish|nap|claw)", text))
    print(search(r"cat(fish|nap|claw)", texttwo))
    print(search(r"cat(fish|nap|claw)", textthree))


if __name__ == "__main__":
    main()
