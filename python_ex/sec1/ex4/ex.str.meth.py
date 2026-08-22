             #Comman string method

sentence = "    hello! my name is suve     "

# 1)Split function
words = sentence.split()
print("split function :",words)

# 2)Join function
joined =" ".join(words)
print("join the words: ",joined)

# 3)Replace function
replaced =sentence.replace("suve","suvx")
print("replace function :",replaced)

# 4) Strip function
result = sentence.strip()
print("strip function :",result)