## CHAPTER 8 Probabilistic reasoning

### 8.1 MEDICAL TESTING AND USES OF PROBABILITIES

After reading this section, you should be able to:

- Explain why medical tests don’t provide guarantees of whether one has a medical condition
- Describe how probability relates to uncertainty and inductive reasoning and give examples of reasoning with probabilities
- Describe three ways probabilities can relate to objective features of the world and to individuals’ beliefs

#### Rapid strep tests

You have a sore throat and so you go to the doctor. The doctor examines your throat and calls for a rapid strep test. While you wait for her to return with the results, you wonder how you should react to the news she brings.

What if she tells you the test was negative? Of course, this doesn’t mean you aren’t sick at all, but does it mean you don’t have strep throat? Not necessarily. A negative result means there’s an approximately 95% chance that you don’t have strep throat. Think about it this way. If you receive 20 rapid strep tests with negative results over the years, about one of those will be a negative result when you actually do have strep throat. So, if you have all the symptoms of the illness, your doctor may want to follow up with another test, called a strep culture, to verify the negative result. Even with the negative result on the rapid strep test, strep bacteria might be lurking there, undetected.

What if your doctor tells you the test was positive? Then you can be pretty certain you do have strep bacteria in your throat. However, about 15%–20% of people are carriers for strep. In other words, one out of every five or six people with strep bacteria in their throat do not have any symptoms of illness. So, even if strep bacteria are present, there’s a chance this isn’t the cause of your sore throat. Of course, because you do have a sore throat, a positive rapid strep test is a pretty good indicator that you are suffering from strep throat. So, when a doctor sees a positive rapid strep test result, they generally prescribe antibiotics right away. Strep throat responds very well to antibiotic treatment, and it’s a good idea to get rid of strep bacteria even if it isn’t causing your symptoms.

The rapid strep test, like most medical tests, gives you statistical data. Medical tests generally don’t guarantee the presence or absence of a medical condition, but instead predict the medical condition with some probability—making it somewhat or very likely, or somewhat or very unlikely. So, with any medical test result, you and your doctor need to decide how to interpret the statistical data, how strong of evidence it provides for the presence or absence of the condition, and what steps to take next.

#### Uses of probabilities

Uncertainty is a fundamental, unavoidable feature of life. This should be obvious from the discussion of inductive reasoning in Chapter 7. As you’ll recall, induction is the main mode of reasoning both in ordinary life and in science. We have seen that, unlike deductive reasoning, induction is risky, since it does not guarantee the truth of its conclusions. For this reason, scientific knowledge based on inductive reasoning is always uncertain to some degree.

Thinking in terms of probabilities is a way to systematically and reliably reason under uncertainty and to represent the degree of uncertainty of the conclusions we draw.

Tools developed to work with probabilities inform inductive and statistical techniques for quantifying uncertainty and the strength of inductive inferences, and for making inferences under uncertainty. Consider questions like: How should economists price options? How should insurance companies calculate risks? What role do random mutations play in biological processes? What’s the chance that my child will inherit a particular trait of mine? What’s the chance you have some illness given a positive test result? Reasoning with probabilities helps scientists answer these and many other questions. Even quantum mechanics, the fundamental laws of physics, are probabilistic: physicists can make only probabilistic predictions, and they can explain only in probabilistic terms how the world we are familiar with relates to fundamental particles.

We regularly encounter probabilities in our everyday lives, too. Probability calculations guide (or at least should guide) betting and gambling, determining insurance premiums, forecasting the weather, predicting the outcome of elections, and much more. You, just like anybody else, often make probabilistic judgments. Consider comments like: “I am 100% sure they will win the prize!”; “There is a one-in-a-billion chance I will be selected for that job”; or “What are the odds he will finish the marathon?” We typically use probabilities to ask or to describe how likely something is to occur or how confident we are that some belief or hypothesis is true.

Let’s consider these uses of probabilities in a bit more depth:

1. Figuring out the likelihood of a random mutation or of getting a particular hand of cards in poker.
2. Predicting whether the stock market will go up or the weather will become colder.
3. Judging whether Inter Milan will win the next Champions League, whether there is life outside Earth, or whether you’ll pass the final exam.

These uses of probabilities differ from one another. In the first set of examples, (1), probability seems to be an objective feature of the world. Random mutations are just that: random. Whether one occurs is a matter of chance. We can calculate how likely a random mutation is to occur in general, but we can’t predict when a particular mutation will occur. Similarly, poker and other card games are designed to start from a randomized hand of cards. This is why you shuffle a deck of cards and deal them in a standard way. In fact, these types of gambling situations first motivated mathematicians to develop a rigorous theory of probability and to systematically study situations involving uncertainty using that theory.

In the second set of examples, (2), probability seems to relate to objective features of the world, as with (1). But for (2), we have to rely on data to infer the probabilities of different outcomes. Economists use observations about the economy and markets, like the price of certain goods and past trends in the stock market (and a variety of models), to predict whether the stock market will go up and down. Meteorologists use a wide variety of data about weather patterns (and intricate computer simulations) to develop a 10-day weather forecast for locations all over the world. As new data become available, these probabilities may change to represent new states of uncertainty. This is why tomorrow’s weather forecast is more accurate than the forecast for 10 days from now.

The third set of examples, (3), are judgments about outcomes that probably are not due to chance. In these instances, the probability isn’t an objective feature of the world or our best estimation of probabilistic features of the world. Instead, the probability reflects your degree of confidence that some outcome will happen or that some hypothesis is true. These probabilities might be different for people with different information or even who disagree about the importance of some information. A fan of Inter Milan will have detailed knowledge of the team’s recent performance and player status to inform their judgment. A coach for the team will have even deeper knowledge of these things and also know the team’s game plan. In cases like these, probability seems to be subjective; it has more to do with one’s beliefs than the objective state of the world. This doesn’t mean we should just believe whatever we want, though. The tools of probability can still apply to our judgments about potential outcomes or ideas about the world.

These sets of examples illustrate that probabilities can be objective features of the world, they can be estimates or predictions of objective features of the world, and they can be our subjective judgments of how things are based on the data we have access to. It’s a tricky business to interpret what probabilities mean, that is, how we should interpret ascribing some probability to some outcome. We’ll delve deeper into how to interpret probabilities later in the chapter.

# EXERCISES

8.1 Recall: Why don’t medical tests provide guarantees of whether one has a medical condition? What do they provide?

8.2 Think: What are the two possibilities when you get a positive result on a medical test, and what are the two possibilities when you get a negative result on a medical test? What are possible considerations relevant for evaluating how to proceed?

8.3 Recall: Describe how probability relates to inductive reasoning and to uncertainty and given an example.

8.4 Apply: Give three examples of you reasoning with probabilities in the past week. (You might not have even realized you were doing it! Think about times you were trying to reason about something uncertain, make a prediction, or decide what to do when you weren’t sure what to expect.) For each example, describe how probabilities were relevant to your reasoning.

8.5 Recall: Briefly characterize the three ways probabilities can relate to objective features of the world and to individuals’ beliefs, and give an example of each.

