# TextReadability

Overview: A model to assess readibility, trained on data from Common Core. The project also creates a glossary, whereby a list of 10 hardest words will be picked out and printed alongside their dictionary definitions. 

* Text data and reading level classficiation taken from Common Core English Language Arts, Appendix B
* Cleaned and processed texts for key features
* Fitted using an ordinal regression model (mord.LogisticAT: https://pythonhosted.org/mord/reference.html#mord.LogisticAT)
* Sorts words by difficulty (calcuted using combined z-scores based on word frequency, length, and syllables per word)
* Prints the definitions of the ten most difficult words
* Pickled and fully productionized, now exists as a web application: www.lexlearntogether.com

By Akul Kesarwani and Anchi (Bryant) Xia, 2020

# Purpose

# Data Used

# Explorartory Data Analysis and Model Fitting

Below is a heatmap showing the correlation coefificent of all variables involved (calculated / constructed variables + difficulty)

![Correlation](https://github.com/AkulK1/TextReadability/blob/master/images/corr.PNG)

# Model Performance

# Final Product
