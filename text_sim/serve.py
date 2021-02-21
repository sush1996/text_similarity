import math
from text_sim.TermFrequency import TermFrequency
from text_sim.TokenProcessing import TokenProcessing
from text_sim.utils import char_grams, text_grams, get_text_stats, tokenized_ngram_score
from text_sim.text_similarity import jaccard_similarity, char_gram_jaccard_similarity, text_gram_jaccard_similarity


def get_model_api():    
	''' wrapping all the main functions into a single api function '''
	
	'''
	arguments: text1->str, text2->str
	return: similarity score -> float
	'''
	def model_api(text1, text2):
		
		jac_sim = jaccard_similarity(text1, text2, tokenize=True, rm_punctuation=True, lower=True)
		jac_sim_char = char_gram_jaccard_similarity(text1, text2, char_ngram=2, rm_punctuation=True, lower=True)
		jac_sim_text = text_gram_jaccard_similarity(text1, text2, text_ngram=3, rm_punctuation=True, lower=True)
		
		''' 
		problem description states that the 2 wtext samples should give a similarity score of 0
		if there are no tokens that are common between the 2 pieces of texts character n-gram does 
		not operate at token level and gives optimistic similarity scores.
		'''
		if jac_sim == 0.0:
			return 0.0
		else:
			# average out the different jaccard similarity scores only if the vanilla jaccard similarity score is > 0
			return round((jac_sim+jac_sim_char+jac_sim_text)/3.0, 4)

	return model_api

if __name__ == "__main__":
	pass
