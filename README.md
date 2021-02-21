# Quantify Text Similarity

This Github repo contains programs to allow you to compare 2 text samples in your browser using a combination of the vanilla Jaccard similarity and slightly modified versions of the same metric using character n-grams and text n-grams.

Navigate to the directory containing `app.py` and run it using the command: <br/>
`python3 app.py` 
<br/>

This will open up something similar to what's shown below:<br/>
![Terminal Output](/images/terminal2.png)
<br/>

Hover your cursor over the hyperlink in red,right click and select `Open Link`. This should pop the below webpage on your browser:<br/>
![Webpage Output](/images/webpage.png)
<br/>

Enter the 2 text samples you want to compute the similarity against and hit `Check Similarity` on the webpage and you should be able to see the similarity score <br/>
![Webpage Output](/images/webpage2.png)
<br/>
<br/>

# Requirements
* flask 1.1.2 `pip3 install flask==1.1.2`

# Running it using Docker
assuming docker is installed in your system, you can run the below command to compute text similarity on a web browser using docker:<br/>
`sudo docker run -p 5000:5000 sush1996/text_similarity:latest`

# References
* [Text n-grams](https://albertauyeung.github.io/2018/06/03/generating-ngrams.html) 
* [Character n-grams](https://github.com/emarkou/Text-Similarity)
* [Jaccard Similarity](https://studymachinelearning.com/jaccard-similarity-text-similarity-metric-in-nlp/)
* [Serving a model using Flask](https://guillaumegenthial.github.io/serving.html)
