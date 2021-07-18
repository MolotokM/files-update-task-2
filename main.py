text_file = open("text_file.txt", "r")
for text in text_file:
    print("Main text:", text)
text_file = open("text_file.txt")
lines = text_file.readlines()
for line in reversed(lines):
    print("New text:", line)
text_file.close()
