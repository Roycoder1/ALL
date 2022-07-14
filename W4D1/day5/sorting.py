text = input("Input comma separated sequence of words")
splitSentence = [word for word in text.split(",")]
print(",".join(sorted(list(set(splitSentence)))))

