import re

class TokenProcessing:
	''' Class for including all pre-processing steps  '''
	
	def __init__(self, text):
		self.text = text
		self.tokenized_text = None
		self.term_count = dict()
		self.norm_term_count = dict()
	
	# replace punctuation with an empty string	
	def remove_punctuation(self):
		self.text = re.sub(r'[^\w\s]', '', self.text)

	# one of the normalization steps in pre-processing text
	def lowercase_text(self):
		if type(self.text) == str:
			self.text = self.text.lower()
		
		elif type(self.text) == []:
			self.text =  " ".join(token.lower() for token in self.text.split(" ") if token != "")
		
	
	# tokenize the sentence based on whitespaces
	def tokenize(self):
		
		self.tokenized_text = self.text.split(" ")
		
		return self.tokenized_text

	'''
	arguments: tokenize->bool, rm_punctuation->bool, lower->bool
	return: self.text -> str (pre-processed text based on bool values)
	'''
	def pre_process(self, tokenize=False, rm_punctuation=False, lower=False):
		
		if lower == True:
			self.lowercase_text()

		if rm_punctuation == True:
			self.remove_punctuation()
		
		if tokenize == True:
			self.tokenized_text = self.tokenize()
			return self.tokenized_text

		return self.text

if __name__ == "__main__":
	pass