8.6 Apply: Refresh your memory of the three ways probabilities can relate to objective features of the world and to individuals’ beliefs, and then look back to the rapid strep test example at the beginning of the section. Which one of these interpretations of probability is the use of probabilities in the rapid strep test example most like? Provide a brief justification for your answer.

### 8.2 PROBABILITY THEORY

After reading this section, you should be able to:

- State the three axioms of probability theory
- Define the terms: random variable, outcome space, independent outcomes, fair, total probability, mutually exclusive, and collectively exhaustive
- Make simple calculations with probabilities by applying the rules of addition, multiplication, and subtraction

### Random variables and outcome spaces

Thinking in terms of probabilities is a way to systematically and reliably reason under uncertainty and to represent the degree of certainty of the conclusions we reach. The tools for doing this are based in probability theory, a mathematical theory developed to quantify uncertainty and to reason about random events.

In the context of probabilistic reasoning, randomness does not mean haphazard or lacking aim or purpose. Instead, random events are outcomes that are individually unpredictable but that behave in predictable ways over many occurrences. These outcomes can be represented in terms of values of random variables. Recall that variables are anything that can vary, change, or occur in different states and that can be measured.

Random variables are variables whose values are individually unpredictable but predictable in the aggregate.

The simplest examples of random variables are things like coin tosses and dice throws. In a normal roll of a die, you can’t know whether you’ll roll a one, two, three, four, five, or six before rolling the die and seeing the outcome. But even before rolling the die, you do know that if you roll the die 500 times, you almost certainly won’t roll a six every time. Probability theory enables you to calculate what that probability is; it can tell you exactly how unlikely it is to roll a six 500 times in a row.

The set of all values a random variable can have is called its outcome space (or sample space). For a coin toss, the random variable is the figure shown on the top of the coin. The only two possible outcomes of a coin toss are heads and tails; these are the two values of the outcome space for the variable figure shown on the top of the coin. We can represent all of this with the following expression:

$X = \{h, t\}$

Here X represents the random variable figure shown on the top of the coin, and h and t represent the values this variable can have (heads and tails, respectively). The symbols “{” and “}” are curly braces, which is the conventional notation used to indicate a set, that is, any grouping of elements in no particular order. So this expression shows that the outcome space for the random variable of a coin toss is simply heads and tails.

There are a few features of random variables that affect how the tools of probability apply to them. First, some variables have independent outcomes, that is, the probability of each outcome does not affect the probability of the other outcomes. This is also called statistical independence, which we define later in this chapter and discuss further in Chapter 9. Whether a coin toss results in heads or tails on each throw is an independent outcome: how the last coin toss went won’t change the probability of getting heads. But how many heads come up on a series of 10 throws is not independent from whether you get a heads or tails on each individual throw.

A useful feature of some random variables is that they are fair, that is, they have independent outcomes that are all equally likely as one another. If a coin is fair, then the probability of the coin landing on heads will equal the probability of it landing on tails. This is useful, since it enables us to immediately know that the probability of getting heads or tails is 50/50. (We’ll see why this is so later, when we begin calculating probabilities.)

A random variable that is not fair may be biased in favor of one or more outcomes. This means some outcomes are more likely—have a higher probability of occurrence—than other outcomes. Roulette is a casino game that developed in France. A French roulette wheel has 37 pockets, numbered 0 through 36, but an American roulette wheel has 38 pockets, two of which are 0. American roulette wheels are not fair, in a probabilistic sense, because the roulette is biased toward 0. Zero will occur more often than any other number on the wheel if we spin the roulette over and over again, because there are two ways to get a 0 but only one way to get every other number on the wheel.

A second way in which a random variable may not be fair is if its outcomes aren’t independent from one another. The most common way this can happen is when previous outcomes influence future outcomes. Coin tosses, dice throws, and roulette spins are usually fair: each one is a new try, and nothing about the last one affects it. Imagine that you are spinning a roulette, and each time the ball lands in a pocket, you put something in that pocket to block it for the next spin. This way of spinning a roulette is not fair because its outcomes aren’t independent. Once you’ve gotten a number, you know you won’t get it on a subsequent spin of the wheel. This also changes the probability of getting the other numbers: they become more likely as you spin and block more numbers.

##### Box 8.1 The Gambler’s Fallacy

Your friend plays video poker, and she reasons as follows: “Since this is a fair video poker, black and red cards come up equally often. There has been a streak of black cards. Therefore, a red card will come up very soon.” This reasoning is called the gambler’s fallacy because it is typical among aficionados of casinos. The gambler’s fallacy is inferring from past variation from the expected frequency of outcomes that there will be future variation from the expected frequency in the opposite direction. Unfortunately for gamblers, this is bad reasoning. It is based on the mistaken idea that the outcomes of games of chance are not statistically independent. It can be tempting to think that unusually common occurrences will be averaged out by becoming unusually uncommon later. But, in fact, each draw of a fair video poker game is statistically independent, as are the outcomes of roulette spins, dice throws, and coin tosses. There is no way for one outcome to influence later outcomes. So, your friend is wrong that red cards become more likely after a streak of black cards. And the gambler’s fallacy applies to much more than games of chance. A family with three girls still has a roughly 50% chance of a fourth child being a boy, though the parents might think they are more likely to have a boy this time around. Last week’s record-breaking heat doesn’t mean this week will be cooler than average.

To recap, a fair random variable must be unbiased and its outcomes must be independent. Coin tosses and dice throws are fair random variables, but lots of random variables are unfair. For example, LeBron James’s free throw success is a random variable with two possible outcomes: LeBron either misses the free throw or scores. But the chance of LeBron scoring versus missing is probably not 50‐50. Instead, there is a bias in favor of the outcome of scoring; for LeBron James, this is more likely than missing. The outcomes might also fail to be independent: missing a shot might make LeBron more, or less, likely to score on the next free throw. It’s much more difficult to calculate probabilities for unfair variables like free throw success. So, for now, we’ll stick with fair random variables, like coin tosses and dice throws.

#### The axioms of probability theory

Probabilistic reasoning begins with the observation of how probable it is for a random variable to take on a given value. The rules for assigning these probabilities are grounded in what are known as the Kolmogorov axioms, which are three basic assumptions that lie at the foundations of probability theory, introduced by the mathematician Andrey Kolmogorov. (Recall from Chapter 6 that axioms are statements accepted as self‐evident truth about a domain used as a basis for deductively inferring other truths about the domain.) These three axioms are the basis for probability theory, that is, for the rules governing the calculation of probabilities.

Axiom 1 defines all probabilities as numbers greater than or equal to zero. We can express this axiom mathematically as:

Axiom 1: $0 ≤ Pr(X=o)$

Here *X* is any random variable and *o* is any value, and “Pr()” means the probability of. Because Axiom 1 prohibits any probabilities lower than zero, this assigns the least likely outcomes—outcomes that are guaranteed not to occur—a probability of 0.

Axiom 2 says that the probability that at least one of the outcomes in the entire outcome space will occur is 1. This can be expressed as:

