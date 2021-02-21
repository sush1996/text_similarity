from text_sim.TokenProcessing import TokenProcessing

class TermFrequency(TokenProcessing):
	''' Inherits properties from the TokenProcessing class '''
	
	def __init__(self, text):
		TokenProcessing.__init__(self, text)
		self.term_count = dict()
	
	'''
	arguments: tokenize->bool, rm_punctuation->bool, lower->bool
	return: self.term_count -> dict() (a frequency dictionary for the tokens in the text sample)
	'''
	def term_frequency(self, tokenize, rm_punctuation, lower):

		for token in self.pre_process(tokenize=tokenize, rm_punctuation=rm_punctuation, lower=lower):
			if token not in self.term_count:
				self.term_count[token] = 1
			else:
				self.term_count[token] += 1

		return self.term_count

if __name__ == "__main__":
	pass
