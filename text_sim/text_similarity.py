import math
from text_sim.TermFrequency import TermFrequency
from text_sim.TokenProcessing import TokenProcessing
from text_sim.utils import char_grams, text_grams, get_text_stats, tokenized_ngram_score

"""
arguments: text1->str, text2->str, text_ngram->int, rm_punctuation->bool, lower->bool
return; score -> float

create a dictioanry of tokens and their respective frequency for each sample and perform IOU

+ vanilla text similarity algorithm
"""

def jaccard_similarity(text1, text2, tokenize, rm_punctuation, lower):
	
	# normalizing the text by removing punctuation and lowercasing the tokens
	# perform same pre-processing steps for each sample
	tf1 = TermFrequency(text1).term_frequency(tokenize=tokenize, rm_punctuation=rm_punctuation, lower=lower) 
	tf2 = TermFrequency(text2).term_frequency(tokenize=tokenize, rm_punctuation=rm_punctuation, lower=lower)

	vocab = set(list(tf1.keys())).union(set(list(tf2.keys())))
	
	intersection = 0.0

	for token in vocab:
		if (token in tf1) and (token in tf2):
			intersection += (tf1[token]*tf2[token])

	union1 = math.sqrt(sum([tf1[token]**2 for token in tf1.keys()]))
	union2 = math.sqrt(sum([tf2[token]**2 for token in tf2.keys()]))

	return round(intersection/(union1*union2), 4)


"""
arguments: text1->str, text2->str, text_ngram->int, rm_punctuation->bool, lower->bool
return: score -> float

create a character level n-gram for each text sample -> set(tuples)

compare every characted n-gram of text1 with the character ngram of text2 and return the jaccard distance

- does not consider word ordering in the text
+ performs character level comparison - a form of stemming and lemmatization is considered
"""

def char_gram_jaccard_similarity(text1, text2, char_ngram, rm_punctuation, lower):
	
	# normalizing the text by removing punctuation and lowercasing the tokens
	# perform same pre-processing steps for each sample
	pp_text1 = TokenProcessing(text1).pre_process(rm_punctuation=rm_punctuation, lower=lower)
	pp_text2 = TokenProcessing(text2).pre_process(rm_punctuation=rm_punctuation, lower=lower)

	# get character level n-grams for each sample
	shingles_text1 = char_grams(pp_text1, char_ngram)
	shingles_text2 = char_grams(pp_text2, char_ngram)

	intersection = len(shingles_text1 & shingles_text2)
	union = float(len(shingles_text1) | len(shingles_text2))
	
	try:
		return round(intersection/union, 4)
	except:
		return 1.0
"""
arguments: text1->str, text2->str, text_ngram->int, rm_punctuation->bool, lower->bool
return: score -> float

create a token level n-gram for each text sample -> set(tuples)

compare every n-gram of text1 with the ngram of text2 and store the normlaized token matches

+ balances ordered vs un-orodered similar pieces of text
"""
def text_gram_jaccard_similarity(text1, text2, text_ngram, rm_punctuation, lower):

	# normalizing the text by removing punctuation and lowercasing the tokens
	# perform same pre-processing steps for each sample
	pp_text1 = TokenProcessing(text1).pre_process(rm_punctuation=rm_punctuation, lower=lower)
	pp_text2 = TokenProcessing(text2).pre_process(rm_punctuation=rm_punctuation, lower=lower)

	# removing duplicate n-grams (might overestimate the score)
	text_grams1 = set(text_grams(pp_text1, text_ngram))
	text_grams2 = set(text_grams(pp_text2, text_ngram))

	score = []

	# find the closest matching n-grams of each sample with the other sample
	for txt_gm1 in text_grams1:
		max_ngram_score = 0.0
		
		for txt_gm2 in text_grams2:
			max_ngram_score = max(max_ngram_score, tokenized_ngram_score(txt_gm1, txt_gm2))

		score.append(max_ngram_score)
	
	return round(sum(score)/len(score), 4)

if __name__ == "__main__":
	
	# sample1-sample2 similarity should be more than sample1-sample3 similarity

	sample1 = "The easiest way to earn points with Fetch Rewards is to just shop for the products you already love. If you have any participating brands on your receipt, you'll get points based on the cost of the products. You don't need to clip any coupons or scan individual barcodes. Just scan each grocery receipt after you shop and we'll find the savings for you."
	sample2 = "The easiest way to earn points with Fetch Rewards is to just shop for the items you already buy. If you have any eligible brands on your receipt, you will get points based on the total cost of the products. You do not need to cut out any coupons or scan individual UPCs. Just scan your receipt after you check out and we will find the savings for you."
	sample3 = "We are always looking for opportunities for you to earn more points, which is why we also give you a selection of Special Offers. These Special Offers are opportunities to earn bonus points on top of the regular points you earn every time you purchase a participating brand. No need to pre-select these offers, we'll give you the points whether or not you knew about the offer. We just think it is easier that way."

	jac_sim1 = jaccard_similarity(sample1, sample2, tokenize=True, rm_punctuation=True, lower=True)
	jac_sim2 = jaccard_similarity(sample1, sample3, tokenize=True, rm_punctuation=True, lower=True)
	jac_sim3 = jaccard_similarity(sample2, sample3, tokenize=True, rm_punctuation=True, lower=True)

	print(jac_sim1, jac_sim2, jac_sim3)

	jac_sim1 = char_gram_jaccard_similarity(sample1, sample2, char_ngram=2, rm_punctuation=True, lower=True)
	jac_sim2 = char_gram_jaccard_similarity(sample1, sample3, char_ngram=2, rm_punctuation=True, lower=True)
	jac_sim3 = char_gram_jaccard_similarity(sample2, sample3, char_ngram=2, rm_punctuation=True, lower=True)

	print(jac_sim1, jac_sim2, jac_sim3)

	jac_sim1 = text_gram_jaccard_similarity(sample1, sample2, text_ngram=3, rm_punctuation=True, lower=True)
	jac_sim2 = text_gram_jaccard_similarity(sample1, sample3, text_ngram=3, rm_punctuation=True, lower=True)
	jac_sim3 = text_gram_jaccard_similarity(sample2, sample3, text_ngram=3, rm_punctuation=True, lower=True)

	print(jac_sim1, jac_sim2, jac_sim3)
