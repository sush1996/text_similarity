import statistics


"""
arguments: text->str, char_ngram->int
return: set(character n-grams)

create character level n-gram for the sample
"""
def char_grams(text, char_ngram=2):
	return set([text[ix:ix+char_ngram] for ix in range(len(text)-char_ngram)])


"""
arguments: text->str, char_ngram->int (odd)
return: list(tuple(token n-grams))

create token level n-gram for the sample
"""
def text_grams(text, text_ngram=3):

	tokenized_text = text.split(" ")
	for i in range(text_ngram//2):
		tokenized_text.insert(0, "<PAD>")
	
	for i in range(text_ngram//2):	
		tokenized_text.append("<PAD>")

	# token n-gram by considering n//2 tokens to the right and and left 
	return [tuple(tokenized_text[ix-(text_ngram//2):ix+(text_ngram//2)+1]) for ix in range(text_ngram//2, len(tokenized_text)-(text_ngram//2))]

"""
arguments: ngram1->list[str], ngram2->list[str]
return: score->float

keeps a count of the similar tokens while masking the <PAD> toke
"""
def tokenized_ngram_score(ngram1, ngram2):
	score, count = 0, 0

	for token1, token2 in zip(ngram1, ngram2):
		if token1 != "<PAD>":
			if token1 == token2:
				score += 1
			count += 1
				
	return score/float(count) if count > 0  else 0.0

"""
arguments: ngram1->list[str], ngram2->list[str]
return: score->float

keeps a count of the similar tokens while masking the <PAD> toke
"""
def get_text_stats(text1, text2):

	if type(text1) == str:
		data = [len(token) for token in text1.split(" ")] + [len(token) for token in text2.split(" ")]
	
	elif type(text1) == list:
		data = [len(token) for token in text1] + [len(token) for token in text2]

	mean, stddev = statistics.mean(data), statistics.stdev(data)
	
	return mean, stddev

if __name__ == "__main__":
	pass