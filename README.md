
# [Text Readability](https://readfluid.com)

Overview: A model to assess readability, trained on data from Common Core. The project also creates a glossary, whereby a list of 10 hardest words will be picked out and printed alongside their dictionary definitions. 

* Text data and reading level classification taken from Common Core English Language Arts, Appendix B
* Cleaned and processed texts for key features
* Fitted using an ordinal regression model (mord.LogisticAT: https://pythonhosted.org/mord/reference.html#mord.LogisticAT)
* Sorts words by difficulty (calculated using combined z-scores based on word frequency, length, and syllables per word)
* Prints the definitions of the ten most difficult words
* Pickled and fully productionized, now exists as a web application: https://readfluid.com/

By Akul Kesarwani and Anchi (Bryant) Xia, 2020

# Purpose

Our intention with the app is to make for a smoother reading experience by helping users understand how complex their text is and provide them with a glossary of some of the most difficult words, printed alongside of their dictionary definitions.

There is a considerable number of English Language Learners in our school district (Lexington Public Schools). For english language learners and young readers, building up their reading ability entails engaging with texts of increasing difficulty. Using various linguistic attributes from the text, from syllables per word to the average length of verbs, we can fit these calculated features into a ordinal regression based model that would return a readability level prediction. This will be informative to users who are interested in knowing how challenging the text is before reading.

By having a glossary, we wish to help users improve their vocabulary without needing to constantly interrupt their reading experience to look up new words. And having familiarized themselves with some of the most difficult words in the text, seeing them again in context could potentially strengthen both the users’ understanding of new vocab and their overall compression of the text.

# Data Used

Texts we used to train the model are from Common Core’s English Language Arts Appendix B. Since text difficulty is our response variable, we wanted to make sure that it cannot simply be calculated from the predictor variables themselves. This meant we could not use, say, the Lexile score as a measurement of readability.

To address the issue, we turned to Common Core’s Appendix B. Included in the appendix are sample texts sorted by grade level. Though educators who performed the sorting did refer to quantitative data like Lexile scores, their insights and experience undoubtedly played a significant role as well. By training our model with their text classifications, we look to capture patterns underlying their understanding instead of relying on quantitative attributes alone.

# Exploratory Data Analysis and Model Fitting

![Correlation](https://github.com/AkulK1/TextReadability/blob/master/images/corr.PNG)

We performed some exploratory data analysis after calculating text attributes. The heat map above shows how predictors correlate with assigned text difficulty as well as with each other. The following list is what went into generating the predictions you get:

* Syllables per word
* Words per sentence
* Percentage of monosyllabic words
* Flesch-Kincaid readability score
* Ari readability score
* Dale readability score
* Gunning-Fog readability score
* CLI readability score
* Linsear Write readability score
* number of determiners / sentence
* number of Subordinating conjunctions / sentence
* Average verb length

We tried a number of models, from a simple decision tree regressor to random forest, before settling on an implementation of the ordinal logistic regression model by Mord . Since our response variable, text difficulty / readability, is a categorical variable with multiple levels, it is no surprise that their model stood out in our model fitting process.

# Model Performance

Our final model had an accuracy of 0.41519, an adjacency of 0.84074 (prediction within +/- 1 of the actual reading level), and a mean absolute error of 0.77037. These measures are averages computed over 50 train-test-split sets with 30% of our data as the test size.

That said, there are reasons to believe that the productionized model is actually better. For one, it is trained on all of our available data instead of 70% of it. We also grouped school grades in the upper level altogether, which makes a predicted score of 6 a slightly broader category, though that should theoretically improve the model’s performance.

# Final Product

https://readfluid.com/model.html