Axiom 2: $Pr(X=\{o_{1−n}\})=1$

Here o represents the entire outcome space of any random variable X. No matter how many values a random variable can have, that whole set of values must have a combined probability of 1. The total probability of the outcome space for any random variable is always 1. Axiom 2 assigns the most likely outcomes—outcomes that are guaranteed to occur—a probability of 1.

Together, Axioms 1 and 2 ensure that all probabilities are between 0 and 1. An outcome that is guaranteed not to occur has a probability of 0. If you roll a regular six‐sided die, you will never roll a 7, as this is not in the outcome space. An outcome that is guaranteed to occur has a probability of 1. If you toss a coin, then the figure on the top of the coin will always be heads or tails. If you check the weather tomorrow, it will always be raining or foggy or clear or snowing or some other precipitation status. The larger the probability of an outcome between these extremes—the closer it is to 1 and the further it is from 0—the more likely it is to occur. If you believe there’s an 80% (or .80) chance of rain tomorrow, you’re more certain it will rain than if you believed there’s a 40% (or .40) chance of rain. If you believe there is a 110% (or 1.10) chance it will rain tomorrow, then this belief violates Axiom 2. If you assign a probability of −0.4 to the outcome of enjoying this chapter, then this also violates Axiom 1. (We hope we do better than 0, too!)

Axiom 3 says that the probability that one of several outcomes occurs is equivalent to the sum of the individual outcomes’ probabilities. This can be expressed as:

Axiom 3: $Pr(X =o_1\or\  o_2\  or\   \ldots) = Pr(X=o_1) + Pr(X=o_2) \ldots$

As earlier, X and o are any random variable and a value that variable can have. There’s an important restriction on which values this axiom holds for, though. This equivalence only holds for mutually exclusive outcomes, or a set of values that a variable cannot take on simultaneously. On a single coin toss, for example, you will never get both heads and tails; so heads and tails are mutually exclusive values or outcomes. Axiom 3 governs the probability of one of multiple outcomes occurring; it enables the calculation of probabilities for general sets of outcomes, like getting heads or tails on a coin toss or it either raining or sleeting tomorrow.

#### Calculating probabilities

Recall that a fair random variable has independent outcomes that are all equally likely. For a fair six‐sided die, rolling any number between 1 and 6 is equally probable. The outcome space for a die roll is D = {1; 2; 3; 4; 5; 6}, and by Axiom 2 we know Pr(D = {1; 2; 3; 4; 5; 6}) = 1. Because these outcomes are equally probable, this means that each of the six numbers has a 1/6 probability of being rolled. Or, Pr(D = 1) = Pr(D = 2) = . . . = 1/6.

We might also want to know the probability of other types of outcomes. For example, on a single die roll, how probable is rolling an even number? What’s the probability of getting anything on our roll except a 4? And, if we roll two dice, what’s the probability of getting two 6s? These probabilities also can be found by doing calculations based on the axioms of probability theory.

Consider the question of how probable it is to roll an even number on a single throw of a fair, six-sided die. This can be found using Axiom 3. The probability we are looking for can be expressed as: Pr( D = 2 or D = 4 or D = 6). Each of these three outcomes has a probability of 1-6, and the three outcomes are mutually exclusive. So, by Axiom 3:

Pr( D = 2 or D = 4 or D = 6) = Pr( D = 2) + Pr( D = 4) + Pr( D = 6)

= 1/6 + 1/6 + 1/6

= 3/6, or 1/2

Remember the importance to this calculation of the outcomes being mutually exclusive. If I ask you about the probability of rolling an even number or a 6 when you roll a single die, you cannot simply apply Axiom 3. Because 6 is one of the even numbers on the die, the outcomes of rolling a 6 and rolling an even number are not mutually exclusive. So, you can’t simply add up the different probabilities to find the answer.

The addition rule is a generalization of this calculation that applies to outcomes that are not mutually exclusive to find the probability of any of those outcomes occurring. For outcomes that aren’t mutually exclusive, the probabilities are still added, but then the probability of both events occurring is subtracted:

Addition rule: $Pr( X = o_1 \ or\  X = o_2) = Pr( X = o_1) + Pr( X = o_2) − Pr( X = o_1 \ and \ o_2)$

Applying this to find the probability of rolling both a 6 and an even number, we get:

Pr( D = even or D = 6) = Pr( D = even) + Pr( D = 6) − Pr( D = even and D = 6)

= 3/6 + 1/6 − 1/6

= 3/6, or 1/2

Anytime you roll a 6, you’ve rolled an even number, so the probability of rolling an even number and a 6 is still 1/6. Remember, the addition rule is a way to calculate the probability of any of multiple outcomes occurring.

We also posed the question of the probability of getting two 6s when we roll two dice; this isn’t a question about any of multiple outcomes occurring, but a question about all of multiple outcomes occurring. According to the multiplication rule, the probability that all of a series of outcomes will occur is the result of multiplying their individual probabilities:

Multiplication rule: $Pr( X = o_1 \ and  \ X = o_2) = Pr( X = o_1) × Pr( X = o_2)$

When we ask about the probability of getting two 6s when we roll two dice, we are asking for the probability of rolling a 6 on one die roll and also rolling a 6 on a second die roll (whether the same die or a different one). The probability we are looking for is thus Pr( D1 = 6 and D2 = 6). Of course, there’s a 1/6 probability of a 6 for any given die roll, so Pr( D1 = 6 & D2 = 6) = Pr( D1 = 6) × Pr( D2 = 6) = 1/6 × 1/6 = 1/36. The probability of 1/36 is a lot closer to 0 than to 1/6. That’s why rolling two 6s is exciting: it seldom happens!

The multiplication rule as we’ve introduced it has an important limitation. It only applies to independent outcomes; recall that outcomes are independent when the probability of each outcome does not affect the probability of the other outcomes. Imagine we wanted to calculate the probability of rolling a 6 on one die roll but also a 1 on the very same die roll. We can’t just multiply 1/6 × 1/6 because these outcomes aren’t independent: if one occurs, the other is guaranteed not to occur. This means the probability in question is maximally improbable: it’s 0. So, we can only use this multiplication rule to find the probabilities of a series of outcomes all occurring if the outcomes in question are independent from one another.

Let’s take a moment to compare the multiplication rule with the addition rule. We saw that the addition rule is used to calculate the probability of any of a series of outcomes occurring. You could use it to calculate the probability of getting a 6 or a 1 on a single die roll: 1/6 + 1/6 = 2/6, or 1/3. The multiplication rule is instead used to calculate the probability of all of a series of independent outcomes occurring. We used it earlier to calculate the probability of getting a 6 on two rolls: 1/6 × 1/6 = 1/36. (They have to be different rolls or different dice to be independent outcomes.)

What about the probability of rolling a 6 on either of two die rolls? This is about any of a series of outcomes, but the outcomes aren’t mutually exclusive. So, we use the addition rule, but we need to subtract the probability of getting a 6 on both rolls. And we found that probability with the multiplication rule! So, here goes: Pr( D1 = 6 or D2 = 6) = Pr( D1 = 6) + Pr( D2 = 6) − Pr( D1 = 6 & D2 = 6) = 1/6 + 1/6 − 1/36 = 11/36. The probability of rolling at least one 6 goes up a lot with two rolls instead of one, but it doesn’t quite double.

