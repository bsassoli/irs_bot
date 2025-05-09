# CHAPTER 10

# Statistical inference

 

  

# 10.1 THE HIGGS BOSON AND DRAWING INFERENCES WITH STATISTICS

After reading this section, you should be able to:

- Identify three roles of statistical inference and illustrate them with examples
- Describe how probability theory extends the reach of statistics
- Distinguish frequency distribution from probability distribution

From a “bump” in data to a new fundamental particle

In 2012, scientists at CERN (European Center for Nuclear Research) in Geneva, Switzerland, announced the discovery of a new boson, a very tiny particle whose existence is crucial to our understanding of the fundamental structure of matter. Using CERN’s Large Hadron Collider (LHC), a 27‐kilometer (17‐mile) tunnel straddling the Swiss‐French border, scientists had been repeatedly observing the outcome of collisions among protons (one kind of particle in the nucleus of atoms). These collisions produce a shower of new particles, most of which are unstable and decay into other particles in a tiny fraction of a second.

New particles formed in proton‐proton collisions in the LHC can be identified by tracking their trajectory, energy, and momentum. Detecting their mass is particularly relevant to distinguishing between different types of particles. However, because sub‐atomic particles are so small, it’s a challenge to distinguish the signature properties of new particles from background events.

In the summer of 2012, scientists recorded a “bump” in their data, corresponding to a particle with a mass between 125 and 127 GeV/c2 (one gigaelectronvolt, or 1.783 × 10−27 kg). This is about 133 times heavier than protons. It was thought that this recorded bump could provide evidence of a new particle—perhaps of the long‐sought Higgs boson. Using methods for statistical inference, the scientists calculated that this bump emerging from background events in the collider would occur by chance, without the presence of a boson, only once in three million trials. Because this probability was so low, the scientists rejected the idea that the bump occurred purely by chance and concluded it had been caused by a Higgs boson.

DOI: 10.4324/9781003300007-11
---
# 242 Statistical inference

 

  

Portrait of Fabiola Gianotti, project leader and spokesperson for the ATLAS experiment at CERN involved in the discovery of the Higgs boson in July 2012

# FIGURE 10.1

Scientists all over the world were thrilled with this news. The discovery of the Higgs boson could lend additional support to the standard model of particle physics, which is scientists’ current best theory of the most basic forces and building blocks of the universe. The hypothesized Higgs boson was supposed to be like the glue of the universe: it’s what joins everything together and gives it mass. It seemed this hypothesis now had been tested and confirmed.

The groundbreaking discovery of the Higgs boson illustrates how fundamental statistical inference is to scientific findings. Very often, techniques of inferential statistics are required to know what conclusions are supported by the empirical evidence.

# From description to inference

Descriptive uses of statistics enable scientists to summarize and represent data sets in meaningful ways. In Chapter 9, we saw how to do this visually with charts and graphs and also numerically with means, standard deviations, and correlation coefficients. However, merely describing data sets regularly falls short of what scientists and everyone else are interested in. We are also interested in generalizing, making predictions, and testing hypotheses based on data sets.

Data collected in pre-election polls are used not merely to describe one group of voters but to make predictions about the eventual outcome of the elections. Basketball fans want to predict, from his past record, whether LeBron James’s free-throw success will...
---
# Statistical inference

improve over time. Health researchers want to test, from observed treatment effects in a medical trial, whether a medical drug is efficacious against a certain ailment in the general population. For these kinds of interests—predicting the future, generalizing from a sample, and testing hypotheses—we need inferential statistics.

Inferential statistics is an important form of inductive reasoning that extends the reach of descriptive statistics with the use of probability theory. Coin tosses, dice throws, LeBron’s free throws, people’s voting intentions, effects of medical drugs, and more can all be treated as random variables. Inferential statistics can be used to analyze data sets to predict yet-to-be-measured values of those variables. For example, one might infer from a sequence of heads and tails whether the coin is unfair, predict from his past record whether LeBron’s free-throw success will improve over time, predict from an opinion poll which candidate will win the election, and infer from observed treatment effects to the efficacy of a medical drug.

Probability theory, introduced in Chapter 8, is used to expand statistical tools from description to inference. The basic idea is that observed frequencies are used to estimate probabilities.

A frequency distribution is how often a variable takes on each value in some data set. This might be depicted in a table or histogram, for instance. A relative frequency distribution records the proportion of occurrences for each value instead of the absolute number. For example, suppose you have a bag containing 35 M&Ms of different colors: M&M Color = {brown, red, yellow, green, blue, orange}. The second column of Table 10.1 depicts the frequency distribution of each color, and the third and fourth columns of Table 10.1 depict the relative frequency distribution—in terms of proportion in column 3 and in terms of percentage in column 4. Each of columns second, third, and fourth is a way to display the proportions of the colors in your particular bag of 35 M&Ms.

# Table 10.1

Frequency Distribution of Bag of 35 M&Ms (second column); Relative Frequency Distribution (third and fourth columns)

|Color|Frequency|Proportion|Percentage|
|---|---|---|---|
|Blue|1|1/35|2.86%|
|Orange|3|3/35|8.57%|
|Yellow|4|4/35|11.43%|
|Red|5|5/35|14.29%|
|Green|5|5/35|14.29%|
|Brown|17|17/35|48.57%|

---
# 244 Statistical inference

Relative frequency distributions can be used to estimate the probability distribution for a variable—that is, how often the variable is expected to take on each of a range of values. In this example, this isn’t a description of your bag of M&Ms, but a prediction about other bags. Some bags will have a distribution of colors similar to yours; others will vary more. Based on your sample bag of M&Ms, you may estimate that if you take a random bag of M&Ms, open it, and choose an M&M at random from that bag, the probability of getting a blue M&M is about 3%.

Let’s consider a very simple probability distribution to illustrate how probability distributions support statistical inference: the probability distribution of the number of times heads are expected to come up over 100 coin tosses. The range of possible outcomes is 0 to 100: heads might come up as few as zero times and up to a maximum of 100 times. In other words, these are the possible values of the variable Heads per 100 coin tosses.

In theory, we could calculate the probability of each outcome in that range using probability theory developed in Chapter 8. Notice that Pr(heads = 0) is equivalent to Pr(tails and tails and . . . tails). If every coin toss comes up tails, then there are zero instances of heads. What is the probability of that ever happening, assuming the coin is fair? The probability of getting tails on a throw is always .5, and we multiply probabilities to calculate the probability of multiple independent events all occurring. The probability of getting 100 tails would be a really, really tiny number: 1/2 × 1/2 × . . . × 1/2, or 1/2100. Notice that it’s also the same as the probability that heads comes up 100 times.

In between 0 and 100, the calculation for the probability of every value of number of times heads comes up is much more complicated, though in principle we know enough probability theory to do these calculations. We won’t carry out the calculations, but considering how they would go gives us a sense for how the probability changes for intermediate numbers of heads.

Notice that there is only one way to get zero heads and only one way to get 100 heads: for one, the coin never lands heads, and, for the other, the coin lands heads all 100 times. Now consider getting exactly one head out of 100 tosses. There are 100 different ways that could happen! It might be the first toss, or the second toss, or the third toss, or the 37th, or any other single toss. So, Pr(heads=1) is equivalent to Pr[(heads and tails and tails and . . . tails) or (tails and heads and tails and . . . tails) or . . .] and so on, up until the circumstance of getting heads only on the 100th toss.

Using our previous calculation, and because we add when calculating the probability of one of several mutually exclusive events occurring, this is 1/2100 + 1/2100 + . . . + 1/2100, or 100 × 1/2100. This is still a tiny number, but it’s 100 times bigger than the probability of heads coming up no times or every time. The same calculation gives us the probability that heads comes up 99 times; so we’re building our probability distribution from both ends at the same time.

There are even more ways for heads to come up twice (or 98 times), and even more ways than that for heads to come up three times (or 97 times). Each time we add another outcome of heads the calculation becomes more complicated, and the probability of getting that number of heads increases. The increasing probability of each of these outcomes isn’t linear; the increase gets bigger each time.
---
# Statistical inference

The probability distribution will be symmetric, since the calculation is the same whether the number of heads = 0 or 100, whether the number of heads = 1 or 99, and so forth. The middle of the distribution, the most probable outcome, is thus 50: that you get heads on 50/100, or .5, of the coin tosses. Figure 10.2 shows a histogram of the whole probability distribution. As the number of tosses increases, the shape of the histogram becomes a bell curve. Recall from Chapter 9 that a bell curve is a perfectly symmetric, unimodal distribution for continuous variables—what is also called a normal distribution.

The normal distribution—unimodal and symmetric—is especially important for statistical reasoning. Like coin tosses, the behavior of random variables over many repeated, independent trials tend to have a probability distribution that is normal. This results from what is known in statistics as the central limit theorem: the statistical claim that samples with a large enough size will have a mean approximating the mean of the population. What varies for different random variables is the central tendency and variability of the normal distribution, which—as we saw in Chapter 9—can be described with mean and standard deviation. Whereas the mean value of heads on 100 coin tosses is 50, the mean value of 6s on 100 dice rolls is 16.67 (1/6 × 100).

|0.09|0.08|0.07|0.06|0.05|0.04|0.03|0.02|0.01|0|
|---|---|---|---|---|---|---|---|---|---|
|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|heads per 100 coin tosses (k)|

Probability distribution of heads for 100 coin tosses; the mean of this distribution is 50 and its standard deviation is 5.
---
# 246 Statistical inference

Standard deviation, but not the mean, is also influenced by the number of trials. You are more likely to get none or all heads in five coin tosses than in 100 coin tosses; the standard deviation is larger for the former.

Probability distributions for fair coins and dice can be calculated directly from the probabilities of the individual outcomes, as sketched earlier for 100 coin tosses. This is not so for variables like success rate at free throws and proportion of blue M&Ms.

For variables like those, the frequency distribution of a data set is used to predict the probability distribution. The predicted probability distribution can then be the basis for our expectations for other, relevantly similar data sets, like future basketball games and unopened bags of M&Ms.

# EXERCISES

# 10.1 Recall:

Describe how inferential statistics can be used to make predictions, generalize from an example, and test a hypothesis, and give an example of each.

# 10.2 Recall:

Define frequency distribution, and describe in your own words how mean and standard deviation in descriptive statistics relate to frequency distributions. Then, define probability distribution, and describe in your own words how inferential statistics makes use of probability distributions.

# 10.3 Think:

Define descriptive statistics and inferential statistics. In your own words, describe how probability theory is used to make inferential statistics possible.

# 10.4 Apply:

In class, or with a group of several classmates, find a coin for each person and carry out the following steps, each person recording the answers individually.

1. Agree in your group about your expectation for the mean percentage of coin tosses that will land heads up; record this percentage.
2. Each person should toss their coin four times, recording each result as either heads or tails. Summarize your individual result as the ratio of heads to tails. This will be either 0:4, 1:3, 2:2, 3:1, or 4:0.
3. Record how many people in your group got each of the possible ratios: 0:4, 1:3, 2:2, 3:1, and 4:0. Draw a histogram showing these results.
4. Some people didn’t get a ratio of 2:2. Why not, when you predicted 50% heads?
5. Should we expect each person to get the same ratio of heads to tails on the next four coin tosses as they did on the first four? Why or why not?
6. Each person should toss his or her coin four more times, recording each result and then summarizing as a new ratio of heads to tails.
7. Add these ratios to the data set of the first round of coin tosses. There should now be twice as many series of four-coin tosses. Draw a new histogram describing the complete data set.
8. Compare the histogram from (d) to the histogram from (g). What has changed? Why?
---
# Statistical inference

# 10.5 Apply:

Convert the following data about the outcomes of 11 rolls of a die to a relative frequency distribution:

- 1st roll: 4
- 2nd roll: 3
- 3rd roll: 4
- 4th roll: 6
- 5th roll: 2
- 6th roll: 1
- 7th roll: 6
- 8th roll: 4
- 9th roll: 5
- 10th roll: 5
- 11th roll: 6

Then, draw a histogram showing the relative frequency distribution for this data set.

  

# 10.6 Apply:

Construct a histogram of the probability distribution for an experiment in which a die is thrown five times and the number of occurrences of 4 is recorded.

# 10.2 STATISTICS IN ESTIMATION

After reading this section, you should be able to:

- Define sample mean and sample standard deviation and indicate how these differ from mean and standard deviation for descriptive statistics
- Describe how inferential statistics is used to estimate population values from a sample
- Indicate how sample size and representativeness matter for estimation

# Estimating from a sample

One common application of statistical inference methods is estimating the features of a population based on data about a sample. Generalizing from a sample to a population is a very common way to learn about the features of a population, especially for populations that are very large. The population in question might be a human population, but it might be different organisms, other entities, or even events instead, such as tree frogs, nations, corporations, and election outcomes. So, statistical inference can be (and has been) used to estimate prevalence of different religions worldwide, variation in tree frog calls, and voter turnout in local versus national elections—among many other things.

The basic idea of statistical estimation is to use the observed frequency distribution for a sample as the basis for estimating the probability distribution for that variable in the general population. The measures introduced in Chapter 9 of mean and standard deviation can be adapted to represent the probability distribution for the variable in the population.

Imagine scientists have a sample of 100 university students, and they want to use that sample to estimate the range of political views among all students at that university. They might administer a questionnaire to the individuals in the sample, with each individual’s responses scored between 1 and 10, where 1 is most politically conservative and 10 is most politically liberal. Imagine the questionnaire scores are as shown in Table 10.2. This data set gives the scientists all the information they need to estimate.
---
# 248 Statistical inference

# Imagined questionnaire scores of 100 university students

|Questionnaire Score|Number of Individuals|
|---|---|
|1|0|
|2|2|
|3|5|
|4|7|
|5|10|
|6|15|
|7|22|
|8|18|
|9|13|
|10|8|

The mean degree of liberality (or, equally, conservativeness) in the full population of university students.

The sample mean is used to estimate the average value for the variable in the population; it’s an estimate of the population mean. It is called sample mean because it is based on the mean found in the sample. The sample mean might not turn out to be the mean value in the population, but it’s the most likely value and thus our best guess.

Now, recall from Chapter 9 how to calculate the mean: you sum the scores, and then divide by the total number of students. For this data set, the mean score is 6.82. (College students do tend to be a rather liberal bunch, on average.) This score is the sample mean. If the sample is representative—this idea was introduced in Chapter 3 and is discussed further later—this score is most likely to be the mean value in the population of university students.

Just like there’s a sample mean, there’s also a sample standard deviation; this is an estimate of the spread of the probability distribution for the random variable. Standard deviation, as introduced in Chapter 9, is a measure of the frequency distribution for the data set, while the sample standard deviation is instead an estimate of the probability distribution. The word sample is included, as with sample mean, to signal that this is a prediction about the population on the basis of data about the sample.

Sample standard deviation is also calculated in a slightly different way from the standard deviation formula introduced in Chapter 9. The sample standard deviation (s) is calculated as follows:

s2 = √[∑(value − mean) / (N − 1)]
---
# Statistical inference