In our examples, the addition rule led to a larger probability (closer to 1) and the multiplication rule led to a smaller probability (closer to 0). This will always happen. Addition will always increase probability, and multiplication will always decrease probability. This is because probabilities are always positive numbers between 0 and 1, and multiplying two numbers in that range, such as two fractions, always yields a smaller number while adding two positive numbers of any kind always yields a larger number. This can provide a quick way to remember when to add and when to multiply. Do you expect the probability to get larger or smaller for the occurrence you’re calculating, compared to the outcomes that generate it? It’s easier (more probable) to get any of some outcomes than each outcome individually: use addition. It’s harder (less probable) to get some outcomes together than each outcome individually: use multiplication. (And these outcomes need to be independent.)

Here’s one more calculation tool for probabilities. Recall Axiom 2: the total outcome space always has a probability of 1. The subtraction rule makes use of this: you can calculate the probability of an outcome you are interested in by subtracting the probability of all other outcomes in the outcome space from 1 (the total probability). So:

Subtraction rule: P$r( X = o_1 ) = 1 − Pr( X =\{ o_2−n\})$

##### Table 8.1 Addition, multiplication, subtraction rules and their conditions

| Rule                | Term | Function          | Condition               | Result                            |
| ------------------- | ---- | ----------------- | ----------------------- | --------------------------------- |
| addition rule       | any  | disjunction (or)  | probability             | always increases                  |
| multiplication rule | all  | conjunction (and) | independent             | probability always decreases      |
| subtraction rule    | not  | negation (not)    | collectively exhaustive | probability can be large or small |



For example, what is the probability of getting anything except a 2 on a single die roll? The total probability is 1, and the probability of rolling a 2 is 1/6 (as it is for any other number from 1 to 6). So, the probability of getting anything but 2 is Pr( D =not‐2) = 1 − Pr( D=2) = 1 − 1/6 = 5/6.

The subtraction rule only applies to collectively exhaustive outcomes, or a set of outcomes of which at least one must occur. For a successful die roll, the die must land with one side up showing a 1, 2, 3, 4, 5, or 6—there is no other option. So, 1–6 are collectively exhaustive outcomes for the variable die roll. This is what makes probabilities sum to 1, which is necessary for the rule. This requirement is most easily satisfied with the use of the word “not”—rolling a 2 and not rolling a 2, rolling an even number and not rolling an even number, rolling two 6s in a row and not rolling two 6s in a row. Each of these pairs is collectively exhaustive; any possible outcome would fall in one or the other category. The word “not” can prompt you to use the subtraction rule, as it is one way of guaranteeing collectively exhaustive outcomes.

The subtraction rule can, of course, also be used in combination with the multiplication and addition rules. Previously we used the latter rules together to calculate the probability of getting a 6 on either of two dice rolls; it was 11/36. What about not getting a 6 on either of two dice rolls? This probability can be found from our earlier calculation combined with an application of the subtraction rule. Pr( D 1=not‐6 and D 2=not‐6) = 1 − Pr( D 1=6 or D 2=6) = 1 − 11/36 = 25/36.

# EXERCISES

8.7 Recall: Write the mathematical formulation of each of the three axioms of probability theory, then say what each means.

8.8 Recall: Define each of the following terms: random variable, outcome space, independent outcomes, fair, total probability, mutually exclusive, and collectively exhaustive.

8.9 Think: Recall from this section that an American roulette wheel is not fair; its outcomes are biased because there are 38 pockets, and two of those are 0. Describe what it means for the wheel to be biased in this way. Are the spins of an American roulette wheel still independent? Why or why not?

8.10 Apply: There are not just cubical dice with six sides but many other polygons as well. Imagine you have a four-sided die with sides numbered 1, 2, 3, and 4. Assume the die is fair: each side is equally likely to be rolled. Write out the following in notation like we’ve introduced in this section for the variable 4-sided die roll (D).

- a. the variable’s outcome space
- b. the total probability of the outcome space
- c. the probability of rolling an odd number

8.11 Apply: Consider the fair four-sided die described in Exercise 8.8. Calculate the following using the addition, multiplication, and subtraction rules as needed. Use notation like we’ve introduced in this section, show the calculation steps, and specify which rule you use for each step.

- a. the probability of rolling a 3 on both of two rolls
- b. the probability of rolling a 3 on every roll for three rolls
- c. the probability of not rolling a 3 on a single roll
- d. the probability of rolling a 3 on at least one of two rolls

8.12 Think: Imagine you are participating in a psychological experiment. The experimenter gives you the following problem: “Linda is 31 years old, single, outspoken, and bright. She majored in philosophy. As a student she was deeply concerned with issues of discrimination and social justice. Which of the following two alternatives is more probable?

- A. Linda is a bank teller
- B. Linda is a bank teller and active in the feminist movement.

Which one would you choose, answer A or B? Why? If your intuitions work like those of most people, you picked B. But B cannot logically be more probable than A. Using the relevant rule for evaluating the probability of a conjunctive statement of the form “x and y,” can you explain why B cannot be more likely than A? Do you think ordinary people understand the term “more probable” in this example in terms of the basic rules of probability, or do they understand it in some other way?

### 8.3 REASONING WITH CONDITIONAL PROBABILITIES

After reading this section, you should be able to:

- Describe how conditional probabilities are important and define the base-rate fallacy
- Calculate a conditional probability with the needed background information
- Apply Bayes’s theorem to calculate a conditional probability with the needed background information

#### Conditional probability

So far, we’ve largely focused on independent outcomes, like individual coin tosses and dice throws, but many outcomes for random variables are not independent. For example, the probability that you get a 6 on two dice rolls goes up once you’ve gotten a 6 on one roll. (That probability goes to zero once you’ve gotten anything but a 6 on the first roll.)

Another useful role for probability is in calculating the probability of an outcome given that some other outcomes occur. For example, what is the probability of rolling a 6, given that you rolled an even number? What’s the probability that global warming will be limited to 1.5° Celsius above pre-industrial levels if countries meet the goals specified in the Paris Agreement? Or—remember our initial example in this chapter—what’s the probability that I have a medical condition, given that I tested positive?

The conditional probability of an event is the probability of its occurrence given that some other event has occurred. In the notation we’ve been developing, we can write the conditional probability of a random variable Y taking the value y, given that a variable X takes the value x as Pr(Y = y | X = x). The symbol “|” can be read as “given that.”

For two independent outcomes, the conditional probability of one outcome given the other’s occurrence will be the same as the original probability of the outcome. Indeed, the concept of conditional probability enables us to specify more exactly what independence amounts to. Two random variables X and Y are statistically independent when Pr(Y = y | X = x) = Pr(Y = y) and Pr(X = x | Y = y) = Pr(X = x). This means that the outcome x occurring doesn’t make the outcome y any more or less likely, and the outcome y occurring doesn’t make the outcome x any more or less likely.

If an outcome y is not statistically independent from an outcome x, then the probability of y occurring goes up or down if x occurs. In extreme cases, one event can result in the probability of another event becoming 1 or 0. For example, the probability of a single die roll resulting in an even number is 1/2. But the probability of an even number given that you roll a 2 is 1, since rolling a 2 is one way of rolling an even number. The probability of an even number given that you roll a 3 is 0, since 3 is odd. That is:

Pr(D1 = 2 or 4 or 6 | D1 = 2) = 1

Pr(D1 = 2 or 4 or 6 | D1 = 3) = 0

In other cases, statistical dependence is subtler: the probability of an event is raised or lowered by the occurrence of another event but not all the way to 0 or 1. Consider again the probability of getting two 6s when two dice are rolled. We calculated that the probability of this outcome is 1/36. But what is the probability of getting two 6s in two dice rolls, given that the first roll yields a 6? The chance has gone up, but it’s still not guaranteed.

Figuring out the conditional probability requires calculation. For two outcomes x and y, the probability of y occurring given that x occurs can be calculated using this formula:

Conditional probability $Pr(Y=y | X=x) = Pr(Y=y \ and \  X=x) / Pr(X=x)$

Think of this formula as a two‐step procedure for finding the probability of y given x. First, you limit your attention only to cases when x occurs. This is the role of Pr(X=x) as the denominator (the bottom) of the equation. Second, you look within those cases of x occurrences for occurrences of y. This is the role of Pr(Y=y & X=x) as the numerator (the top) of the equation. If the outcomes are restricted to only those cases when x occurs, this becomes the new outcome space for the variable Y. (This calculation only works when the probability of x is greater than 0, since dividing by 0 doesn’t yield a real number.)

Let’s try this out to find the probability of getting two 6s in two dice rolls, given that the first roll is a 6. Imagine that you decide to roll the dice one at a time, and you’ve rolled the first but not yet the second. Plugging this example into the formula gives us:

Pr(D=6 & D=6 | D=6) = Pr((D=6 & D=6) & D=6) / Pr(D1=6)

Before we solve this equation, take a moment to figure out why this equation is the right version of the formula for calculating conditional probabilities. Then, we can just plug in the probabilities we already know and do some simple math to solve the equation. Pr((D=6 & D=6) & D=6) just is the probability of getting two 6s; D1=6 is just listed twice. It shows up twice because the first roll had to be 6 for it to be possible for both rolls to be 6s. So, plugging in the probabilities:

Pr(D=6 & D=6 | D1=6) = (1/36) / (1/6) = 6/36 = 1/6

One nice thing about starting with this simple example is that we can check the answer. What is the probability of rolling two 6s given that you’ve already rolled one 6? This is the same as the probability of getting a 6 on one roll, since that’s exactly what needs to happen now to get two 6s (since you already have one 6). And we know the probability of getting a 6 on a single die roll is 1/6. So, our calculation of the conditional probability gave us the right answer.

Let’s try our hand at finding a slightly more difficult conditional probability for dice throws. What’s the probability that you roll a number that is less than 4 on a single throw, given that you roll an odd number? This is the same as asking about the probability of rolling a one, two, or three (the outcomes less than four) given that you roll a one, three, or five (the odd outcomes). Applying our conditional probability formula, this yields:

Pr(D=1 or 2 or 3 | D=1 or 3 or 5) = Pr(D=1 or 2 or 3 & D=1 or 3 or 5) / Pr(D=1 or 3 or 5)

Pr(D&lt;4|D=odd)

Pr(D&lt;4) Pr(D=odd)

 

Using the addition rule, the probability of rolling a 1, 3, or 5 is 3/6: 1/6 + 1/6 + 1/6.

We plug this in as the denominator. To find the probability of both rolling a 1, 2, or 3 and rolling a 1, 3, or 5, we need to notice that this can only happen when you roll a 1 or 3. Why? Because those are the only two ways of rolling both an odd number and a number less than four. Using the addition rule, the probability of rolling a 1 or 3 is 2/6. (We can’t use the multiplication rule to calculate the probability, because the outcomes of rolling a number under four and an odd number aren’t independent.)

Plugging these into the earlier formula yields (2/6)/(3/6), which is equivalent to 2/3. The probability of rolling a number less than four given that you’ve rolled an odd number is 2/3; consulting Figure 8.2 should help you convince yourself that this is the right answer.

#### Bayes’s theorem

The definition of conditional probability can be used to derive Bayes’s theorem. Recall that a theorem is a statement deductively inferred from a set of axioms. This theorem is named after Reverend Thomas Bayes, an English statistician in the 18th century, and it has become central to many uses of probability and statistics in science. Bayes’s theorem provides a way to calculate the conditional probability of an outcome Y given X from information about the conditional probability of X given Y (the opposite conditional probability) and general probabilities of X and Y. We’ll talk through the formula, and then we’ll see how this can be useful.

Recall the definition of a conditional probability we have just introduced:

Pr(Y=y | X=x) = Pr(Y=y &amp; X=x)/Pr(X=x)

The same equation holds of the probability of X given Y:

Pr(X=x | Y=y) = Pr(Y=y & X=x)/Pr(Y=y)

We can transform this second equation to solve for Pr(Y=y & X=x); that’s just Pr(X=x | Y=y) × Pr(Y=y) (instead of dividing the right side of the equation by this, multiplying the left side of the equation by it). Substituting that in for Pr(Y=y & X=x) in the first equation yields Bayes’s theorem:

Bayes’s theorem: $Pr(Y=y | X=x) = (Pr(X=x | Y=y) × Pr(Y=y))/Pr(X=x)$

This equation is useful when the conditional probability of Y given X can’t be calculated directly, but there’s information about the conditional probability of X given Y and the general probabilities of X and Y. You can think of the Xs in this equation, then, as information we have, and the Y what we are trying to determine the probability of given this information.

Medical testing is one of many useful applications of Bayes’s theorem. Imagine I am screened for a medical condition that affects about one person in 1,000. I have no symptoms, and I know the test is accurate 90% of the time. This means that if I do have the medical condition, then the test result is positive with 90% probability; and if I do not have the condition, the test result is negative with 90% probability. (In other words, about 9 people out of 10 who have the medical condition get a positive result, and about 9 out of 10 who don’t have the medical condition get a negative result.) After several anxious minutes, the test results come back: positive! Do you think I have good reason to worry? Why?

At the beginning of the chapter, we noted that a positive test result, such as a rapid stress test, doesn’t guarantee that you have the condition tested for, and a negative test result doesn’t guarantee that you don’t have the condition. Bayes’s theorem can be used to calculate the actual probability that you have the condition given that you received a positive test result. We want to find via Bayes’s theorem the probability that you have the medical condition (C=yes) given that the test was positive (T=yes). Plugging these variables and values into the theorem shows us what we are looking for:

Pr(C=yes | T=yes) = (Pr(T=yes | C=yes) × Pr(C=yes))/Pr(T=yes)