For comparison, standard deviation (*σ) is calculated from √[∑(value − mean) / 2N. The change is the denominator: N – 1 (for the sample standard deviation, s*) instead of N. This is a way of correcting for systematic underestimation about the population mean. We won’t ask you to perform this calculation here, but for our example of estimating the political views of university students, the sample standard deviation of the data set works out to be 1.98.

The probability distribution estimated with the sample mean and sample standard deviation is the “middleman” so to speak: a statistical model enabling a prediction of the characteristics of interest in the population. A helpful rule of thumb for getting a rough probability estimate of a characteristic of interest, given its standard deviation, is the **68–95–99.7 rule**. This rule can be used to remember the percentages of probabilities within a certain range around the mean in a normal distribution. It says that about 68%, 95%, and 99.7% of the values lie, respectively, within one, two, and three standard deviations of the mean. (The other 32%, 5%, and 0.3% are equally scattered on either side of these ranges.) Look back at Figure 9.11 in Chapter 9 to see a visual depiction of this.

Applying the 68–95–99.7 rule to our example of political views of university students (taking into account sample mean and sample standard deviation) yields the following results. Any given student has a 68% probability of having a score between 4.84 and 8.80 on our conservative/liberal scale, which is calculated by subtracting/adding the sample standard deviation (1.98) from/to the sample mean (6.82). Given that 5.00 is the dividing line between liberal and conservative, a student thus has about a 68% chance of being more liberal than conservative. Any given student has a 95% probability of having a score of 2.86 to 10.00, which is calculated by subtracting/adding two standard deviations (3.96) from/to the mean (6.82). We can be much more confident that some student will fall within this range than within one standard deviation, but it is also a wider, and thus less informative, range. The only thing this tells us is that most (95%) of college students are predicted to be outside the most conservative part of the scale.

# Managing errors in estimation

A complication in using a sample mean to make predictions about the mean of a population is that the sample mean can vary from sample to sample. Were you to sample a different 100 students at the university, you could get a sample mean of 5.00 or 6.93 (for example) instead of 6.82. The distribution of the sample means you would get from repeated sampling is called the **sampling distribution of the sample mean. How much this varies from the true population mean can be estimated with the standard error**. Standard error measures sampling error. This can be calculated as:

**SE = s / √(sample size)**

As earlier, *s* is the sample standard deviation. The standard error measures the precision of the sample mean, that is, how much uncertainty there is about the estimated mean of the population. The formula shows that the standard error, and hence uncertainty about the population mean, decreases as the sample size increases. This is because a
---
# 250 Statistical inference

A large sample size helps control for chance variation. For our imagined survey of political views, the standard error is 1.98/√100, which is .198.

The standard error can be used to calculate a confidence interval. A sample mean score is a point estimate: it gives you a single value to serve as your best guess of the true population mean. If the sample is large, your point estimate will be good, but you can’t know how good. Confidence intervals provide this type of information. A confidence interval is an interval within which the value of the variable should lie for a given percentage of possible samples. For our political survey with a standard error of .198, 68% of sample means will fall within .198 of the true population mean, and 95% will fall within .396 of the true population mean. (This is for the same reason as the 68–95–99.7 rule introduced earlier.) So, for the sample mean of 6.82, the interval 6.42–7.22 will contain the true population mean 95% of the time.

Standard error and confidence intervals are ways to measure sampling error due to chance variation. (Recall from Chapter 9 that sampling error is the difference between the features of a sample and a population due to the unrepresentativeness of the sample.) Larger samples can be expected to have less sampling error than smaller samples, that is, to be more representative.

In Chapter 3, we introduced the idea of random sampling, using a chance method for selecting a sample to investigate from the population so every member of the population has an equal chance of being selected for participating in an experiment. Besides chance variation, a sample might be unrepresentative due to nonrandom sampling. Samples chosen in ways that make some individuals in a population less (or more) likely to be included than others will introduce bias in the inferences made about the population based on the sample. A poll that only solicited the political views of the students in a particular club, for example, may not be representative of the views of the full student population.

Here’s a historically significant case of nonrandom sampling resulting in serious sampling error. In 1936, a magazine, Literary Digest, sent out 10 million postcards asking Americans how they would vote in the year’s presidential election. They received almost 2.3 million back, which is a very large sample. In that sample, Alfred Landon had a decisive lead over Franklin Roosevelt: 57% to 43%; Figure 10.3 shows the headline of the story they ran about the poll’s result. The Digest did not gather information that would allow it to judge the representativeness of its sample. A young pollster, George Gallup, utilized a much smaller sample of 50,000 (which is still larger than most modern political polls). His sample was representative, and it showed Roosevelt on track to win by a landslide. That was, of course, the eventual outcome of the election. The Literary Digest closed down soon after, and Gallup’s name lives on in the well-known Gallup poll approach to measuring public opinion based on surveying a sample.

In many research contexts, random sampling and large sample sizes are very difficult to accomplish. For example, in a telephone poll of voter preference prior to an election, the phone numbers dialed can be randomly selected. But who picks up the phone, whether a person hangs up immediately or answers the questions, and even who has a phone and who doesn’t are all nonrandom influences on the people sampled, and those influences might correlate with voter preferences. And, even when sampling is truly random, smaller samples have greater sampling error.
---
# Statistical inference

# Announcement of results of 1936 Literary Digest poll

Still, as with so many decisions in science, real‐world limitations need to be factored into sampling procedures. Sometimes researchers can’t eliminate confounding variables but only limit them as much as feasible and note that confounding variables are possible. As important as representative samples are, simply pointing out that a sample isn’t truly random or is somewhat limited in size isn’t usually reason to entirely dismiss a prediction or estimation based on a sample. Careful analysis is needed of sampling procedure, potential confounding variables, and statistical properties like sample standard deviation and sampling error.

# EXERCISES

# 10.7 Recall:

Define sample mean and sample standard deviation and indicate how these differ from mean and standard deviation for descriptive statistics, considering what each measure means and how it is calculated.

# 10.8 Think:

Summarize the steps of estimating population values on the basis of a sample.

# 10.9 Apply:

There are 3,000 people at a party. (It’s a very large party!) 100 are interviewed at random, and it is discovered that 80 are philosophers, 10 are geologists, and 10 are artists.

- a. What’s the percentage of philosophers in this sample of 100 party guests?
- b. What’s the point estimate for the percentage of philosophers at the party?
- c. Suppose the standard error for this data is .08, or 8%. What’s the probability that the percentage of philosophers at the party is in the range of 72-88%? (Hint: consult the discussions above about confidence intervals.)
- d. You’re 95% sure that the percentage of philosophers at the party falls within a certain range. What range is that?
- e. Can you conclude most of the partygoers are philosophers? Why or why not?

# 10.10 Think:

Consider the following statements according to the information provided in Exercise 10.9. For each, say whether the data support the conclusion. Motivate.
---
# 252 Statistical inference

your answers with reference to the information provided and what you know about statistical estimation.

- a. It’s highly probable that the majority of party guests are philosophers.
- b. 80% of the people at the party are philosophers.
- c. It’s more likely than not that at least 8% of the guests are non-philosophers.
- d. It’s highly likely that the geologists are outnumbered at this party.
- e. It’s highly probable that most people in the world are philosophers.

# 10.11 Recall:

Describe how sample size and representativeness matter for estimation.

# 10.12 Apply:

Find an article in a newspaper, magazine, or reputable online source that draws conclusions from a poll. Alternatively, your instructor may provide one article for the whole class to use for this exercise. Answer the following questions; if you can’t find the answer, say so, providing your best guess if possible. If you selected your own article, please submit a copy or printout of it with your responses.

- a. What variable was under investigation? What were the researchers interested to know?
- b. What was the sample size? How was the sample selected?
- c. Is the sample likely to be representative? Why or why not?
- d. What data did the researchers collect about the sample?
- e. What conclusions about the population did the researchers draw from the sample?
- f. Assess the poll, the results, and the researchers’ conclusions. Are there any problems with any of these? How could the poll or the conclusions be improved?

# 10.3 STATISTICS IN HYPOTHESIS-TESTING

After reading this section, you should be able to:

- • List the steps of statistical hypothesis‐testing and describe the role of each
- • Assess whether to reject the null hypothesis from data and a probability distribution, supporting your reasoning with statistical considerations
- • Define statistical significance, p-value, type I and type II errors, and effect size and analyze these in an example

# Null hypothesis significance testing

Methods for inferential statistics are routinely used to test hypotheses. While there are lots of different methods for hypothesis‐testing that are suited to different circumstances, these methods generally involve the use of sample data to infer whether and to what extent the available evidence confirms or disconfirms competing hypotheses about the phenomenon. This is what happened when scientists at CERN rejected the possibility that the bump in their data was due simply to chance and instead posited a newly discovered particle, the Higgs boson, as the source of the data.
---
# Statistical inference

In this section, we’ll focus on one prominent approach to statistical inference for testing hypotheses, namely null hypothesis significance testing (NHST).

In this approach, two competing statistical hypotheses are formulated. One is the null hypothesis, which is a kind of default assumption; often, this just amounts to the hypothesis that nothing unusual is going on or that two variables are independent. For the scientists at CERN, this was the hypothesis that the bump in their data was just generated by background noise. The other hypothesis is the alternative hypothesis, since it is posited as an alternative to the default assumption; this is a bold conjecture under investigation. For the scientists at CERN, this alternative was the hypothesis that a new particle, the Higgs boson, was responsible for the bump in their data.

The null hypothesis leads one to expect a certain range of data and is generally, but not always, just a negation of the alternative hypothesis—the bold conjecture. When the data collected are within that range, there’s no grounds for questioning the null hypothesis. But when the data collected are sufficiently far outside the range of data expected from the null hypothesis, scientists reason that such data would be overwhelmingly unlikely if the null hypothesis were true. And so, in that case, they reason that the null hypothesis is likely to be false and should be rejected. The data instead support the alternative hypothesis—the bold conjecture.

This is basically a statistical version of the hypothetico-deductive (or H-D) method encountered in Chapter 6: expectations are derived from a hypothesis, and if observations don’t match those expectations, the hypothesis is rejected (or, at least disconfirmed). In statistical hypothesis-testing, expectations for likely values of a random variable are determined from the null hypothesis. If a value is observed that falls far enough outside the expected range, the null hypothesis can be rejected, and, in its place, the alternative hypothesis can be tentatively accepted for further scrutiny. When scientists fail to reject the null hypothesis, their test results are deemed inconclusive. Technically this does not provide evidence in favor of the null hypothesis because the alternative hypothesis hasn’t been ruled out by the data. Just like the H-D method, the value of NHST is when it identifies grounds to reject a null hypothesis.

In null hypothesis significance testing, as with estimation, inferential statistics is used to generate a probability distribution for potential outcomes based on the null hypothesis. This probability distribution represents the expectations if the null hypothesis is true. The scientists at CERN set out a protocol for statistical analysis in advance of gathering data, which enabled them to determine, for any bump in data observed, how probable that bump would be given the null hypothesis that no boson was responsible.

The probability distribution provides a statistical framework for assessing data that are collected. Data are evaluated for the degree to which they violate expectations based on the null hypothesis. For the unexpected bump in data observed at CERN, scientists determined that if the null hypothesis were true—that is, if no boson were responsible—then the probability of observing the bump in data would be extremely low: about one in three million.
---
# 254 Statistical inference

So, probabilistic expectations are developed from the null hypothesis with the use of inferential statistics, and actual observations are compared with those expectations. Then, finally, scientists draw a conclusion from that comparison. This final step is always a judgment call. Scientists have to decide how unlikely the data would have to be, given the null hypothesis, to warrant them rejecting the null hypothesis. If the observations are not too far from what is expected from the null hypothesis, then scientists have no reason to reject the null hypothesis in favor of the alternative hypothesis. If, on the other hand, the observations do violate expectations, then this provides a reason to reject the null hypothesis in favor of the alternative hypothesis. This was the exciting scenario encountered at CERN: given the observation of a bump in data that would have been exceedingly unlikely without a boson responsible for it, the scientists rejected the null hypothesis and declared they had evidence for accepting the alternative hypothesis. That is, they declared they had discovered the long-sought Higgs boson, a new kind of fundamental particle.

The steps of NHST are summarized in Table 10.3, emphasizing how these steps conform to the basic ingredients of scientific methods—hypotheses, expectations, and observations—outlined in Chapter 2.

# Developing probability distributions

How did the CERN scientists determine that the probability of the data they collected was so miniscule if the null hypothesis were true? That question is at the heart of null hypothesis significance testing. To answer it, let’s turn our attention to a classic experiment on the tasting of tea, due to Ronald Fisher, a geneticist and one of the designers of NHST.

Imagine a friend asks you, when preparing tea for her, to add milk to the cup first and only then add the tea. She claims she can discriminate by taste the order in which the milk and the tea were poured into the cup—she thinks the tea tastes better when the milk is added first. Intrigued, you decide to test this claim. According to the steps.

# Summary of steps in statistical hypothesis-testing

|Step|Procedure|
|---|---|
|Hypothesis|Formulate alternative hypothesis (the bold conjecture) and corresponding null hypothesis (the default expectation)|
|Expectations|Determine what range of outcomes and probability distribution to expect if the null hypothesis were true|
|Observations|By experiment or observational study, determine one or more actual outcomes|
|Conclusion|Evaluate whether the actual outcome is unlikely enough given expectations from the null hypothesis to provide grounds for rejecting the null hypothesis|

---
# Statistical inference

of NHST, summarized in Table 10.3, you should start by formulating the null and alternative hypotheses. In this circumstance, what would you choose for each of these? The bold and speculative conjecture is that your friend really can discern by taste the order in which milk and tea were poured into a cup. This would be surprising! The null hypothesis is simply that your friend cannot do this. This is, probably, your default assumption.

You prepare a cup of tea out of view, tossing a fair coin to determine whether you pour tea or milk first. (This randomizes the order, which is a way to control for extraneous variables; recall our discussion of randomization.) Then, your friend has a sip. She says that you added the tea first, and she’s right. But this isn’t terribly impressive; there was a .5 probability of her guessing correctly by accident, since either the tea was poured first in the cup or else the milk was. To see whether there is support for the alternative hypothesis, whether the evidence really supports your friend’s claim, you need to have your friend make repeated guesses that are, on average, much more accurate than chance would allow.

You prepare eight new cups of tea at once, tossing a coin to determine milk-first or tea-first for each. You put the cups of tea in front of your friend and ask her to say of each whether the milk or the tea was added first. What does the null hypothesis lead us to expect? We can develop a probability distribution to let us know what to expect if your friend is just guessing at random. As with estimation, the probability distribution can be characterized by a mean and standard deviation.

If your friend is merely guessing, she is most likely to be right about four of the eight cups. This is the mean expected outcome, which you can calculate by multiplying the probability of success on each trial, which we said was .5, by the number of trials: mean = Pr(O=success) × # trials = .5 × 8 = 4.

In this context, the mean is the most likely outcome. If your friend were to make repeated guesses about the eight cups, and the null hypothesis were true, most of the time she’d be right about four cups. Since your friend is only making guesses about one series of eight cups, the mean indicates the most likely outcome. But this outcome is not guaranteed, even if the null hypothesis is true. By sheer luck, your friend might guess correctly more often or less, just as you might happen to get more or fewer heads than 50% in a series of coin tosses.

The standard deviation for the probability distribution can be calculated using this formula:

σ = √[mean × (1 − Pr(O=success))]

Notice that this is very different from the other standard deviation formulas we have encountered. Here, 1 is the total probability, and Pr(O=success) is the probability of success (in the tea experiment, guessing correctly) in a single trial. Multiplying that by the mean number of successes yields the variance; the square root of that number is, then, the standard deviation. For the tea experiment, the standard deviation is √[4 × (1 − .5)] = √2 = 1.414.

Figure 10.4 shows the probability distribution of the number of guesses your friend will get correct if she is randomly guessing, that is, if the null hypothesis is true. This
---
# 256 Statistical inference

 

  

# Probability distribution of the number of guesses your friend will get correct if she is randomly guessing

The probability distribution can be estimated from the range, mean, and standard deviation that we have calculated.

The probability distribution can be used to establish the significance level required for rejecting the null hypothesis. This is a decision about how improbable, given the null hypothesis, an experimental result must be to warrant rejecting the null hypothesis. Later we’ll discuss some further considerations for this choice. For now, we’ll adopt .05 as the significance level, which is the most common choice.

# Assessing statistical significance

With all of this preparatory statistical work completed, you are now ready to test your friend’s tea‐tasting skills. This is the third step NHST: collecting the data. You ask your friend to judge “tea‐first” or “milk‐first” for all eight cups of tea. She correctly judges all eight cups! Given this data, would you be tempted to conclude that you were wrong and your friend was right, that maybe she can perceptually discern something about tea and milk order?

There are two possibilities consistent with the data: (1) the null hypothesis is true, and our experimental result was an unlikely event of eight correct guesses purely by chance, or (2) the null hypothesis is false, and the alternative hypothesis that your friend can discriminate between milk‐first and tea‐first cups of tea is true. The goal of statistical hypothesis‐testing is to do our best to decide whether (1) should be rejected in favor of (2). The probability distribution we’ve prepared can tell us exactly how unlikely our experimental result would be if (1) is the case, which should guide our decision of whether to reject (1).

From the outcome of the experiment, when your friend correctly judged all eight cups of tea as tea‐first or milk first, we can calculate a p-value. This is the probability of the observed data (or even more extreme outcomes) assuming the null hypothesis is true. The smaller the p‐value, the more unlikely your observed data is if the null hypothesis is true. Notice that the p-value doesn’t give us the probability that the null hypothesis is true.
---
# Statistical inference

hypothesis is true or the probability that the alternative is true. It is just a yardstick we can use to answer the question: how likely is it to get data like you have observed if the bold conjecture you are interested in is not true?

We can visually estimate the *p-value for the tea-tasting experiment from Figure 10.4: it’s clear there is only a very small chance of guessing all eight cups correctly via random guessing. We can find the precise p*-value with the multiplication rule; it’s just the probability of the first guess being correct by chance multiplied by the probability of the second guess being correct by chance, and so on, for all eight guesses: 0.5 × 0.5 × 0.5 × 0.5 × 0.5 × 0.5 × 0.5 × 0.5, or 0.58, which is .0039. The probability of your friend guessing correctly on all eight cups by random guesswork is only .0039, or 0.39%. Put another way, if your friend tasted many series of eight cups of tea, she could get this outcome by guessing randomly only about one out of 256 series of eight cups. If she guessed all eight correctly by sheer luck, on her first try, she’s really lucky!

Whether one should reject the null hypothesis is determined by comparing the *p-value and the significance level. If the *p*-value is less than or equal to the significance level that had been selected, the researchers can reject the null hypothesis with reasonable confidence. When the p-value is greater than the significance level, we can’t rule out the null hypothesis. The p*-value of .0039 in our tea-tasting experiment is lower than our chosen significance level of .05, and so the outcome of this experiment is statistically significant. That means the outcome is unlikely enough if the null hypothesis is true that it provides grounds for rejecting the null hypothesis.

Most p-values can’t be calculated so simply from probabilities as the one in our tea-tasting example. Another approach to evaluating statistical significance uses the mean, standard deviation, and 68–95–99.7 rule introduced in the previous section. By the 68–95–99.6 rule, outcomes that are two standard deviations away from the mean are the threshold for statistical significance at the significance level of .05. Two standard deviations in this case is 2.828 (1.414 × 2), so outcomes outside the range of 4 (the mean) ± 2.828 are statistically significant. That range is 1.17 to 6.828. So, guessing eight cups correctly is statistically significant at the .05 level.

Notice that statistically significant results aren’t necessarily important results. Here significance is a technical term that only means grounds for rejecting the null hypothesis. Many statistically significant results from NHST are theoretically uninteresting and practically irrelevant. Like the tea-tasting experiment, you could test whether people can reliably distinguish humans from dogs when passing them on the street. If your observations are statistically significant, thereby allowing you to reject the null hypothesis that people cannot distinguish between dogs and humans, you wouldn’t be surprised. So, we should be wary of statistically significant findings that are nonetheless not worth our attention.

Another important feature of data that might be confused with statistical significance is effect size, which is a quantitative measure of the strength of a phenomenon, that is, of the magnitude of difference some variable makes. Statistical significance does not mean the effect size is large; the latter is a separate question. So, just as statistical significance doesn’t guarantee an important finding, it also doesn’t guarantee a strong influence. If you surveyed enough of the incoming students at a university, you might
---
# 258 Statistical inference

be able to conclude that their political views were more liberal or conservative, on average, than those of existing students—even if the difference were miniscule. Sometimes scientists represent the effect size along with the statistical significance of their findings, and this additional information can help put the finding into perspective.

 

  

# Drawing conclusions

Comparing the p-value of the experimental outcome to the significance level provides a simple, objective criterion for deciding whether to reject the null hypothesis on the basis of observations. But there is a role for choice in what level of statistical significance to require. One can always ask whether this outcome is unlikely enough to reject the null hypothesis. This is a version of the more general decision we’ve seen elsewhere in this book regarding when there’s sufficient evidence to believe a hypothesis.

In many fields, it’s common to use a significance level of .05 as the dividing line. Observed results with a probability of less than .05 given the null hypothesis are said to be statistically significant at the .05 level. One can abbreviate this: p < .05. This is true of the outcome of our tea-tasting experiment, which is why we rejected the null hypothesis. Notice, though, that we could still be wrong: it’s possible that our friend really was just extraordinarily lucky. But if we instead decided to play it safe and not reject the null hypothesis, we could be wrong about that as well. We might have then failed to detect our friend’s tea-tasting superpower. By its very nature, statistical hypothesis-testing gives no guarantees.

The choice of significance level indicates the degree to which you’re willing to accept the risk of erroneously rejecting the null hypothesis when it is true versus the risk of erroneously failing to reject the null hypothesis when it is false. These are the two different ways you could be wrong, and one or the other is always a risk. The risk of erroneously rejecting the null hypothesis when it is true is called a type I error, or false positive. The risk of erroneously failing to reject the null hypothesis when it is false is called a type II error, or false negative.

Scientists sometimes adjust the conventional .05 line for statistical significance considering whether type I or type II errors are riskier. Requiring a lower significance level means that you need stronger evidence to reject the null hypothesis; this decreases the chance of a type I error but increases the chance of a type II error. Requiring a higher significance level means that you need less evidence to reject the null hypothesis; this decreases the chance of a type II error but increases the chance of a type I error.

Imagine a new drug is being tested. If the drug is for a life-threatening illness with no treatment options otherwise—say, pancreatic cancer or Ebola—and experiments regarding the efficacy of the drug find it works better than a placebo with a p-value of .055, just missing the line for statistical significance at .05, researchers may still be inclined to bring the drug to market or at least continue testing. This result suggests the drug is very likely better than nothing! They want to avoid the type II, or false negative, error of accidentally rejecting a treatment that might be valuable. In contrast, if scientists are thinking about announcing a new particle, and they know their colleagues
---
# Statistical inference

will scrutinize their findings, they may be especially careful about avoiding a type I or false positive error, and so will lower the significance level. The Higgs boson discovery was only announced after the probability of the experimental data was found to be just one in three million assuming the null hypothesis of no boson present. This significance level is so close to zero, it’s difficult to even display numerically.

A related issue is that statistical tests vary in their power to detect an effect. The power of a statistical test is the probability that the test will enable the rejection of a null hypothesis. More powerful tests increase the chance of rejecting the null hypothesis, thus decreasing the chance of a type II or false negative error, where we fail to reject the null hypothesis when it is actually false. Power increases with sample size. In the tea-tasting experiment, we weren’t able to reject the null hypothesis after one cup was guessed correctly, but we were able to after eight cups were guessed correctly. Increasing sample size to increase the power of a statistical test can be a good thing, but it also has a downside: this increases the chance of making a type I or false positive error. Studying a very large sample makes it relatively easy to uncover statistically significant findings, but this also makes it relatively easy to erroneously reject the null hypothesis—that is, to uncover findings that turn out to be false.

Statistical tests that increase power by using very large samples also enable findings that have very small effect sizes. For example, a certain gene has been linked with the chance of someone smoking cigarettes: if you have this gene, you are more likely to smoke cigarettes. Can researchers tell from your genes whether you have smoked, or will smoke? As the researchers acknowledged, absolutely not: there was only a very weak relationship. Finding factors with very small effect sizes has advantages and drawbacks. It can be useful to detect subtle statistical relationships, but weak statistical relationships are often uninteresting or unimportant. Further, it’s not uncommon for people to take too seriously a statistical relationship with a very small effect size, especially if the finding fits with our expectations.

# Box 10.1 Types of statistical hypothesis-testing

We have characterized null hypothesis significance testing as if it were a single technique, but there are actually multiple forms of statistical hypothesis-testing, with different names and different uses. Which type of test should be used depends on the kind of hypothesis under investigation, the type of data available, and other circumstances. The sort of statistical hypothesis-testing we’ve encountered in this section are t tests, where data about some group are used to test whether the group deviates systematically from what’s typical. But t tests come in multiple varieties, depending on how many samples of data researchers collect and whether the alternative hypothesis predicts how the sample will deviate from the population mean. So, you might hear of one-sample or two-sample t tests, or one- or two-tailed t tests, for example. Another approach is analysis of variance,
---
# 260 Statistical inference

or ANOVA, which is used when there are more than two groups to compare. ANOVA also comes in multiple versions for different circumstances of statistical analysis. Pearson’s r, in turn, is used to test whether a correlation in a sample provides a basis for concluding the variables in question are correlated in the population (the alternative hypothesis). All of these approaches to NHST share the same basic structure, but they differ mathematically and in how the results should be interpreted. There are also statistical techniques for when we can’t assume a variable has a normal distribution. Calculations of any of these types of statistical tests are typically now carried out using software—so the hard part isn’t the math but understanding and interpreting its significance.

# EXERCISES

# 10.13 Recall:

In your own words, define statistical significance, p-value, and effect size. Then, give an example of a result that is statistically significant but not important.

# 10.14 Apply:

Consider the tea-tasting experiment again. Suppose that your friend correctly guessed six cups of tea instead of all eight. Decide whether this result is statistically significant at the .05 level by using the mean and standard deviation calculated previously and applying the 68–95–99.7 rule. Then, say whether this outcome is a basis for rejecting the null hypothesis.

# 10.15 Apply:

It’s estimated that 10% of the general population is left-handed. Imagine testing whether your group of friends contains an unusually large number of left-handed people. Let’s say you have 75 friends, and 14 of them are lefties.

- a. Write out the null hypothesis and alternative hypothesis.
- b. Calculate the mean and standard deviation for how many of your group of friends would be expected to be lefties if the null hypothesis were true.
- c. From the information you calculated in (b), evaluate whether the data are significant at the .05 level.
- d. Decide whether to reject the null hypothesis, and justify your decision with statistical considerations.
- e. Is your decision at risk of a type I or type II error? Why?

# 10.16 Apply:

Each of the following is a bold conjecture that can serve as an alternative hypothesis. For each, (i) formulate the null hypothesis, (ii) describe what a type I error would be and what a type II error would be, and (iii) say which kind of error would be more serious, and why.

- a. Adding water to toothpaste helps protect against cavities.
- b. This man is guilty of murder.
- c. The use of social media makes users depressed.
- d. The new drug is more effective than the old drug.
- e. The new drug is more dangerous than the old drug.
- f. Reading books promotes happiness.
---
# Statistical inference

# 10.17 Think:

Classify each of the following statistical techniques as belonging to descriptive statistics, statistical estimation, or statistical hypothesis-testing. Give your rationale for each answer.

- a. displaying a data set in a chart
- b. surveying a group about their pizza preferences to decide if they have an unusual preference for anchovies
- c. surveying a group about their pizza preferences in order to place an order
- d. calculating the sample mean and sample standard deviation
- e. surveying a group about their pizza preferences in order to guess what all Canadians’ pizza preferences are
- f. finding the mean level of preference for anchovies on pizza among a group and the standard deviation in that level of preference
- g. rejecting a null hypothesis on the basis of data
- h. finding the correlation coefficient of a data set

# 10.18 Think:

Scientific journals tend to publish statistically significant results much more often than they publish findings of statistical insignificance. Why do you think this might be? Considering the earlier discussion about power, type I and II errors, and effect size, can you think of any concerns with this practice?

# 10.4 DIFFERENT APPROACHES TO STATISTICAL INFERENCE

After reading this section, you should be able to:

- Characterize three limitations of classical statistics and how Bayesian statistics solves each of them
- Describe how Bayesian statistics can be used (1) to establish the probability a hypothesis is true given an observation and (2) to compare how much an observation favors different hypotheses
- Describe two problems with Bayesian statistics

# Problems with classical statistics

Null hypothesis significance testing, the approach to statistical hypothesis-testing described so far, is part of classical statistics, also called frequentist statistics. This approach is called “classical” because it is more or less standard—at least presently. But it’s not the only game in town, and someday it may no longer be the standard way of doing statistics.

In this section, we’ll describe three limitations of classical statistics. To set up the discussion, think back to the last step of the procedure of NHST. What results from this application of inferential statistics is a p-value: that is, the probability of the observation occurring given that the null hypothesis is true, which is then compared with a pre-established significance level to decide if the data are statistically significant. There are three oddities about this.

The first oddity is that scientists’ primary interest in statistical hypothesis-testing is to figure out which hypotheses are true. But a p-value doesn’t indicate how probable...
---
# 262 Statistical inference

The hypothesis itself is, that is, how likely the hypothesis is to be true. It only indicates how probable observed data are if the null hypothesis is true. If the p-value is small enough, we can decide that the observations we in fact made are so unlikely given the truth of the null hypothesis that we should reject the null hypothesis. But we still don’t know anything about the chance the null hypothesis is true.

A second limitation is that NHST doesn’t allow us to take into account any prior information we might have in favor or against the truth of the null hypothesis. For example, in our tea-tasting example, it may be the right decision not to reject the null hypothesis even though your friend guesses correctly so often. What we know about how tasting works and about what properties a cup of tea can and can’t have suggest this tasting feat should be impossible. Maybe your friend was just extraordinarily lucky, or maybe she had a way of cheating. In contrast, someone discerning two different types of wine in a blind taste test wouldn’t really be that surprising. The same success rate may thus lead us to want to reject the null hypothesis of random guessing for wine tasting but not reject the null hypothesis of random guessing for tea tasting. As this illustrates, we often find different hypotheses more or less credible, and it seems this should influence our threshold for how much evidence we require to believe them. NHST does not allow us to take such prior information into account.

A third limitation of classical statistical techniques like NHST is that the statistical test doesn’t directly relate to the alternative hypothesis at all. Again, all we are learning is the probability of the data we observed if the null hypothesis is true. And yet, the alternative hypothesis, the bold and speculative conjecture, is what scientists are truly interested in evaluating. How likely is the alternative hypothesis to be true? This is the million-dollar question in hypothesis-testing, but NHST gives us no way to answer it.

# Bayesian statistics

The Bayesian approach to statistics solves all three of these problems with classical statistics. The Bayesian approach to statistical hypothesis-testing aims to determine when data count as evidence for one hypothesis and against a competing hypothesis and how data should change our degree of belief that each of these competing hypotheses is true. Bayesian statistics is based on Bayes’s theorem and the subjectivist interpretation of probability, both introduced in Chapter 8. For Bayesians, an observation counts as evidence for a hypothesis when it raises our rational degree of belief in the hypothesis.

The simplest formulation of Bayes’s theorem applied to a hypothesis and observation is:

Pr( H | O ) = Pr( O | H ) Pr( H ) / Pr( O )

This formula states that the probability of a hypothesis H given an observation O — which is what we want to find out — is the probability of the observation given the hypothesis multiplied by the prior probability of the hypothesis, then divided by the probability of the observation.
---
# Statistical inference

Pr( H ) is the prior probability of the hypothesis, while Pr( H | O ) is the posterior probability of the hypothesis. The prior probability is our rational degree of belief before (prior to) making the observation, while the posterior probability is our rational degree of belief after (posterior to) making the observation. Considering the prior probability of a hypothesis is a way of holding implausible hypotheses to a higher standard of evidence than plausible hypotheses. So, we’d look for more evidence before agreeing that someone can tell milk-first or tea-first in a cup of tea than we would before agreeing that someone can tell the difference between different kinds of wine.

This formula takes three things as input: the prior probability of the hypothesis, Pr( H ); the probability of the observation if the hypothesis is true, Pr( O|H); and the probability of the observation under all possible hypotheses, Pr( O ). If all three of these probabilities are known—a major source of controversy for Bayesian statistics—we can use them to calculate the probability the hypothesis is true given the observation that has been made (or the data that have been gathered). And this is the main thing scientists want to discover from statistical hypothesis-testing.

Additionally, comparing prior and posterior probabilities shows us whether an observation confirms or disconfirms a hypothesis and by how much. If Pr( H | O) > Pr( H ), then the observation O confirms hypothesis H. In other words, an observation confirms a hypothesis if the probability of the hypothesis—the rational degree of belief that the hypothesis is true—goes up once the observation has been made. A big increase in probability implies a large degree of confirmation, and a small increase implies a small degree of confirmation, while a big decrease in probability implies a large degree of disconfirmation, and a small decrease implies a small degree of disconfirmation.

Bayes’s theorem also can be used to calculate the degree to which some observation or data set favors one hypothesis over another. Posterior probabilities can be calculated for any number of hypotheses from the same observation, considering the prior probabilities of the various hypotheses and the probability of the observation given each of the various hypotheses. These posterior probabilities can then be compared with one another to decide which hypothesis is more likely given the observation that’s been made. Unlike classical statistics, this provides a comparative approach to hypothesis-testing.

There’s also a shortcut to comparing how much an observation favors different hypotheses. It’s possible to compare the likelihood of the observation given each hypothesis, or Pr( O | H ) versus Pr( O | H1), instead of posterior probabilities. These likelihoods are usually easier to find than posterior probabilities. An observation favors one hypothesis over another to the degree that the first hypothesis predicts the observation better than the other hypothesis does. This can be expressed numerically with the Bayes factor, which is the ratio of the probability of the observation given one hypothesis to the probability of the observation given another hypothesis, that is, Pr( O | H )/Pr( O | H1).

Imagine that Lasha and Janine are interested in public opinion about the theory of evolution. Lasha believes that 70% of the public is convinced by the theory of evolution, while Janine believes that 60% of the public is convinced. They decide to
---
# 264 Statistical inference

Poll 100 randomly selected people about their views on evolution to decide which of these is correct. Lasha’s and Janine’s different hypotheses lead them to have different expectations: Lasha predicts that about 70/100 will believe in the theory of evolution; Janine predicts it’s about 60/100. (We can use tools of inferential statistics from earlier in this chapter to find the probability distribution each predicts for this random sample of 100 people.)

As it turns out, of the 100 people surveyed, 62 said they are convinced by the theory. According to the probability distribution based on Lasha’s hypothesis of 70% belief in evolution, this observation has a probability of .02, that is, Pr(O | H1) = .02. According to the probability distribution based on Janine’s hypothesis of 60% belief in evolution, this observation has a probability of .08, that is, Pr(O | H2) = .08. The Bayes factor is .08/.02, or 4. The survey result favors Janine’s hypothesis over Lasha’s by a factor of 4.

# Problems with Bayesian statistics

We’ve seen a few of the benefits of Bayesian statistics over classical statistics, but Bayesian statistics faces its own problems. First, Bayesian statistics is often criticized for a lack of objectivity. There’s often not enough information to have objective grounds for the prior probability—the probability of the hypothesis before data are gathered—but this prior probability is needed to use Bayes’s theorem.

In some cases, we can calculate prior probabilities from established facts. For example, the probability that a 42‐year‐old woman has breast cancer can be estimated from the incidence of breast cancer in the general population. But such data is unavailable for many hypotheses. Recalling our earlier example, what prior probability should the scientists at CERN have assigned to the hypothesis that they’d detect a Higgs boson? It doesn’t seem there’s an objective way to assign a probability to this possibility before they ran their experiments. Without objective information to guide the selection of prior probabilities, individual biases and subjective values can find their way in. This is a problem because prior probabilities influence posterior probabilities in Bayesian statistics, and so biases and subjective values could then influence the conclusions drawn from experimental data. This possibility seems to undermine the objectivity of Bayesian reasoning and is perhaps the main challenge facing Bayesian statistics.

Some have responded to this challenge by suggesting rules for how prior probabilities should be established. Another response has been to suggest that exposing and taking into account people’s different background beliefs is actually a good thing. Different choices of prior probabilities make it transparent how two scientists’ judgments differ, so those differences can be justified by the scientists and assessed by others. In this respect, Bayesian statistics and classical statistics are similar. In NHST, researchers must decide on significance levels, sample size, and so forth, and these decisions are also judgment calls open to criticism. Nonetheless, the choice of Bayesian prior probabilities is a direct influence of background beliefs on degree of belief in hypotheses under investigation that many scientists are uncomfortable with.

A second problem for Bayesian statistics is that it’s not obvious that posterior probabilities are always the best basis for updating one’s beliefs. Some have suggested that...
---
# Statistical inference

Abductive reasoning, discussed in Chapter 7, can be a better alternative. Recall that when people engage in abductive reasoning, they use explanatory considerations as evidence to support one hypothesis over others. You see cheese crumbs, small droppings, and some chewed up paper, and so you might reason that a mouse resides in your kitchen. It’s not clear that these kinds of inferences follow Bayesian statistical analysis. The reasoning of paleontologists, for example, can be akin to “CSI”-style forensic work, what we called methodological omnivory in Chapter 4. They gather different kinds of evidence to assess the plausibility of hypotheses about the deep past. Statistics—Bayesian or classical—may not be involved at all.

# EXERCISES

1. Recall:
1. Describe three limitations for classical statistics, especially as it’s used in NHST.
2. For each of the three limitations for classical statistics you described, indicate how Bayesian statistics avoids it.
2. Recall: Write out Bayes’s theorem; label prior probability, posterior probability, and likelihood; and describe what Bayes’s theorem says when applied to a hypothesis and observation. Then, describe
1. how Bayes’s theorem can be used to calculate the probability of a hypothesis given certain evidence, and
2. how a Bayes factor can be used to compare support for two competing hypotheses.
3. Apply: Suppose that your smartphone is being tested for a bug that affects about one device in a thousand. The bug could transfer all data on your phone to all your contacts. Your device has no apparent problem, and the test is accurate 90% of the time. This number means that if your smartphone actually has the bug, then the test result is positive with 90% probability, and if your smartphone does not actually have it, the test result is negative with 90% probability. After several anxious minutes, the test results come back: positive! Do you have good reason to be worried all your data will be exposed?
1. Define the prior probability of the hypotheses that your device has the bug and that your device doesn’t have the bug, the probability of the test result given the hypothesis that your device has the bug, and the probability of the test result given the hypothesis that your device doesn’t have the bug.
2. Explain how these probabilities can be used in Bayes’s theorem to determine whether you should be worried.
3. Think again about this situation, considering that, out of 1,000 devices, 100 will test positive for the bug. Would this consideration change any step in your reasoning?
4. Apply: You take an at-home covid test; it is negative. The false positive rate is less than 1%, while the false negative rate is about 20%.
1. Write out the Bayes factor expression for this observation (negative test result) and the hypotheses that you do not have covid (H1) and that you do have covid (H2), then calculate the Bayes factor.
2. What can you conclude from this Bayes factor? Can you conclude you do not have covid?
---
# 266 Statistical inference

# 10.23 Think:

Describe two problems for Bayesian statistics. For each, analyze how problematic you think the problem is, giving reasons for your opinion.

# FURTHER READINGS

 

  

For a historically informed treatment of different approaches to statistical inference and their relationships, see Gigerenzer, G. (1993). The superego, the ego, and the id in statistical reasoning. In G. Keren & C. Lewis (Eds.), A handbook for data analysis in the behavioral sciences: Methodological issues (pp. 313–339). Erlbaum.

For a recent defense of the use of p-values and frequentism in statistical hypothesis-testing, see Mayo, D. G., & Cox, D. R. (2006). Frequentist statistics as a theory of inductive inference. In J. Rojo (Ed.), Optimality: The second Erich L. Lehmann symposium (pp. 77–97). Institute of Mathematical Statistics. And Mayo, D. G., & Hand, D. (2022). Statistical significance and its critics: Practicing damaging science, or damaging scientific practice? Synthese, 200(3), 220.

For short, critical surveys of problems with null hypothesis significance testing, see McCloskey, D., & Ziliak, S. (1996). The standard error of regressions. Journal of Economic Literature, 34, 97–114; and especially, Gigerenzer, G. (2004). Mindless statistics. The Journal of Socio-Economics, 33(5), 587–606.

For more on Bayesianism, see Howson, C., & Urbach, P. (2006). Scientific reasoning: The Bayesian approach (3rd ed.). Open Court.

For a compact comparison between frequentist and Bayesian approaches to statistical inference, see Sprenger, J. (2016). Bayesianism vs. frequentism in statistical inference. In The Oxford handbook of probability and philosophy (pp. 382–405). Oxford University Press.
---
# CHAPTER 11

# Causal reasoning

 

  

# 11.1 POVERTY AND THE CHARACTERISTICS OF CAUSAL REASONING

After reading this section, you should be able to:

- Describe the phenomenon of poverty and what the Niger experiment revealed about it
- List three characteristics of causal reasoning
- Give examples of how causal knowledge is of theoretical and practical importance

How can science help reduce poverty?

According to the United Nations’ Sustainable Development Goals Report in 2022, more than 650 million people worldwide live in extreme poverty, surviving on less than $1.90 per day. This number may get higher in the coming years, especially if economic and social inequalities, war, and the environmental consequences of climate change worsen.

Poverty doesn’t occur only in some remote regions of our planet. Poor people live in all countries and likely live in your neighborhood too. This is because poverty is not just about money. It is a complex phenomenon. Some of the salient aspects of poverty concern one’s economic resources like assets and income, but other aspects are medical, psychological, and social, like malnutrition, psychiatric conditions, and lack of opportunity.

When people experience poverty, basic human needs go unsatisfied. The poor can suffer from hunger, malnutrition, ill health, deficient education, and insufficient access to technologies, infrastructure, social networks, and cultural opportunities. For individuals, poverty can cause or worsen social isolation, shame, anxiety, and depression. For communities and nations, poverty affects migration trends, public health, and political stability. These consequences partly depend on social norms preventing certain households, such as immigrant households, or individuals, such as women, from seizing new economic opportunities or benefitting from the support of a social network. Given all these complexities, how can scientists help to reduce poverty and prevent or mitigate its negative effects?

DOI: 10.4324/9781003300007-12
---
# 268 Causal reasoning

One promising idea comes from Niger. Niger is one of the world’s poorest countries. In 2022, approximately half of its 25 million residents live in extreme poverty; in 2005, that number was 80%. In 2012, the government of Niger began giving small amounts of money to its poorest citizens. These small cash transfers had an obvious effect: they significantly improved the livelihoods of many of the poorest people. You may worry that people would use free cash in foolish ways. But several meta‐analyses from developmental economics have shown otherwise. Rather than buying what are called “temptation goods,” poor people typically use money received through a cash‐transfer or microcredit program to improve their condition and the condition of their families.

Though cash transfers are helpful, they do not address the lack of opportunities associated with poverty. Researchers collaborated with Niger’s government to determine whether the effects of its cash‐transfer program would improve by adding other components. The researchers conducted a randomized controlled trial, randomly assigning 322 villages in Niger to a control group or one of three experimental groups. Households across all villages in the control and experimental groups received monthly cash transfers. Households in all three experimental groups also received training in business and administration. And then, the three different experimental groups provided (1) an extra cash grant, (2) life‐skill training by social workers and a community film promoting communication, boosting aspirations, and noting women’s lack of opportunities compared to men in the same village, or (3) the extra cash as well as life‐skill training and the community film.

The researchers measured several variables related to the well‐being of the participants in this experiment, especially variables related to women’s empowerment, before.

# Share of population living in extreme poverty in African nations, 2019; Niger

FIGURE 11.1 is circled
---
# Causal reasoning

starting the experiment and at 6 and 18 months afterwards. They also calculated the cost‐effectiveness of each intervention by comparing the monetary costs with the impact in each of the experimental conditions.

It turned out that the households in all conditions increased their consumption of food and domestic products. Households that also received psychosocial support showed improved levels of mental health, more positive expectations about the future, and increased social support, which in turn had further positive impacts on their economic situations over time. The researchers also discovered that integrating economic and psychosocial support to alleviate poverty had more lasting effects and low additional cost compared to simple cash transfers. This finding highlights that there is much more to poverty than a mere lack of money and that programs that target both monetary and psychosocial factors might be especially cost‐effective.

Experiments like this can provide economists and policymakers with evidence about the causes and effects of poverty, as well as evidence about the relative efficacy of different interventions to reduce poverty. Economic concepts like poverty can seem abstract, but causal knowledge in economics plays key roles in the formulation of social policies and design of institutions. Such policies and institutions have many impacts on people’s daily lives.

# Three characteristics of causal reasoning

Causal knowledge is useful for goals such as alleviating poverty, mitigating global warming, preventing epidemics, and much more. But it can be tricky to uncover causal knowledge. Scientists have devised a number of methods to make reliable causal inferences in different experimental circumstances and for different theoretical and practical purposes. This chapter examines some of these methods for acquiring causal knowledge.

Chapter 3’s discussion of experimentation, Chapter 5’s discussion of modeling, and Chapter 10’s discussion of statistical hypothesis‐testing are all relevant to using experiments and models to test causal hypotheses, and we will draw from those discussions in this chapter.

The Niger experiment investigating the causes and effects of poverty illustrate three general characteristics of causal reasoning that apply both in science and to everyday life. First, causal relationships can be uncovered from information about the timing, location, and frequency of events. If you get sleepy after lunch, perhaps eating lunch is a cause of your drowsiness. In the Niger example, researchers measured variables related to poverty before and after interventions to establish whether outcomes associated with reduced poverty were more frequent after some interventions than others.

Second, testing causal hypotheses often involves doing something in the world, such as performing an intervention. Intervening on a suspected cause while keeping other variables the same or ensuring they vary at random can provide more insight into causal relationships than just observing a correlation in two variables. In the Niger experiment, scientists tested the roles of different interventions using multiple experimental groups receiving different interventions. Because long‐term economic prospects increased more, on average, in households receiving both monetary and psychosocial.
---
# Causal reasoning

support, this suggests that poverty is not just about money and that policies should concentrate also on psychological and social factors.

Third, causal reasoning has great theoretical and practical significance. Causal information is an important variety of scientific knowledge and can be used to explain features of our world, as we shall see in Chapter 12. Besides theoretical knowledge, information about causes is also how we can make things happen—and prevent things from happening—in the world. Causal knowledge is not only crucial for effectively reducing poverty but also for treating medical conditions, improving environmental outcomes, and much more.

# EXERCISES

# 11.1 Recall:

Poverty is not merely a monetary deficit but a complex phenomenon. What are some of the causes of poverty? What are some of the negative effects that people deal with as a result of being poor?

# 11.2 Recall:

The Niger experiment examined the effects on poverty of four experimental conditions. What were the four experimental conditions? What was the null hypothesis? What did the researchers find?

# 11.3 Think:

Refresh your memory of external experimental validity, introduced in Chapter 3. Then, assess the external experimental validity of the Niger experiment described in this section. How confident can researchers be that these findings are accurate for residents of Niger? Should they be just as confident that the experimental results hold for poor households in other nations? Why or why not?

# 11.4 Recall:

List the three characteristics of causal reasoning introduced in this section. Why is intervention useful for testing causal hypotheses? Why is causal knowledge more important than knowledge of correlations?

# 11.5 Apply:

Provide your own example of (a) causal knowledge with theoretical importance and (b) causal knowledge with practical importance, and explain the importance of each.

# 11.6 Apply:

Suppose you’re a lead scientist following up on the Niger experiment to see if you can similarly reduce poverty in your local community. However, you yourself have very limited financial resources with which to conduct your study; for instance, you have no money for cash payouts. What interventions could you make in your follow-up study?

# 11.2 THE NATURE OF CAUSATION

After reading this section, you should be able to:

- Indicate how spatiotemporal contiguity and correlation each can be clues to causation but fall short of ensuring causation
---
# Causal reasoning

# Define the physical-process and difference-making accounts of causation

# Assess the strength of a causal relationship and indicate how causal background is relevant

Imagine that you are playing a game of billiards at your local pool hall. You hit the cue ball, which then rolls across the felt and strikes the 8‐ball, which is itself then set in motion. Did the cue ball cause the 8‐ball to move? The answer seems obvious. What else could have possibly made the 8‐ball move?

In the 18th century, philosopher David Hume asked what our experience allows us to say about the nature of causation. He suggested there’s no reason to say that causation is anything beyond regular associations between events. Hume’s argument goes as follows. If you were to observe the cue ball hit the 8‐ball, what you would have observed is just a series of events, one after another. You saw the cue ball moving towards the 8‐ball, the cue ball touching the 8‐ball, and then the 8‐ball itself moving. There is no additional experience of causes and effects in all of that. We should then conclude that there is no ingredient to causation beyond just the series of observable events that are regularly associated. (You may recall from Chapter 7 that Hume was also skeptical about inductive reasoning.)

Hume’s skepticism has motivated accounts of causation that go beyond mere regular association. Causal knowledge is important to science, but it’s tricky to say what, exactly, causation amounts to. This skepticism can also motivate us to clarify the specifics of reliable causal reasoning. What is it, exactly, that you would look for to decide, for example, whether poverty causes social isolation, or whether routinely eating processed meats causes cancer?

Let’s start by considering how spatiotemporal contiguity and correlation—together, Hume’s regular associations between events—relate to causation. The perception of causal relationships was systematically investigated by psychologist Albert Michotte in the 1940s. Michotte’s experiments showed that causal perception depends on spatial and temporal information. If two events—for example, pressing a piano key and hearing B‐sharp—are spatially and temporally contiguous, that is, if they happen at the same time and place, then we perceive them as causally related. This is so even if we only experience these occurring together once. When there is a spatial or a temporal gap between two events, we are much less likely to perceive the one event as causing the other. Spatiotemporal contiguity can be a powerful indicator of a causal relationship.

On the other hand, spatiotemporal contiguity can also be misleading. Not all events that occur together are causally related, of course: some events occur together once or even several times by pure coincidence. So, spatiotemporal contiguity doesn’t guarantee causation. Spatiotemporal contiguity is not necessary for causation, either. An effect can occur far away both in space and time from its cause. For instance, poverty in childhood can have effects much later in life, and poverty rates are influenced by geopolitical events that occur far away in time and space.
---
# 272 Causal reasoning

Indeed, many of the causal relationships investigated in science and important for everyday life are spatiotemporally separate to some degree. Sometimes the degree of separation is used to distinguish among an event’s causes. Proximate causes are those occurring more closely in time and place to the caused event, while distal causes occurred further away in time or place. For example, when asked about the cause of a friend’s poverty, you may describe her lack of social support and of a job at the moment, or you might note instead that many generations of her family have not accumulated much wealth and were denied access to social and economic opportunities. The former causes are proximate, while the latter distal. Proximate causes can be easier to identify, but distal causes are sometimes more important influences. This distinction between proximate and distal causes shows that events can have more than one cause. So, identifying a cause doesn’t mean that you have identified the only cause or the most important cause, or that you have ruled out other causes. We have seen that poverty has many causes, for example.

Besides spatiotemporal contiguity, we also tend to use information about correlation between events to discern causal relations. Indeed, correlation can be used in combination with spatiotemporal contiguity as a guide to causation. As we know from Chapter 9, two variables are correlated when the value of one variable raises or lowers the probability of the other variable taking on some value. Different events can occur together a few times by chance, but if the values of two variables are correlated across many instances, this is some reason to think one variable may causally influence the other. For example, there is a clear correlation between childhood poverty and many negative life outcomes. It’s thus worth investigating which (if any) of these life outcomes are caused by childhood poverty.

But correlation too is an imperfect guide to causation. For one thing, correlation is symmetric: if event A correlates with another event B, then B correlates with A as well. Causation isn’t symmetric. If studying for an exam and getting a good grade on the exam are correlated, this is because studying causes getting a good grade and not the other way around. Yet a correlation alone doesn’t provide information about which event is the cause and which event is the effect.

Further, correlations between

Per capita consumption of cheese
correlates with the number of people who died from getting tangled in their bedsheets
---
# Causal reasoning

Events can exist even though neither event causes the other. Some events are correlated because they share a common cause—a third event that causes both. Famously, ice cream consumption is correlated with drowning, but eating ice cream is not a cause of drowning. Instead, there is evidence that the occurrence of hot days increases both ice cream consumption as well as swimming, and so also drowning rates. Finally, some correlations are spurious, that is, not causally related at all, such as the relationship between annual per capita cheese consumption and the number of people who died from becoming tangled in their bedsheets.

These are all ways correlations may fail to indicate causation. But the reverse can also happen: events can be causally related even when they are not correlated. Consider this example, due to philosopher Nancy Cartwright. Smoking cigarettes is well established as a cause of heart disease. Adequate exercise prevents heart disease. If smoking is strongly correlated with exercise, then this well-established cause of heart disease will also be strongly correlated with its prevention, and smoking and heart disease will not in general be correlated. This could be so even though smoking causes heart disease.

# Box 11.1 Simpson’s paradox

In August 2021, less than a year after Covid-19 vaccines first became available, headlines announced the findings of a new study published in the prestigious journal Science: “Nearly 60% of hospitalized COVID-19 patients in Israel fully vaccinated.” The vaccine was supposed to help against Covid, but now more vaccinated people than unvaccinated were getting seriously ill! People worried that the vaccine’s efficacy waned very rapidly, no longer offering protection after a few months. But no: the vaccine was still very effective at preventing severe illness from Covid-19. Instead, this was an instance of Simpson’s paradox, where a correlation between two events disappears or is reversed when data are grouped in a different way. Israel had a very high vaccination rate: there were many more vaccinated than unvaccinated people. Further, age is correlated with the probability of vaccination: as in many other parts of the world, older Israelis were more likely to be vaccinated than younger Israelis. But older people are significantly more likely to suffer severe illness from Covid-19. The 40% of hospitalized Covid-19 patients who were unvaccinated was thus a much larger proportion at lower risk of severe illness than the 60% of hospitalized Covid-19 patients who were vaccinated. Accounting for the vaccination rate in the overall population and controlling for age revealed that Israelis over 50 were seven times more likely to be hospitalized if they were unvaccinated, while younger Israelis were 13 times more likely to be hospitalized if they were unvaccinated. There are many other real-life cases of Simpson’s paradox. Understanding how and why the paradox emerges is important for drawing correct causal conclusions from statistical evidence.
---
# Causal reasoning

 

  

FIGURE 11.3 By 2021, nearly 92% of Israelis over 50 had been vaccinated for Covid-19. An unvaccinated Israeli over 50 had a nearly 1% chance of hospitalization from Covid, while a vaccinated Israeli over 50 had a .014% chance of hospitalization.

# Accounts of causation: difference-making and physical processes

We have seen that spatiotemporal contiguity and correlation can be guides to causal relationships, but neither is a perfect guide. Despite Hume’s skepticism, there must be more to causation than mere association between events. Here are two ideas about what that might be.

One idea is that causal relationships are relationships of difference‐making. Put simply, the difference-making account of causation is the idea that if the occurrence of one event makes a difference to the occurrence of a second event, then the first event is a cause of the second event. If the billiard ball had not struck the 8‐ball, then the 8‐ball wouldn’t have moved. If the billiard ball had struck the 8‐ball in a different place or at a different speed, then the 8‐ball would have moved in a different direction or at a different speed. The billiard ball’s motion made a difference to the 8‐ball’s motion. Thus, the billiard ball’s motion caused the 8‐ball to move.

This difference‐making relationship goes beyond the mere correlation of events: a focus on intervention can help us see how. Recall that an intervention is a direct manipulation of the value of the independent variable. The idea of difference‐making is that, for one variable to count as a cause of another, an intervention on this variable, while controlling all other variables, will change the value of the other variable. A difference‐making account of causation uses the ideas of intervention and variable control to give an answer to what causation might be beyond mere correlation or association between events.
---
# Causal reasoning

# Box 11.2 Difference-making and counterfactual conditionals

According to the difference-making account of causation, causally relevant factors make a difference to whether an effect happens. The idea of difference-making relies on reasoning about counterfactual conditionals. Recall that a conditional is any if-then statement. Counterfactual conditionals have the following form: if C had occurred, then E would have occurred. For example, consider the conditional “if you had scored the penalty, then your team would have won the game.” If this counterfactual conditional were true, this would be reason to say that you not scoring a goal caused your team to lose. Such conditionals are called counterfactuals because the antecedent of the conditional is contrary to fact. Recall from Chapter 6 that material conditionals are false only when the antecedent is true and the consequent is false. This isn’t so for counterfactual conditionals. After all, the antecedent of a counterfactual conditional is always false. In our example, you didn’t score a goal, but that doesn’t guarantee your team would have won if you had—maybe that wouldn’t have been enough to win. It’s a matter of debate in philosophy how to assess whether a counterfactual conditional is true. It seems that to do so we need to consider how things would be in conditions unlike what has really occurred—in another “possible world,” philosophers sometimes say. The difference-making account of causation makes use of the concept of an ideal intervention to help with this. If we imagine intervening on what really happened to make it so that you scored a goal, keeping everything else exactly the same, then would your team have won? If so (and if you didn’t in fact win), then you not scoring a goal did cause your team to lose.

A second idea about the nature of causal relationships is that they are based on physical processes. On the physical process account of causation, causation occurs when there is a continuous physical process connecting a cause to its effect, such that a cause transmits its effect with the transfer of mass, energy, momentum, charge, or other physical properties. When the billiard ball knocked into the 8‐ball, some of its kinetic energy transferred to the 8‐ball, which is why the 8‐ball started moving. This is a physical process connecting the billiard ball’s motion to the 8‐ball’s motion. Thus, the billiard ball’s motion causes the 8‐ball’s motion. The physical process account gives a different answer than the difference‐making account to how causation goes beyond mere association, pointing instead to the transmission of physical properties.

The physical process and difference‐making accounts of causation may be compatible. But each account is more useful for thinking about causal reasoning in different circumstances. For some causal claims, physical processes are the benchmark; with others, they are difficult to track. Recall the research on alleviating poverty in Niger. How would you investigate energy transfer or other physical processes of the causes of poverty? You wouldn’t. In contrast, it’s clear how to think about increasing income.
---
# Causal reasoning

with cash transfers, a suspected causal variable, and to test how those changes affect variables associated with poverty. This suggests a difference‐making account is apt.

For other causal claims, the idea of difference‐making doesn’t neatly apply. The moon orbits around the sun because of the curvature of space‐time. How could we intervene on this curvature to assess whether our intervention makes a difference to the orbit of the moon? It’s a bit confusing; this seems like a feature of reality that can’t be changed with an experimental intervention. And without even a way to conceive of such an intervention, we can’t use difference‐making to assess causal influence.

Watch Video 14

# Strength of causation

Earlier in this section, we considered how correlation could provide clues to causal relationships. Correlation between variables occurs when the value of one variable raising or lowering the probability of the other variable takes on some value. These conditional probabilities are also useful in characterizing the strength of causal relationships.

Consider some cause, C, and its effect, E. To start at the extreme, if Pr(E | C) = 1, then the occurrence of a cause guarantees the effect. For example, having no income, family resources, or any other source of funds or necessities guarantees that someone will experience poverty. Having no source of funds or necessities is a sufficient cause of poverty, in the sense that this cause always brings about this effect. If Pr(E | not‐C) = 0, then the occurrence of a cause is necessary for the effect to occur. For example, a motionless 8‐ball will not roll across a flat pool table unless something strikes it. Another ball or other object striking an 8‐ball is thus a necessary cause of a motionless 8‐ball rolling across a flat pool table: a cause that must occur in order for the effect to come about. (See Chapter 6 for discussion of necessary and sufficient conditions, which is relevant to this use of necessity and sufficiency.) If both conditional probabilities hold, if both Pr(E | C) = 1 and Pr(E | not‐C) = 0, then the cause is both necessary and sufficient for the effect. The cause occurring guarantees the effect will occur, and without the cause occurring, there’s no way the effect will occur.

The strength of virtually all causal relationships falls short of these extremes. Most causes aren’t necessary or sufficient for their effects to come about. For example, though having no income can often result in poverty, family or governmental support could interfere with that effect. Having no income isn’t sufficient for poverty. Nor is it necessary: the working poor is a term for people who spend substantial time in paid employment and yet are experiencing poverty. A cause that raises the probability of an outcome occurring but does not guarantee the outcome is called a contributory cause, or partial cause, of that outcome. Most causes are contributory causes.

In general, you can judge the strength of a causal relationship with the following calculation:

S = Pr(E | C) − Pr(E | not‐C)

This measures the degree to which the occurrence of the cause increases the probability of the effect occurring by taking into account the likelihood of the effect when
---
# Causal reasoning

The cause does and does not occur. If more people without an income experience poverty and fewer people with an income experience poverty in the US compared to the Netherlands, for example, then we could say that lack of income is a stronger influence on poverty in the US than in the Netherlands. It’s important to notice that, although conditional probabilities can be used to characterize the strength of a causal relationship, they can’t identify when one variable is a cause of another. Recall from our previous discussion of correlation that simply identifying a correlation between the conditional probability of variables doesn’t mean one causes the other.

Most causes are merely contributory causes, rather than being necessary or sufficient for their effects, because causal relationships are often sensitive to other variables. The causal background consists in all the other factors that might causally influence an outcome, thereby also potentially affecting the causal relationship between the two events. The causal background for how lack of income causes poverty includes factors like family wealth, governmental support, savings, financial responsibilities, money management skills, and much more besides. This is one reason why poverty is a complex phenomenon. The conditional probabilities between a cause and its effect can change in different causal backgrounds or may only hold in some causal backgrounds.

Often, the causal background is ignored when causal claims are made. You do not generally consider that oxygen is a causally relevant factor when you explain how a defective stove caused an apartment fire, for example. But accounting for the relevant causal background is crucial in sound causal reasoning. For example, the value of cash transfers to mitigating poverty will depend on the causal background that shapes the extent to which lack of access to cash is responsible for experiencing poverty.

# EXERCISES

1. Recall: How is spatiotemporal contiguity a clue to causation, and how does it fail to be a perfect guide to causation? How is correlation a clue to causation, and how does it fail to be a perfect guide to causation?
2. Apply: List three possible relationships that can result in a correlation between events A and B even though A does not cause B. Give a new example illustrating each.
3. Recall: Define the difference-making and physical process accounts of causation.
4. Think: What was Hume’s skepticism about causation? Evaluate the merits of his concern, taking into account the discussion throughout this section.
5. Apply: Define proximate causes and distal causes. Then, for each of the following questions, give one explanation that cites a more proximate cause and one explanation that cites a more distal cause. You might need to invent some details about these causal relationships to answer this question; that’s fine. Feel free to get creative.

1. Why did the Titanic sink?
2. Why did Ruth leave a tip after her meal at the restaurant?
3. Why did the hurricane happen?
---
# 11.12 Apply:

Write down the formula that gives the strength of causal relationships. Then, considering that formula, order the following causal relationships from strongest to weakest, giving a brief rationale for the order of each item.

1. Brushing your teeth, flossing, and visiting the dentist prevents cavities.
2. Frequent smiling increases well-being.
3. Eating pizza prevents getting the flu.
4. Consuming anabolic steroids improves physical strength.
5. Increase in the minimum wage produces higher attendance at football games.
6. Warmer summers lead to longer periods of drought.

# 11.13 Think:

For each of the causal relationships in 11.12, name one feature of the causal background that would make the causal relationship stronger and one feature of the causal background that would make the causal relationship weaker. It might help to consider the conditional probability relationship that gives the strength of causal relationships.

# 11.3 TESTING CAUSAL HYPOTHESES

After reading this section, you should be able to:

- Characterize how the difference‐making account of causation relates to intervention
- Describe how intervention, direct and indirect variable control, random sampling, and statistical hypothesis‐testing is each important to discerning causal relationships
- Articulate how statistical hypothesis‐testing is used to test causal hypotheses

# Experimental interventions and difference-making

Discovering causal relationships requires more than just passively observing what happens. The idea of causation as difference‐making is useful for making sense of various methods scientists can use to acquire knowledge of causes. One such method is to run an experiment—ideally, a perfectly controlled experiment, as detailed in Chapter 3.

Suppose that you are a farmer interested in learning whether using a new fertilizer will increase your crop yield, that is, make a difference (positive difference) to the yield. This is a causal hypothesis. How would you test it? One way would simply be to try out the fertilizer on your crops and see what kind of a yield you get. But the causal background might vary from last year to this year in a way that affects crop yield: rainfall, temperatures, last frost date, and more. You wouldn’t be able to distinguish that influence from the specific effect of the fertilizer on the yield.

A better approach would be to divide your field into different plots of equal size. You can then use the new fertilizer on some plots but not others and compare the crop yield from the fertilizer plots to the crop yield from the other plots. If the plots treated with the fertilizer produce, on average, a larger crop yield than the other plots, then the fertilizer made a difference; we could then say the new fertilizer causes increased crop yield. If the two groups of plots yielded about the same amount of crop, then...
---
# Causal reasoning

the new fertilizer is probably ineffective. If the fertilizer plots do worse, the fertilizer makes a difference—but the wrong kind!

Applying concepts introduced in Chapter 3, we can say that the farmer has created an experimental group (plots to which the fertilizer is applied) and a control group (plots handled according to the farmer’s past practices). The application of fertilizer to plots in the experimental group is an intervention. The farmer intervenes on a suspected cause to see whether this makes a difference to the suspected effect. The suspected cause is the independent variable, and the suspected effect is the dependent variable. The causal background consists of extraneous variables. Some extraneous variables are directly controlled by comparing yield in the same season, in the same field, with the same irrigation, and so on, while other extraneous variables are indirectly controlled by random assignment of plots of land to experimental group and control group.

Some experiments testing causal hypotheses aim to establish whether there is a causal relationship, and others aim to clarify the strength of a causal relationship. For example, some drug trials simply seek to establish safety: that a drug won’t have negative effects. Others seek to establish efficacy: that a drug will have the expected positive effect. And still others aim to establish the relative strength of a causal relationship: whether some drug is more effective than another already on the market.

Experimental interventions introduce an external influence on a system, which can help disentangle causal relations. This is why the suspected cause is called an independent variable—the intervention independently determines its value, which, if all goes well, eliminates the possibility that the suspected cause is affected by the causal background. Other features of experimental design, such as using random sampling to select experimental participants and having a control group, are designed to minimize the chance that changes to the suspected effect are due to the causal background instead of the intervention. Altogether, these features help scientists test causal hypotheses, identifying whether a particular factor is a genuine difference-maker.

# Statistical variation and testing causal hypotheses

In experimental tests of causal hypotheses, hypotheses about the existence, direction, and strength of causal relationships are used to develop specific expectations regarding how dependent variables will change in response to changes to independent variables. But testing causal hypotheses is complicated by extraneous variables and chance variation. The experimental techniques of intervention, direct and indirect variable control, random sampling, and statistical hypothesis-testing are motivated in large part by their ability to discern causal relationships from mere correlation, cause from effect, and causal influence from chance variation.

We just saw how intervention and variable control are useful. Let’s now consider how statistical hypothesis-testing and random sampling help to test causal hypotheses in the face of statistical variation. In the fertilizer experiment we imagined earlier, we expected the new fertilizer to improve crop yield in the plots to which it is applied. Does this mean we should expect all fertilized plots to have better yield compared to all the standard plots? Surely not; varying causal background, and perhaps sheer
---
# Causal reasoning

random variation, will introduce variability among the plots. So, then, how many of the fertilized plots need to have a better yield to show that fertilizer makes a difference? To answer that question, we’d need to use inferential statistics.

As this illustrates, statistical hypothesis‐testing is crucial for testing causal hypotheses. Inferential statistics can be used to generate specific expectations of a group’s statistical properties, which is important for hypotheses that predict probabilistic causal influence. As we’ve seen, this is much more common than causes guaranteeing their effects. In null hypothesis significance tests, causal hypotheses play the part of the alternative hypothesis. The null hypothesis is usually that the posited cause does not actually influence the phenomenon of interest.

# Box 11.3 Mill’s methods

In the late 19th century, the English philosopher John Stuart Mill emphasized the role of observation and experimentation in discerning causal relationships. Mill identified five methods to evaluate causal hypotheses. These can still be useful, though statistical analysis and intervention are both important tools of causal hypothesis-testing not captured by Mill’s methods.

1. Method of concomitant variations: Observing that the value of one variable changes in tandem with changes to the value of another variable. In modern terms, this just is using correlation between variables to infer that the variables might be causally related. Of course, mere correlation does not guarantee causation.
2. Method of agreement: Considering cases where an effect occurs to see what they have in common. If there is a prior event or condition common to all, then one may infer that this event or condition caused the effect.
3. Method of difference: Considering cases where an effect does not occur to see what distinguishes those from when the effect occurs. If an event or condition present when the effect occurred is absent when the effect does not occur, then one may infer it caused the effect.
4. Joint method of agreement and difference: Considering cases where the effect occurs to see what they have in common (method of agreement), as well as considering cases where the effect does not occur to see what was different (method of difference). If an event or condition common across cases where the effect occurs is absent when the effect does not occur, one may infer it causes the effect.
5. Method of residues: Comparing cases in which a set of causes brings about a set of effects to cases in which some of those causes bring about some of those effects and inferring, on that basis, that the absent cause(s) are responsible for the absent effect(s). Unlike the other methods, this is a way to reason about which of a set of causes are responsible for which effects.
---
# Causal reasoning

So, for our farmer, the null hypothesis is that the fertilizer is causally inefficacious: the range of crop yield from the fertilized plots of land will only differ from the range of crop yield from the other plots by chance variation. The mean crop yield and crop-yield variation in the control group, together with the sample size, can be used to calculate the probability distribution for the experimental group’s crop yield assuming the new fertilizer does not make a difference. If the measured crop yield is sufficiently unlikely, we can reject the null hypothesis and conclude the new fertilizer causes increased crop yield.

Another complication of expectations from a causal hypothesis due to causal background relates to external experimental validity, that is, the extent to which experimental results generalize from the experimental conditions to other conditions. For example, should we expect the new fertilizer to have the same effect as in our experiment in a rainier season, when the causal background is different? Due to considerations of external experimental validity, it’s not sufficient just to ensure extraneous variables do not vary systematically between the experimental and control groups. Conclusions about a causal hypothesis may also go wrong when the causal background of an experiment is not sufficiently similar to the causal background in circumstances in which we seek to apply the causal knowledge.

Random sampling is helpful on this front. A sufficiently broad range of conditions that are randomly selected enables us to expect the range of experimental conditions to be similar to the real-world circumstances in which the causal knowledge would apply. This increases external experimental validity and, in turn, the relevance of our causal knowledge. Perhaps our farmer will have to test out the fertilizer over several seasons or on plots arranged to mimic expected variation such as in rainfall and temperature to know the new fertilizer causes increased crop yield across the range of growing conditions the farmer is likely to encounter.

# EXERCISES

# 11.14

Recall: Describe the importance of intervention for testing causal hypotheses. Watch Video 15. Then, define the difference-making account of causation and characterize how it relates to intervention.

# 11.15

Apply: Headlines in popular media often misrepresent the scientific studies they discuss. In particular, many headlines suggest a causal relationship where the evidence provided by the scientific study only supports a correlation. Consider the following headlines. For each, (a) identify whether it makes either a causal or a correlational claim; (b) rewrite any headline using causal language so that it reads as a correlational study; and (c) suggest a possible explanation for each correlation that is not the posited or suspected causal relationship.

1. “Lack of Sleep May Shrink Your Brain” (CNN, September 2014)
2. “To Spoon or Not to Spoon? After-Sex Affection Boosts Sexual and Relationship Satisfaction” (Science of Relationships, May 2014)
3. “Daytime TV (Soap Operas) Tied to Poorer Mental Scores in Elderly” (Reuters, March 2006)
---
# Causal reasoning

1. “Study Suggests Attending Religious Services Sharply Cuts Risk of Death” (Medical Xpress, November 2008)
2. “Facebook Users Get Worse Grades in College” (Live Science, April 2009)
3. “Texting Improves Language Skill” (BBC, February 2009)
4. “Study Suggests Southern Slavery Turns White People Into Republicans 150 Years Later” (Think Progress, September 2013)
5. “Dogs Walked by Men Are More Aggressive” (NBC News, November 2011)
6. “Want a Higher GPA? Go to a Private College” (New York Times, April 2010)
7. “Sexism Pays: Men Who Hold Traditional Views of Women Earn More Than Men Who Don’t” (Science Daily, September 2008)

# 11.16

Apply: Choose two of the headlines from Exercise 11.15, and look up the text of both. Write a paragraph evaluating the strength of the evidence cited in the media report supporting the claim (causal or correlational) in the headline.

# 11.17

Recall: Describe why each of the following is important for discerning causal relationships: direct and indirect variable control, random sampling, and statistical hypothesis-testing.

# 11.18

Apply: How would you design an experiment to determine whether smoking marijuana causes schizophrenia?

1. a. Identify the intervention and describe how you would control extraneous variables.
2. b. Identify the expectations given the hypothesis, that is, what finding would enable you to conclude that smoking marijuana is a cause of schizophrenia.
3. c. Describe how statistical hypothesis-testing and random sampling are employed and why each is important.

# 11.4 CAUSAL MODELING

After reading this section, you should be able to:

- Describe how causal modeling can yield causal knowledge
- Define causal Bayes nets and describe how they are developed and applied
- Identify three assumptions of causal Bayes nets and discuss their significance

# From correlation to causation

Besides controlled experiments and statistical hypothesis‐testing, another important approach to gaining causal knowledge is causal modeling. Causal modeling involves the use of computational and statistical methods for representing, manipulating, and testing causal hypotheses. When experimental interventions cannot be conducted, causal modeling can be used to evaluate causal hypotheses. Even when interventions can be made, combining experiments with causal modeling can be used to evaluate whether
---
# Causal reasoning

Correlational evidence supports the causal hypothesis and to help identify factors in the causal background that must be controlled during an experiment.

Like controlled experiments, causal modeling is also related to the difference-making account of causation, which defines causal relationships in terms of potential intervention and variable control. If an event C causes another event E, then an intervention on C influences the value of E. If C and E are merely correlated, share a common cause, or if E causes C, then interventions on C won’t causally influence the value of E. In causal modeling, difference-making is identified from patterns of conditional probabilities between variables representing different features of a target phenomenon. Scientists can leverage these patterns of conditional probabilities to represent causal structure and reason about how variables influence one another.

The method of regression analysis, introduced in Chapter 9, is one of the oldest causal modeling procedures. It is used to estimate the correlation of two variables, conditional on all other measured variables. It’s like drawing a best-fitting line for the relationship in the values of two variables based on data on a scatterplot. For a suspected causal relationship, regression analysis is used to estimate how a causal variable affects another variable. Merely running a regression analysis, however, cannot deliver causal knowledge when causal influence isn’t yet known. We need additional evidence from meta-analyses, experiments, or non-experimental studies to supply that information, then regression analysis can be used to estimate the nature of the causal effect, including its direction and strength.

As in regression analysis, the building blocks of many causal modeling approaches are statistical correlations and probabilistic dependencies between variables that represent different features of a target phenomenon. In causal models, variables represent potential causes and effects. Here we will focus on Bayes networks, or “nets.” A Bayes net is a kind of causal model that uses joint probability distributions to provide a compact, visual representation of causal relationships and the strength of those relationships. Nodes in the graph stand for variables of interest, and arrows connecting different nodes stand for hypothesized causal relationships between variables.

Conditional probabilities specify how each variable depends on its direct causes in a joint probability distribution: the probability distribution for each of a set of variables, taking into account the probability of the other variables in the set. These causal models are called Bayes nets because they use Bayes’s theorem to update the probabilities based on new information about the value of variables or their probabilistic relationships. (Bayes’s theorem was introduced in Chapter 8 and Bayesian statistics discussed in Chapter 10.)

# Developing Bayes nets

To better understand how scientists use Bayes nets to learn about causal relationships, consider this scenario from an introduction to the main concepts and applications of Bayesian networks:

Suppose that a patient has been suffering from shortness of breath (called dyspnea) and visits the doctor, worried that he has lung cancer. The doctor knows
---
# Causal reasoning

that other diseases, such as tuberculosis and bronchitis, are possible causes of this symptom, as well as lung cancer. She also knows that other relevant information includes whether the patient is a smoker (increasing the chances of cancer and bronchitis) and what sort of air pollution he has been exposed to. A positive x‐ray would indicate either TB or lung cancer.

There’s plenty of causal information here, but how that information relates to the case at hand is tricky to determine. Doctors can use causal Bayes nets to generate medical diagnoses. To construct such a model, the relevant variables first need to be identified. Each variable is represented with a node. While there’s no uniquely right way of setting up the Bayes causal net, it helps to make choices about what nodes to include that enable us to represent the relevant aspects of the situation with enough detail to perform the desired reasoning. One possible modeling choice is shown in Table 11.1. In this case, the variables include dyspnea, smoker, pollution exposure, age, x-ray result, tuberculosis, and lung cancer.

The second step of constructing a causal Bayes net is to specify the system’s causal structure by drawing arrows between the nodes. If one variable affects another, then the corresponding nodes should be connected with an arrow indicating the direction of the effect. Smoking and living in a polluted area are two factors affecting the patient’s chance of having lung cancer. In turn, having lung cancer is a factor affecting the result of an x‐ray and the patient’s difficulty in breathing. If this is the structure of the situation, then we may draw the graph pictured in Figure 11.4.

Causal relationships represented in a causal Bayes net can take several forms. Causes can increase or decrease the probability of some variable taking on a given value, and there can be a feedback loop where two or more variables influence one another in a cyclical way. Most of the time, however, Bayes nets are assumed to be directed acyclic graphs (sometimes abbreviated DAG), which means that all the causal relationships are taken to go in one direction without feedback loops. This assumption means that earlier causes are not also later effects. You can see from Figure 11.4 that our graph makes this assumption; no arrows form circles like X → Y → Z → X, and no arrow is bidirectional like X ⟷ Y.

# Possible values for variables in the dyspnea case

|Variable|Values|
|---|---|
|dyspnea|{T, F}|
|smoker|{T, F}|
|pollution|{low, high}|
|x-ray|{positive, negative}|
|lung cancer|{T, F}|
|tuberculosis|{T, F}|

---
# Causal reasoning

#  

#   

# A causal graph for the dyspnea case

# FIGURE 11.4

# Conditional probabilities of developing lung cancer given level of pollution exposure and whether one smokes

|Pollution|Smoker|Pr(cancer = T | pollution, smoker)|
|---|---|---|---|
|high|T|0.050| |
|high|F|0.020| |
|low|T|0.030| |
|low|F|0.001| |

After specifying the nodes and their structure, the strength of the relationships between connected nodes must be specified. To do so, one needs to define a probability distribution for each node, conditional on any node(s) that causally influences it. In the example of patient diagnosis, statistical information from previous medical studies or from observed frequencies are used to specify these probability distributions. For variables with no such information available, initial probabilities can be based on an intuition, guess, or estimation about the case. Recall from Chapter 10 that Bayesian statistics is supposed to make these initial guesses unimportant in the long run. Bayes nets allow us to infer conclusions even if we start off with imprecise or inaccurate initial probabilities.

Let’s look at the node cancer in Figure 11.4. Its parent nodes are pollution and smoker, each of which can take two possible values for a total of four combinations of joint values: {# ; # ; <low, T>; <low, F>}. We can then specify the conditional probability of having cancer for each of these four cases. One way to represent these conditional probabilities is in a table, as in Table 11.2.

# Reasoning with Bayes nets

Once all conditional probability distributions are determined, our causal Bayes net captures the relevant knowledge available. Now we can start to reason with it. Reasoning with a Bayes net amounts to computing posterior probability distributions for one or more nodes of interest given the values of nodes that you have information about. These computations are governed by Bayes’s theorem or other algorithms.
---
# Causal reasoning

for computing approximations to posterior probabilities. Think of this as updating your beliefs about the value of a node based on changes to your beliefs about the values of other nodes. The arrows connecting nodes show the paths that probability distribution changes follow.

 

Belief updating can happen either from cause to effect or vice versa. For example, if we’re certain that the patient has dyspnea, and her x‐ray results are negative, then we can update our diagnosis about whether the patient has cancer, a causal influence on both dyspnea and x‐ray results. In turn, updating our diagnosis about whether the patient has cancer will affect our beliefs about whether the patient smokes and lives in a high‐pollution area, proceeding up the chain of causal influence. Or, if we are certain that the patient smokes, we can update our beliefs about her chance of having lung cancer accordingly, which is causally influenced by smoking status. This also influences our expectations of the x‐ray result.

A different type of reasoning with causal Bayes nets regards the relationship between two causes that compete to explain an observed effect. In our case, smoker and pollution are two such causes. They compete to explain the value of the variable cancer, which they both influence. Suppose we learn that the patient has cancer. This new information raises the probability of both possible causes. Suppose that we learn further that the patient lives in a badly polluted city. Something interesting would now happen in our causal Bayes net. This new piece of information both explains the patient having cancer and lowers the probability that the patient is a smoker. Although the variables smoker and pollution are initially probabilistically independent, given that we know that the patient has cancer and lives in a highly polluted area, the probability that the patient is a smoker goes down. Knowing that the patient has been exposed to significant pollution accounts for the lung cancer and thus disrupts the probabilistic association between lung cancer and smoking. Now we needn’t speculate that the patient was a smoker in order to explain the lung cancer.

In the simple case we’ve considered, a Bayes net is specified and then used to make causal inferences and predictions. In many other scientific applications, causal Bayes nets are incomplete in two ways. First, there are many variables that could be added that would precede, mediate, or follow the variables explicitly represented in the model. Second, information might be lacking about the causal relationships between the variables represented in the model. In that case, the structure of the network and the relevant probabilistic dependencies must be learned from data, since defining a complete Bayesian network would be too complex. For this, scientists rely on computational methods like machine learning algorithms that search correlational data for causal dependencies.

Cognitive neuroscientists, for example, are interested in the causal relationships between brain areas that support a cognitive capacity. To find out about these causal relationships, they often rely on brain imaging data, where subjects perform tasks that tap the cognitive capacity of interest while having their brain activity recorded. Neuroscientists use background knowledge about which brain regions might be involved in a task to focus their attention on activity in a few regions of interest, each one of which can be treated as a variable and represented as a node in a DAG. The challenge
---
# Causal reasoning

is then to discover the causal structure of these regions. Machine learning algorithms help neuroscientists to tackle this challenge. An algorithm searches the brain imaging data set to find the causal structure that best explains observed statistical dependencies between the variables of interest. Using DAGs, it is then possible to determine whether a causal structure is in principle identifiable from a probability distribution and to derive the probabilistic expression for this quantity.

 

  

# Assumptions of Bayes nets

Reasoning with causal Bayes nets requires making several theoretical assumptions; these assumptions are needed to infer causal relationships from data about conditional probabilities. Three key assumptions are the common cause principle, modularity, and the causal Markov condition. These assumptions are not always satisfied by a data set, but when they are, causal Bayes nets are especially promising for learning about causal relationships between variables from their observed statistical features.

We encountered the idea of a common cause earlier in this chapter. The common cause principle says that every correlation between two variables is either due to a direct causal effect linking the correlated variables or is brought about by a third factor that causes both, that is, a common cause. This idea is of central importance in causal explanation and causal modeling. For example, suppose that two lamps in your room go out suddenly and simultaneously. You may look for whether the common power supply was interrupted. This interruption would be the common cause of the two simultaneous events and would explain this improbable coincidence.

# Modularity

is an assumption about how systems can be manipulated; it implies that interventions into causal relationships in a system should not change other causal relationships in the system. When a system is not modular, interventions on some causal relationship(s) change the nature of other causal relationships. If a system is modular, then dependencies between variables in a causal Bayes net model of the system that are not directly manipulated should not change. Modularity is a useful feature, as it allows for precise and focused predictions about what would happen in the target system if certain causal relationships were manipulated. When the modularity assumption is violated, Bayes nets won’t correctly specify the state of a system after an intervention.

Closely associated with modularity is the causal Markov condition. One of the most important assumptions of causal Bayes nets, the causal Markov condition is the requirement that the probability of causal variables conditional on their parent causes are probabilistically independent of all their other ancestors. The basic idea is that remote causes are irrelevant to conditional probabilities, and thus to causal inference, when we know the immediate causes of an effect. In our medical diagnosis example, the value of tuberculosis is influenced by the value of cancer, but probabilistically independent of pollution and smoker conditional on cancer. This is because cancer and tuberculosis are causally related, whether the cancer was caused by smoking or by pollution.

The causal Markov condition is motivated by the idea that, when probabilistic dependencies are found between variables, these dependencies are due to one variable causing the other or to their sharing a common cause. The causal Markov condition
---
# Causal reasoning

specifies which variables will be probabilistically independent conditional on other variables in a set of variables under study. If the causal Markov condition holds of a set of variables associated with a system, then conditional independence between variables indicates the absence of a causal relationship. For example, a causal chain like X → Y → Z implies that X, Y, and Z are all probabilistically dependent on one another but that X and Z should be probabilistically independent if Y takes a fixed value. In some cases, the Markov condition might fail if the set of variables included in the Bayes net omits common causes or includes variables that aren’t relevant causes.

These are three key assumptions underlying reasoning with causal Bayes nets, though there are others as well. Understanding how different strategies for causal modeling work when some of their assumptions fail, and what kinds of errors they would yield, are two of the most important challenges of current causal modeling approaches.

# EXERCISES

# 11.19 Recall:

Explain what causal modeling is good for, pointing out its advantages and limitations.

# 11.20 Apply:

For each of the following cases, (a) indicate the causal hypothesis involved, distinguishing causal variables from effects; (b) offer another plausible cause for the effect; and (c) explain whether the reasoning described in the case is good or bad with the help of a simple causal model (consider using a directed acyclic graph, or DAG).

1. a. You have eaten your birthday dinner at your favorite pizzeria in town for the past 10 years. This year you got sick. This was also the first time your Uncle Sam was there. You conclude you got sick because Uncle Sam was there.
2. b. Eryka normally goes to bed at midnight and gets up by 7:00 am each morning. She usually runs two kilometers after having some breakfast. This morning, however, she ran only half a kilometer and had to stop, as she was so tired. She recalled that she went to sleep unusually early the night before and concludes that too much sleep made her too tired to run.
3. c. Phineas Gage’s moral character changed dramatically after an explosion blew a tamping iron through his head. Gage was leading a railroad construction crew near Cavendish, Vermont, when the accident occurred. “Before the accident he had been a most capable and efficient foreman, one with a well-balanced mind, and who was looked on as a shrewd smart business man.” After the accident, he became “fitful, irreverent, and grossly profane, showing little deference for his fellows. He was also impatient and obstinate, yet capricious and vacillating, unable to settle on any of the plans he devised for future action.”

# 11.21 Recall:

Describe (a) what a causal Bayes network is, (b) how a causal Bayes net is developed, and (c) how it is applied.

# 11.22 Apply:

Consider the following story: A group of psychologists is interested in how intrinsic motivation of university students affects their exam results. They
---
# Causal reasoning

believe that intrinsic motivation affects both class attendance and home preparation (reading the textbooks, doing the assignments, etc.). They also believe that both class attendance and home preparation affect exam results. They do not believe that there are any further causal interactions. All relevant variables (intrinsic motivation, class attendance, home preparation, exam results) are considered to have two values: “High” and “Low” for intrinsic motivation, class attendance, home preparation; and “Pass” and “Fail” for exam results. The psychologists observe the following frequencies:

- 40% of all students have a high intrinsic motivation.
- 90% of all highly motivated students attend classes regularly, as opposed to 60% of all students with low motivation.
- 70% of all highly motivated students prepare well, as opposed to 20% of all students with low motivation.
- 80% of all students who prepare well and attend class regularly pass the exam.
- 60% of all students who prepare well and do not attend class regularly pass the exam.
- 45% of all students who do not prepare well and do attend class regularly pass the exam.
- 40% of all students who do not prepare well and do not attend class regularly pass the exam.

On the basis of this information, find the conditional probabilities and draw the causal Bayes net that corresponds to the story.

# 11.23 Recall:

Describe the assumptions of common cause principle, modularity, and the causal Markov condition, and indicate why each is important for causal modeling.

# 11.24 Apply:

Suppose that we measure the variables storm (S), barometer reading (B), and atmospheric pressure (A). You find that S and B are dependent, as are both B and A and S and A. Furthermore, you find that S and B given A are independent. From these constraints alone, what causal structure can you infer? Draw a simple DAG showing the causal relationship. Then, explain the role of the common cause principle and Markov condition in making reliable inferences about the causal relationships in the example.

# FURTHER READINGS

For more on poverty, see Lister, R. (2021). *Poverty. John Wiley & Sons. A more concise treatment is Wolff, J., Lamb, E., & Zur‐Szpiro, E. (2015). A philosophical review of poverty*. Joseph Rowntree Foundation. www.jrf.org.uk/report/philosophical‐review‐poverty

For more on normative and descriptive accounts of causation and their importance in scientific explanation and psychology, see Woodward, J. (2021). *Causation with a human face: Normative theory and descriptive psychology*. Oxford University Press.

For a pluralist view of the nature of causation and discussion of causal analysis, including
---
# 290 Causal reasoning

causal Bayes nets, see Cartwright, N. (2007). Hunting causes and using them: Approaches in philosophy and economics. Cambridge University Press.

For a short introduction to causal modeling, with a focus on the epistemology of causation, see Eberhardt, F. (2009). Introduction to the epistemology of causation. Philosophy Compass, 4(6), 913–925.

For an advanced treatment of causal modeling, see Pearl, J. (2009). Causality: Models, reasoning, and inference (2nd ed.). Cambridge University Press.
---
# CHAPTER 12

# Explaining and theorizing

 

  

# 12.1 PSYCHIATRY AND SCIENTIFIC THEORIES

After reading this section, you should be able to:

- Summarize psychiatric knowledge bearing on depression and its treatment
- Describe the primary features of scientific theories and why they are important to science
- Indicate how scientific theories go beyond hypotheses

# Understanding and treating depression

Depression is a mood disorder—not just mere sadness or some kind of pessimism. There is extensive variation in the patterns and severity of symptoms that clinically depressed patients experience. People afflicted by major depressive episodes often feel tired, irritable, and distracted; their thoughts and affect turn negative; activities they once found fun don’t elicit the same level of joy or interest; their motivation to spend time with friends or family diminishes; and despair and hopelessness set in.

Approximately one in 20 adults (or 5%) worldwide experience a major depressive episode. Rates of clinical depression are rising steeply—especially amongst young adults in affluent countries. We know there are many causes of this disease, including social, psychological, and biological factors. People who have gone through traumatic events, for example, are more likely to develop depression. Disrupted sleep patterns, including disruptions caused by smartphone use, are a contributing factor to depression and other mood disorders. Obesity and depression can undergo feedback loops, where each condition makes the other condition worse. Dysfunctions in neuron growth and brain connectivity are salient in patients with clinical depression, too. And family and twin studies have highlighted various genetic factors associated with an increased risk of developing depression. These genetic, neurological, health, psychological, and social factors are among the known causes of this debilitating disorder.

Despite knowledge about some of the causal influences on depression, psychiatric understanding of depression remains limited. There’s no clear-cut way to diagnose depression. Standard definitions of depression in diagnostic manuals are qualitative, listing clusters of possible symptoms.

DOI: 10.4324/9781003300007-13
---
# Signs of depression

FIGURE 12.1 shows a high degree of comorbidity, which means that if a patient has depression, then that person is also likely to suffer from other conditions, such as anxiety, alcohol abuse, and bipolar disorder. Further, many of the associations that have been found between depression and genes, brain structures, and psychological and social events are weak or uncertain. These and other challenges mean that, currently, there is no general theory of depression—that is, no well‐established conception of what it is or account of how it unfolds.

The medical treatment of depression is also a mixed bag. Several treatments work in many—but not all—cases. A number of antidepressant drugs are commonly prescribed as treatment, but it can be difficult to find the best medication or combination of medications for a specific patient, and effectiveness may change over time. Psychotherapy, such as cognitive behavioral therapy, is often an effective non‐pharmacological approach to treating depression. But the efficacy of psychotherapy varies, and it’s unclear when any one therapeutic approach will be particularly promising in treating depression. Psychedelic compounds and deep‐brain electrical stimulation are sometimes used when medication and psychotherapy aren’t effective. They show some promise, but research into the safety and efficacy of these treatments is ongoing.

# Scientific theories

Chapter 1 discussed how science aims at the production of knowledge—an aim that is constitutive of the very meaning of the word science. We also saw that science aims to produce a distinctive kind of knowledge: scientific knowledge is explanatory.
---
# Explaining and theorizing

knowledge of why or how the natural world is the way it is. Scientists aren’t simply accumulating a list of confirmed hypotheses about our world and ourselves. The project is bolder: scientists are charged with helping us understand why, and how, things happen. Scientists are asked to furnish the tools for making sense of, predicting, and changing the world around us. To accomplish this, they develop scientific theories, which are comprehensive accounts of phenomena, broader and more explanatory than individual hypotheses and models, and backed by more evidence. In studying depression, psychiatric researchers have discovered a variety of explanatory factors bearing on the mental illness, as well as a variety of approaches to treating it. But, while there is now much more knowledge about incidence and causes of depression and effective treatments, psychiatry is still far from a satisfactory understanding of the mental illness.

Theories often go beyond what is readily observable. The Darwinian theory of evolution by natural selection is a grand theory about the origins of all the diverse lifeforms on Earth, and Einstein’s theory of relativity is a grand theory about the very nature of gravity, space, and time. Empirical evidence has been central to testing and confirming the content of these and other theories. But that content is more expansive than just what we’re led to expect to observe in some particular circumstance. Evolutionary theory, for example, indicates what happened from the earliest years of life on Earth, and the various hypotheses comprising it have been confirmed by a wide variety of forms of converging evidence, from extensive fossil records and geophysical data to features and relationships among current lifeforms. As we saw in Chapter 3, relativity theory was dramatically confirmed by the light deflection observed during an eclipse, but the theory also tells us what would happen if we traveled at the speed of light and gives us a reason to believe that nothing but light will ever travel that fast.

In ordinary language, the term theory is sometimes used to mean that some thought is only a guess or that it hasn’t been tested out. Scientific theories are not like that. Quite the opposite, scientific theories are major accomplishments, as both the Darwinian theory of evolution and Einstein’s theory of relativity illustrate. Yet, because scientific theories have implications that are not immediately observable, they are never taken to be true beyond all doubt, no matter how much empirical data supports them. Scientists couldn’t be more certain of the theories of evolution and relativity. Even so, it’s possible that someday one or another of these theories, or another theory among our prized scientific achievements, will be replaced by a better theory. This possibility is due to the open and self-correcting nature of science.

Just as scientific theories go beyond the readily observable, theories also come about not simply by generalizing from observations. Often, when a new theory is formed, this is from a significant conceptual shift—some feat of imagination—that gives rise to a new way of thinking about observations. Darwin wondered whether the similar forms of life he observed across continents might be evidence that they dispersed from some ancient common ancestor. And he was inspired by an economist, Thomas Richard Malthus, about the pressures to survive created by population increases. Einstein was inspired by the puzzle of how to set clocks that are far apart to the exact same time, and by how observers’ experiences vary depending on whether they are in motion, to reconsider the very nature of space and time. In both cases, extensive observations
---
Explaining and theorizing were subsequently obtained to empirically support the theories. But the initial idea was a kind of spark of insight, a different way of thinking about what we already know about the world.

 

# Box 12.1 Reductionism, integration, and complex systems

Historically, many scientists and philosophers of science have expected that appealing to the fundamental laws of physics will ultimately explain all the features of the world, even in biological organisms and societies. This view is called reductionism. The idea behind this is that everything in the universe is composed of physical matter (sometimes called physicalism) and so their features are all explained by the laws governing physical matter. But reductionism has fallen out of favor. Even if everything in the world is made of physical matter and subject to physical law, our scientific knowledge of physics isn’t likely to give us predictions and explanations of, say, how cognition works or how biological organisms have evolved. Over the past century or so, there have also been two trends in scientific research that seem to run counter to reductionism. First, many scientific questions have been productively explored by bringing together and integrating research from multiple fields. Our knowledge of depression, for example, is informed by research in neuroscience, molecular biology, cognitive science, and the social sciences. This pattern of integration contrasts with what we would expect if reductionism were true. Second, scientific research in several areas has productively advanced by recognizing patterns in behavior across systems with very different physical compositions. Complex systems research—across many fields of science and relying on a variety of methodologies, particularly from network theory and dynamical systems theory—productively explores how interactions shape phenomena and seeks patterns across very different types of systems.

# EXERCISES

# 12.1 Recall:

Summarize scientific knowledge about depression. Remember to consider what we know about its causes, its treatment, and related knowledge about human emotional regulation.

# 12.2 Think:

What might a theory of depression offer that goes beyond the current state of scientific knowledge about depression? Motivate your response by referencing features of theories described in this section.

# 12.3 Recall:

Define scientific theory and describe three primary features of scientific theories based on the discussion in this section.

# 12.4 Think:

Briefly summarize the theory of evolution, and describe how the theory of evolution exhibits the three primary features of scientific theories. (You may need to)
---
# 12.5 Recall:

What do scientific theories add to science, beyond the processes of hypothesis-testing we have mostly focused on in this book? How does theorizing relate to hypothesis-testing?

# 12.6 Apply:

Review the discussion of the Higgs boson discovery in Chapter 10. This discovery provided additional confirmation of the so-called standard model in physics. Investigate this theory, and then answer the following questions about it as best you can.

1. What is the theory a theory of—that is, what phenomena is it supposed to be about?
2. What are the central parts of the theory?
3. What kind of evidence has been used to support the theory?
4. Does the standard model make claims about things that we can’t directly observe? About what kinds of things?
5. What are some of the considerations that sparked the development of the theory?
6. Has the theory undergone any changes over time? What change(s) and why?

# 12.2 USING SCIENCE TO EXPLAIN

After reading this section, you should be able to:

- Describe the scientific goal of providing explanation and say why it is important
- Define the nomological, pattern‐based, and causal accounts of explanation
- List one advantage and two problems with each of these three accounts of explanation

# Scientific explanation

We said that scientific theories are important for producing explanatory knowledge. The explanatory knowledge produced in science is a special kind, explicitly supported by evidence through the use of methods discussed in this book. But there’s significant overlap between scientific and everyday forms of explanation, too. All of us sometimes notice things that cry out for explanation. We routinely ask questions like “Why did you kiss him?” “How much does exercise improve my health?” “Why did the economic crisis happen?” “How did the dinosaurs go extinct?” Even children regularly engage in this pursuit of explanatory knowledge.

Many children—and adults too—have wondered why the sky is blue. A parent might quickly answer that the sky is blue because it looks that way to us, or because that’s just the way the sky is. Such answers don’t explain why the sky is blue; they offer no insight into why or how the phenomenon is the way it is. A satisfying explanation of
---
Explaining and theorizing why the sky is blue relies on some sophisticated scientific theorizing: sunlight travels in straight lines unless some obstruction either reflects it, like a mirror; bends it, like a prism; or scatters it, like the molecules of gas in the Earth’s atmosphere. Because blue light has shorter wavelengths, it is scattered more than other colors in the spectrum. That’s why we normally see a blue sky. In contrast to most parents’ quick answers to this question, this explanation appeals to other facts about the world and scientific laws or theories to give a deeper understanding of the phenomenon.

Generating explanations plays important cognitive roles. As we discussed in Chapter 7 with abductive reasoning—also known as inference to the best explanation—explanatory considerations can be used as evidence in support of a hypothesis, making the hypothesis more credible. Generating explanations to oneself or to others also routinely facilitates the integration of new information into existing bodies of knowledge and can lead to deeper understanding; this is called the self-explanation effect. Performance on a variety of reasoning tasks can be improved when one is asked to explain. That’s why explaining ideas and responding to explanatory questions is such a good way to learn new material. And instructors and tutors learn material faster and with more depth of insight in virtue of explaining it to others.

Perhaps most important among its cognitive roles, explanation produces understanding. Understanding the world around and within us is a supreme achievement that is central to science. Understanding is a kind of insight, grasping why or how something came about or is the way it is. This makes it possible for us to intervene in the world and to anticipate what will happen next. When we understand how a system works—say, the tidal system of the San Francisco Bay, an example from Chapter 5—we can anticipate how changes in some features of the system (like the Reber plan) will lead to changes in some other features (tides, salinity, and so forth).

Because explanations generate understanding, they satisfy our curiosity. To satisfy our curiosity and have that experience of “Aha! Now I get it!” can feel really good. Psychologist Alison Gopnik once likened understanding to orgasm. Sex evolved to feel good because it leads to babies, which is needed for a species to continue. Similarly, Gopnik reasoned, understanding is enjoyable because explanations help people navigate their environment. And so, the desire to satisfy our curiosity has led humans to ever more sophisticated and accurate theories about our world.

The satisfaction of curiosity is no guarantee of a good explanation, though. Sometimes people have a sense that they understand something without genuinely understanding it—explanations can be wrong. People also can fall prey to an illusion of explanatory depth, believing they understand the world more clearly and in greater detail than they actually do. We all regularly overestimate our competence and depth of knowledge; recall our discussion in Chapter 1 of the cognitive errors, like confirmation bias, that science is designed to correct for.

An illustration of how one can be dangerously misled by the feeling they understand something is the public reception of climate change research. As you may recall, climate change was originally called “global warming.” But this terminology misled many people about what they should expect to experience. When a season was not
---
# Explaining and theorizing

warmer than usual in some location, some people were tempted to doubt the reality of climate change, for it seemed to them as if things weren’t getting warmer after all. But climate change does not produce warmer temperatures in every location at every point in time. Instead, it produces a global increase in average temperatures over time, as well as increasingly extreme weather—both hot and cold—and storms.

Another example of the illusion of explanatory depth concerns public reception of neuroscience. Experimental data suggest that people are often misled into judging bad psychological explanations as better than they really are when those bad explanations are accompanied by completely irrelevant neuroscience information. The allure of neuroscience information, which sounds technical and cites biological details, might interfere with people’s ability to critically evaluate the overall quality of an explanation. This interference can have negative practical effects when, for example, it is exploited by advertisements for “brain training” that promise cognitive enhancement. This is the opposite of the climate change case. Instead of scientific expertise being disregarded because of personal experience, scientific credibility is misapplied to get people to believe something there’s not actually sufficient evidence for.

Given the centrality of explanation to science and the potential for all people, including scientists, to feel like they understand something even when they do not, it’s an important task to clarify the nature of scientific explanation. If we can say what features good explanations must have, then we will be better able to judge whether something counts as an adequate explanation.

Philosophers of science have thought long and hard about what features scientific explanations should have. Some have suggested that explanations should cite laws of

# Oklahoma Senator James Inhofe denying the climate crisis in the US Congress

FIGURE 12.2 while brandishing a snowball (February 26, 2015)
---
# 298   Explaining and theorizing

nature in order to account for phenomena. Another idea is that explanations should show how phenomena fit into patterns. Still others have suggested that explaining is a kind of causal reasoning, and that explanations should state what causes a phenomenon.

 

# Explaining with laws and patterns

The idea of successful explanations appealing to scientific laws is at the heart of the nomological account of explanation (from the Greek nomos, meaning law). According to this view, phenomena are explained only when explanations reference laws that can account for them.

The nomological account of explanation was developed most fully by the philosopher of science Carl Hempel. Hempel proposed that explanations are logical arguments that appeal to general scientific laws to derive statements about the occurrence of the phenomena we want to explain. Hempel thought that some nomological explanations were valid deductive arguments, while others were strong inductive arguments. In either case, the premises must include at least one scientific law, which enables us to derive the phenomenon we want to explain. Hempel believed that knowing the scientific laws and background conditions that guarantee or make very likely the occurrence of the phenomenon would lead people to realize the phenomenon in question was to be expected. By rendering phenomena expectable, scientific explanations reveal our world to be ordered, proceeding in accordance with general laws.

Many scientific explanations fit this nomological account of explanation. Consider how scientists might explain the increase in the average global temperature of Earth’s atmosphere. Energy from stars that reaches a planet is reflected off planetary surfaces. Greenhouse gases—carbon dioxide, water vapor, methane, and others—have molecular structures that absorb energy and then release it. Greater concentration of greenhouse gases in an atmosphere thus leads to increased temperature at the surface of a planet. These are law-like generalizations that describe these regularities in nature. Next, note that the concentration of greenhouse gases in Earth’s atmosphere has increased. This is a background condition, a fact about current circumstances here on Earth. Together, these claims deductively imply the conclusion that the Earth’s average temperature has increased. This argument is deductively valid with all true premises, yielding a simple nomological explanation of global warming.

# Box 12.2   Scientific laws

Historically, many scientists have taken the purpose of science to be discovering laws of nature, which can in turn be used to provide explanations and make predictions. Examples include Newton’s law of universal gravitation in physics; the three laws of thermodynamics, central to physics and chemistry; and the laws of supply and demand in economics. A scientific law can be thought of as a set of rules for inferring what must follow from some set of conditions.
---
# Explaining and theorizing

The law of supply, for example, is a way to infer the relative price of goods from the quantity of goods supplied. Newton’s law of universal gravitation is a way to infer the force between two bodies based on their masses and the distance between them. And yet, many useful scientific insights do not provide exceptionless rules for how things must occur. Indeed, the law of supply in economics is at best an approximation for how supply influences price. Even Newton’s law of universal gravitation fails to take into account the influence of other forces, such as magnetic charge. Further, many scientific advances do not even attempt to capture laws of nature at all. Philosophers of science thus debate what is required for something to count as a law, as well as the extent to which scientific inquiry involves discovering laws as opposed to, say, causal mechanisms.

Just as phenomena can be explained by laws, scientific laws themselves can be explained by appealing to other, more comprehensive laws. For example, consider Galileo’s law that bodies fall toward Earth at a constant acceleration. This law can be deductively derived from the Newtonian law of gravitation. The Newtonian force of gravity explains the constant acceleration of bodies falling toward Earth. Newtonian laws, in turn, can be explained by appealing to the more comprehensive general theory of relativity developed by Einstein. The Earth’s gravity is explained as a distortion of space caused by the Earth’s mass. Objects speed up as they fall toward Earth, just as a ball rolling from the edge to the center of a bowl speeds up.

The idea of explaining scientific laws with reference to other, more general laws introduces a second account of explanation. According to the pattern account, explanations fit particular facts into a more general framework of laws and principles. This also has been called a unification account of explanation, since the number of assumptions required to explain phenomena decreases when an explanation is provided. Descriptions of phenomena, and scientific laws as well, are unified by uncovering the basic patterns that govern them.

Although we previously gave a nomological explanation of global warming, this can also be construed as a pattern explanation. The phenomenon of anthropogenic global warming on Earth due to human activities is explained as one instance of a general pattern of atmospheric effects on planetary climate, a pattern that also includes Earth before human activity drastically increased greenhouse gas concentration in the atmosphere and other planets with different atmospheres entirely.

One advantage of the pattern account over the nomological account is that it doesn’t require scientific explanations to cite laws. Pattern explanations can cite regularities that may not qualify as laws. In place of the law requirement, there’s an emphasis on descriptions that fit the phenomenon to be explained into a wider pattern, to see the phenomenon as one instance of a more general regularity. Our earlier discussion of depression illustrates the advantage of this. Scientific knowledge of depression is not developed enough to provide scientific laws that convey the relations between.
---
300 Explaining and theorizing properties of this disorder and that govern the occurrence of depression or effectiveness of treatments. Indeed, the phenomenon of depression may not be governed by general laws at all. But there are still descriptions of patterns that can be explanatory.

For example, to explain why selective serotonin reuptake inhibitors (or SSRIs), the most commonly prescribed category of depression medication, are effective, one can point out that low serotonin levels are associated with depression, and taking SSRIs increases serotonin concentration in the brain by blocking its reabsorption by neurons. There is no law that decreasing serotonin leads to depression or that increasing it will effectively treat depression. But there is a broad pattern between serotonin levels and depression that this explanation, and the treatment itself, rely upon.

Another example comes from evolutionary theory, which explains many facts about the traits of organisms and the relationships among them with reference to a simple pattern that plays out in a multitude of ways. The pattern at the heart of evolutionary theory is that natural selection acts on variation among organisms to produce cumulative change in species. The theory of evolution is not a single general law of nature. It recognizes many different influences on evolution and that evolution proceeds in different ways depending on several factors. Evolutionary explanations are thus not productively construed as nomological explanations. But they do conform to the pattern account rather well.

The idea behind the nomological and pattern accounts of explanation—that explanations make phenomena less surprising by referencing laws or by showing how they fit into a wider pattern—captures important features of many scientific explanations. But both also face significant objections.

We’ve already encountered one problem with the nomological account: many good explanations don’t appeal to any scientific laws. We saw this with evolutionary explanations and with the example of explaining why SSRIs treat depression.

The pattern account faces a related difficulty. It focuses on explanations that show how to fit a phenomenon into a wider pattern, but some explanations are highly specific. Consider the explanation for humans’ large brains. As early hominids (ancestral humans) faced environmental changes and developed more complex social exchanges, this led to the selection for and eventual evolution of increasingly large and complex brains, eventually tripling human brain size from its ancestral size. Brain size increased especially rapidly between about 800,000 and 200,000 years ago. This explanation is compelling, and there’s significant evidence backing it up. But it is also highly specific. It appeals to the general pattern of evolutionary theory, again, selection acting on variation to produce cumulative change; but much of the explanation is highly specific to humans' unique evolutionary past.

A second problem for both nomological and pattern accounts is that they neglect a key feature of explanation: asymmetry. If one thing explains another, then this explanatory relation does not usually hold in reverse. Consider the following example. Your mobile phone sends you a weather alert, and you explain this with reference to the fact that a storm is approaching and the generalization that weather alerts are sent out when storms are approaching. But, it seems, this explanation doesn’t work in reverse. You can’t explain the approaching storm by citing the weather alert you received and
---
# Explaining and theorizing

 

  

# Evolution of human brain size

The generalization that weather alerts are sent out when storms are approaching. This mixes things up: the storm isn’t approaching because you received the weather alert. The weather alert gives you evidence of the storm, but it isn’t an explanation for why the storm is happening.

But the nomological and pattern accounts of explanation don’t illuminate this asymmetry. According to the requirements for explanation on those views, a generalization about weather alerts being sent out when storms approaching and the background condition of receiving a weather alert should explain the storm occurring! This seems strange to say the least. An approaching storm can be a good explanation for why you receive a weather alert, but the weather alert is no explanation for why the storm is approaching. You can do a lot with your mobile phone, but you can’t usually bring about a storm.

# Causal explanation

Another account of explanation is inspired by this asymmetry of explanation that the nomological and pattern accounts fail to illuminate. According to the causal account of explanation, explanations appeal to causes that bring about the phenomenon to be explained. On this view, appealing to the approaching storm explains the weather alert on your phone because the storm causes weather alerts to be sent out. But, as we just...
---
# 302 Explaining and theorizing

noted, your phone’s weather alert doesn’t cause the storm—so on the causal account of explanation, it doesn’t explain the storm either.

The causal account seems to apply well to many explanations in science, including in fields that have not developed scientific laws. As we emphasized in Chapter 11, knowledge of causes enables prediction and manipulation of phenomena, via intervention on causal factors. It’s plausible that identifying causal factors is also central to explanation.

In one variety of causal explanation, the focus concerns how causal factors regularly combine into systems that produce the target phenomenon. Some call this variety of explanation mechanistic. The search for causal mechanisms seems to play an especially important role in some parts of the social and life sciences. For example, the scientific explanation of an organism’s regulation of blood sugar appeals to how pancreatic endocrine hormones maintain blood sugar within a range of about 70–110 mg per 100 ml blood. If glucose (blood sugar) decreases below this range, pancreatic alpha cells secrete glucagon, which causes the liver to release stored glucose. If blood sugar increases above the range, pancreatic beta cells secrete insulin, which causes adipose tissue to absorb glucose from the blood. This explanation is also part of the explanation of diabetes, which is a disorder characterized by the pancreas producing insufficient amounts of insulin. This explanation displays how an interrelationship among pancreatic hormones, liver tissue, and blood sugar ordinarily work together in a complex way to maintain blood sugar levels within a narrow range.

We’ve seen that the causal account of explanation accommodates the asymmetry of explanation. It can also address the other concern raised earlier with the nomological and pattern accounts of explanation, that not all explanations seem to feature scientific laws or to describe broad patterns. Some causal relationships follow very general patterns, or are law-like in nature, but others are not. If you heat ice, it will melt or evaporate. There are virtually no exceptions to this. If you heat chocolate, it will usually melt—but if you heat it too quickly, it gets thick and lumpy instead. This is a general pattern, but it has some exceptions. In contrast, perhaps the evolution of large brains will only happen once in history. Perhaps background conditions had to be just right for such a trait to evolve. But all of these, from the law-like to the highly particular, are still cause-effect relationships. And on the causal account, all are successful explanations.

However, the causal account of explanation faces its own difficulties. First, just as it seems some explanations may not cite laws or patterns, it also seems that other explanations don’t cite causes. For example, we said previously that Einstein’s general theory of relativity explains why Newtonian law of gravitation holds, which in turn explains Galileo’s law of constant acceleration. But it would be strange to say that general relativity causes the Newtonian law of gravitation, or that the law of gravitation causes constant acceleration. A related concern is that, if it is right that general patterns and scientific laws can help us understand the world, at least sometimes, then the causal account of explanation is lacking because it doesn’t identify that explanatory value.

A second difficulty with the causal account of explanation stems from the observation that many phenomena have many causes. For this reason, causal explanations may come too easily. Causal explanations may cite only one or a few causal influences, when
---
# Explaining and theorizing

we know there are many causal infl uences on the phenomenon that’s explained. How is this enough to explain the phenomenon? Some respond to this challenge by saying that the more causal information you can give, the better explanation you have. Others seek another principle to decide what causal information belongs in an explanation.

Yet another difficulty is that, as discussed in Chapter 11, there are different conceptions of what causation is, but an account of causal explanation requires a successful definition of causation.

So far, we have talked about these three accounts of explanation as if one is right and the others wrong. But it’s possible that each account captures certain elements of what helps us understand the world. One initial reason to think this might be so is that each of these accounts of explanation aptly characterize some, but not all, of the examples of successful explanation we have discussed. Perhaps laws, patterns, and causes all can contribute to our understanding, and so any of these can be an ingredient of explanation, even if none is involved in every single explanation in science.

# EXERCISES

1. Recall: What are three ways explanation is useful for our thinking? How are these valuable to science?
2. Think: In your own words, describe why explanation is important to science.
3. Recall: Define illusion of explanatory depth. Why is this risky in science?
4. Recall: Define the nomological, pattern-based, and causal accounts of explanation. List one advantage and two problems with each of these three accounts of explanation.
5. Apply: Choose one account of explanation: nomological, pattern, or causal. Find a novel example of a scientific explanation that seems to conform to the account you chose. Describe the example, making clear how it succeeds as an explanation. Then describe why this example should be seen as conforming to the account of explanation you chose.
6. Think: Construct a chart or table listing the strengths and weaknesses of each of the three accounts of explanation discussed in this section. Decide which account(s) of explanation is the most promising, and support your answer with an argument.

# 12.3 SCIENTIFIC BREAKTHROUGHS AND THEORY CHANGE

After reading this section, you should be able to:

- Define and give an example of a scientific breakthrough
- Outline Kuhn’s view of the four stages of science
- Describe how the discovery of oxygen led to changes to the field of chemistry
---
# Explaining and theorizing

# Scientific breakthroughs

We said in section 12.1 that, when a new theory is formed, this sometimes involves a significant conceptual shift or feat of imagination that gives rise to new ways of thinking about observations. No scientific theory is accepted beyond any doubt, and theories are sometimes replaced by successors. The differences between a theory and its successor can be minor, while in other cases there is a radical shift. The most significant scientific breakthroughs, when there has been a radical shift in theory in some field of science, have been changes in worldview: they involve comprehensive revision to how background assumptions, data, and ideas are combined, and thus to which scientific theory is supported.

Consider again theories of our universe and the bodies within it. The worldview that arose with Aristotle had great scope and logical coherence. The Aristotelian theory of falling bodies claims that heavy bodies fall faster than light ones, and its geocentric conception of the universe placed Earth at the center, which fits with most common observations of how the world is. But, over time, observations were made that the Aristotelian worldview couldn’t easily accommodate. Eventually it was replaced by a Copernican, and then Newtonian, conception of the universe, with the Earth not a fixed center, but a planet in motion around the Sun.

Because of the dramatic change in worldview, astronomers from the 4th century BCE and the 17th century would have agreed about the positions of the stars in the sky, but they would have radically different interpretations of those observations. Similar observations provided clues to constructing the theories, but the differences between those theories were vast. This is the Scientific Revolution of the 16th and 17th centuries, discussed also in Chapter 2.

Additional radical shifts followed on the heels of the rejection of the Aristotelean worldview, and with these changes came radical revisions to accepted ideas about the position and movement of Earth, the shape of orbits, and the nature of universal forces. In general, each new theory accounted for some body of evidence better than its predecessor. Still, most of the changes were rather radical changes in perspective. The same is true of the later replacement of Newtonian mechanics with Einstein’s theory of relativity, when universal forces were replaced by non-Euclidean geometries of space-time.

Scientific breakthroughs have occurred in other fields of science as well. This is as you’d expect if scientists are genuinely open to revising or replacing any theory when doing so is warranted by the evidence. And breakthroughs seem rewarding and significant: there’s a sense that, after a scientific breakthrough, we more clearly understand our world. An initial spark of insight leads to a conceptual shift or feat of imagination that results in reinterpreting existing data to support a new theory, and then more data are discovered that confirm this new theory.

From another perspective, though, the idea of scientific breakthroughs is also troubling. What happened to our scientific knowledge from before the breakthrough—were scientists just wrong? How do we know that our current best theories won’t suffer the same fate and also be rejected for new and better theories? Can we trust our current scientific theories at all, then? These are deep and troubling questions that strike right.
---
# Explaining and theorizing

at the heart of science. But let’s postpone that discussion until later in this chapter, after we have a fuller picture of what scientific breakthroughs are like, and how and why they occur.

 

# Kuhn’s scientific revolutions

The series of scientific breakthroughs in the 17th century just described suggests we might think about scientific breakthroughs in terms of revolution. Revolutions are pretty dramatic; think of political revolutions like the French revolution at the end of the 18th century, the fall of the Soviet Union two hundred years later, or the Arab Spring in the early 2010s. A scientific revolution is a radical change of a reigning theory being overturned or abandoned in favor of a new theory, often involving an alternative worldview. Scientific revolutions don’t just change which scientific theories are accepted; they also influence the trajectory of science itself, including how to interpret evidence, which scientific procedures are accepted, and often the social and institutional structure of science, such as who is accepted as a scientific authority.

The sociologist, historian, and philosopher Thomas Kuhn wrote a famous book, The Structure of Scientific Revolutions, first published in 1962. In this book, Kuhn advanced an influential model of scientific change based on the notion of revolution. He suggested that scientific revolutions have occurred and will continue to occur periodically as an important part of science. In his view, this prevents science from proceeding in a straight line by accumulating an increasing body of knowledge and an expanding store of explanations. Kuhn argued that science instead proceeds in phases.

Kuhn called the earliest phase of science pre-paradigm. This is characterized by the existence of different schools of thought that debate very basic assumptions, including research methods and the nature and significance of data. Data collection is unsystematic, and it’s easy for theories to accommodate new observations because the theories are inchoate, or undeveloped. Such theories can easily be adapted in different ways to accommodate new observations. There are many puzzles and problems but not very many solutions.

Kuhn’s second phase is the normalization of scientific research. One school of thought begins to solve puzzles and problems in ways that seems successful enough to draw adherents away from other approaches. Kuhn called this period normal science, because scientific researchers’ widespread agreement about basic assumptions allows the research to become stable. Scientific practices become organized. Laboratories or other workspaces may be set up, research techniques and methods become widely accepted, and agreed-upon measurement devices are improved.

During normal science, scientific developments are driven by adherence to what Kuhn called a paradigm. Broadly conceived, a paradigm is just a way of practicing science. It supplies scientists with a stock of concepts, symbols, and assumptions about the world that they can use to communicate more effectively. A paradigm also involves methods for gathering and analyzing data, as well as habits of scientific research and reasoning more generally. For example, in 20th-century psychology and psychiatry, the behaviorist overthrow of the introspectionist and psychoanalytic paradigms weren’t
---
# 306 Explaining and theorizing

just a change in theory; rather, this ushered in new experimental tools, methods of operant conditioning, and ways of thinking about how to perform science. A paradigm stems from elements of the reigning school of thought, a risky conjecture that has been sufficiently confirmed by evidence to be taken on board and developed into a scientific theory.

Kuhn thought that, during a period of normal science, each field of science is governed by a single paradigm. But, scientists in the grip of some paradigm have often ended up with observations that are at odds with it, or that lead to worrying puzzles called anomalies: deviations from expectations that resist explanation by the reigning theory. Usually, anomalies are just noted and set aside for future research. But anomalies can accumulate, and this creates a kind of increasing tension for the accepted scientific theory. Some scientists begin to worry that the theory might not be right after all.

The accumulation of anomalies sets science up for a crisis. A crisis occurs when scientists finally lose confidence in the reigning theory in the face of mounting anomalies. For Kuhn, a paradigm is only rejected if a critical mass of anomalies has led to crisis and there’s also a rival paradigm to replace it. Another theory has been developed by some renegade scientists, and the problems with the existing paradigm mean that this new theory—together with its background assumptions, methods, and so forth—can finally get attention. If this is so, a crisis might be followed by a scientific revolution.

In this phase of science, all the elements of the accepted paradigm are up for negotiation. Data, interpretations of data, background assumptions, methods and technical apparatus, and so on—any and all might be rejected, replaced, or reinterpreted from the perspective of the new paradigm. This four-stage view of scientific change is summarized in Table 12.1.

# The chemical revolution

The Scientific Revolution began when geocentrism was replaced with heliocentrism in astronomy: the Earth was no longer seen as the central heavenly body but instead taken to revolve around the Sun. According to Kuhn, this perfectly fit his ideal description of Kuhn’s four stage account of scientific change.

**Kuhn’s four stage account of scientific change**
|Stage|Features|
|---|---|
|1. Pre-paradigmatic science|Different schools of thought debate basic assumptions|
|2. Normal science|A paradigm is accepted, and efforts are devoted to basic research and puzzle-solving|
|3. Crisis|Scientists lose confidence in the dominant paradigm upon the accumulation of anomalies|
|4. Revolution|The old paradigm is rejected in favor of a new one|

---
# Explaining and theorizing

scientific revolution. Another abrupt revolutionary change in science that Kuhn recognized as a scientific revolution involved sweeping changes in the field of chemistry in the 18th century. Two of the protagonists of this scientific revolution were the chemists Antoine-Laurent and Marie-Anne Paulze Lavoisier. When they began their work, scientific understanding of matter and its transformations was still grounded in the Aristotelian worldview. Aristotle had believed that all earthly materials are composed of the elements air, earth, fire, and water. This theory of the four elements had been slowly modified by the medieval alchemists, who aimed to turn base metals into gold and to produce an elixir of immortality. By the 18th century, alchemists believed all things were compounds of sulfur, mercury, and salt.

In the early 18th century, one pressing scientific question was: what happens when something burns? Alchemists thought that materials lose sulfur when they change into slag, rust, or ash by heating. The physician and chemist Georg Ernst Stahl modified this idea, developing the theory that every combustible material contains a universal fire-like substance, which he named phlogiston (from Greek, meaning flammable). Combustible materials like wood tend to lose weight when burned, and Stahl explained this change in terms of the release of phlogiston from the combustible material to the air. When the air becomes saturated with phlogiston or when a combustible material releases all its phlogiston, the burning stops. Stahl believed that the residual substance left behind after a metal burns is the true substance of the original metal, which lost its phlogiston during combustion. This residue, which was called “metal calx” (what we would now call an oxide), has the form of a fine powder. Both metal calx and the gases produced during combustion could be captured, measured, and experimentally manipulated.

Unlike gases and calx, though, phlogiston was an utter mystery. Nobody had isolated it, and nobody had found a way to manipulate it experimentally. In fact, phlogiston seemed to have properties that were inconsistent with Stahl’s theory. Stahl believed phlogiston had a positive weight. When you burn a piece of wood, the remaining ash loses phlogiston, and it weighs less than the original log. But in other cases, for example, when magnesium or phosphorus burn, the residue left behind weighs more than the original material. If phlogiston is released during the burning process, why was there a gain in weight in these cases?

Intrigued by this anomaly, the Lavoisiers experimented with various metals and gases to investigate why and how things burn. They observed that lead calx releases air when it is heated. This suggested that combustion and air were, somehow, linked. Explaining the link was a difficult task, however, because at that time little was known about the composition and chemistry of air. Meeting Joseph Priestley helped. Priestley had discovered a gas he called “dephlogisticated air,” which was released by heated mercury calx. This gas was thought to greatly facilitate combustion because, being free from phlogiston, it could absorb a greater amount of the phlogiston released by burning materials. Candles burning in a container with “dephlogisticated air” would burn for much longer, for example. This gas, Priestley observed, facilitated respiration too: mice in containers with dephlogisticated air lived longer than mice placed in containers without this gas.
---
# Explaining and theorizing

A depiction of one of the Lavoisiers’ experiments from the late 18th century

FIGURE 12.4

The Lavoisiers tried to replicate Priestley’s experiments; and, based on their own results and observations, they elaborated a new theory of combustion. The central idea was that combustion was the reaction of a metal or other material with the “eminently respirable” part of air. Believing (incorrectly) that this kind of air was necessary to form all sour‐tasting substances, or acids, Lavoisier called it oxygène, from the Greek words for acid generator. According to this new theory, combustion did not involve the removal of phlogiston from the burning material but, rather, the addition of oxygen.

This emerging rival paradigm set the basis for the revolution from which modern chemistry emerged. In the 1780s, the Lavoisiers and other scientists adopted the idea of a chemical element, and of chemical compositions of simpler elements. This new system of chemistry was set out by Antoine‐Laurent Lavoisier in a textbook in 1789. This book didn’t just describe the theory, but also explained the effects of heat on chemical reactions, the nature of gases, and how acids and bases react to form salts. It also described the technological instruments used to perform chemical experiments. And it contains a “Table of Simple Substances”—the first modern listing of chemical elements.

After the publication of this textbook, most young chemists adopted Lavoisier’s theory and abandoned phlogiston. “All young chemists,” he wrote in 1791, “adopt the theory, and from that I conclude that the revolution in chemistry has come to pass.” From a Kuhnian perspective, the next phase of normal science had begun.
---
# EXERCISES

# 12.13 Recall:

Define scientific breakthrough and give an example.

# 12.14 Think:

How are scientific breakthroughs valuable for scientific knowledge? How are they challenging for scientific knowledge?

# 12.15 Recall:

Describe the features of each of Kuhn’s four stages of science: pre-paradigm science, normal science, crisis, and scientific revolution. Illustrate each stage by describing how it applies to the chemical revolution.

# 12.16 Recall:

The case of phlogiston presented an anomaly for Stahl’s theory. How so? Describe the extensive changes that the discovery of oxygen led to for the field of chemistry.

# 12.17 Apply:

The advent and rapid development of computers was a major technological advance. Given your background knowledge, would you describe the development of computers as a Kuhnian revolution? Why or why not?

# 12.4 SCIENTIFIC PROGRESS AND THE SECURITY OF SCIENTIFIC KNOWLEDGE

After reading this section, you should be able to:

- Give two examples of incremental theory change in science and describe their differences from Kuhnian paradigm shifts
- Identify two challenges for scientific knowledge from scientific breakthroughs and at least one response to each challenge
- Describe three reasons to think scientific knowledge is safe, regardless of the possibility of radical theory change

# Incremental theory change

Kuhn’s notion of scientific revolution seems to accurately characterize some episodes in the history of science—the times of especially radical transformation in accepted scientific knowledge. But, this is a particularly extreme form of scientific change. Most other episodes of scientific change seem to be less dramatic, and there’s also a question about whether ordinary scientific activity fits Kuhn’s characterization of normal science.

Incremental changes in science are more common and less abrupt than Kuhn’s account suggests. Consider, for example, the Darwinian revolution in the 19th century. Darwin’s theory of evolution has had a dramatic and lasting impact on our understanding of the nature of lifeforms, the relationships among different species, and how species have changed over time, and—like the change from geocentrism to heliocentrism—the establishment of Darwinian theory was arguably a scientific revolution if anything is. But Darwin did not produce the first evolutionary theory, nor has evolutionary theory...
---
310   Explaining and theorizing remained entirely the same as what Darwin first described. Changes in the field of biology, both before and after Darwin’s revolutionary breakthrough, have been more gradual than a Kuhnian paradigm shift.

The general idea of evolution is that whole species—not just individuals—can change over time, and this idea is many centuries old. The nature of biological change as a scientific research program can be traced to the work of several naturalists over 50 years before the publication of Darwin’s *Origin of Species* in 1859. Even Darwin’s specific ideas about evolution were significantly influenced by other scientific work; we’ve already mentioned the influence of the political economist Thomas Richard Malthus. And another scientist working at the same time as Darwin, Alfred Russel Wallace, was independently developing a theory of evolution by natural selection strikingly similar to Darwin’s. So, although Darwin’s ideas were a tremendous breakthrough, they built upon existing scientific work, and they were inspired by and related to concurrent scientific work by others.

Furthermore, the science of biology since the Darwinian revolution has not simply consisted in the application of Darwin’s ideas, as Kuhn would have us expect for a period of normal science. Rather, our understanding of evolution has been in continual development. The so-called modern synthesis in the early 20th century integrated the existing knowledge of genetics and Darwinian evolutionary theory, which had previously been construed as competing theories. Other elements of evolutionary theory have been revised since, like the recognition of nongenetic influences on traits and how significantly organisms shape their environment.

Another point in support of incremental rather than revolutionary scientific change is that theory change doesn’t always involve the rejection of existing theories. Sometimes it comes from the joining of theories, as in the modern synthesis just mentioned, and other times it can come from new methods. Biologist James Watson and physicist Francis Crick, for example, reached their groundbreaking conclusion that the DNA molecule exists in the form of a double helix by applying a new modeling approach to data gathered by Rosalind Franklin. Using cardboard cutouts to represent the chemical components of DNA, Watson and Crick tried to make different arrangements, as though they were solving a jigsaw puzzle. Through this concrete model-building, the double helix structure of DNA was identified. This had enormous consequences for subsequent biological research.

Nonscientific pursuits, such as mathematics and philosophy, can drive scientific theory change too. The development of a new kind of geometry—non-Euclidean Riemannian geometry—paved the way for Einstein’s theory of relativity. Einstein’s theory adopted this purely mathematical geometry as a description of physical space-time. One basic difference between Euclidean and non-Euclidean geometry concerns the nature of parallel lines. In Euclidean geometry, there’s only one line through a given point that is parallel to another line. In some non-Euclidean geometries, there are infinitely many lines through a point that are parallel to another line and, in others, there are no parallel lines. This development in mathematics made it possible for Einstein to wonder whether the geometry of our own universe might be non-Euclidean. Around this same time, the development of new logical systems of predication, quantification,
---
# Explaining and theorizing

and operators helped move far beyond the syllogistic logic that had dominated for the past two millennia. These developments in turn affected, and were affected by, these upheavals in mathematics and led to the generation of set theory, mathematical logic, and computer science.

 

In summary, scientific theories undoubtedly change. But these changes may be influenced by changes in method, data, mathematics, or other relevant ideas or practices.

  

And the changes tend to be incremental and cumulative more often than radical and transformative.

# Box 12.3 Merton’s priority rule

According to sociologist of science Robert Merton, the first scientist making a novel discovery is rewarded with prestige and recognition. The second discoverers, runners-up, get nothing. Priority in discovery matters for patents and copyrights in applied science. It also matters more generally for recognition and prestige, which are the common currencies of scientific credit. Prestige in science comes in different forms. It can include promotion, prizes like the Fields Medal or Nobel Prize, and eponymy—that is, having a discovery named after oneself, like Parkinson’s disease. If the first scientist to publish a new discovery receives recognition and the seconds get nothing, then priority is a strong motivator for scientists, which then shapes the reward structure of their field. Scientists often worry about their work being scooped, and priority disputes occur regularly in science. Famous cases include Isaac Newton versus Gottfried Leibniz over the invention of calculus, Charles Darwin versus Alfred Wallace over the discovery of natural selection and evolution, and more recently, researchers at MIT versus UC Berkeley over the discovery of CRISPR-Cas9, a very significant genome-editing technology.

# Scientific progress

Earlier, we raised worries about how scientific breakthroughs may undermine our confidence in scientific theories. If some theories that were seemingly well supported by evidence are eventually rejected, who’s to say our current theories won’t also be rejected? And do such scientific breakthroughs make it so that science isn’t really making progress at all? Let’s consider these questions in a bit more depth and isolate a few important considerations.

When scientific theories change, do we have reason to think that the new theory is an improvement on the last one and that science is progressing towards truth? This question is complicated by two features of theories and theory change. First, theories often appeal to phenomena that cannot be directly observed. Examples of this we have encountered in this book include the Higgs boson, the first moments of the universe’s existence after the Big Bang, and the original common ancestor of all life on Earth.
---
# 312 Explaining and theorizing

How can we ever be sure we are right about these and other phenomena like them? Second, at least some instances of theory change have been radical: scientists eventually rejected phlogiston, decided they were wrong about the placement of Earth in the universe, and learned that psychiatric conditions such as depression are not imbalances of bodily humors. How can we ever be sure that our scientific findings are on a path to truth, when the next radical revision could be right around the corner?

There’s at least one influential argument suggesting that, despite all this, we have reason to believe that our best mature scientific theories are approximately true. This argument is an abductive inference, or inference to the best explanation, from the success of science. It begins with the observation that our best scientific theories are extraordinarily successful: they enable scientists to make empirical predictions, to explain phenomena, to design and build powerful technologies. What could explain this success? One possible explanation is that our best scientific theories are approximately true. If these theories were not approximately true, then the fact that they are so successful would be astonishing. So, it seems, the best explanation for the success of science is that our best theories are true—or, at least on the path to true and getting closer. This is sometimes called the no miracles argument, suggesting that all of the scientific successes we know about would be utterly mysterious—that is, would have no explanation—unless scientific theories are approximately true.

Yet, some believe that this conclusion is overly optimistic. Here’s an inductive argument for the opposite conclusion. If we examine the history of scientific theories in any given field, we find plenty examples of older and successful theories rejected in favor of newer, more successful theories. So, most past theories, which were also predictively successful and empirically adequate, turned out to be false. Therefore, by generalizing from these cases, our current scientific theories are likely to be false as well, standing a good chance of eventually being replaced themselves by new theories. This is sometimes called the pessimistic meta-induction, since it draws a pessimistic conclusion about the eventual fate of today’s scientific theories based on inductive reasoning from the rejection of many past scientific theories. The upshot of this argument is that we do not have a strong reason to think our current best scientific theories are approximately true.

# Why scientific knowledge is safe

The pessimistic meta-induction raises important questions about how certain we can be about our current scientific theories. What it doesn’t do is undermine the fact that science is the single most successful project of generating knowledge that humans have ever embarked on. There are reasons to think scientific knowledge is trustworthy and safe, even if we can’t be certain that our current scientific theories are the final say on how the world is.

First, consider the point we made earlier about incremental theory change. Some theoretical breakthroughs may resemble Kuhnian paradigm shifts, but many more developments in scientific theory are small and incremental, suggesting that previous successes may persist—and be further built upon—as scientific theories advance.
---
# Explaining and theorizing

seems so for the development of both psychiatry theories of depression and evolutionary theory. And, even when new research has shown limitations in earlier theories, often the abilities and insights based on those theories persist. Sometimes, it’s even the case that scientists return to earlier, rejected theories for inspiration when current theoretical frameworks come up short. For example, recall from Chapter 2 how limitations of the germ theory of disease inspired a restored focus in public health to social determinates of disease.

Second, scientific theories are only one part of the overall scientific endeavor. Even if some of the theoretical claims at the heart of a scientific theory are eventually shown to be wrong or only approximately true, that can leave intact the value of many ideas, observations, and technological advances associated with the theory. Those ideas, observations, and advances qualify as factors in the production of scientific knowledge in their own right. For example, although phlogiston is no longer posited as a chemical created from combustion, the observable features of combustion that motivated phlogiston theory, such as the residues produced and their volumes, are still counted as part of our body of knowledge of combustion.

Third, scientific knowledge is safe despite the possibility of future breakthroughs because science is not just a collection of theories. At its heart, science is a collection of methods, a set of recipes for investigating our world featuring common ingredients—most prominently, hypotheses, expectations, and observations. Parts of these recipes, like empirical observation and attempts to explain, are common to people of all ages all around the world. Other parts, like experimentation and mathematical tools, have developed in several cultures at different times. And some aspects, like a social institution balancing trust and skepticism, developed with contemporary institutionalized science. This set of recipes for science has persisted and been improved through continual refinement for centuries. It will continue to evolve, but it is unlikely ever to be supplanted, even if individual scientific theories are sometimes abandoned. Over the long arc of history societies have much to gain, and little to lose, by relying on the best science of their day.

# EXERCISES

1. Recall: Describe why Darwinian evolutionary theory is better seen as incremental theory change. How does this instance of theory change differ from Kuhnian paradigm shifts? Watch Video 16
2. Recall: Define the no miracles argument and the pessimistic meta-induction. Explicitly state the conclusion of each argument.
3. Think: Consider again the no miracles argument and the pessimistic meta-induction. Assess each argument, one at a time, writing at least one paragraph evaluating each. Then, for each, say whether you are ultimately convinced of its conclusion.
4. Think: How does the existence of scientific breakthroughs, or revolutions, challenge the ideas of scientific truth and scientific progress? Motivate the concern.
---
# 12.22 Recall:

Describe three reasons to think scientific knowledge is safe, regardless of the possibility of radical theory change.

# 12.23 Think:

How convinced are you by these three reasons to think scientific knowledge is safe? Why? Can you think of additional grounds for trusting scientific knowledge? What lingering concerns, if any, do you still have about science’s trustworthiness?

# FURTHER READINGS

For more on depression and psychiatry, see these volumes in Oxford’s very short introduction series:

- Scott, J., & Tacchi, M. J. (2017). *Depression*. Oxford University Press.
- Burns, T. (2018). *Psychiatry*. Oxford University Press.

For an introduction to scientific explanation, see McCain, K. (2022). *Understanding how science explains the world*. Cambridge University Press.

For Kuhn’s view of scientific revolutions, see Kuhn, T. (1962). *The structure of scientific revolutions*. University of Chicago Press.

For more on scientific realism, see Anjan Chakravartty’s “Scientific realism.” In E. N. Zalta (Ed.), *The Stanford encyclopedia of philosophy* (Summer 2017 ed.). https://plato.stanford.edu/archives/sum2017/entries/scientific-realism/.
---
# CHAPTER 13

# Science in society

 

  

# 13.1 ANIMAL BEHAVIOR AND SCIENCE’S SOCIAL CONTEXT

After reading this section, you should be able to:

- Summarize sexual selection theory and give examples of a showy trait and an aggressive trait thought to evolve through sexual selection
- List three concerns with classic sexual selection theory and suggestions for how the theory might be expanded or rethought on the basis of these concerns
- Describe three ways in which science can be influenced by its social and historical context

# Sex and reproductive strategies in animals

Some animal traits have clear value to the animal. Predators like the leopard have eyes on the front of their head to make it easier to track their prey, while prey like the antelope have eyes on the sides of their head so they can keep an eye out to ensure their safety. Eye placement evolved differently in predator lineages and prey lineages because each placement has different advantages.

Other traits are less obvious in their function. Since Charles Darwin first developed the scientific theory of evolution by natural selection in the 19th century, scientists have puzzled over the emergence and biological function of traits like the peacock’s long, colorful tail feathers, also called a train. What’s puzzling about the peacock’s showy train is that it makes it easier for predators to spot the peacock and more difficult for the peacock to move quickly. And it’s not the kind of trait that would just occur by accident!

The widely accepted explanation for the peacock’s colorful train is that the showy tail feathers don’t help with survival but, instead, with reproduction. This trait—and many others, across many species of animals—is thought to evolve through sexual selection, when a trait is valuable simply because it appeals to potential mating partners. If the trait is inherited by offspring, then sexual selection can explain how the trait can become more pronounced and widespread over time. So, the peacock,

DOI: 10.4324/9781003300007-14
---
# 316 Science in society

 

  

# The peacock’s showy tail feathers

FIGURE  13.1 over time, is thought to have evolved a longer, showier train because of this process of sexual selection.

Sexual selection theory traditionally emphasizes how female mate choice can lead males to evolve showy traits—the peacock’s train, the cardinal’s red coloration, the lion’s mane—and how male competition for mating opportunities with females can lead males to evolve aggressive traits—the elephant seal’s huge size and aggressive behavior, the deer’s large antlers, the rhinoceros beetle’s horns. But some scientists have criticized this focus. Among them are anthropologist and primatologist Sarah Blaffer Hrdy and biologist Joan Roughgarden.

Hrdy researched primate behavior in the second half of the 20th century. She criticized the assumption behind sexual selection theory that the norm across animal species is for choosy females to select among many promiscuous males who are eager for mating opportunities. Darwin presented this as a matter of the “coy” female engaging with the “eager” male. The problem with this idea is that, across many species, females are actually quite eager to engage sexually. So, a basic assumption of sexual selection theory turns out often to be inaccurate. Beyond that, Hrdy emphasized that sexual behavior is a very small portion of all animals’ lives—also relevant is time spent finding food, resting, fleeing dangers, rearing their young, playing, building homes, socializing, and so on.

Joan Roughgarden is a biologist who researched genetics and, later in her career in the early 21st century, turned to research on the variety of sexual, reproductive,
---
# Science in society

and parental strategies across animal species. Roughgarden’s book Evolution’s Rainbow catalogs that variety. Animals engage in a wide variety of mating strategies, such as bluegill sunfish, which have three distinct male types with dramatically different body sizes, appearances, and mating strategies. Roughgarden suggests these different types should be thought of as distinct genders. She also emphasized the wide variety of factors that determine the sex of animals, that is, whether they are male or female. In some species, including humans, genes play a central role in determining whether an animal is female or male. In others, like frogs, environmental factors such as temperature determine sex, and in still other species, sex of an individual changes over their lifespan.

Animals also vary widely in their parental strategies. Some species leave their offspring to fend for themselves immediately, while other species invest significantly in caring for and protecting their young. Sexual selection theory has emphasized female contribution to caring for offspring. But, in species that care for their young, this is sometimes a two-parent project; sometimes a male project, as with seahorses, whose males carry the young around in a pouch much like kangaroos; and sometimes a group collaboration, where larger social groups collectively rear their young, as in several species of birds.

After cataloging the extensive variation in animals’ sexual, reproductive, and parental strategies, Roughgarden began to reconsider how those strategies may have evolved. She criticized sexual selection theory for focusing exclusively on reproductive sexual encounters, ignoring how sexual activities can play nonreproductive social roles like resolving conflicts, and how pairs and communities can cooperate to successfully raise offspring. She also pointed out that animals engage in a wide variety of social encounters, with members of the opposite sex and same sex alike, and that these can also have evolutionary significance.

Roughgarden has developed several competing hypotheses for traits targeted by sexual selection theory. These hypotheses emphasize extensive social exchanges and cooperation as potential reasons for the evolution of traits typically explained as the result of sexual selection. While most biologists still think of sexual selection theory as a cornerstone of evolutionary theory, many biologists’ understanding of sexual selection theory has at least been updated to acknowledge more variation in how reproductive pressure influences evolution. Sometimes females compete for reproductive access to males, and this has led, in some cases, to females having showy traits or aggressive traits. Sometimes males invest more in offspring care than females do. And sometimes broader social groups are relevant to the evolution of sexual and reproductive behaviors.

If Roughgarden and Hrdy are right, then more attention should be paid to the evolutionary impacts of how animals engage with one another—sexually, cooperatively, and competitively—outside of reproduction. This might lead some traits that have been explained as instances of sexual selection to be reclassified as the evolutionary result of the influence of social dynamics.

Returning to the example of the peacock’s colorful tail feathers, this is still broadly accepted as a primary example of a showy trait resulting from sexual selection. But more than a decade ago, researchers in Japan published a paper showing that, in local
---
# 318 Science in society

Feral populations of peafowl, more elaborate tail feathers weren’t associated with mating success. Male displays involving the colorful train are certainly involved in mating behavior. But other researchers have found that displaying the tail feathers by fanning them out in mating rituals serves to amplify peacocks’ verbal calls, which raises the question of whether the trains themselves are important to mating or just their role in amplifying verbal cues. Furthermore, peacocks also display their tail feathers when faced with a predator, making themselves seem larger and distracting the predator, as a bite to the colorful train simply leads to the loss of some feathers rather than bodily injury. Sexual selection theory is meant to account for traits that wouldn’t evolve by natural selection alone, but it seems like the peacock’s colorful tail feathers may have direct contributions to survival as well.

# Science in a social context

Beyond her primatology research, Sarah Blaffer Hrdy also asked why primatologists began to take issue with standard sexual selection theory in the 1970s, first beginning to notice the active sexual lives of female primates. She suggests that, especially when studying primates, scientists tend to identify with and observe more closely animals of the same sex as themselves. Humans are, after all, one species of primate. So, in Hrdy’s view, an increasing number of women in the field of primatology brought with it increasing attention to female primates and their behaviors, instead of the previous focus on male primates with females more in the background.

Joan Roughgarden is also reflective about how her social identity influenced her research. In the preface to her book about variability in sex and reproduction in animals, she reflects on attending her first Pride Parade in San Francisco and transitioning shortly after to confirm her identity as a transgender woman. These experiences led her to wonder about all the diversity across the animal kingdom, and how evolution and development lead to such diversity. Roughgarden associates this with her growing realization that sexual selection theory was overly limited, as well as with the insight that “kindness and cooperation are basic to biological nature.”

Way back in Chapter 2, we introduced the idea that science—including both its aims and its methods—is influenced by social values, or priorities and moral principles accepted in some community. In the scientific investigation of sex and reproduction in the animal kingdom, the influence is felt in the question of which sex is focused on (male or female), on whether reproductive variability beyond biological sexes—what Roughgarden urges us to think of as different genders—is investigated, on which traits and patterns are emphasized, and perhaps even on whether the focus is on the cooperative or competitive value of traits.

Because scientific reasoning is a fundamentally human endeavor, it always occurs in specific social, institutional, and historical contexts. Scientists make observations, develop theories, make discoveries, and interact with one another all within specific interpersonal, institutional, and cultural circumstances. Further, science is embedded
---
# Science in society

in institutional structures like universities, labs, museums, journals, and publishing companies. These social contexts and institutions in which science occurs are influenced by history, by who is part of them, and by the social identities scientists bring to their work.

Further, social and historical context influences the nature of science. Even as science aspires to produce knowledge that is not limited by specific perspective, scientific theories are in some ways creatures of the times, places, and people who created them. Some have suggested that Darwin’s statement of sexual selection theory was strongly influenced by Victorian moral sentiment in its assumption that, throughout the animal kingdom, male animals are promiscuous and aggressive and female animals “coy” and selective. This looks suspiciously like gender norms in Victorian England, Darwin’s cultural setting. While Darwinian evolutionary theory was certainly a tremendous step forward for biology, it was also influenced by the time and place of its creation, and perhaps by the interests and personal values of the individuals who created it.

So, science seems to be shaped by its social, institutional, and historical context. Science also is regularly used to promote particular social aims, either explicitly or implicitly. Specific scientific aims can support different social aims. Consider how Roughgarden is explicit about her motivation to explore variation in sex and reproductive strategies in the animal kingdom in order to support social aims of inclusion. Even if some scientific research does not relate directly to social aims, a scientist’s interests and values may still influence how the aims of their scientific research connect with social concerns.

The difficult truth is that, throughout history, science has often been used to promote objectionable social aims and, at times, has even been pursued in ways that incorporate morally horrendous views like eugenics and scientific racism. Science has been used to expand power over others, to invent nuclear and chemical weapons for the purpose of mass destruction, and to amass wealth for the few, as with research for the fossil fuel industry. Science has also been used to promote misinformation, as when the British doctor Andrew Wakefield fraudulently claimed that the combined measles, mumps, and rubella (MMR) vaccine was linked to autism or when tobacco corporations paid scientists to present cancer research in a way calculated to mislead the public.

Science has also been used to directly harm and oppress marginalized groups, as when the Nazis ran deeply cruel experiments on the prisoners of concentration camps and when the US Public Health Service ran the Tuskegee syphilis experiment. In this clinical study, researchers withheld treatment from 399 impoverished, rural, Black men who had syphilis. They never informed the participants that they had syphilis or that there was a cure for the disease. Scientific research has also indirectly supported racism and sexism by focusing on aims like identifying a genetic basis for racial differences in intelligence or neurological differences between men’s and women’s brains.

All of this suggests that an important aspect of investigating science is learning about science’s relationship to society. We need to understand how science is shaped.
---
# 320 Science in society

by scientific and historical context, ways in which science can be influenced by social values, how to uncover problematic values or problematic roles for values in science, and how science can be used to promote positive social aims.

 

# EXERCISES

# 13.1 Recall:

Summarize sexual selection theory and give one example of a showy trait and one example of an aggressive trait thought to evolve through sexual selection.

# 13.2 Apply:

Choose an example of a showy or aggressive trait, either from the text or a new one. Using Google Scholar, a library catalogue, or a similar search tool, find 3–5 research articles focused on that trait as an instance of sexual selection. Summarize the main finding of each article in one sentence; you can probably do this just by reading their titles and abstracts. Do these articles together provide adequate support for the hypothesis that the trait is an instance of sexual selection? Why or why not?

# 13.3 Recall:

Describe (a) Hrdy’s criticism of the assumption that female animals are “coy” while males are “eager,” (b) Roughgarden’s point about variety of sexual, reproductive, and parental strategies, and (c) Roughgarden’s idea about how cooperation might be important instead of competition. For each, say how it challenges sexual selection theory.

# 13.4 Recall:

How did Hrdy think research into sexual selection was influenced by social factors? How did Roughgarden think research into sexual selection was influenced by social factors?

# 13.5 Think:

In your own words, describe how you think historical and social factors have influenced research into the evolution of sex, reproduction, and parental strategies. Give one example of an influence that you think was problematic for scientific or ethical reasons and one example of an influence that you think was acceptable (scientifically and ethically).

# 13.6 Apply:

Choose an example of a scientific theory or finding discussed anywhere in this book. Describe how you think historical and social factors may have influenced the research bearing on that theory or finding. Does the influence by historical and social factors you identified call the theory or finding into question, or not?

# 13.2 PARTICIPATION IN SCIENCE

After reading this section, you should be able to:

- Describe how people with some social identities have been historically excluded from or marginalized in science
- List three ways in which diversity of scientists is beneficial to science
- Indicate how members of the public can be included in scientific research and how this can affect scientific research
---
# Science in society

# Exclusion from science

Just as we must acknowledge the historic contribution of science to immoral social aims and objectionable values, including classism, racism, and sexism, we also must acknowledge that science has never been—and still is not—fully inclusive. This means that many people—because of their geographical location, institutional affiliation, language, sex, race, or creed—do not receive a fair chance to participate in and contribute to scientific inquiry. Historically, the institutions that house today’s science disproportionately developed in Europe and, later, the United States and predominantly included wealthy, White men. Women, people of color, people without wealth, and people in other nations have always contributed to science. But people from these and other marginalized social groups have historically had very limited access to resources to make scientific contributions and very little recognition afforded to them for their scientific contributions.

Polymath Alan Turing did groundbreaking research in computer science, logic, mathematics, cryptography, and morphology in Great Britain. During World War II, he helped crack the code used by the Nazis to protect their military communication, an achievement that many historians believe was the single greatest contribution to the Allied victory. Turing was also a visionary of artificial intelligence. You may have heard of the Turing machine and Turing test that he invented; he anticipated that human intelligence would one day be matched by machines. Turing was also gay, and at the time this was illegal in Britain. Despite his groundbreaking contributions to the computer, or “digital,” revolution, Turing was arrested and chemically castrated by the British government. Humiliated and resentful, he committed suicide at the age of 41.

If being outed as gay in mid-20th century Great Britain was awful, matters were no brighter for women in science for most of history. Cecilia Payne-Gaposchkin’s groundbreaking dissertation Stellar Atmospheres in 1925 became a cornerstone of modern astrophysics, but she couldn’t get a professorship, so she had to do low-paying adjunct teaching for the next 20 years. Rosalind Franklin was a chemist and x-ray crystallographer, who we mentioned in Chapter 5 for her important contributions to the discovery of DNA’s structure in the mid-20th century. Franklin was responsible for an x-ray diffraction image that was shared with Watson and Crick without her knowledge (pictured in Figure 13.2). After seeing that image, Watson and Crick developed their physical model of DNA. They went down in history as having discovered DNA’s double helix structure, eventually winning the Nobel Prize for this work. In contrast, Franklin’s enormous contributions to the discovery were recognized only after her death.

A similar story is that of neuroscientist Kathleen Montagu, who published her discovery of the neurochemical dopamine in the human brain in 1957. Her work was largely overshadowed by a very similar discovery three months later by Swedish neuropharmacologist and Nobel Prize winner Arvid Carlsson and colleagues. This is a common enough phenomenon that is has been named. The Matilda effect is the bias against recognizing women scientists’ achievements, whose work is often uncredited or else attributed to their male colleagues instead.
---
# 322 Science in society

 

  

a. Rosalind Franklin (left); b. Franklin’s x-ray diffraction image that famously inspired Watson and Crick’s double helix model of DNA

Societal prejudice and structural exclusion have made it more difficult for not only women but also racial and ethnic minorities, sexual and gender minorities, people with disabilities, first-generation college students, people from low socioeconomic backgrounds, residents of the Global South (Latin America, Asia, Africa, and Oceania), and other marginalized groups to be supported in their scientific work and even to become scientists in the first place. Even today, opportunities and rewards in science disproportionately go to men from families with financial resources and college educations and who live in wealthy nations. That said, the inclusion of people from social groups underrepresented in science is increasing, as more attention is focused on making science more inclusive and equitable.

# Diversity in science

When only certain kinds of people participate in science, science suffers. Systemic exclusion and marginalization result in science squandering or losing out entirely on the contributions of the people who were excluded or marginalized. A second way in which science suffers is that there are fewer role models for aspiring scientists. When scientists like Turing or Franklin are dishonored or not acknowledged, younger people do not have the opportunity to look up to them. When groups of people are systematically underrepresented and marginalized in science, young people may not see themselves as potential participants in science.

These are reasons for the scientific establishment to prioritize inclusion, that is, to take steps to ensure people with a full range of backgrounds have a fair opportunity.
---
# Science in Society

to become scientists and to gain recognition for their achievements. We should also look back to the history of science, revisiting standard accounts of who discovered what, who qualified as scientists, and which societies influenced the development of science as an institution. We have tried to keep that in mind as we selected examples and scientists to feature in this book, though we acknowledge we did not fully succeed. There is a broad project needed, and to some extent underway, to update our collective understanding of science to more fully credit the full range of individuals and societies that shaped it.

Diversity in science has important effects beyond simply not losing out on scientific discoveries or future scientists. Who participates in science and who is excluded affects the nature of scientific knowledge and its trustworthiness. The features of scientists—nationality, gender and sexuality, socioeconomic background, race and ethnicity, religious belief, political affiliation—all help determine what questions scientists are interested to investigate, what bold conjectures they come up with, and perhaps in some cases which methods they tend to use. When a group of scientists in some field is sufficiently diverse, all differences among them can contribute to the range of questions, richness of ideas, and ultimately the quality of inquiry. If, instead, only certain kinds of people participate in science or in some particular field of science, then the kinds of questions posed, ideas generated, and interpretations of data may reflect the limited perspectives of those scientists. For example, recall Hrdy’s observation of the changes to primatology research that occurred when a critical mass of women became primatologists. And, back to our point about role models, the influx of women to primatology might well have been influenced by the publicity received by Jane Goodall’s research on chimpanzees in the mid-20th century.

Charles Henry Turner was an African American zoologist who pioneered the study of animal cognition, particularly in insects. Born in the US just two years after the end of slavery, Turner was the first Black student to graduate with a master’s degree from the University of Cincinnati and the first Black student to be awarded a PhD at the University of Chicago. Turner was a victim of racism and could not find work in a university. He worked in an all-Black high school, while continuing his research on animal behavior. Turner rejected the prevailing ideas of the time that animals like birds, bees, and ants do not have sophisticated abilities of perception or cognition. His research demonstrated that these animals possess impressive powers of memory, learning, and problem-solving, drawing attention to sophisticated behaviors like mound building in ants and hunting habits of wasps. Although Turner could not work in a university and did not have access to adequate laboratory equipment, he still managed to publish the results of his studies in prestigious scientific journals. His research was ahead of its time, predating more recent cognitivist approaches to analyzing and explaining animal behavior.

The value of diversity of science, then, is more than just who is recognized for what discovery, how breakthroughs are received, and who gets to be a scientist. People with different social identities can bring different styles of reasoning to the table, and scientific progress often demands creativity and seeing things anew. For these reasons, the conscious inclusion and encouragement of people from diverse social groups and with
---
# 324 Science in society

 

  

# Charles Henry Turner, African American zoologist

working in the late 19th and early 20th centuries

diverse social identities to participate in science doesn’t just benefit those individuals and benefit society; it also makes science more successful at achieving its paramount goal of generating knowledge.

# Public participation in science

Science welcoming new scientists from diverse social groups and with diverse social identities is one way to gain new perspectives in science. Another way, which is also gaining popularity, is to include members of the public as collaborators in scientific research. Participatory research is any scientific research in which members of the public who aren’t trained scientists participate in doing the research. Participatory research goes by many names; you may have heard it called citizen science, community-based research, or action research. We encountered this in Chapter 7’s discussion of how scientific research helped uncover the Flint water crisis. Community members in Flint reached out to environmental scientists for help, and a local pediatrician led research into pediatric lead exposure.
---
# Science in society

# Box 13.1 Open science

The term open science indicates several practices that support the free sharing of scientific research and calls for broadening the demographic composition and theoretical approaches of scientific research. The overarching aim of open science is to enhance the quality of research, accelerate the rate of discovery, and make science more inclusive.

Open science has several dimensions. One is open access to research products, where scholarly outputs such as software, scientific articles, and books are disseminated open source—free to read, use, and share by anybody. An example is open-access repositories of electronic preprints of scientific papers such as arXiv. Another more controversial example is Sci-Hub, a shadow library website created by Kazakhstani computer programmer Alexandra Elbakyan, providing free access to millions of published research papers without regard to copyright and paywalls.

Another dimension of open science is pedagogical. The aim here is to make a diverse range of teaching and learning materials freely available and accessible through schools, libraries, museums, and even theaters. A third dimension of open science is preregistration and open data: specifying one’s research plans in advance of a study and making all data available and accessible in public repositories. These all aim to improve the transparency, accountability, and replicability of research. Finally, another dimension are calls to identify the social, economic, and political dynamics that have historically shaped and still shape participation in science and to work to empower marginalized scientists, striving to make scientific institutions fairer.

Scientists sometimes choose to include the public in research efforts in order to increase the amount of data that can be collected. For example, the Cornell Lab of Ornithology in the United States has involved members of the public in collecting data about bird breeding, courtship, habitats, and colors for decades, which has enabled more data and in a broader range of locations. But that’s not the only benefit from public participation in the Cornell Lab’s research. Participation in gathering data about birds is also an opportunity for students and interested adults to learn more about birds and about how scientific research occurs. And it is an important opportunity for education about conservation and participation in conservation efforts.

Some participatory research even involves members of the public in shaping the research aims and methods. When research focuses on topics of community interest, such as health outcomes, local environmental conservation, and community access to services, involving members of the relevant communities early in the process of designing the research enables scientists to benefit from their inside perspective. This can help the research target issues of genuine community concern, in ways the community will value, and it can help legitimize the research in community members’ eyes, which can help with recruiting participants into the study as subjects (to respond to surveys,
---
# 326 Science in society

be interviewed, or donate genetic samples, for example). In Chapter 2, we mentioned how local, indigenous knowledge is increasingly recognized as valuable for certain kinds of scientific research, for example, on how to adapt to local effects of climate change. That is one pattern participatory research can follow.

Because of science’s history of exclusion and its contributions to injustice, members of some communities hesitate to participate in scientific research. If participatory research is pursued with true concern for community member’s priorities and is developed to empower public participants and their communities, then participatory research can perhaps help ameliorate this problem. But it’s worth pointing out that participatory research can also be pursued in problematic ways. This can occur, for instance, if researchers do not empower public participants to influence the research, do not heed community members’ recommendations, or do not follow through in their commitments to the community related to the research. Indeed, science has developed a bad reputation for so-called helicopter or parachute research, where scientists from wealthy nations visit poorer countries to study underserved communities and local ecosystems, perhaps collecting artifacts or biological samples, and publishing results in scientific journals with no involvement from local scientists and without concern for whether and how the community is impacted or whether community members have access to the knowledge generated.

# EXERCISES

# Watch Video 17

1. # 13.7 Recall:

Describe how people with some social identities have been historically excluded from or marginalized in science. List three social identities affected by this exclusion and marginalization.
2. # 13.8 Apply:

Choose one social identity underrepresented in science (such as a racial or ethnic minority, a sexual or gender minority, people with disabilities, first-generation college students, people from low socioeconomic backgrounds, or residents of the Global South). Use the internet to identify three prominent scientists with the social identity you have selected. For each, provide their name, the approximate time period of their career, their research field(s), and a brief summary of their main scientific contributions.
3. # 13.9 Recall:

List three ways in which diversity of scientists is beneficial to science.
4. # 13.10 Think:

Describe three steps that you think could be taken to increase diversity in science. Then, indicate any concerns or downsides you can think of for each of the steps. Which of the steps you described do you think should be implemented, and why?
5. # 13.11 Recall: Define participatory research.

Describe three ways in which participatory research can improve scientific research.
6. # 13.12 Apply:

Go to the website www.zooniverse.org; this is a major platform for participatory research projects. Look at some of the projects on the website and find.
---
# Science in society

one that’s particularly interesting to you. Describe the project, what the aim of the research is, and why you think it is designed to include public participation. What is the value for the scientific research of public participation? What is the value for the public of participating in this research? Make sure you provide the name and link of the project you chose.

 

  

# 13.3 SOCIAL VALUES AND SCIENCE

After reading this section, you should be able to:

- Define the value-free ideal and describe what about it is correct and what is incorrect
- Give an example of when values have influenced science in a problematic way
- List five ways in which values influence science in legitimate ways and give an example of each

# The value-free ideal

In Chapter 1, we emphasized how the institution of science has been developed to control for and overcome human limitations in reasoning like confirmation bias. One feature of this is that science is supposed to provide a way to subject our pre-existing ideas to rigorous test. Wanting something to be true isn’t good grounds for believing it is true, and science provides methods of hypothesis-testing, reasoning, and theorizing to evaluate the grounds for our beliefs. This idea inspires what has been called the value-free ideal for science, which is the thesis that scientific reasoning should proceed free from the influence of our values—such as moral, social, or political beliefs.

There is something right about the value-free ideal. Whether or not we want something to be true is irrelevant to whether it is in fact true, and science aims at the production of genuine knowledge. So, in science, hypotheses and theories should be judged not for their desirability but instead for the grounds for thinking they are true. Some scientific questions—about the reality of climate change, humans’ evolutionary history, and gender differences in cognition, for example—may evoke emotional reactions, but those emotions aren’t relevant to how scientific research bears on the questions. Instead, these questions can only be answered by conducting experiments or studies, constructing models, evaluating evidence, applying statistical reasoning—by applying the recipes for science.

On the other hand, it is clear that science regularly is influenced by values. For example, we mentioned earlier how Darwin’s evolutionary theory encodes Victorian morality and how Hrdy’s and Roughgarden’s research was inspired by values each of these scientists held. Positing the value-free ideal as an ideal enables us to acknowledge that sometimes values have in fact played a role in science, while insisting that they should not. Still, if science regularly does incorporate values, it’s worth asking whether being value-free should even be considered an ideal for science to aspire to.
---
# 328 Science in society

Indeed, we discussed in Chapter 2 how social values can influence both the aims and methods of science. Is discovering a vaccine for the Zika virus, which is easily transmitted to humans by mosquito bites and leads to serious birth defects when pregnant women are infected, more important than discovering new facts about quasars, pulsars, supernovas, or other astral phenomena? Deciding this requires consideration of social values. It’s clear that the US Public Health Service should not have withheld syphilis treatment from 399 impoverished Black men without their knowledge in the Tuskegee syphilis experiment; saying why requires consideration of values. The value-free ideal is not only inaccurate of how science has in fact played out; it’s also undesirable as an ideal for science to aspire to. Values should, at least in some ways, influence scientific reasoning.

# How values shape science

The value-free ideal suggests that science should simply be a source of objective facts about the world, immune to influence by human values. On the other extreme, some people believe science only serves preexisting political or economic values. The right view of how values should influence science is somewhere between these two extremes. Science is not and should not be value-free, but there are ways in which science should limit the influence of values.

Scientists are human beings with different moral, political, and religious values, and we have seen that the social context for science and who participates in science can both influence scientific findings. And yet, the recipes for science are designed to limit the kinds of influence social and individual values have on science. When scientists’ values lead them to violate the recipes for science—acceptable approaches to data collection and modeling, to hypothesis-testing and abductive reasoning, to statistical analysis, and so forth—this is illegitimate. When scientists use values to supplement, inform, or guide the use of the recipes for science, this can be legitimate.

In his book, A Tapestry of Values, philosopher Kevin Elliott divides the legitimate roles values can play in science into five categories, as helping to answer five different questions. These questions are summarized in Table 13.1. Answers to these questions are needed in order to know which scientific methods to employ, on which phenomena, and to what end. These roles for values thus align with our suggestion that legitimate uses of values supplement or guide the methods of science but do not violate those methods.

To begin, scientists’ individual values and societies’ collectively held values help answer the first question about what to study. Individually, a researcher’s interests and values surely shapes what field of science they pursue, which lab they work in, and what problems they tackle. Collectively, we choose what kinds of scientific research to support when funding agencies, including tax-supported governmental agencies, designate the areas of research they fund and which specific research projects in those areas to fund.

Beyond what to study, values also inform decisions about how phenomena should be studied. Scientists can bring different questions, methods, and background assumptions to bear on any given topic, and these choices in how research is pursued reflect
---
# Science in society

# Five questions that our values help answer when doing science

|Question|Example|
|---|---|
|1. What should we study?|what kind of research is prioritized for funding|
|2. How should we study it?|how the initial hypothesis and assumptions about the causal background both guide experimental design|
|3. What are we trying to accomplish?|getting the most accurate information vs. accurate-enough information quickly enough to guide policy|
|4. What if we are uncertain?|how much evidence to require before accepting or rejecting a given hypothesis|
|5. How should we talk about the results?|the level of certainty conveyed to the public about some scientific finding|

Source: Adapted from Elliott (2017)

Researchers’ and society’s values. One instance of this influence is how the initial hypothesis and assumptions about the causal background both guide experimental design, including the nature of the intervention and which extraneous variables to control. As with the initial choice of what to study, funding agencies can also influence how phenomena are studied. For example, research into depression can focus on the efficacy of cognitive therapy; the role of sleep, diet, and exercise; or the efficacy of pharmaceutical intervention. The choice to strongly prioritize pharmaceutical intervention to the exclusion of other focuses reflects the outsized influence drug companies have had on medical science.

The third question that a focus on values helps to answer is what, exactly, scientists are trying to accomplish in studying some phenomenon. This is an even more fine-grained decision than just what to study and how to study it. In climate research, for example, scientists might prioritize getting information about climate trends available quickly so that it can guide policy, or they might prioritize getting as accurate of information as possible, no matter how long it takes. This decision about the aim of research is influenced by values, including views about the social role the scientific research is expected to have.

Fourth, values influence how scientists proceed in the face of uncertainty. Scientific results are never free from uncertainty. There’s the basic problem of measurement error. We’ve also seen that, if observations don’t match expectations, it could be the fault of the hypothesis, or it could be the fault of some auxiliary hypothesis. In an experiment, no matter how perfectly controlled, there’s always the chance that an unexpected confounding variable has interfered with the finding. In statistical hypothesis-testing, scientists choose whether to reject the null hypothesis or not, and either choice could be wrong, resulting in a type I error (false positive) or type II error (false negative). These are just a few examples of the unavoidable uncertainty in science and the need.
---
# 330 Science in society

to choose how to proceed in the face of inductive risk, that is, the risk of wrongly accepting or rejecting a scientific hypothesis. These kinds of uncertainty are all forms of underdetermination. Recall from Chapter 3 that underdetermination is when the evidence available to scientists is insufficient to determine which of multiple theories or hypotheses is true. Some believe that there is even permanent underdetermination in science: that there will never be enough evidence to conclusively decide in favor of one hypothesis or theory and against all possible alternatives. When scientists face underdetermination, they must choose what to believe or whether to suspend judgment.

Because of this unavoidable uncertainty, scientists must decide how much evidence to require before endorsing a theory or hypothesis (or before rejecting a theory or hypothesis). Safety is very important to us, whether for drinking water or medications, so toxicology tests must have a high bar for success. There is a lower bar for deciding whether a new drug is more effective than an already available drug. Scientists also must decide how to represent scientific uncertainty to the public. In 1988, climate scientist James Hansen declared that climate change, global warming, was occurring. He described that as a decision based on weighing “the costs of being wrong to the costs of not talking.” There was already enough evidence for Hansen to be relatively confident in his choice to speak up. Decades later, of course, there is now incontrovertible evidence of climate change.

This introduces a fifth category of values’ legitimate influence on science, regarding how scientists, journalists, and others who communicate scientific findings to the broader public should talk about those findings. As Elliott stresses, this isn’t just a decision to be accurate. Scientific findings also can be discussed in their relationship to previous findings, their potential social effects, or—picking up on the point just above—their level of certainty. This framing influences whether and how the public will engage with research, and this is a choice not dictated by scientific methods but by scientists’ and society’s priorities.

So, what scientists should study, how they should study it, what they aim to accomplish, how much evidential support should be required, and how scientists should communicate their results all depend on moral considerations—on values. These are legitimate influences of values on science. Recognizing these roles for values in science is crucial. This enables us, as a society, to critically assess what values are employed at each of these junctures. The influence of values on science can be problematic or even nefarious if the wrong values are employed at any one of these stages. Figuring out the right and wrong values is tricky, and it is not a matter for scientists alone to decide. Instead, this is an issue that needs to be engaged with broadly in our society.

Examples of problematic values influencing science are, unfortunately, very easy to come by. Here’s one. In 2017, the US president Donald Trump proposed that NASA resources should be dedicated to exploring the solar system instead of to climate change research. This research priority—a decision about what to study—reflects the values endorsed by a small but vocal contingent of politicians in the US. Choosing not to fund climate change research amounts to deciding that knowledge about the rate and
---
# Science in society

impact of climate change is relatively unimportant. Space exploration is important! It, too, should be funded. But because climate change is already having disastrous effects on populations, the environment, and economies across the world, and because the long‐term costs of ignoring it will be disastrous, pulling funding from NASA’s earth science division in order to avoid investigating climate change and its effects upheld the wrong priority.

We have suggested that science doesn’t have to be free from values to be trustworthy and objective. What matters is that values influence science in the right ways and that science effectively resists the influence of harmful, unethical values. Values, even good values, shouldn’t play the wrong roles in science; we should never decide a theory is true simply because we wish it were true. Further, the wrong values shouldn’t influence science, even through the proper channels. To better understand how science earns its trust and objectivity, it’s important to acknowledge the many roles of social and moral values in scientific reasoning and to critically examine the values that influence our science. By doing these things, we can clarify what values should influence science, and in what ways.

# EXERCISES

# 13.13 Recall:

Define the value‐free ideal for science and describe what is correct about it and what is incorrect about it.

# 13.14 Think:

Describe an example of when values have influenced science in an illegitimate way. (Your instructor might ask you to take an example from this section or to come up with a different example.) Then diagnose what went wrong: what was wrong about the values or the nature of their influence, and what was the detrimental effect to science?

# 13.15 Recall:

List the five ways discussed in this section in which values legitimately influence science. Give an example of each.

# 13.16 Think:

Describe the value-free ideal of science. Then, summarize the view of how values can legitimately factor into science. In your view, does that view of values’ influence violate the value-free ideal, or is it consistent with that ideal? Give an argument in support of your answer.

# 13.17 Apply:

Suppose you are working for an NGO (nongovernmental organization) on the task of measuring poverty levels across countries. For each of the following decisions, describe at least two ways to proceed, and say how values are relevant to making the decision.

- a. Which countries will you include in the study?
- b. How will you define and measure poverty?
- c. What extraneous variables will you take into account?
- d. How will you make comparisons across countries?
- e. How will your results be publicized?
---
# 13.18 Apply:

Look back at the case of climate change discussed in Chapter 1. Identify at least five ways in which values are likely to have affected that research and describe how those values have impeded or promoted scientific knowledge of climate change.

 

  

# 13.4 CHANGES IN SCIENCE AND NEW CHALLENGES

After reading this section, you should be able to:

- Describe the move toward ABC research in the 21st century and what remains unchanged
- List three challenges to science’s capacity for self‐correction related to incentive structures and sources of funding
- Characterize the current challenges of diversity and public communication in science

# Changes in 21st century science

Antireductionist, big, and corporate. This is the distinctive new “ABC” of scientific research in the 21st century. ABC research investigates complex phenomena at multiple scales (antireductionist), capitalizes on big collaborations between many scientists with diverse expertise and big data (big), and involves business partnerships with private corporations (corporate). An example is proteomics, which is the study of how proteins influence organisms. Proteins, the building blocks of organisms, are complex molecules that play many vital biological functions. These functions depend on proteins’ physical shapes. Proteins acquire their distinctive shapes when the long chains of hundreds or thousands of smaller molecules composing them, called amino acids, fold into a wide variety of three‐dimensional physical structures.

Since the discovery of the structure of DNA in 1950s, one of biology’s grandest challenges has been the problem of protein folding. This is the problem of determining the 3‐D shape of the proteins in an organism from proteins’ amino‐acid sequence. Unlocking the mystery of how proteins fold is key to preventing and treating many diseases, like cancer; to understanding how life emerged on Earth and how organisms develop; and to many bioengineering applications. This is not just a very important problem; it is also a very hard problem. For any organism, the number of possible amino acid sequences and proteins is very large, and any given sequence of amino acids might fold into a huge number of different 3‐D structures. So, it has been difficult, if not impossible, to tackle this problem with traditional experimental methods.

A machine learning tool called AlphaFold, first developed in 2018, has been a game‐changer in the field of proteomics. Developed by the Google‐owned firm DeepMind, AlphaFold leverages deep‐learning artificial neural networks trained on big data sets about hundreds of thousands of experimentally determined protein structures to predict the shape of thousands of other proteins, in organisms from bacteria to humans.
---
# Science in society

from their genetic sequence. Its predictions are surprisingly accurate. AlphaFold has some limitations—for example, it is not designed to predict the effects of mutations on a protein’s structure—but it is already changing the field of proteomics. It saves biologists a lot of time‐consuming manual labor, so it accelerates research. It can also open new avenues of research, as it makes available new biological hypotheses and interpretations.

Research relying on AlphaFold exemplifies ABC research in its antireductionist approach to studying protein folding in all its variety in an open‐ended, exploratory way; by involving many scientists with diverse expertise, as well as big data methods; and by relying on corporate partnership in producing needed technology. Of course, not all contemporary scientific research fits this pattern, and it’s more relevant to some fields than others. But ABC research is a good characterization of recent trends in scientific research nonetheless. Let’s look at each of these features.

Reductionist methods attempt to account for a system by considering the behavior of its fundamental components, explaining even complex features as the result of component parts. It’s increasingly clear that this approach is inadequate to account for complex, possibly chaotic, systems such as the Earth’s weather and climate; the economic, cultural, and political behaviors of societies; and the workings of the brain. The same goes for the intricate dynamics of protein folding. Antireductionist approaches grapple directly with complexity, employing a variety of methods and approaches from multiple disciplines, often including big data techniques, to probe how networks might self‐organize, what surprising patterns exist, and how systems flexibly adapt to different circumstances. Proteomics and other “omics” disciplines, like genomics, exemplify this anti‐reductionism. And even in fields that fit this model less closely, some techniques employ antireductionist methods.

ABC research is also big. Scientific research has become highly collaborative and ever hungrier for data and computing power. For example, the scientific article first

# Sequencing data of genome analysis and particle molecular structure
---
# 334 Science in society

Introducing AlphaFold had more than 30 authors. Each of these authors brought specialized expertise to the research, from machine learning and software engineering to molecular and system biology. Studies in fields like particle physics, genetics, and medicine can feature even larger collaborations, among thousands of scientists who together co-author a single peer-reviewed paper. Running a study in these fields can be like running a Hollywood movie. It requires specialized competences and well-defined roles in a team pursuing an overarching research goal. Large collaborations also typically involve sophisticated equipment and large data sets. And, as we just saw, big data and computational approaches also are made necessary by embracing antireductionist approaches.

# Box 13.2 Co-authorship in large collaborations and with AI

Pick any recent issue of a scientific journal. Most articles you’ll find will list several co-authors, possibly hundreds or even thousands. The co-authors of a scientific paper are often from different countries and based in different institutions. They have different disciplinary backgrounds, so different co-authors may not fully understand other co-authors’ contributions. The research sometimes involves complex methods or instruments, whose workings may not be transparent to all collaborators. Increasingly often, scientific authors also rely on AI tools such as large language models, for example ChatGPT, for generating and editing text. In a few cases, AI chatbots have also been credited as co-authors of published research. But what if a large collaborative project, where expertise and responsibility are decentralized and distributed among several individuals and even AI tools, produces a published research article introducing a patentable new discovery? Or containing a mistake? Who deserves credit for the discovery or who should be held accountable for the mistake? And can an AI be a genuine co-author? These questions are important—and difficult—to answer. Co-authors are those who make a significant scholarly contribution to an article and who publicly agree to be legally, epistemically, and morally accountable for the published research. This is clear enough. But questions about co-authorship, credit and blame, and accountability become murkier with large collaborations, especially with the advent of AI tools, as there is no single, universal norm for how co-authorship should be determined in collaborative work.

Finally, ABC research is corporate. Large-scale collaborations geared towards understanding complex phenomena can also benefit from involving private corporations. This isn’t inevitable. Most scientific research is still conducted by researchers based at universities and funded by governments and other public institutions. But, there is a trend toward scientific research led by teams of scientists based at corporate research labs like Google DeepMind. With the emergence of machine learning and artificial
---
# Science in society

intelligence, an increasing number of scientists have been recruited from universities to big companies like Amazon, Meta, Google, Tesla, and Uber. The same trend applies to smaller firms and start‐ups, especially in the biotech and food sectors.

The declared mission of corporate science is sometimes basic research, sometimes innovation, sometimes profit. The complicated interplay of these aims has contributed to the discovery of life‐saving drugs, smartphones, and electronic vehicles. It can also boost research in an entire field by making valuable data sets and methodologies openly available to all, as in the case of AlphaFold, where the researchers at DeepMind have made openly available their data sets and computer code. But the relationship between science and corporations is complicated. This foregrounds challenges like the corruption of science from a motive of profit rather than pursuit of knowledge and how patentable data and methodologies should be shared.

Again, not all contemporary scientific research fits this model of antireductionist, big, and corporate. Reductionist approaches remain valuable in numerous research projects; not all scientific research is or should be collaborative; and much research proceeds without influence from corporations or clear application to industry. Note also that, even in ABC research, big data and machine learning tools like AlphaFold are not likely to replace human scientists. Science’s power consists, at least in part, in bringing to bear new ideas in creative ways, making judgment calls about how research should proceed, and looking beyond correlations to seek explanation. In many instances, those aspects of science are best conducted by human intellects.

# Challenges facing science

Scientific knowledge is worthy of trust due to its characteristics outlined in Chapter 1 — especially its capacity for self‐correction based on evidentialism and social structure, and the many methods and patterns of reasoning used to find evidential support for hypotheses and theories. We saw in Chapter 1 that science’s capacity for self‐correction requires scientists’ openness to criticism and dissent, their sincere and transparent communication of their results and uncertainties, and scientific communities’ welcoming of diverse perspectives. Trustworthy scientific knowledge is produced when scientists’ judgments are critically and openly assessed in light of other data, competing interpretations, and alternative possibilities.

Yet this process of collaboration and criticism, and thus science’s capacity for self‐correction, currently faces significant challenges. Some of these challenges relate to the incentive structure in science and how it shapes scientific findings in ways that can undermine trustworthiness. Facing up to these challenges requires us to think carefully about the scientific process, the role of incentives in shaping that process, and what values are thus finding their way into science.

First, scientists face pressures that make them more likely to focus only on research that will lead to surprising, new results. As we have seen, science is a social practice that occurs in institutions like universities and national research centers. Scientists are professionals who get paid for teaching and for doing research. But university salaries are, in most cases, not enough to fund scientific research. Scientists need extra money to
---
# 336 Science in society

pay for scientific instruments and lab equipment, for experimental participants, and for their assistants. This extra money is generally awarded by public agencies like the ERC (European Research Council) in Europe and the NSF (National Science Foundation) and NIH (National Institute of Health) in the US. The competition is fierce: every year the number of applicants for funding grows, while, partly due to budget cuts, the number of available awards shrinks.

Scientists’ ability to secure grants determines their career prospects. And their chance of securing grants depends on their quantity and quality of publications, frequency of citations, previously awarded grants, and the public attention they are able to attract. “Publish or perish” is the phrase coined to capture the increasing pressure in science to rapidly and continually publish research articles in order to sustain one’s career.

The competition for space in prestigious journals is also fierce; many journals reject over 90% of the articles submitted. And journal editors usually prefer to publish novel results that support an exciting hypothesis rather than negative results, even if they are robust and well documented, or studies replicating earlier findings. The tendency to publish surprising, new results more often than negative results, replication studies, and exploratory work is called publication bias.

Publication bias is common in all scientific journals but especially strong in the most prestigious journals. Consequently, scientists have a strong incentive to produce surprising, positive results. Their careers literally depend upon it! So, this is where scientists tend to put more of their attention, compared to writing up negative findings, replicating or assessing previous results, or even conducting preliminary, exploratory investigations.

Publication bias, combined with the scarcity of resources and employment opportunities, generates a challenge to science’s capacity for self-correction. For one thing, science’s openness to criticism depends on researchers publishing negative findings and attempting to replicate existing studies to see if the evidence holds up. Replication of previously published studies can increase the credibility of scientific claims when the supporting evidence for these claims is reproduced. When findings are not replicated, this can improve experimental designs or data analysis or even give scientists reason to rethink accepted theories. So, a disincentive from publishing negative findings and conducting replication studies undermines self-correction and the accumulation of trustworthy knowledge across science.

The scientific research associating specific foods with cancer risk, for example, may be seriously distorted by a lack of attention to replication. In Chapter 9, we discussed how statistically significant associations with cancer risk have been claimed for most food ingredients, from beef to tea. Careful analysis of this literature highlights that many published studies report implausibly large effects, even when the actual evidence is weak and effect sizes are small. Publishing negative results and greater emphasis on replicability would improve the internal and external validity of research about how different foods influence cancer risk.

Second, the incentive structure of current science also negatively impacts scientists’ communication of their results. The emphasis on producing exciting, publishable results may lead scientists to cut corners in how experiments are designed and how
---
# Science in society

data are analyzed and presented. For example, whether a conscious decision or not, scientists may not randomize group assignment in their experiment or may not control for some known confounding factors. Another common shortcut is data dredging, where data mining techniques are used to uncover patterns in the data that support a hypothesis not under investigation. Data dredging increases the chance of a type I error (see Chapter 10), making it more likely that the endorsed hypothesis is wrong.

Relatively few studies report effect sizes and measures of uncertainty in a transparent way, so it can be hard for others to assess the quality of a study.

Third, science’s capacity for self‐correction and thus its trustworthiness can be compromised by the financial interests funding scientific research. Fierce competition in academic science also is leading scientists to abandon academic research for jobs in industry. IT, AI, and pharmaceutical, chemical, and agricultural industries are hiring more and more scientists, often with better pay and greater job security. This raises another worry about sincere and transparent communication of scientific results. Being funded by a private company to carry out research may pose conflicts of interest, introducing funding bias. Funding bias is when researchers distort the results or modify conclusions of their study due to pressure from the study’s funders. This can happen through the ways in which values influence science—what to study and how, what the aim is, how to handle uncertainty, and how to present the findings. This can also happen via intended or unintentional improper influence on data or methods. Regardless, funding bias leads to corporations having outsized influence on the nature of our scientific knowledge and, in some cases, even misleading the public with bad information.

Another challenge to science’s trustworthiness relates to diversity of ideas and of practicing scientists. Diversity in scientific approaches fosters science’s capacity for self‐correction. But the institutional structure of contemporary scientific inquiry has reduced incentives for and freedom to pursue research challenging existing scientific ideas or moving in new directions. This has fostered increasing specialization in the sciences, and it has also shielded popular theories and methods from being challenged by competing, and perhaps better, theories and methods. Further, as we have seen earlier in this chapter, diversity among practicing scientists—in their social identities, worldviews, and more—is also important for science’s capacity for self‐correction. Yet the diversity of professional scientists remains limited.

Another challenge for science’s trustworthiness relates to public communication. Too much science is inaccessible to the general public. Scientific studies get published by for‐profit journals, and these journals typically put articles behind pricey paywalls. Academic institutions pay for their faculty and students to have journal access, but those without institutional affiliation are left without easy access. By the time science is reported in newspapers and popular magazines, it is often characterized inaccurately and misleadingly, full of hype and exaggeration. This too is due to an incentive structure, this time for journalism: media outlets are rewarded for splash and clicks, not for careful accuracy. This can fuel serious misunderstanding of scientific findings.

In this book, we have painted a picture of science as fallible, but with a formidable set of tools to help in the discovery of knowledge. Some scientific knowledge has had dramatic practical importance—just think about the outstanding progress of the
---
# 338 Science in society

medical sciences and of computer science and AI. Other knowledge regards fascinating aspects of the faraway universe and the strange behavior of microparticles. The ability of science to produce trustworthy knowledge requires openness to criticism and dissent, the pursuit of meaningful questions, and the communication of results in a sincere and transparent way. Only by ensuring these features are maintained and strengthened can science be self‐correcting, generate objective knowledge, and thus deserve our trust.

# EXERCISES

1. Recall: Describe three ways in which science has changed in the 21st century. Then, describe three important ways in which science is the same, even with these changes. For the second part of this question, you may want to consider topics from earlier in the book.
2. Think: Describe how big data and machine learning approaches are used in science. How transformative do you think these approaches will be for scientific methods and accomplishments? Provide justification for your response in 2–3 sentences.
3. Recall: List five current challenges for science described in this chapter. For each, indicate how it threatens science’s objectivity and/or public trust in science.
4. Apply: List five potential ethical problems arising from scientific research funded by the pharmaceutical industry. For at least three of these problems, describe a concrete action to address that ethical problem that could be taken by government, pharmaceutical companies, or some other party.
5. Apply: Choose a current or recent example of societally important scientific research. Describe the nature of scientific uncertainty and what kinds of action had to be taken even with this uncertainty. Describe how social, economic, and moral considerations might have factored into the decision of how to proceed.
6. Apply: In recent years, there have been several retractions of published scientific articles that have captured the world’s attention. In 2015, it was the retraction of a paper about gay marriage that was initially published in the prominent scientific journal Science. Read the description of this case on Retraction Watch, then answer the following questions.
1. a. What risks do people who report misconduct in science (whistleblowers) face?
2. b. Were human subjects “harmed” in this case, and if so, how?
3. c. Describe how data management issues influenced this case.
4. d. Describe how authorship issues influenced this case.
5. e. Does this case raise any conflict of interest?
6. f. What issues does the case raise about collaborating with others?
7. g. Describe how replication issues influenced this case.
---
# Science in society

# FURTHER READING

For a readable account of the wide variation of sex and reproductive strategies in the animal kingdom, see Roughgarden, J. (2004). *Evolution’s rainbow*. University of California Press (reprint 2013).

On participation in science and relationship to the public, see Potochnik, A. (2024). *Science and the public*. Elements in Philosophy of Science, Cambridge University Press.

For an introduction to the roles values play in science, see Elliott, K. (2017). *A tapestry of values: An introduction to values in science. Oxford University Press and (2022). Science and values*. Elements in Philosophy of Science, Cambridge University Press.

On complexity, see Mitchell, M. (2000). *Complexity: A guided tour*. Oxford University Press.
---
# Glossary

 

  

68–95–99.7 rule
the percentages of values that lie within one, two, and three standard deviations around the mean of a normal distribution

abductive inference
a type of nondeductive inference that attributes special status to explanatory considerations; also sometimes called inference to the best explanation

absolute risk
the number of individuals experiencing some condition in relation to the relevant population

abstraction
omitting or ignoring known features of a system from a representation or account of it

accuracy
the extent to which a model represents the actual features of its target system

addition rule
the probability that any of a number of outcomes will occur is the sum of their individual probabilities, subtracting the probability of multiple outcomes occurring

affirming the antecedent
a valid pattern of deductive inference in which a conditional statement and its antecedent are used as premises for concluding the consequent is true; also, modus ponens

affirming the consequent
an invalid pattern of deductive inference in which a conditional statement and its consequent are used as premises for concluding the antecedent is true

algorithm
a procedure for obtaining some outcome that halts in a finite number of steps

alternative hypothesis
in statistical hypothesis-testing, the alternative to the null hypothesis; the bold conjecture under investigation

ampliative inference
an inference in which the conclusion expresses content that surpasses what is present in the premises

analogical model
representations with features similar to focal features of a target system

anomaly
deviation from expectations that resist explanation by the reigning scientific theory; on Kuhn’s view, motivation for scientific revolution and paradigm shifts

antecedent
in a conditional claim, a condition that guarantees some consequence; logically prior to the consequent

appeal to ignorance
concluding that a certain statement is true because there is no evidence proving that it is not true

appeal to irrelevant authority
appealing to the views of an individual who has no expertise in a field as evidence for some claim

applied research
scientific research used to develop some tangible output like techniques, software, drugs, or new materials; often, a core motivation is to generate products for profit

argument
a set of statements in which some (premises) are intended to provide rational support or empirical evidence in favor of another (the conclusion)

assumption
a specification that a target system must satisfy for a given model to be similar to it in the expected way
---
# Glossary

# auxiliary assumptions

assumptions about how the world works that often go unnoticed but that are needed for a hypothesis or theory to have the expected implications

# axiom

a statement accepted as a self-evident truth about some domain, used as a basis for deductively inferring other truths about the domain (see theorem)

# background conditions

the physical, technological, and social aspects of an experiment or study

# bar chart

visual representation of statistical distribution in which bars of different heights show amount for different values of a variable

# base-rate fallacy

neglecting the base rate or prior probability of some occurrence and focusing only on the individual information at hand

# basic research

scientific research that aims at knowledge for its own sake

# Bayes factor

the ratio of the probability of the observation given one hypothesis to the probability of the observation given another hypothesis, i.e. Pr(O | H1)/Pr(O | H2)

# Bayes net

a kind of causal model that uses joint probability distributions to provide a compact, visual representation of causal relationships and the strength of those relationships

# Bayes’s theorem

Pr(H | O) = Pr(O | H)Pr(H)/Pr(O), also Pr(H | O) = Pr(O | H)P(H)/Pr(O | H)P(H) + Pr(O | not-H)Pr(not-H) for opposed hypotheses; a mathematical result at the heart of Bayesian statistics

# bell curve

see normal distribution

# biased variable

a random variable for which some outcomes are more likely than others (unfair)

# big data

very large data sets that cannot be easily stored, processed, analyzed, or visualized with traditional methods

# bimodal distribution

two values in a range are the most common; in a histogram, there are two peaks

# biological sex

the categories male, female, or intersex, which, in humans, are determined by X and Y chromosomes, hormones, reproductive organs, and other physical traits

# blinding

when researchers or subjects are temporarily kept unaware of group assignment, hypotheses under test, or other experiment details; also called masking

# calibration

comparing the measurements of one instrument with those of another to check the instrument’s accuracy and adjusting it if needed

# case study

a detailed examination of a single individual, group, system, or situation in a real-life context

# causal account

the view that explanation involves appealing to causes that brought about the phenomenon to be explained

# causal background

all the other factors that might causally influence an outcome, thereby also potentially affecting the causal relationship between the two events

# causal Markov condition

the requirement that the probability of causal variables conditional on their parent causes are probabilistically independent of all their other ancestors; an assumption of causal Bayes nets

# central limit theorem

the statistical claim that samples with a large enough size will have a mean approximating the mean of the population

# cluster indicators

markers or features of some variable that allow researchers to more precisely define it without oversimplification

# cohort study

a study in which researchers select a group of subjects sharing some defining trait and study them over time, in comparison to another group of subjects that is as similar as possible except without this trait

# collectively exhaustive outcomes

when at least one outcome of a set of outcomes must occur at any given time
---
# 342 Glossary

common cause
: when neither of two covarying types of events causes the other but a third event causes both

computer simulation
: computer program developed from data about a phenomenon to simulate its behavior; also computer model

conclusion
: in an argument, a statement that is supported by the premises

conditional probability
: the probability of an event’s occurrence given that some other event has occurred; expressed Pr(X | Y) where X is conditional on Y

conditional statement
: a statement in which one circumstance, the antecedent, is given as a condition for another circumstance, the consequent; the antecedent guarantees the occurrence of the consequent

confidence interval
: an interval within which the value of the variable should lie for a given percentage of possible samples

confirmation
: a possible consequence of the H-D method; the observation matches the expectation based on the hypothesis, providing evidence in favor of the hypothesis

confirmation bias
: the tendency to look for, interpret, and recall evidence in ways that confirm and do not challenge existing beliefs

conflict of interest
: financial or personal gains that have the potential to inappropriately influence scientific research, results, or publication

confounding variables
: extraneous variables that are not controlled and affect the relationship between the independent and dependent variables

conjunction fallacy
: the error in judgment when we judge a conjunction of two events to be more likely than either one of the events on their own

consequent
: the condition that arises from, or is guaranteed by, the antecedent

contributory cause
: a cause that raises the probability of an outcome occurring but does not guarantee the outcome; also called a partial cause

control group
: a group similar to the experimental group but that does not receive the intervention and experiences other value(s) of the independent variable

correlated variables
: the value of one variable raises or lowers the probability of the other variable taking on some value

correlation coefficient
: describes the direction and strength of correlation; a positive or negative sign indicates positive or negative correlation, and a number between 0 and 1 indicates the strength of the correlation

counterexample
: a situation, real or imagined, in which the premises of an argument are true but the conclusion false; shows that a deductive argument is invalid

crucial experiment
: an experiment that decisively adjudicates between two hypotheses

curve fitting
: extrapolating from a data set to expected data by fitting a continuous line through a data plot; there are always multiple different lines consistent with the data

data
: public records produced by observation, sensory experience, or some measuring device; allow observations to be recorded and compared

data cleansing
: identifying and correcting errors in a data set by deciding which data are questionable and should be eliminated

data dredging
: using data mining techniques to uncover patterns in the data that support a hypothesis not under investigation

data model
: a regimented representation of data, often with the aim of discerning whether the data count as evidence for a given hypothesis

deception
: when researchers actively misinform participants about some aspect of an experiment or study
---
# Glossary

# deductive argument

: an argument in which the truth of the premises is supposed to guarantee the truth of the conclusion; in a valid deductive argument this is so, in an invalid deductive argument it is not

# degree of belief

: amount of confidence in the truth of a given hypothesis

# denying the antecedent

: an invalid pattern of deductive inference in which a conditional statement and the denial of its antecedent are used as premises for concluding the consequent is also false

# denying the consequent

: a valid pattern of deductive inference in which a conditional statement and the denial of its consequent are used as premises for concluding the antecedent is also false; also modus tollens

# dependent variable

: a variable measured for changes after an intervention to an independent variable. The value of the dependent variable is anticipated to depend on, or be affected by, the independent variable

# descriptive claim

: a statement about how things are without making any value judgments

# descriptive statistics

: tools for summarizing, describing, and displaying data in a meaningful way

# difference-making account of causation

: the idea that if the occurrence of one event makes a difference to the occurrence of a second event, the first is a cause of the second event

# direct variable control

: when extraneous variables are all held at constant values during an intervention

# directed acyclic graphs

: abbreviated DAG; graphs in which all the causal relationships are one-directional (none of a cause’s effects are also among its causes) and do not move in a circle (following a series of cause-effect relationships will not lead you back to an earlier cause as a later effect)

# distal causes

: causes that occurred further back in time from the effect, and perhaps further away as well

# double-blind

: an experiment or study in which both scientists and subjects are unaware of which subjects are in the experimental or control groups

# Duhem-Quine problem

: the idea that scientific hypotheses can never be tested in isolation but only against the background of auxiliary assumptions

# ecological validity

: the degree to which experiment circumstances are representative of real-world circumstances

# effect size

: a quantitative measure of the strength of a phenomenon

# empirical investigation

: inquiries that ground the justification for beliefs about the world in sensory information and observations

# estimation

: predicting properties of a population on the basis of a sample

# eugenics

: the idea that a human population can be improved by controlling breeding; historically linked to racist and classist science that threatened human liberties and dignity

# evidence

: anything that plays the role of supporting belief

# evidentialism

: the thesis that a belief’s justification is determined by how well it is supported by evidence

# exemplar

: a model that is one of the target systems it is used to represent

# expectation

: a conjecture about observable phenomena, which are based on a hypothesis and which should be true if the hypothesis is true

# experiment

: a type of empirical investigation where researchers perform an intervention that changes some feature of a system and observe the effects, with the aim of understanding how the system works or why a certain outcome occurs

# experimental group

: a group that receives the intervention to the independent variable, or experiences the intended value of the independent variable
---
# 344 Glossary

explanatory knowledge : sufficiently justified truths about how things work and why they are the way they are

exploratory experiment : an experiment that may not rely on existing theory and is not aimed to test a specific hypothesis; used to gather data to suggest novel hypotheses or to assess whether a poorly understood phenomenon actually exists

external experimental validity : the extent to which experimental results generalize from the experimental conditions to other conditions—especially to the phenomena the experiment is supposed to yield knowledge about

extraneous variables : all other variables besides the independent variable that may influence the value of the dependent variable; if uncontrolled, these may become confounding variables

fair : a random variable that has independent outcomes that are all equally likely

falsifiable : when it is possible to describe what kind of evidence would, if found, show a claim to be false; without being falsifiable, a claim would be unscientific

falsificationism : the thesis that scientific reasoning proceeds by attempting to disprove claims rather than to prove them right

field experiments : an experiment conducted outside of a laboratory, in the participants’ everyday environment

frequency : how often some outcome occurs in a data set

frequency distribution : how often a variable takes on each value in some data set

frequency interpretation : the idea that the probability of an outcome is the limit of its relative frequency

funding bias : when researchers distort results or modify conclusions of their study due to pressure from the study’s funders

gambler’s fallacy : inferring from past variation from the expected frequency of outcomes that there will be future variation from the expected frequency in the opposite direction; for example, “the coin has landed on heads a lot; I bet it will land on tails next time.”

gender : behaviors, social roles, appearances, and identities of individuals traditionally associated with the expression of masculinity, femininity, or non-binary features

generality : a model’s applicability to a greater number of target systems

germ theory of disease : the theory that microbes like bacteria, viruses, and fungi, or other “germs” cause illnesses

histogram : a graphical display of data that uses bars of different heights to represent a frequency distribution

historical sciences : fields of science that investigate past events, such as archaeology, paleontology, and cosmology

hypothesis : a conjectural statement about what some aspect of the world is like, which is not (yet) backed by sufficient, or perhaps any, evidence

hypothetico-deductive method : to test a hypothesis, an expectation is deductively inferred from the hypothesis, then compared with an observation; violation of the expectation deductively refutes the hypothesis, while a match with the expectation nondeductively boosts support for the hypothesis

idealization : an assumption made without regard for whether it is true, often with full knowledge it is false

illusion of explanatory depth : believing that one understands the world more clearly and in greater detail than actually is the case

illusion of understanding : failure to appreciate the depth of one’s ignorance about a topic when one lacks genuine understanding
---
# Glossary

# independent outcomes

: the probability of each outcome does not affect the probability of the other outcomes

# independent variable

: a variable that is changed or observed at different values in order to investigate the effect of the change

# indigenous knowledge

: true claims based on the observations, practices, and ideas developed about some geographic region by people native to the area, typically outside the institution of science

# indirect variable control

: extraneous variables are allowed to vary but researchers ensure the variation is independent from the value of the independent variable

# inductive inference

: an inferential relationship from premises to conclusion that is one of probability rather than necessity

# inductive generalization

: an inference to a general conclusion about a class of objects based on the observation of some number of objects in that class

# inductive projection

: an inference to a conclusion about the feature of some object that has not been observed based on the observation that some objects of the same kind have that feature

# inductive risk

: the risk of wrongly accepting or rejecting a scientific hypothesis

# inference

: a logical transition from one thought to another

# inferential statistics

: using statistical reasoning to draw broader conclusions on the basis of limited data

# instruments

: technological tools or other kinds of apparatus used in experiments

# intelligent design

: the idea that lifeforms are so complex that they couldn’t possibly have come about without the help of an intelligent designer (such as the Judeo-Christian God)

# internal experimental validity

: the extent to which researchers can infer accurate conclusions about the relationship between the independent and dependent variables

# intervention

: a direct manipulation of the value of the independent variable

# Islamic Golden Age

: an important period in the development of science prior to the Scientific Revolution from roughly the 8th through 13th centuries, stretching from Central Asia to the Iberian Peninsula

# joint probability distribution

: the probability distribution for each of a set of variables, taking into account the probability of the other variables in the set

# laboratory experiment

: an experiment conducted in a laboratory, giving scientists control over interventions performed and direct and indirect control of many extraneous variables

# life history

: (biology) the traits and circumstances that affected survival and reproduction of members of a species

# likelihood

: the probabilities of getting the observed data given the truth of some specific hypothesis

# logic

: the study of the rules and patterns of inference

# longitudinal study

: an observational study in which observations are made of the same variables over time, in many cases over a long period of time

# machine learning algorithms

: step-by-step procedures run on powerful computers that enable scientists to mine large data sets for patterns or to perform other tasks

# material conditional

: a conditional statement (with an antecedent and consequent) that is false only if the antecedent can be true while the consequent is false

# mathematical model

: mathematical equations that use variables, parameters, and constants to represent one or more target systems

# Matilda effect

: the bias against recognizing women scientists’ achievements, whose work is often uncredited or else attributed to their male colleagues instead
---
# 346 Glossary

mean
: a measure of the central tendency of a data set; the sum of all values for that variable in the data set divided by the number of instances

measurement standards
: rules or norms for regulating the use of quantity concepts, which help create a meaningful scale to apply across instruments

mechanistic model
: a model that represents the component parts and operations constituting some recurring process

median
: a measure of the central tendency of a data set; the middle value in a distribution when the values are arranged from the lowest to the highest

meta-analysis
: technique to combine multiple experiments or observational studies of the same hypothesis to strengthen the conclusions that can be drawn

metascience
: using scientific techniques to study science itself

methodological omnivory
: the use of multiple methods and specially tailored tools to generate evidence about specific targets

mode
: a measure of the central tendency of a data set; the most frequent or numerous value in a data set

models of phenomena
: models that represent target systems and are used to investigate those systems

modus ponens
: See affirming the antecedent

modus tollens
: See denying the consequent

monotonic inference
: an inference that cannot be invalidated by the addition of new information

multiplication rule
: the probability that two independent events both occur is the result of multiplying their individual probabilities

mutually exclusive
: a set of values that a variable cannot take on simultaneously

natural experiment
: an intervention on an independent variable that occurs naturally without experimenters influencing the system

natural phenomena
: objects, events, or processes that are sufficiently uniform so as to be susceptible to systematic study

naturalism
: the thesis that science provides natural explanations of natural phenomena

nature of science
: the orientation, values, and methods that are specific to science and allow it to generate knowledge in the ways that it does

necessary cause
: a cause that must occur in order for the effect to come about

necessary condition
: a condition that must be satisfied for the occurrence of the specified outcome

negatively correlated
: when greater values for one variable are related with smaller values for a second variable

neglect of probability
: a bias in judgment or decision under uncertainty that comes from disregarding probabilistic information

no miracles argument
: an abductive argument that the best explanation for the success of science is that mature scientific theories are approximately true

nodes
: used to represent variables in causal Bayes nets

nomological account
: the idea that explanation involves inferring statements of phenomena from scientific laws and statements of initial conditions

normal distribution
: a unimodal distribution with the most common values clustered around the middle, with decreasingly common outcomes as the values get higher or lower

normal science
: the most common phase of science, according to Kuhn; scientific research is stable, based on widespread agreement about basic assumptions; this follows either pre-paradigm science or scientific revolution
---
# Glossary

# normative claim

: a statement about how things ought to be, which might or might not correspond to how they in fact are

# null hypothesis

: a kind of default assumption; in statistical hypothesis-testing, often this just amounts to the hypothesis that nothing unusual is going on or that two variables are independent

# observational study

: collecting and analyzing data without performing interventions and sometimes without aiming to control extraneous variables

# observation

: any information gained from the senses—not only what one sees, but also what one hears, smells, touches, or any other way one experiences the world

# observer-expectancy effect

: the influence of a scientist’s expectations on the behavior of experimental subjects

# openness to falsification

: the requirement that a claim be willingly abandoned when the preponderance of evidence indicates that it’s false

# operational definition

: a specification of the conditions when some term applies, enabling measurement

# outcome space

: the set of all values a random variable can take on; also called sample space

# outliers

: measured values for a variable that are notably different from the other values in the data set

# p-value

: the probability of the observed data assuming the null hypothesis is true

# paradigm

: according to Kuhn, a way of practicing science; provides scientists with a stock of assumptions about the world, concepts and symbols for effective communication, methods for gathering and analyzing data, and other habits of research and reasoning

# parameter

: a quantity whose value can change in different applications of a mathematical equation but that only has a single value in any one application of the equation

# participatory research

: scientific research in which members of the public who aren’t trained scientists participate; sometimes called citizen science, community-based research, or action research

# pattern account

: the view that explanation involves fitting statements of phenomena into a more general framework of laws and principles

# perfectly controlled experiment

: an experiment in which all variables are controlled except for the independent variable, an intervention is performed on the independent variable, and the effects on the dependent variable are measured; no confounding variables are possible

# pessimistic meta-induction

: reasoning inductively from the rejection of many past scientific theories to the conclusion that many of our current best scientific theories are also not true

# phenomenological analysis

: description and analysis of what some experience is like for a particular individual

# phenomenon

: an object, event, regularity, or process that exists or occurs; plural phenomena

# philosophy of science

: the investigation of science, focused especially on questions of what science should be like in order to be a trustworthy route to knowledge and to achieve the other ends we want it to have, such as usefulness to society

# physicalism

: the view that everything in the universe is composed of physical matter

# physical constant

: a quantity believed to be universal and unchanging over time

# physical process account of causation

: the idea that causation occurs when there is a continuous, physical process connecting a cause to its effect, such that a cause transmits its effect with the transfer of mass, energy, momentum, charge, or other physical properties

# pie chart

: visual representation of statistical distribution in which a circle is divided into different-sized slices to depict how much of the outcome space for a variable falls into different categories of values
---
# 348 Glossary

placebo effect
: the phenomenon of an experimental subject’s expectations leading to the outcome the subject expects; this can be an extraneous variable

plagiarism
: the fraudulent theft of someone else’s ideas, scientific results, or words, which are subsequently presented as one’s own work without giving proper credit

population
: a large collection of entities that share some characteristic

population validity
: the degree to which experimental entities are representative of the broader class of entities or population of interest

population variance
: a measure of the variability of a data set; the average of the squared differences of values from the mean

positively correlated
: when greater values for one variable are related with greater values for a second variable

posterior probability
: the probability of a hypothesis conditional on an observation that has been made; Bayes’s theorem can be used to calculate this

power of a statistical test
: the probability that the test will enable the rejection of the null hypothesis

pre-paradigm
: the earliest phase of science according to Kuhn; characterized by the existence of different schools of thought that debate very basic assumptions, including research methods and the nature and significance of data

precision
: the extent to which a model finely specifies features of a target system

premise
: a statement that provides support for some conclusion; the starting point for an inference

prior probability
: the probability of an outcome without conditionalizing on known information (also: base rate)

probability
: how often some outcome is expected to occur

probability distribution
: how often a variable is expected to take on each of a range of values

probability theory
: a mathematical theory developed to quantify uncertainty and to reason about random variables, or outcomes that are individually unpredictable but that behave in predictable ways over many occurrences

problem of induction
: the concern that inductive inference cannot be logically justified, since any possible justification would need to employ inductive reasoning and would thus be circular

proximate cause
: a cause that occurs closely in time and perhaps in space to its effect

pseudoscience
: a nonscientific activity designed to look enough like science to deceive people into thinking it has scientific legitimacy

publication bias
: the tendency to publish surprising, new results more often than negative results, replication studies, and exploratory work

qualitative data
: information that is non-numerical and without some other standard that makes it easily comparable, such as diary accounts, unstructured interviews, and observations of animal behavior

qualitative variable
: a variable with values that are not numerical but descriptive, such as the variable sport, with values basketball, hockey, and so on

quantitative data
: data that is easily comparable, often in numerical form, such as numbers, vectors, or indices

quantitative variable
: a variable with numerical values, such as height or percent correct on an exam

random sampling
: the individuals composing the sample are selected randomly from the population

random variable
: a variable whose values are individually unpredictable but predictable in the aggregate
---
# Glossary

# randomization

: the use of arbitrariness or some chance procedure like a lottery to assign experimental entities to experimental and control groups

# range

: the difference between the smallest and largest values of variables in a data set.

# rational degree of belief

: the extent to which a rational agent should believe some claim

# reasoning

: a cognitive process of drawing inferences in support of some conclusion

# reductionism

: the view that appealing to the fundamental laws of physics will ultimately explain all the features of the world

# refutation

: a possible consequence of the H-D method; the observation contradicts the expectation deductively inferred from the hypothesis, so the hypothesis is deductively proven to be false

# regression analysis

: finding the best-fitting line through the points on a scatterplot

# regression to the mean

: a statistical phenomenon where, if a sample of values is extremely higher or lower than the mean, the next sample will tend to be closer to the mean

# relative frequency distribution

: a frequency distribution that records proportions of occurrences of each value of a variable rather than absolute numbers of occurrences

# relative risk

: a comparison between the incidence of a condition in two groups, generally expressed as a ratio or percentage

# reliability

: the extent to which an instrument accurately and consistently measures what it is supposed to measure

# replication

: performing an experiment or study again to check whether the result remains the same

# representative sample

: the experimental entities studied do not vary in any systematic way from the general population

# retrograde motion

: the historic astronomical observation of planets seeming to stop in their orbit, reverse course back across the sky, stop again, and reverse yet again to continue on their original path

# robustness

: a measure of insensitivity to features that differ between a model and the target system

# robustness analysis

: analyzing multiple models or different versions of a model to determine whether and to what extent their results are consistent

# sample

: a subset of the population of interest to be studied

# sample mean

: the most likely average value of the trait of interest in a population

# sample size

: the number of individual sources of data in a study, often the number of experimental entities or subjects

# sample standard deviation

: an estimate of the spread of the probability distribution for the random variable; s = √[∑(value−mean) / (2n − 1)]

# sampling error

: differences between the features of a sample and a population due to the unrepresentativeness of the sample

# scale model

: a concrete physical object that is a downsized or enlarged representation of its target system

# scatterplot

: a graph in which the values of one variable are plotted against the values of the other variable

# science

: an inclusive social project of developing natural explanations for natural phenomena; these explanations are tested using empirical evidence and should be subject to additional open criticism, testing, refinement, or even rejection

# scientific breakthrough

: a radical shift in theory in some field of science

# scientific knowledge

: explanatory knowledge of why or how the world is the way it is

# scientific model

: constructed to represent phenomena of interest and investigated to learn about those phenomena
---
# 350 Glossary

scientific revolution: a period of cultural, social, and technological changes that unfolded in Europe roughly between 1550–1750, which inaugurated the modern institution of science; also, a radical change of a reigning theory being overturned in favor of a new theory, often involving an alternative worldview.

scientific theory: a comprehensive account of phenomena, broader and more explanatory than individual hypotheses and models and backed by more evidence.

scientism: a derogatory term for an excessive belief in science as a solution to every problem.

self-explanation effect: the phenomenon in which generating explanations to oneself or to others can facilitate the integration of new information into existing bodies of knowledge, leading to deeper understanding.

set: any grouping of elements in no particular order.

sexual selection: occurs when a trait is valuable because it appeals to potential mating partners, so increases reproductive success; this can lead the trait to evolve to be more pronounced over time.

significance level: how improbable, given the null hypothesis, an experimental result must be to warrant rejecting the null hypothesis.

Simpson’s paradox: a correlation between two events that disappears, or is reversed, when data are grouped in a different way.

social determinants of health: social factors relevant to disease susceptibility and severity, such as education, income and benefits, housing conditions and exposure to pollution, pervasive stress from poverty, access to healthy food and activities, and more.

social values: group priorities and moral ideas accepted in a community.

sound inference: a valid deductive argument with all true premises.

spurious correlation: two events are correlated but aren’t causally related in any way.

standard deviation: a measure of the variability of a data set; the square root of the variance; for a population, = √[∑(value − mean) / 2 n].

standard error: estimate of how much the standard deviation of the sampling distribution of the mean varies from the true population mean; SE = s /√(sample size).

statistically independent: two events for which the occurrence of one does not increase or decrease the probability of the other; that is, when Pr(Y | X) = Pr(Y) and Pr(X|Y) = Pr(X).

statistically significant: in null hypothesis significance testing, the outcome is found to be unlikely enough if the null hypothesis is true that it provides grounds for rejecting the null hypothesis.

statistics: a set of tools broadly used in science to systematically collect, curate, analyze, present, and interpret data.

strength of correlation: how predictable the values of one variable are based on the values of the other variable.

strength of inductive inference: the probability that the conclusion is true assuming that all the premises are true.

subjects: humans, non-human animals, or inanimate objects in an experiment or non-experimental study; also called experimental entities or participants.

subtraction rule: the probability that some outcome doesn’t occur is the result of subtracting the probability of that outcome from the total probability (Pr=1).

sufficient cause: a cause that always brings about the effect.

sufficient condition: a condition that, if met, guarantees the occurrence of the specified outcome.

super-observational access: using tools to enhance our powers of observation beyond what they ordinarily include.

target system: the real-world system that scientists want to study using a model.
---
# Glossary

|testimony|: a spoken or written statement that something is the case|
|---|---|
|The Scientific Revolution|: beginning with the work of Copernicus and ending with the work of Newton; a fundamental transformation in ideas about how knowledge claims ought to be justified, which led to the development of the scientific method|
|theorem|: a statement deductively inferred from a set of axioms|
|theoretical claims|: claims made about entities, properties, or occurrences that are not directly observable|
|thought experiment|: an imagined intervention on an imagined system to learn about the role of the independent variable in the real world; may supplement or replace empirical evidence|
|total probability|: the probability of the full outcome space for any random variable; always 1|
|tractability|: the degree of ease in developing or using a model|
|triangulation|: conducting an experiment or analyze data using different instruments or techniques to detect any variation depending on instruments or experimental design|
|type I error|: a false positive; the erroneous rejection of a null hypothesis|
|type II error|: a false negative; failing to reject the null hypothesis when it is actually false|
|underdetermination|: when evidence is insufficient to determine which of multiple theories or hypotheses is true|
|understanding|: grasping why or how something came about or is the way it is|
|uniform distribution|: all values in a range are equally likely; a histogram shows a flat line|
|uniformity of nature|: the idea that the natural world is sufficiently uniform, or unchanging, that we are justified in thinking our future experiences will resemble our past experiences|
|unimodal distribution|: one value in a range is the most common; in a histogram, there is one peak|
|valid inference|: a deductive inference in which the truth of the premises logically guarantees the truth of the conclusion|
|value of a variable|: the particular state or quantity of a variable in some instance|
|value-free ideal|: the thesis that scientific reasoning should proceed free from the influence of our values—such as moral, social, or political beliefs|
|variability|: the distribution of values in a data set|
|variable|: anything that can vary, change, or occur in different states|
|variable control|: creating conditions such that no extraneous variable can change the value of a dependent variable during or as a result of an intervention on the independent variable|
|zero-risk bias|: a preference for policies that entirely eliminate a risk instead of alternatives that more effectively reduce risk (by being cheaper, easier to implement, etc.)|

---
# Bibliography

 

  

# CHAPTER 0

The discussion of HPV vaccination draws from Spayne, J., & Hesketh, T. (2021). Estimate of global human papillomavirus vaccination coverage: Analysis of country-level indicators. BM J Open, 11(9), e052016.

# CHAPTER 1

On Manson’s early climate change research see Manson, M. (1893). Geological and solar climates— their causes and variations. G. Spaulding & Co. The Arrhenius quote in section 1.1 comes from p. 54 of Arrhenius, S. (1908). Worlds in the making: The evolution of the universe. Harper & Brothers. The Callendar quote comes from p. 38 of Callendar, G. S. (1939). The composition of the atmosphere through the ages. Meteorological Magazine, 74(878), 33–39. Historic comparisons of atmospheric carbon dioxide are supported by Ahmed, M. et al. (2013). Continental-scale temperature variability during the past two millennia. Nature Geoscience, 6, 339–346. Global mean temperature comparisons are drawn from NOAA National Centers for Environmental Information, Monthly Global Climate Report for Annual 2022, published online January 2023. www.ncei.noaa.gov/access/monitoring/monthly-report/global/202213/supplemental/page-3. For expert agreement about climate change see Anderegg, W. R. L., Prall, J. W., Harold, J., & Schneider, S. H. (2010). Expert credibility in climate change. Proceedings of the National Academy of Sciences, 107, 12107–12110. On public acceptance of climate change see Lee, T. M., Markowitz, E. M., Howe, P. D., Ko, C. Y., & Leiserowitz, A. A. (2015). Predictors of public climate change awareness and risk perception around the world. Nature Climate Change, 5(11), 1014–1020. On the illusion of explanatory depth see Keil, F. C. (2003). Folkscience: Coarse interpretations of a complex reality. Trends in Cognitive Sciences, 7(8), 368–373. On falsification, see Popper, K. (1963). Conjectures and refutations: The growth of scientific knowledge. Routledge and Kegan Paul. The research on confirmation bias regarding views on the death penalty is Lord, C. G., Ross, L., & Lepper, M. R. (1979). Biased assimilation and attitude polarization: The effects of prior theories on subsequently considered evidence. Journal of Personality and Social Psychology, 37(11), 2098–2109. https://doi.org/10.1037/0022-3514.37.11.2098.

The discussion of Clever Hans draws from Pfungst, O. (1911). Clever Hans (The horse of Mr. von Osten): A contribution to experimental animal and human psychology (C. L. Rahn, Trans.). Henry Holt. (Originally published in German, 1907.) In the discussion of fabricated scientific results we refer to Retraction Watch. Tracking retractions as a window into the scientific process, http://retractionwatch.
---
# Bibliography

com/

The discussion of the checklist approach to defining science is influenced by the Understanding Science website, https://undsci.berkeley.edu. In the discussion of pseudoscience, we use an example from Oreskes, N., & Conway, E. (2010). *Merchants of doubt. Bloomsbury. Box 1.2 draws from Merton, R. K. (1942). A note on science and democracy. Journal of Legal and Political Sociology*, 1, 115–126; the quote is from p. 117.

​    

# CHAPTER 2

The Covid-19 gender disparity research we consulted included Jin, J. M., Bai, P., He, W., Wu, F., Liu, X. F., Han, D. M., Liu, S., & Yang, J. K. (2020). Gender differences in patients with COVID-19: Focus on severity and mortality. *Frontiers in Public Health, 8, 152. https://doi.org/10.3389/fpubh.2020.00152; Takahashi, T., Ellingson, M. K., Wong, P. et al. (2020). Sex differences in immune responses that underlie COVID-19 disease outcomes. Nature, 588, 315–320. https://doi.org/10.1038/s41586-020-2700-3; and Danielsen, A. C., Lee, K. M. N., Boulicault, M., Rushovich, T., Gompers, A., Tarrant, A., Reiches, M., Shattuck-Heidorn, H., Miratrix, L. W., & Richardson, S. S. (2022). Sex disparities in COVID-19 outcomes in the United States: Quantifying and contextualizing variation. Social Science & Medicine*, 294. https://doi.org/10.1016/j.socscimed.2022.114716.

The brief discussion of race in medicine draws from Tsai, J. (2018). What role should race play in medicine? *Scientific American. https://blogs.scientificamerican.com/voices/what-role-should-race-play-in-medicine/. Discussion of social determinates of health was influenced by Yong, E. (2021). How public health took part in its own downfall. The Atlantic. www.theatlantic.com/health/archive/2021/10/how-public-health-took-part-its-own-downfall/620457/. Box 2.1 draws from Wallisch, P. (2020). How to read a scientific article: The QDAFI method of structured relevant gist. Critical reading across the curriculum: Volume 2. Social and Natural Sciences*, 152–164.

# CHAPTER 3

The case study of scientific research on light draws from Newton, I. (1704/1998). *Opticks: Or, a treatise of the reflexions, refractions, inflexions and colours of light. Also two treatises of the species and magnitude of curvilinear figures. Commentary by Nicholas Humez (Octavo ed.). Octavo; Schaffer, S. (1989). Glass works: Newton’s prisms and the uses of experiment. In D. Gooding, T. Pinch, & S. Schaffer (Eds.), The uses of experiment: Studies in the natural sciences (pp. 67–104). Cambridge University Press; Al-Khalili, J. (2015). In retrospect: Book of optics. Nature, 518 (7538), 164–165; Herschel, W. (1801). Observations tending to investigate the nature of the Sun, in order to find the causes or symptoms of its variable emission of light and heat; With remarks on the use that may possibly be drawn from solar observations. Philosophical Transactions of the Royal Society of London, 91, 265–318. The urine-fertilizer example is inspired by Wald, C. (2022). The urine revolution: How recycling pee could help to save the world. Nature, 602 (7896), 202–206. The discussion of population validity considers as an example Simon, V. (2005). Wanted: Women in clinical trials. Science, 308(5728), 1517–1517. Discussion of Eddington’s experiment testing Einstein’s relativity theories is based on Dyson, F. W., Eddington, A. S., & Davidson, C. R. (1920). A determination of the deflection of light by the sun’s gravitational field, from observations made at the solar eclipse of May 29, 1919. Philosophical Transactions of the Royal Society A*, 220, 571–581. The discussion of Planck’s constant
---
# 354 Bibliography

Haddad, D., Seifert, F., Chao, L. S., Possolo, A., Newell, D. B., Pratt, J. R., . . . Schlamminger, S. (2017). Measurement of the Planck constant at the National Institute of Standards and Technology from 2015 to 2017. *Metrologia*, 54 (5), 633.

The Herschel case study draws from Herschel, W. (1801). XIII. Observations tending to investigate the nature of the sun, in order to find the causes or symptoms of its variable emission of light and heat; with remarks on the use that may possibly be drawn from solar observations. *Philosophical Transactions of the Royal Society of London*, (91), 265–318.

Box 3.2 draws from Yong, E. (2012). Nobel laureate challenges psychologists to clean up their act. *Nature. https://doi.org/10.1038/nature.2012.11535; Romero, F. (2019). Philosophy of science and the replicability crisis. Philosophy Compass*, 14 (11), e12633.

# CHAPTER 4

Section 4.1’s case study is based on Wooller, M. J., Bataille, C., Druckenmiller, P., Erickson, G. M., Groves, P., Haubenstock, N., . . . Willis, A. D. (2021). Lifetime mobility of an Arctic woolly mammoth. *Science, 373, 806–808; Miller, J. H., Fisher, D. C., Crowley, B. E., Secord, R., & Konomi, B. A. (2022). Male mastodon landscape use changed with maturation (late Pleistocene, North America). Proceedings of the National Academy of Sciences*, 119(25), e2118329119.

Examples of non-experimental studies in section 4.2 are drawn from Broca, P. (1861). Remarques sur le siège de la faculté du langage articulé, suivies d’une observation d’aphémie (perte de la parole). *Bulletins de la Société d’anatomie, 2e serie, 6, 330–357; Chattopadhyay, R., & Duflo, E. (2004). Women as policy makers: Evidence from a randomized policy experiment in India. Econometrica, 72 (5), 1409–1443; Dockery, D. W., Pope, C. A., Xu, X., Spengler, J. D., Ware, J. H., Fay, M. E., & Speizer, F. E. (1993). An association between air pollution and mortality in six US cities. New England Journal of Medicine, 329 (24), 1753–1759; Harlow, J. M. (1848). Passage of an iron rod through the head. Boston Medical and Surgical Journal, 39, 389–393; Harlow, J. M. (1868). Recovery from the passage of an iron bar through the head. Publications of the Massachusetts Medical Society*, 2, 327–347; Kogan, V., & Lavertu, S. (2021). The COVID-19 pandemic and student achievement on Ohio’s third-grade English language arts assessment (p. 14). Early Childhood Longitudinal Study Program. The Ohio State University. https://nces.ed.gov/ecls/.

The phenomenological analysis discussion in section 4.2 draws from Carel, H. (2011). Phenomenology and its application in medicine. *Theoretical Medicine and Bioethics, 32(1), 33–46; Gallagher, S., & Sørensen, J. B. (2006). Experimenting with phenomenology. Consciousness and Cognition, 15(1), 119–134; Carel, H. (2011). Phenomenology and its application in medicine. Theoretical Medicine and Bioethics*, 32, 33–46.

The discussion of thought experiments draws from Brown, J. R., & Fehige, Y. (2022). Thought experiments. In E. N. Zalta & U. Nodelman (Eds.), *The Stanford encyclopedia of philosophy (Winter 2022 ed.). https://plato.stanford.edu/archives/win2022/entries/thought-experiment/; Bokulich, A. (2001). Rethinking thought experiments. Perspectives on Science*, 9, 285–307; (1638). Discourses and mathematical demonstrations concerning two new sciences [Discorsi e Dimostrazioni Matematiche intorno a Due Nuove Scienze, Elsevier, Leiden]; The System of the World, London, 1728. The original version of the third book of the Principia, retitled by the translator and reissued in reprint form, London: Dawsons of Pall Mall, 1969.

Computer simulation discussion based on Adam, D. (2020). Special report: The simulations driving the world’s response to COVID-19. *Nature, 580(7802), 316–319. Big data discussion is influenced by Floridi, L. (2012). Big data and their epistemological challenge. Philosophy and Technology*, 25,
---
# Bibliography

435–437; Lazer, D., Kennedy, R., King, G., & Vespignani, A. (2014). The parable of Google Flu: Traps in big data analysis. *Science, 343 (6176), 1203–1205; Dastin (2018, October 10). Amazon scraps secret AI recruiting tool that showed bias against women. Reuters. Section 4.4 on meta-analysis is based on Kovaka, K. (2022). Meta-analysis and conservation science. Philosophy of Science, 89(5), 980–990; Wernsdorff, M. von et al. (2021). Effects of open-label placebos in clinical trials: A systematic review and meta-analysis. Science*, 11.

  

# CHAPTER 5

Section 5.1’s case study of the Bay model and many other points in the chapter draw from Weisberg, M. (2013). *Simulation and similarity: Using models to understand the world. Oxford University Press. Examples of models in sections 5.2 and 5.3 are drawn from (prisoner’s dilemma) Axelrod, R. (1984). The evolution of cooperation. Basic Books; Rapoport, A., Seale, D. A., & Colman, A. M. (2015). Is tit-for-tat the answer? On the conclusions drawn from Axelrod’s tournaments. PLoS ONE, 10 (7), e0134128. (Lotka-Volterra model) Volterra, V. (1928). Variations and fluctuations of the number of individuals in animal species living together. Journal du Conseil. Conseil Permanent International pour l’Exploration de la Mer, 3, 3–51. (DNA) Watson, J. D. (1968). The double helix. Atheneum Press. (MONIAC) Morgan, M., & Boumans, M. J. (2004). Secrets hidden by two-dimensionality: The economy as a hydraulic machine. In S. de Chadarevian & N. Hopwood (Eds.), Model: The third dimension of science (pp. 369–401). Stanford University Press. The discussion of idealization draws from Potochnik, A. (2017). Idealization and the aims of science. University of Chicago Press; McMullin, E. (1985). Galilean idealization. Studies in the History and Philosophy of Science, 16, 247–273. Section 5.4 draws from Levins, R. (1966). The strategy of model building in population biology. American Scientist, 54, 421–431. Box 5.1 draws from Winsberg, E., & Harvard, S. (2022). Purposes and duties in scientific modelling. Journal of Epidemiology and Community Health*, 76, 512–517.

# CHAPTER 6

The discussion of Aristotle’s views draws on John Philoponus’s (1987). *Against Aristotle on the eternity of the world (C. Wildberg, Trans.). Bristol Classical Press. Hubble’s (1929) paper “A relation between distance and radial velocity among extra-galactic nebulae” was published in Proceedings of the National Academy of Sciences, 15 (3), 168–173. See also Kragh, H., & Smith, R. W. (2003). Who discovered the expanding universe? History of Science, 41 (2), 141–162. For more on Hubble’s discovery from a nonspecialist’s perspective, see Fox, K. C. (2002). The big bang theory. Wiley. The rehearsal of Semmelweis’s case comes from his (1861/1983) book The etiology, the concept and the prophylaxis of childbed fever, and is also discussed in Hempel, C. (1966). Philosophy of natural science. Prentice-Hall. Box 6.3 draws from Wason, P. (1968). Reasoning about a rule. Quarterly Journal of Experimental Psychology, 20, 273–281; Cosmides, L. (1989). The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task. Cognition*, 31 (3), 187–276. Discussion of the JWST reflected in the extensive NASA site: https://webb.nasa.gov/.
---
# 356 Bibliography

# CHAPTER 7

Discussion of the case of poisoned water in Flint, MI, derives from various journalistic sources, including reporting from *Politico, NPR*, and elsewhere. CNN has maintained a list of facts and timeline here:

 

The URL for the US EPA report from (2015), “High Lead Levels in Flint, Michigan” is   

The locus classicus for the problem of induction comes from Hume, D. (1748/1999). *An enquiry concerning human understanding (T. L. Beauchamp, Ed.). Oxford University Press. The discussion of abductive inference draws on Peirce, C. S. (1903/1904) (1931–1936). The collected papers, volumes 1–6 (C. Hartshorne & P. Weiss, Eds.). Harvard University Press. See also Huygens, C. (1690/1962). Treatise on light (S. P. Thompson, Trans.). Dover Publications. The case of continental drift owes to Wegener, A. (1929/1966). The origin of continents and oceans. Dover. Sources for the Jebel Irhoud remains come from Callaway, E. (2017). Oldest Homo sapiens fossil claim rewrites our species’ history. Nature News. https://doi.org/10.1038/nature.2017.22114; see also Hublin, J. J. et al. (2017). New fossils from Jebel Irhoud, Morocco and the pan-African origin of Homo sapiens. Nature*, 546 (7657), 289–292.

# CHAPTER 8

There are many introductions to the theory of probability and its uses in science and everyday life. One enjoyable and accessible introduction is Olofsson, P. (2015). *Probabilities: The little numbers that rule our lives. John Wiley & Sons. The rapid strep test example in section 8.1 is an example of the base-rate fallacy (cf., https://en.wikipedia.org/wiki/Base_rate_fallacy), which is discussed, among many others, by Gigerenzer, G., & Edwards, A. (2003). Simple tools for understanding risks: From innumeracy to insight. BMJ, 327 (7417), 741–744. The estimates we refer to about the carriage rate of strep (Streptococcus pharyngitis) can be found in: Martin, J. (2016). The Streptococcus pyogenes carrier state. In J. J. Ferretti, D. L. Stevens, & V. A. Fischetti (Eds.), Streptococcus pyogenes: Basic biology to clinical manifestations. The University of Oklahoma Health Sciences Center; and Oliver, J., Malliya Wadu, E., Pierse, N., Moreland, N. J., Williamson, D. A., & Baker, M. G. (2018). Group A Streptococcus pharyngitis and pharyngeal carriage: A meta-analysis. PLoS Neglected Tropical Diseases, 12 (3), e0006335. Exercise 8.12 is based on Tversky, A., & Kahneman, D. (1982). Judgments of and by representativeness. In D. Kahneman, P. Slovic, & A. Tversky (Eds.), Judgment under uncertainty: Heuristics and biases (pp. 84–98). Cambridge University Press. Exercise 8.16 is based on Gigerenzer, G. (2008). Rationality for mortals: How people cope with uncertainty (pp. 174ff). Oxford University Press. The three probabilistic biases described in Box 8.2, viz. the conjunction fallacy, neglect of probability, and zero-risk bias, have been widely studied in psychology, economics, law, and philosophy. Seminal studies of each include Tversky, A., & Kahneman, D. (1983). Extensional versus intuitive reasoning: The conjunction fallacy in probability judgment. Psychological Review, 90(4), 293–315. Sunstein, C. R. (2002). Probability neglect: Emotions, worst cases, and law. Yale Law Journal, 112 (1), 61–107. And Allais, M. (1953). Le comportement de l’homme rationnel devant le risque: critique des postulats et axiomes de l’école américaine. Econometrica, 21 (4), 503–546. There are many introductions to the interpretations of probability discussed in section 8.4. A book-length treatment is Gillies, D. (2000). Philosophical theories of probability*. Routledge. A shorter, article-length introduction is Galavotti, M.
---
# Bibliography

C. (2015). Probability theories and organization science: The nature and usefulness of different ways of treating uncertainty. Journal of Management, 41(2), 744–760.

# CHAPTER 9

 

  

There are many introductions to statistical reasoning. One comprehensive resource relevant to the content of Chapters 9 and 10 is Freedman, D., Pisani, R., & Purves, R. (2007). Statistics (4th ed.). W. W. Norton & Company. A helpful, free, online textbook is Daniel Lakens’s Improving your statistical inferences. https://lakens.github.io/statistical_inferences/

The statistics about world religions presented in section 9.1 come from recent reports by the PEW Research Center (www.pewresearch.org/topic/religion/): Pew Research Center, November 10, 2020, “In 2018, government restrictions on religion reach highest level globally in more than a decade”; Pew Research Center, April 11, 2017, “Global restrictions on religion rise modestly in 2015, reversing downward trend”; Pew Research Center, April 5, 2017, “The changing global religious landscape.”

The research about loud bars and alcohol consumption in section 9.2 is reported in Guéguen, N., Jacob, C., Le Guellec, H., Morineau, T., & Lourel, M. (2008). Sound level of environmental music and drinking behavior: A field experiment with beer drinkers. Alcoholism: Clinical and Experimental Research, 32(10), 1795–1798.

Part of Galton’s work on correlation can be found in Galton, F. (1889). Natural inheritance. Macmillan. Box 9.1 on the history of statistics and eugenics is based on Bodmer, W., Bailey, R. A., Charlesworth, B., Eyre-Walker, A., Farewell, V., Mead, A., . . . Senn, S. (2021). The outstanding scientist, R.A. Fisher: His views on eugenics and race. Heredity, 126, 565–576. https://doi.org/10.1038/s41437-020-00394-6; Gillham, N. W. (2001). Sir Francis Galton and the birth of eugenics. Annual Review of Genetics, 35(1), 83–101; Wijsen, L. D., Borsboom, D., & Alexandrova, A. (2022). Values in psychometrics. Perspectives on Psychological Science, 17(3), 788–804.

The medical example in section 9.4 concerning the impact of relative vs. absolute risks on understanding risk comes from Kurz-Milcke, E., Gigerenzer, G., & Martignon, L. (2008). Transparency in risk communication: Graphical and analog tools. Annals of the New York Academy of Sciences, 1128(1), 18–28. The bar graphs in this section are based on their Figure 4.

Another concise and helpful reference here is Spiegelhalter, D., Pearson, M., & Short, I. (2011). Visualizing uncertainty about the future. Science, 333(6048), 1393–1400.

The study of correlations between cancer and food ingredients in section 9.4 is Schoenfeld, J. D., & Ioannidis, J. P. (2013). Is everything we eat associated with cancer? A systematic cookbook review. The American Journal of Clinical Nutrition, 97(1), 127–134.

The case of IQ, education, and SAT scores in the US is based on Sackett, P. R., Kuncel, N. R., Arneson, J. J., Cooper, S. R., & Waters, S. D. (2009). Does socioeconomic status explain the relationship between admissions tests and post-secondary academic performance? Psychological Bulletin, 135(1), 1–22.

Nisbett, R. E. (2013). Schooling makes you smarter: What teachers need to know about IQ. American Educator, 37(1), 10–39.

Ritchie, S. J., & Tucker-Drob, E. M. (2018). How much does education improve intelligence? A meta-analysis. Psychological Science, 29(8), 1358–1369.

On IQ and intelligence more generally, a helpful resource is Ritchie, S. (2015). Intelligence: All that matters. John Murray.

Box 9.2 on panic headlines refers to “Panic Headlines: Alcohol Changes Face Shape, Induction Lowers IQ,” ParentData by Emily Oster newsletter, e-mailed March 9, 2023.

The GDP and austerity case in section 9.4 concerns research reported in Reinhart, C. M., & Rogoff, K. S. (2010). Growth in a time of debt. American Economic Review, 100(2), 573–578.

Websites containing information about several real-life examples of bad data visualizations, which we
---
# 358 Bibliography

discuss in section 9.4, include www.statisticshowto.com/misleading-graphs/ and https://venngage.com/blog/misleading-graphs/#Using-the-wrong-graph. On article-length advice about data visualizations, see Wolfe, J. (2015). Teaching students to focus on the data in data visualization. *Journal of Business and Technical Communication, 29(3), 344–359. Chen, C. (2010). Information visualization. Wiley Interdisciplinary Reviews: Computational Statistics, 2(4), 387–403. The research on statistical reporting inconsistencies in psychology referenced in section 9.4 is by Nuijten, M. B., Hartgerink, C. H., Van Assen, M. A., Epskamp, S., & Wicherts, J. M. (2016). The prevalence of statistical reporting errors in psychology (1985–2013). Behavior Research Methods, 48, 1205–1226. Similar research showing a lower rate of misreporting in experimental philosophy compared to psychology is by Colombo, M., Duev, G., Nuijten, M. B., & Sprenger, J. (2018). Statistical reporting inconsistencies in experimental philosophy. PLoS One*, 13(4), e0194360. Exercise 9.23 is based on https://marketinglaw.osborneclarke.com/retailing/colgates-80-of-dentists-recommend-claim-under-fire/ and Exercise 9.24 is based on www.washingtonpost.com/politics/2021/09/28/tucker-carlson-ties-his-vaccine-fearmongering-core-republican-insecurity/

# CHAPTER 10

There are many introductions to statistical reasoning. Relevant to the content of this chapter and Chapter 9 is Freedman, D., Pisani, R., & Purves, R. (2007). *Statistics (4th ed.). W. W. Norton & Company. A helpful, free, online textbook is Daniel Lakens’s Improving your statistical inferences. The discovery of the Higgs boson described in section 10.1 is by Chatrchyan, S., Khachatryan, V., Sirunyan, A. M., Tumasyan, A., Adam, W., Aguilo, E., . . . Friedl, M. (2012). Observation of a new boson at a mass of 125 GeV with the CMS experiment at the LHC. Physics Letters B, 716(1), 30–61. The 68–95–99.7 rule we cover in section 10.2 is explained in more detail in Pukelsheim, F. (1994). The three sigma rule. The American Statistician, 48(2), 88–91. Our discussion of confidence intervals on page is especially indebted to Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E. J. (2014). Robust misinterpretation of confidence intervals. Psychonomic Bulletin & Review, 21(5), 1157–1164. The example of nonrandom sampling relies on Squire, P. (1988). Why the 1936 Literary Digest poll failed. Public Opinion Quarterly, 52(1), 125–133. The tea tasting experiment described in section 10.3 is from Fisher, R. A. (1956). Mathematics of a lady tasting tea. In J. R. Newman (Ed.), The world of mathematics (pp. 1512–1521). Simon & Schuster. (Original work published in Fisher, R. A. (1935). The design of experiments. Oliver and Boyd.) The discussion of statistical significance is indebted especially to Gelman, A., & Stern, H. (2006). The difference between “significant” and “not significant” is not itself statistically significant. The American Statistician, 60(4), 328–331. For the association between genes and smoking behavior, see Thorgeirsson, T. E., Gudbjartsson, D. F., Surakka, I., Vink, J. M., Amin, N., Geller, F., . . . Gieger, C. (2010). Sequence variants at CHRNB3-CHRNA6 and CYP2A6 affect smoking behavior. Nature Genetics, 42(5), 448–453. The criticism in section 10.4 that NHST says nothing about the probability different hypotheses are true is partly based on work by Cohen, J. (1994). The earth is round (p < .05). American Psychologist, 49(12), 997–1003. The second criticism of NHST is partly based on Lindley, D. V. (1993). The analysis of experimental data: The appreciation of tea and wine. Teaching Statistics, 15, 22–25. The problem of the prior we discuss is based on Gelman, A., & Hennig, C. (2017). Beyond subjective and objective in statistics (with discussion). Journal of the Royal Statistical Society*, 180(4), 967–1033. https://doi.org/10.1111/rssa.12276.
---
# Bibliography

# CHAPTER 11

For the statistical information on poverty in section 11.1 we relied on United Nations. Department of Economic and Social Affairs. (2022). *The sustainable development goals: Report 2022*. UN. https://unstats.un.org/sdgs/report/2022.

Causal evidence about the relationships between poverty and psychiatric conditions is discussed in Ridley, M., Rao, G., Schilbach, F., & Patel, V. (2020). Poverty, depression, and anxiety: Causal evidence and mechanisms. *Science*, 370(6522), eaay0214.

Another key reference here is: Sen, A. (1983). Poor, relatively speaking. *Oxford Economic Papers*, 35(2), 153–169.

The experiment on poverty in Niger is by Banerjee, A., Duflo, E., Goldberg, N., Karlan, D., Osei, R., Parienté, W., & Udry, C. (2015). A multifaceted program causes lasting progress for the very poor: Evidence from six countries. *Science*, 348(6236), 1260799.

Evidence about the bearing of cash transfers on temptation goods is discussed in Evans, D. K., & Popova, A. (2017). Cash transfers and temptation goods. *Economic Development and Cultural Change*, 65(2), 189–221.

One of the major works in philosophy, where Hume engaged with questions about causation, is Hume, D. (1738/2007). *A treatise of human nature* (D. F. Norton & M. J. Norton, Eds.). Clarendon Press.

Evidence that “poverty in childhood can have effects much later in life, and poverty rates are influenced by geopolitical events that occur far away in time and space” is presented in Duncan, G. J., Magnuson, K., & Votruba-Drzal, E. (2017). Moving beyond correlations in assessing the consequences of poverty. *Annual Review of Psychology*, 68, 413–434.

The Israeli case in Box 11.1 is described in Wadman, M. (2021). A grim warning from Israel: Vaccination blunts, but does not defeat Delta. *Science*, 373(6557), 838–839.

For more on the Simpson’s paradox, see Sprenger, J., & Weinberger, N. (2021). Simpson’s paradox. In E. N. Zalta (Ed.), *The Stanford encyclopedia of philosophy* (Summer 2021 ed.). https://plato.stanford.edu/archives/sum2021/entries/paradox-simpson/.

One key reference for the difference making account of causation in section 11.2 is Woodward, J. (2003). *Making things happen: A theory of causal explanation*. Oxford University Press.

One reference on physical process theories of causation is Salmon, W. (1984). *Scientific explanation and the causal structure of the world*. Princeton University Press.

The methods presented in Box 11.3 were originally developed in Mill, J. S. (1893). *A system of logic, ratiocinative and inductive: Being a connected view of the principles of evidence and the methods of scientific investigation*. Harper & brothers.

The scenario described in section 11.4 is a direct quotation from page 30 of Korb, K., & Nicholson, A. (2010). *Bayesian artificial intelligence* (2nd ed.). Chapman & Hall/CRC.

Scientific applications of Bayes nets are explained and discussed in more detail in e.g. Glymour, C. (2007). When is a brain like the planet? *Philosophy of Science*, 74(3), 330–347.

The example of the two lamps and the principle of common cause is from Reichenbach, H. (1956). *The direction of time* (p. 157). University of California Press.

Many cases of “spurious” correlations often explained by the presence of some common cause are discussed in Vigen, T. (2015). *Spurious correlations*. Hachette Books.

Several fun examples of spurious correlations are also available at the website: www.tylervigen.com/spurious-correlations.

# CHAPTER 12

The case study of depression in section 12.1 draws from Sohn, E. (2022). Tackling the mental-health crisis in young people. *Nature*, 608, S39–S41. https://doi.org/10.1038/d41586-022-02206-9; also the WHO fact sheet on depression, www.who.int/news-room/fact-sheets/detail/depression.

Section 12.2 on explanation draws from Gopnik, A. (1998). Explanation as orgasm. Minds and
---
# 360 Bibliography

Machines, 8(1), 101–118; Weisberg, D. S., Keil, F. C., Goodstein, J., Rawson, E., & Gray, J. R. (2008). The seductive allure of neuroscience explanations. Journal of Cognitive Neuroscience, 20(3), 470–477. The discussion of explanation is also influenced by Strevens, M. (2004). The causal and unification accounts of explanation unified—causally. Noûs, 38, 154–179. The mention of the illusion of explanatory depth is based on Rozenblit, L., & Keil, F. (2002). The misunderstood limits of folk science: An illusion of explanatory depth. Cognitive Science, 26(5), 521–562. The discussion of scientific revolutions in section 12.3 is based on Kuhn, T. (1962/1970). The structure of scientific revolutions. University of Chicago Press (1970, 2nd ed., with postscript). The discussion of the chemical revolution draws from Donovan, A. (1993). Antoine Lavoisier: Science, administration, and revolution. Blackwell; the Lavoisier quote is drawn from this source as well. The discussion of Merton’s priority rule is based on Merton, R. K. (1957). Priorities in scientific discovery: A chapter in the sociology of science. American Sociological Review, 22(6), 635–659.

# CHAPTER 13

The case study about sexual selection draws from Roughgarden, J. (2004). Evolution’s rainbow. University of California Press and (2009). The genial gene. University of California Press; Hrdy, S. B. (1874). Empathy, polyandry, and the myth of the coy female. In E. Sober (Ed.), Conceptual issues in evolutionary biology. Darwin, C. (1874). The descent of man, and selection in relation to sex (2nd ed.). John Murray; Knight, J. (2002). Sexual stereotypes. Nature, 415, 254–256. The mention of helicopter research is influenced by Minasny, B., Fiantis, D., Mulyanto, B., Sulaeman, Y., & Widyatmanti, W. (2020). Global soil science research collaboration in the 21st century: Time to end helicopter research. Geoderma, 373, 114299. The discussion of diversity in science and participatory research are influenced by Angela Potochnik’s forthcoming Science and the public, elements in philosophy of science (J. Stegenga, Ed.). Cambridge University Press. Section 13.3’s discussion of how values influence science is guided by Elliott, K. C. (2017). A tapestry of values: An introduction to values in science. Oxford University Press. Section 13.4 on changes and challenges in science is influenced by Jumper, J., Evans, R., Pritzel, A., Green, T., Figurnov, M., Ronneberger, O., & Hassabis, D. (2021). Highly accurate protein structure prediction with AlphaFold. Nature, 596(7873), 583–589; Callaway, E. (2022). What’s next for the AI protein-folding revolution. Nature, 604, 234–238; Lucier, P. (2019). Can marketplace science be trusted? Nature, 574, 481–485. The cancer-risk of food example comes from Schoenfeld, J. D., & Ioannidis, J. P. (2013). Is everything we eat associated with cancer? A systematic cookbook review. The American Journal of Clinical Nutrition, 97(1), 127–134.
---
# Index

 

  

Note: Page numbers in italic indicate a figure and page numbers in bold indicate a table on the corresponding page.

- abductive inference 164 – 165, 172 – 179, 181 – 182
- autism 27, 319
- auxiliary assumptions 153 – 155
- abductive reasoning 161 – 184, 265, 296, 328
- abstraction 128, 130 – 131
- accuracy 129 – 131, 131
- Axelrod, Robert 125, 127, 130
- addition rule 194 – 196, 196, 200
- axiomatic methods 155 – 159
- affirming the antecedent 139 – 147
- affirming the consequent 139, 145 – 147, 175
- al-Bīrūnī, ibn Aḥmad 52
- background conditions 61, 298, 302
- alchemy 307
- bacteria: streptococcus 187
- bad arguments, uncovering 144 – 147
- al-Khwārizmī, ibn Mūsā 52
- bar charts 216 – 220, 225 – 226, 233 – 235
- ampliative inferences 164 – 165
- analogical models 120 – 122, 121 – 122
- anomaly 56, 307, 309
- antecedents 139 – 148
- anti-vaccination advocacy 27
- appeal to ignorance 147
- appeal to irrelevant authority 13
- applied research 16, 20, 58
- archaeology 85, 90
- arguments 43, 134 – 139, 146 – 150, 155 – 156, 337; publication 336; random variables and 68, 191 – 192, 238
- Big Bang theory 146, 311
- Aristotle 52, 134, 137 – 138, 141, 304, 307
- big data 97 – 101, 332 – 335
- bimodal distribution 219 – 220, 226
- black holes 18
- blind experiments 68
- brain: activity 48, 87, 286; areas or regions 77, 83, 286; damage 25; metabolism 77
- Broca, Paul 87, 87
---
# 362 Index

Callendar, Guy 10 confounding variables 63 – 64, 67 – 68, 88 – 89, California 106 – 107 101 – 102

Cal Tech 25 consequent 139 – 145, 147 – 150

calx 307 continental drift 172 – 174, 176, 179

cancer 37 – 38, 283 – 287, 285 control groups 66 – 68, 71 – 74, 85 – 87,  

carbon dioxide, atmospheric see climate change 99 – 101, 279 – 281   

Carlsson, Arvid 16, 321 Copernicus, Nicolaus 51, 53 – 54

Cartwright, Nancy 273 correlated variables 216, 221, 287

case studies 89 – 90 correlation 221 – 226, 233 – 242, 260 – 261, causal background 277 – 283

causal Bayes nets 282, 284, 286 – 288, 290

counterexamples 147

causal hypotheses 269 – 270, 278 – 282 creationism and intelligent design 27

causal modeling 282 – 289

Crick, Francis 119, 120 – 121, 310, 321 – 322

causation 236, 239 – 240; accounts of 274 – 276; causal modeling 282 – 288; clues

crucial experiments 74 – 76, 153 curve-fitting 118, 126

Centers for Disease Control and Prevention (CDC) 167

central limit theorem 245 central tendency 227 – 232

CERN (European Organization for Nuclear Research) 61

Cepheid variable 136 chemical revolution 306 – 308

classical statistics 261 – 265 cleansing, data 117, 238

Clever Hans 21 – 22, 22, 25

climate change 8 – 15, 14, 28 – 32, 296 – 297, 326 – 327, 330 – 332

cluster indicators 67 cohort studies 86, 89, 92

collaborative experiments 62 collecting data 48, 52, 63, 67 – 68, 214, 325

collectively exhaustive outcomes 196 color 58 – 64, 72 – 75, 78 – 79, 243 – 244, 315 – 318

common cause 37, 273, 283, 287 – 289

computer models 120, 125, 128, 132 – 133

computer simulations 96 – 97, 100 – 104, 125

conditional probability 197 – 201, 277 – 278

conditionals 275 conditional statements 139 – 142, 144 – 145, 147 – 149

confirmation bias 20 – 21, 26, 327 conflicts of interest 25, 337

deductive arguments 138 – 144, 164 – 166 defining science 26 – 31, 40

denying the antecedent 139, 144, 147 denying the consequent 142 – 144, 147 – 150

dependent variables 63 – 69 descriptive statistics 212 – 217, 246 – 247

Clever Hans 21 – 22, 22, 25 de Vlamingh, Willem 167

difference-making 274 – 278, 281 – 283 directed acyclic graphs 284, 228

direct variable control 65 – 71, 92 – 93, 278 – 279

disease: germ theory of 34 – 39, 313; heart 35 – 38, 41 – 42, 273; Parkinson’s 16, 93, 311; sexually transmitted 1; syphilis 319, 328

distal causes 272, 277 diversity in science 56, 322 – 323, 326

DNA (deoxyribonucleic acid) 119 – 121, 119, 321 – 322

Doppler, Christian 136 – 137 Doppler effect 136 – 137

double-blind experiments 68 drinking water 9, 88, 108, 161, 184, 330

Du Châtelet, Émilie 78, 80

Duhem, Pierre 154 Duhem-Quine problem 148, 154 – 155
---
# Index

363

# Early Childhood Longitudinal Study

false positives 10, 258 – 259, 265, 329

# earthquakes

173

# ecological validity

70, 73, 102, 104

# economics

266 – 269, 298 – 299

# Eddington, Arthur

74 – 75, 153

#  

# Edwards, Marc

162

# Flint, Michigan, water crisis

161 – 165, 163

#   

# effect size

102, 257 – 261, 336 – 337

# Franklin, Rosalind

120

# Einstein, Albert

74 – 75, 302 – 304

# electromagnetic radiation

79

# Elements of Geometry

155 – 156, 156

# fruit flies (Drosophila melanogaster)

111, 114

# Elliott, Kevin

328 – 330, 339

# functional magnetic resonance imaging (fMRI)

# empirical evidence

17 – 19, 23 – 24, 27 – 29, 48, 77

# errors, sampling

215, 249 – 251

# Ethyl Corporation

25

# Euclid

155 – 160, 304, 310

# eugenics

225, 319

# Europe

51 – 52

# European Organization for Nuclear Research

see CERN (European Organization for Nuclear Research)

# evidence, empirical

17 – 19, 23 – 24, 27 – 29, 41 – 43

# evidentialism

15 – 20, 28 – 29

# evolution, theory of

263, 293 – 294, 300, 309 – 310, 315

# exemplar

110 – 111

# experimental groups

66 – 68, 71 – 74, 279 – 281

# experimentation, modeling as

126 – 127

# experiments:

blind 68; case studies and natural 86 – 88, 92, 168; collaborative 62; crucial 74 – 76, 80, 153; double blind 68; experimental setup of 60, 67, 69, 76, 79; exploratory 74, 78, 81, 97; field 70, 73, 168; intervention 85, 276, 278 – 279, 282; laboratory 65, 69; on light 58 – 60; perfectly controlled 63 – 64; replication of 336; thought 93 – 97, 100 – 101, 104 – 105

# explanation:

causal 287, 301 – 303; natural 15 – 17, 27 – 32; nomological 298 – 300

# explanatory knowledge

12, 15, 295

# external experimental validity

69, 73, 102, 281

# extraneous variables

64 – 66, 68 – 70, 72 – 74, 85 – 92, 279 – 281, 329 – 331

# Gage, Phineas

288

# Galilei, Galileo

54, 94

# Gallup polls

250

# Galton, Francis

222 – 224, 233

# gambler’s fallacy

191 – 192, 203

# game theory

123 – 124

# Gaussian distribution

226

# generality

129 – 130

# generalizations, inductive

165, 168, 171

# geocentrism

48 – 49, 52, 306, 309

# geometry

52, 155 – 157, 160, 310

# Gianotti, Fabiola

242

# glaciers

9, 12, 29, 62

# global warming

9, 14, 18, 146, 179, 198, 269, 296 – 299, 230

# Google Flu Trends

99

# Gopnik, Alison

51, 296

# greenhouse gases

9 – 10, 13, 16, 29, 298

# Hansen, James

330

# Harvard University

35, 38

# Hauser, Marc

24

# Heezen, Bruce

173, 174

# heliocentrism

48 – 49, 51, 53 – 54, 306, 309

# Hempel, Carl

150, 298

# heredity

222, 233

# Herschel, William

78 – 79, 79

# Higgs boson

241 – 246, 252 – 254

# Hindu-Arabic numeral system

52

# histograms

216 – 220, 225 – 233, 243 – 247

# history of science

309, 323

# Homo sapiens

177 – 178, 178
---
# 364 Index

Hubble, Edwin    134 – 138, 147 – 150

human reasoning, flaws in    20 – 22

James, LeBron    192, 242 – 243

Jebel Irhoud (Morocco)    177

Hume, David    170, 185, 271, 274, 277

joint method of agreement and difference    280

Huygens, Christian    176

joint probability distributions    283

hypotheses: alternative    59, 69 – 75, 253 – 256, justification    147 – 148

 

  

259 – 262; deductive reasoning in testing    5, 153 – 154, 165 – 166; null    252 – 262, 280 – 281; testing causal    269 – 270, 278 – 281

Kahneman, Daniel    76

Keeling, C. David    11, 23

Keeling Curve    11, 11, 23

Kehoe, Robert A.    25

Kekulé, Friedrich August    40

Kepler, Johannes    54

Ibn al-Haytham    52, 58, 81, 156

Ibn Rushd    52

Ibn Sina    52

ice cores    12

illusion of explanatory depth    296 – 297, 303

illusion of understanding    14

importance of science    23

incentive structure in science    335

independent outcomes    190 – 198

independent variables    63 – 68

indigenous knowledge    50, 55 – 57, 326

indirect variable control    65 – 68, 92 – 93, 278 – 279

Industrial Revolution    9, 12, 12, 29

inferences: abductive    138, 161, 164 – 165, 172 – 184, 312; ampliative    161 – 165, 174; bad reasons to reject    146 – 147; deductive reasoning    134 – 159; inductive    164 – 172, 174 – 175; sound    144, 147; strength of    166 – 168

inference to the best explanation    5, 164, 185, 296, 312

inferential statistics    211 – 216, 242 – 243, 246 – 247, 252 – 253, 280

ingenuity    157

Inhofe, James    297

instruments    60 – 61, 75 – 77, 153 – 154

Intergovernmental Panel on Climate Change (IPCC)    13

internal experimental validity    69, 73, 74, 102

material conditionals    140, 275

mathematical models    113, 122 – 123, 126 – 132, 155 – 159, 159
---
# Index

Matilda effect 321, 345

natural phenomena 15 – 17, 28 – 32

Mauna Loa Observatory (Hawai’i) 11

natural selection 310 – 311

Maxwell, James 79

mean 227 – 229, 228, 232, 247 – 251, 260 – 261; regression to the 224

 

measles, mumps, and rubella (MMR) vaccine 319

  

measurement error 215, 238, 329

mechanistic models 120 – 122, 122

Mill’s methods 280

methods 45 – 46; axiomatic 155 – 157, 156

normal distribution 226 – 227, 232 – 233;

different 41 – 43; hypotheses 46 – 47; myth of the scientific method and 40 – 41, 40;

observation 47 – 49, 49; in science 17 – 19

norms, social 23 – 25

Michotte, Albert 271

Mill, John Stuart 280

mode 227 – 229

models: analogical 120 – 122; Bay Model 106 – 109, 107

computer 120, 125, 128, 132 – 133; of data 117 – 118; as experimentation and theorizing 126 – 127; mathematical 122 – 123, 126 – 132, 155 – 159; mechanistic 120 – 122;

of phenomena 117 – 119; scale 109, 118 – 120; and targets 109 – 111, 110

of 119, 125 – 126

modern synthesis 319

modularity 287, 289

modus ponens 141 – 143

modus tollens 142 – 143

Monetary National Income Analogue Computer (MONIAC) 120

Montagu, Kathleen 16, 321

Mount Wilson Observatory (California) 136

multiplication rule 194 – 196, 200, 257

mutually exclusive outcomes 193

NASA (National Aeronautics and Space Administration) 158 – 160, 331

National Institutes of Health 168

National Institute of Standards and Technology (NIST) 77

National Research Council 11

natural experiments 86 – 88

natural explanations 15 – 17, 28 – 32

naturalism 16 – 17, 28 – 29

Phillips, William 120

Phillips machine (MONIAC) 120 – 121, 121

Pangaea 172

paradigms 305 – 313; pre-paradigmatic phase of science 305 – 306

parameters 111 – 116, 122 – 123

Paris Agreement 8, 198

partial cause 276 – 277

Patterson, Clair 25, 134

Payne-Gaposchkin, Cecilia 321

payoff matrix 123 – 124

Peano, Giuseppe 157

perfectly controlled experiments 63 – 64

Pfungst, Oskar 22

phenomena: models of 117 – 119, 125 – 127; natural 15 – 17, 27 – 32, 39 – 42
---
# Index

# philosophy of science

3 – 7

# reasoning

abductive 161 – 184; causal 267 – 289; deductive 134 – 159; statistical 211 – 239

# phrenology

21

# physical constants

77 – 78

# physical processes

274 – 276

# pie charts

214 – 218, 225 – 226, 233

# placebo effect

68, 102 – 103

# plagiarism

6, 24

# Planck, Max

77 – 78

# plate tectonics

174

# pollution

36 – 37, 41 – 42, 118, 284 – 287

# Popper, Karl

18 – 19, 26 – 28

# population validity

69 – 71, 102

# positive correlation

221, 223 – 224

# posterior probability

202 – 204, 263, 285

# power

63 – 68

# predictions

27 – 30, 40 – 43, 52 – 54, 97 – 100, 112 – 116, 130 – 132, 162 – 164, 169 – 171, 188 – 189, 242 – 251, 286 – 287

# Priestley, Joseph

307 – 308

# prior probability

201, 204, 262 – 265

# prisoner’s dilemma

123 – 127, 130 – 132

# probability distributions

244 – 249, 253 – 256, 281 – 287

# probability theory

190 – 194, 207 – 209, 241 – 246

# problem of induction

165, 169 – 172, 185

# projections, inductive

168 – 169

# proximate causes

272, 277

# pseudoscience

26 – 33

# psychology

30 – 31, 91 – 93

# Ptolemy

52 – 53

# publication bias

336

# puerperal fever

150 – 153, 151, 152

# p-value

256 – 262

# qualitative data

90, 92, 228

# qualitative variables

217, 227 – 228

# quantitative data

90

# quantitative variables

218, 221, 225

# questionnaires

60, 67, 77, 117, 247 – 248

# Quine, Willard van Orman

154

# randomization

66, 255

# random sampling

70, 278 – 282

# rapid strep test

186 – 187, 187

# rational degree of belief

2205, 207, 262 – 263
---
# Index

challenges facing 12 – 14; value-free ideal in sufficient condition 139 – 141, 144, 147

scientific breakthroughs 303 – 308

scientific law 296 – 302

scientific method 39 – 45, 328 – 330

scientific progress 19, 81, 309 – 313

Scientific Revolution 50 – 57, 304 – 309

Tapestry of Values, A 328

scientific theories 291 – 294

self-correction 332, 335 – 337

self-explanation effect 296

self-interest 126

Semmelweis, Ignaz 150 – 155

significance level 256 – 261, 264

Simpson’s paradox, Edward 273 – 274

skepticism 24 – 26, 180 – 182, 172, 274

social context, science in 315 – 320

social norms 23 – 26, 32 – 33

social sciences 37, 81, 90, 294

sound inferences 144, 147

space exploration 331

spatiotemporal contiguity as guide to causation 271 – 274

spurious correlations 236 – 237

Stahl, Georg Ernst 307

standard deviation 227 – 233, 245 – 251, 255 – 257, 260 – 261

standard error 249 – 251, 266

Stapel, Diederik 24

State Research Centre of Virology and Biotechnology 167

statistical evidence 211, 273

statistically independent variables 192, 198, 221, 225

statistical significance 256 – 260

statistics: descriptive (see descriptive statistics); inferential (see inferential statistics); probability theory in 190 – 194, 207 – 209, 241 – 246

Stellar Atmospheres 321

string theory 16, 18

Structure of Scientific Revolutions, The 305, 314

Stumpf, Carl 21 – 22

subject matter, defining science by its subjects, experimental 21, 66 – 70, 76, 169

subtraction rule 195 – 197

sufficient causes 276

value-free ideal 327 – 328

value of a variable 63

Trump, Donald 330

trust 182 – 184

truth 141 – 150, 181 – 182, 311 – 313

Turing, Alan 313, 321 – 322

Tuskegee Syphilis Experiment 319, 328

type I error 258, 260, 329, 337

type II error 252, 258, 260, 329

understanding 1 – 5; illusion of 14; illusion of explanatory depth and 296 – 297

unification conception of explanation 299

uniform distribution 220, 226

uniformity of nature 170 – 171

UC Berkeley 311

US Army Corps of Engineers 109

US Public Health Service 319, 328

vaccinations 1 – 2

validity: deductive reasoning and 138 – 139, 144, 147; ecological 70, 73, 102 – 104; population 69 – 71, 102
---
# 368 Index

values: trust and objectivity 331

value-free ideal visualization, data 357–358

and 327 – 328

visual representation of values of variables 217

variability 227 – 232; measures of 231 221, 234, 283

variables; controlling 64 – 66; correlated 221,

Volterra, Vito 113

287; qualitative 217, 227 – 228; quantitative 218, 221, 225; random 190 – 193,

197 – 198, 216 – 217, 227 – 229, 243 – 245;

Wallace, Alfred Russel 40, 310 – 311

value of 283

water crisis, Flint, Michigan 161 – 164

Watson, James 120 – 121, 310

Wegener, Alfred 172 – 173

women in science 321

virus: Covid-19 1 – 2, 34 – 38, 36, 41 – 42,

88 – 89, 273; ebola 258; human papilloma

virus (HPV) 1; smallpox (variola) 167 – 168;

Zika 328

World Health Organization (WHO) 1, 7,

34, 167

World War II 10, 321