Now we need to find the probabilities on the right‐hand side from the information provided. The general probability that I have the medical condition, Pr(C=yes), is .001, since we know that about one person in a thousand is affected by the condition. If you pick 1,000 people randomly from the human population, you’d expect to find one person with this medical condition. The chance that I have the medical condition thus is .001, which just is 1/1,000. This is often called the prior probability, since it’s the probability of the outcome we are interested in, not taking into account the new information (in this case, the result of the medical test).

We also know the probability of getting a positive test result given that one has the medical condition, Pr( T=yes | C=yes ); this is .90. Remember that this medical test is 90% accurate. If one has the condition, the probability of a positive test result is .90. This number is often called the likelihood —how likely the outcome we’ve observed (positive test result) would be if the outcome we’re curious about (having medical condition) has in fact occurred.

The last probability we need to use Bayes’s theorem is Pr( T=yes ), or the probability of receiving a positive test result regardless of whether one has the medical condition. We don’t immediately have this probability, but we can figure it out. Either one has the medical condition or not, and in each of these circumstances, there’s some likelihood of getting a positive test result. What are those likelihoods? We’ve already said that the likelihood of a positive test result if one has the medical condition, Pr( T=yes | C=yes ), is .90. The likelihood of getting a positive test result if one does not have the condition, Pr( T=yes | C=no), is .10, since if one does not have the condition, there’s a 90% chance of a negative result. This leaves a 10% chance of still getting a positive result. But it’s not equally likely that one does and doesn’t have the condition; recall that the medical condition affects just 1/1000 people, or .001; 999/1000 people, or .999, don’t have it. We can put all of this together to find the probability of a positive test result as follows:

| Pr( T=yes ) | =    | (Pr( T=yes                  | C=yes ) × Pr( C=yes)) + (Pr( T=yes | C=no ) × Pr( C=no ) |
| ----------- | ---- | --------------------------- | ---------------------------------- | ------------------- |
|             | =    | (.90 × .001) + (.10 × .999) |                                    |                     |
|             | =    | .0009 + .0999 = .1008       |                                    |                     |

Now we have all the ingredients we need to apply Bayes’s theorem. Plugging in the probabilities we’ve found, we get Pr( C=yes | T=yes) = .001 × .90 / .1008 = .0089, or .89%. This result is called the posterior probability since it is conditional on an observed outcome, namely the positive test result. It turns out that the probability that I have the medical condition given the positive test result is small: it’s still less than 1%! So perhaps I should not yet get too worried. The probability that I have the medical condition has gone up a lot, from .001 to .0089, but it’s still very likely that I don’t have the condition. Bayes’s theorem just gave me an incredible sense of relief.

We called the general probability of having the medical condition the prior probability. Prior probabilities are also known as base rates. These terms both refer to the probability of some outcome in the absence of other information. The proportion of the population in a country that is employed by the government in civil service, the proportion of all humans struck by lightning, and the proportion of all people with a certain medical condition are all examples of base rates. For example, in the US, 1.9 % of the population works for the federal government, and 98.1% do not. The base rate of civil servants in the US is 1.9%, or 19/1,000. The base rate of people struck by lightning is estimated to be 1/15,300.

In scientific and everyday reasoning, base rates provide us with important information for making correct probability judgments, though it’s easy to forget about base rates. The base-rate fallacy is neglecting the base rate and focusing only on the individual information. For example, this happens when people, sometimes including healthcare professionals, assume someone has an unusual medical condition because they have received a positive test result. Consider that, for the medical test example we just worked through, many more of the people testing positive for the condition do not have the condition than do have the condition, simply because the condition only affects 1/1,000. In situations where some event is particularly striking, like a new disease outbreak, a terrorist attack, or a lightning strike, ignoring base rates can result in mistaken judgments and in wasting money and time trying to intervene on very unlikely events. Base rates and new evidence should both be taken into account in probabilistic reasoning, and Bayes’s theorem is an important tool for doing so.

##### Box 8.2 Probabilistic biases

Several cognitive biases influence probabilistic reasoning and judgment. We have already encountered the base-rate fallacy and the gambler’s fallacy. Three other examples are the conjunction fallacy, the neglect of probability bias, and the zero-risk bias.

**The conjunction fallacy** The conjunction fallacy is the error in judgment when we judge a conjunction of two events to be more likely than either one of the events on their own. For example, if you meet a random person in their twenties and know nothing about them, do you think they are more likely to be a student or a student struggling for money? Sure, students are often poor, and so that might strike you as likely. But it’s always more probable to be a student than to be a student and broke.

**The neglect of probability** The neglect of probability is a bias in judgment or decision under uncertainty that comes from disregarding probabilistic information. People’s purchase of lottery tickets, anxiety about terrorist attacks, and opinions about the safety of vaccines all tend to neglect relevant probabilities—all of these are extremely unlikely outcomes.

**The zero-risk bias** The zero-risk bias is a preference for policies—especially about health and the environment—that entirely eliminate a risk instead of alternatives that more effectively reduce risk (by being cheaper, easier to implement, etc.) Many people asked if they prefer (a) winning $100 for sure, or (b) 10% chance of winning $500, 89% chance of winning $100, and 1% chance of winning nothing, opted for the zero-risk alternative (a)—even though (b) is 99% likely to yield at least the same earnings and has a good chance of yielding lots more.

##### EXERCISES

8.13 Recall: Write out the formula defining a conditional probability. In your own words, describe how the formula can be used to find the probability of getting two 6s in two dice rolls, given that the first roll is a 6.

8.14 Apply: Use the formula for conditional probability to find the probability of getting an odd number on a single die roll given that you did not get a 6. Show each step of your reasoning and indicate any rules you use (addition, multiplication, subtraction).

8.15 Recall: Write out Bayes’s theorem. Label the parts of the formula that are the prior probability, the likelihood, and posterior probability. In your own words, describe how we used the theorem to find the probability that you had a medical condition given a positive test result (with the numbers involved in our example).

8.16 Apply: Imagine you arrived in a new town and ask a random stranger about the best bar in town. You know in this town 10 out of every 100 people will lie. You also know of the 10 people who lie, 8 have a red nose. Of the remaining 90 people who don’t lie, 9 also have a red nose. Suppose you meet a group of 100 people in the town with a red nose. Use Bayes’s theorem to calculate how many people out of this group of 100 will lie.

8.17 Think: Describe how conditional probabilities are important. Then, define and give an example of the base-rate fallacy.

8.18 Think: Consider a fair 10,000 ticket lottery that has exactly one winning ticket. You are justified to believe that any particular ticket of the lottery will not win, because the probability of any one ticket winning is 1/1000. But if you are justified to believe that ticket #1 (#2 & #3 & . . . #10000) will not win, then you should also believe the paradoxical conclusion that no ticket will win in that lottery!

There are three individually plausible ideas that together seem to generate this “lottery paradox”:

1. One is justified to believe a proposition that is very likely true.
2. If one believes that A is true and they also know that A deductively entails B, then they should also believe B.
3. One is never justified to believe a contradiction.

First explain why you should believe the paradoxical conclusion no ticket will win in that lottery, and then reflect on how to solve the lottery paradox. Do you think that the trouble may be with one of the three prior ideas? Which one and why?

### 8.4 INTERPRETING PROBABILITIES

After reading this section, you should be able to:

- Describe the problem of interpreting probability and why it is challenging
- Describe the subjectivist interpretation of probability and the two main challenges for it
- Describe the frequency and propensity interpretations of probability and indicate the main challenge for each

#### The problem of interpreting probability

The first section of this chapter gave three types of examples of probabilities:

1. Figuring out the likelihood of a random mutation or of getting a particular hand of cards in poker.
2. Predicting whether the stock market will go up or the weather will become colder.
3. Judging whether Inter Milan will win the next Champions League, whether there is life outside Earth, or whether you’ll pass the final exam.

You have surely faced situations like these. And you have made and heard claims like, “A coin is just as likely to land heads as tails,” “There’s an 80% chance of snow tomorrow,” and “I will probably pass the exam.” But what do these kinds of claims about probabilities mean? And what makes them true or false?

In the beginning of the chapter, we said of these sets of examples that (1) seems to be objective features of the world, (2) seems to be our estimates of objective features of the world, and (3) are our guesses of what outcomes will arise for processes that probably aren’t actually based on probabilities. Now we’ll delve deeper into the question of how probabilities should be interpreted, including whether situations like (1), (2), and (3) should be interpreted in the same way. Different interpretations of probability provide different accounts of what kind of things probabilities are and of what makes probability claims true or false. Given the ubiquity of probability claims in science and everyday life, it is important to understand how probabilities should be interpreted and why.

There are two broad families of interpretations. The first family is called epistemic (this word means relating to knowledge, knowing, or rational belief) and grounds interpretations of probability in the notion of rational degree of belief, or the extent to which a rational agent should believe some claim. Within the family of epistemic interpretations, we will focus on the subjective interpretation. The second family is called objective and understands probability as an objective feature of the world, just like rocks, sunshine, and water—on this interpretation, probabilities, just like these things, exist regardless of any opinion you or anybody else may have about them. We will focus on two kinds of objectivist interpretations: the frequency interpretation and the propensity interpretation.

#### Subjective interpretation

According to the subjective interpretation of probability, the probability of an outcome is the subjective, rational degree of belief of a suitable agent that the outcome will obtain. If I say I will probably pass the exam or that the weather forecast predicts an 80% chance of snow tomorrow, for example, these probabilistic judgments express some suitable agents’ rational degrees of confidence or certainty about certain outcomes—not just about what my confidence happens to be but about the confidence someone should have. On this interpretation, probability claims aren’t made true or false by how the world is but instead by the rational degrees of belief of suitable agents.

To understand this view, we need to be clear on what a degree of belief is and when a degree of belief is rational. A degree of belief is the amount of confidence in the truth of a given hypothesis. But how can you find out about somebody’s degree of confidence that some hypothesis is true? Probability theorists have tried to quantify this by thinking of it in terms of possible bets agents would accept or reject. The idea behind this is suggested by ways of talking like “You can bet she will be late to the meeting” or “I am willing to risk all my salary on the result of the political election,” which express the conviction something will happen or will not happen.

We can figure out somebody’s degree of belief in a hypothesis or degree of confidence in an outcome by identifying the odds on a bet about the hypothesis such that the person would be equally willing to take either side of the bet. To bet on the truth of a hypothesis at odds of 10:1, say, means to be willing to risk losing \$10 if the hypothesis is false while gaining only \$1 if the hypothesis is true. This would be a bad bet on a coin toss because each time you happen to guess correctly you only gain \$1 while you lose \$10 for each (equally likely) incorrect guess. But if you are really certain about something, this bet gets you easy money, since you know you aren’t actually risking \$10. So, the higher odds you are willing to accept on a bet corresponds to increased confidence that the hypothesis you are betting on is true.

At some odds, you aren’t going to be sure whether you should bet for or against a hypothesis. Imagine you gain \$10 if you correctly guess whether the coin will land heads and lose \$10 if not. Should you guess that it will or won’t land heads? If you think the coin is fair, you probably can’t decide. Guessing it will land heads is not obviously a bad bet (risking more than you stand to gain) or a good bet (gaining more than you stand to lose). When I am equally willing to take a bet that a coin will land heads and a bet that the coin will not land heads at certain odds, this means those are subjectively fair odds for me. The odds are subjective, and so they might be different for someone else.

These subjectively fair odds for me indicate my degree of belief in the hypothesis the bet is about. (I don’t know about you, but for me, that’s 50/50 for a coin toss.) In general, if my subjectively fair odds for a bet on some hypothesis is X : Y, then my degree of belief that the hypothesis is true can be calculated as X / (X + Y). This is the ratio between my stake X (how much I could lose) and the total amount staked X + Y. For example, if you believe that a 3:1 odd is fair for a bet that you will pass this course, then I can conclude that your degree of belief you will pass this course is 75% (or .75). You are willing to lose \$3 if you fail in return for $1 if you pass, because you’re pretty sure (but not incredibly sure) you will pass. Your degree of belief that you will pass the course is 3/(3 + 1) = 3/4 = 75%. You might not have been able to specify this, but your betting behavior revealed it.

Now we have a way to find degrees of belief through (imagined) betting behavior. But we’ve emphasized that these are subjective degrees of belief—what each of us happens to choose, with no right or wrong choices. The next step is to explore what makes a degree of belief rational. This is often understood as probabilistic coherence: a rational degree of belief respects the axioms of probability.

The basic idea for why it’s rational for your degrees of belief, and betting behavior, to conform to the axioms of probability is that not doing so leads you to accept bets that guarantee you lose money. This is called the Dutch book argument; a Dutch book is a set of bets that guarantees the person establishing the betting terms, the bookmaker, will profit. The only way not to lose money (or, not to be wrong more often than you are right) is to have subjective degrees of belief that align with the rules of probability. This alignment with the rules of probability is taken to be what makes a degree of belief rational.

Imagine my degree of belief that a coin toss will land heads is 0.6, and my degree of belief that the toss will land tails is also 0.6. These beliefs violate the rules of probability theory because the full outcome space, heads or tails, must have a probability of 1, but I’ve assigned it a probability of 1.2. Someone offers to bet me $10 to my $15 that the outcome will be heads and also $10 to my $15 that the outcome will be tails. Given my degrees of belief about the outcomes of heads and tails, I should accept both bets as fair. If the coin lands heads 60% of the time, as I believe it will, then I’ll win six out of every 10 coin tosses, so the $15 losses will be made up for by getting more $10 wins. And the same for the coin landing tails, given what I believe. (To check this, remember that for odds X : Y, my degree of belief can be calculated as X / (X + Y). So to accept 15:10 odds, my degree of belief should be 15/25, or 0.6, which it is.) It’s easy to see I’m going to lose money on this bet! And this is because my degrees of belief fail to be rational because they violate the rules of probability theory.

So, on the subjective interpretation, probabilities just are the rational degrees of belief of suitable agents. This interpretation is intuitive for many uses of probability, especially situations like those in (3) earlier, where it seems probabilities are describing our judgments of what is likely to occur. But there are at least two challenges for the subjective interpretation.

One challenge is that, if the only constraint on rational degrees of belief is coherence with the rules of probability theory, this does not prohibit rational degrees of belief that are very odd. For instance, you may judge that the probability that the Netherlands will disappear under water tomorrow is 0.9. Given what you know about climate change and the Netherlands, this belief of yours would be very odd and not informed by relevant evidence, but it doesn’t violate probability theory, so it counts as rational. In other words, mere coherence with probability theory is a very weak criterion for rational belief. Another challenge with the subjective interpretation concerns the link between belief and betting behavior. In particular, betting behavior doesn’t seem to be a good guide about what one should believe. One might dislike gambling, be more or less attached to money, or value money differently in different circumstances. This would change one’s betting behavior, but it wouldn’t change what one believes to be true.

#### Objective interpretations: frequency and propensity

Suppose an honest person tells me, “Draw a card from a standard 52‐card deck. If you draw an ace of hearts, you pay me \$1. If you draw any other card, I pay you $1000.” Should I accept?

The answer seems obvious. I should accept because it is less probable to draw an ace of hearts than to draw some other card in a standard 52‐card deck. The probability of drawing an ace of hearts is only 1/52 (about 0.019). This seems like an objective feature of the world that does not depend on anybody’s opinion or beliefs. Probabilities like this one, like the situations described in (1), seems to refer to probabilities that are objective features of how the world is. How can we make sense of probabilities as objective features of the world?

According to the frequency interpretation, the probability of an outcome is the limit of its relative frequency, or how often the outcome occurs, in a very long series of trials. Consider the random variable Card drawn from a standard 52-card deck. This variable can take the values ace of spades, ten of clubs, king of diamonds, queen of hearts, and so forth. Each draw is a trial: each draw returns a value for that random variable. If you put the card you drew back in the deck, shuffle the deck, and draw another card, and you repeat this operation over and over, that will be series of trials. Over a very (very) long series, you will observe the outcome ace of hearts once for every 52 trials. According to the frequency interpretation, this proportion is the probability of the value ace of hearts for the random variable *Card drawn from a standard 52-card deck*.

One challenge for this interpretation of probability is that it does not assign probabilities to one‐off events, that is, for outcomes where there couldn’t possibly be a long series of trials. For example, there will never be a series of trials for whether humans will land on Venus by 2025 or for whether the LA Lakers will win the NBA Championships next year. These events only happen once. So, on the frequency interpretation, it would be meaningless to say that the probability my party will win the next elections is 10% or that the probability you’ll pass the exam is 75%. These are like the scenarios in (3) earlier.

A different objective interpretation of probability is the propensity interpretation. On this view, the probability of an outcome is the propensity of the physical conditions to produce the outcome. We can understand propensities as causal dispositions to produce certain outcomes, or the tendency to behave in certain ways under certain circumstances. Consider properties like being fragile or being soluble. Fragility is the causal disposition of glass to shatter when struck; solubility is the causal disposition of salt to dissolve when put into water. So, according to the propensity interpretation, a standard 52‐card deck has a causal disposition to produce the outcome ace of hearts when a card is drawn from it. This causal disposition is the propensity to produce the outcome ace of hearts about once every 52 draws. On the propensity interpretation this is the meaning of the claim that there is a 1/52 probability to draw an ace of hearts from the deck.

The propensity interpretation can assign probabilities to one‐off events since it doesn’t rely upon the idea of series of trials. But it faces its own challenges. One challenge is to make sense of the relationship between causality and probability. If propensities are causal tendencies, then the propensity interpretation does not seem to allow us to make sense of some conditional probabilities. We can specify the probability of having a headache given that one drank too much wine, and we can also specify the probability that one drank too much wine given that one has a headache. But, while drinking wine has some propensity to produce a headache, headaches don’t cause one to have consumed wine in the past. Some probabilities, like the probability that you drank too much wine given that you have a headache, don’t seem to be causal dispositions.

The subjective, frequency, and propensity interpretations of probability differ in how they interpret what a probability claim means.  Each of these interpretations of probability can account for some uses of probability and has difficulty making sense of other uses. It might be that the mathematical tools of probability theory can be employed in multiple ways. Perhaps these tools capture how truly random outcomes play out, like the scenarios in (1), and as suggested by the frequency and propensity interpretations, and the tools also apply to how we reason, or should reason, about the likelihood of outcomes, like the scenarios in (3), and as suggested by the subjective interpretation. Consider again the scenarios in (2): predicting whether the stock market will go up or the weather will become colder. These seem to be in a gray area between (1) and (3), where the probabilities are about occurrences in the world but are shaped by our knowledge and reasoning processes. It’s unclear whether one interpretation of probability can be developed to accommodate all these uses of probabilities, and others still, or if probability means different things in different uses.

# EXERCISES

8.19 Recall: Describe the problem of interpreting probability. Why is this a challenge?

8.20 Recall: Describe the subjectivist interpretation of probability and the two main challenges facing it.

8.21 Recall: Describe each of the frequency and propensity interpretations of probability, and then indicate the main challenge for each.

8.22 Apply: Consider the scenarios described in (1)–(3) at the beginning of this section (also introduced in section 8.1). Choose one scenario from each numbered group and describe how subjective, frequency, and propensity interpretations would each interpret the probability claim. Put an asterisk next to the interpretation you think is most successful for each of the three scenarios you’ve focused on, and briefly say why you think it’s the most successful.

8.23 Think: Based on the interpretations introduced in this section and the discussion of their pros and cons, what do you think is the right way(s) to interpret probability? Do you believe there must be only one correct interpretation of probability? Why, or why not? Use simple examples to support your answers to these questions.

##### FURTHER READINGS

For a comprehensive treatment of various formal approaches to uncertain reasoning, see Halpern, J. Y. (2017). Reasoning about uncertainty. MIT Press.

For more on how people (mis)use probability for reasoning and decision‐making under uncertainty, and what this means for human rationality, see Tversky, A., & Kahneman, D. (1993). Probabilistic reasoning. In A. Goldman (Ed.), Readings in philosophy and cognitive science (pp. 43–68). MIT Press. Also see Samuels, R., Stich, S., & Bishop, M. (2002). Ending the rationality wars: How to make disputes about human rationality disappear. In R. Elio (Ed.), Common sense, reasoning and rationality (pp. 236–268). Oxford University Press.

For a historical perspective on how the modern concept of probability emerged, see Hacking, I. (2006). The emergence of probability: A philosophical study of early ideas about probability, induction and statistical inference (2nd ed.). Cambridge University Press.

For more on the leading philosophical interpretations of probability, see Hájek, A. (2019). Interpretations of probability. In E. N. Zalta (Ed.), The Stanford encyclopedia of philosophy (Fall 2019 ed.). https://plato.stanford.edu/archives/fall2019/entries/probability-interpret/