# Machine Learning Learning Log

This repository is a **living learning notebook**. The goal is not to be complete or perfect, but to:

* Track what I’ve learned
* Capture intuition (not just formulas)
* Add examples as things start to *click*
* Build real understanding over time

---

## 📚 Table of Contents

* [Colab Projects] (#colab)
* [Decision Trees](#decision-trees)
* [Random Forests](#random-forests)
* [Interpreting Models](#interpreting-models)
* [Feature Engineering](#feature-engineering)
* [Categorical Variables](#categorical-variables)
* [Evaluation Metrics](#evaluation-metrics)
* [Data Collection & Logging](#data-collection--logging)
* [Reverse Analysis (Goal → Inputs)](#reverse-analysis-goal--inputs)
* [Future Topics](#future-topics)

---
## Colab

## Decision Trees

**What they are:**
A decision tree is a flowchart-like model that splits data based on feature thresholds to make predictions.

**What they’re good for:**

* Interpretability (you can *read* the logic)
* Understanding which features matter
* Small to medium datasets
* Explaining decisions to humans

**What they’re bad for:**

* Overfitting
* Instability with small datasets
* Poor generalization alone

**Example (Pizza Project):**

* Used a decision tree to predict pizza texture
* Observed that `bake_day_sit_method` often dominated splits
* Learned that trees can change structure across runs without `random_state`

---

## Random Forests

**What they are:**
An ensemble of many decision trees, each trained on random subsets of data and features.

**What they’re good for:**

* More stable than single trees
* Better performance on noisy data
* Feature importance ranking

**What they’re bad for:**

* Less interpretable than a single tree
* Slower
* Can hide simple relationships

**Example (Pizza Project):**

* Used Random Forests to identify which dough variables correlate with airy crust
* Extracted feature importances instead of relying on a single tree path

---

## Interpreting Models

**Key ideas learned:**

* A split like `feature <= 0.5` usually means a one-hot encoded category
* `<= 0.5` ≈ False (feature absent)
* `> 0.5` ≈ True (feature present)

**Important realization:**
Models don’t explain *why* something happens — they show *patterns in the data*.

**Pizza example:**

* Instead of asking "predict my result", I asked:

  > "What conditions usually produce airy pizza?"

---

## Feature Engineering

**What it means:**
Turning raw observations into useful model inputs.

**Examples:**

* Converting categorical text into one-hot encoded columns
* Defining composite labels like `is_airy`
* Separating inputs from outcomes

**Pizza features logged:**

* Yeast amount
* Fermentation time
* Dough handling
* Bake-day rest method

---

## Categorical Variables

**Problem:**
Models don’t understand words.

**Solution:**
One-hot encoding:

* `bake_day_sit_method = room temp`
* Becomes: `bake_day_sit_method_room_temp = 1`

**Lesson learned:**

* Trees split on encoded columns, not original labels

---

## Evaluation Metrics

**Current focus:**

* Not accuracy-first
* Focused on interpretability and learning

**Metrics to learn next:**

* Accuracy
* Precision / Recall
* Confusion matrix

---

## Data Collection & Logging

**Important insight:**
Machine learning quality depends more on **data quality** than model choice.

**Pizza logging goals:**

* Log consistently
* Change one variable at a time
* Add notes for intuition

**Tools used:**

* CSV files
* Python scripts
* GitHub for versioning

---

## Reverse Analysis (Goal → Inputs)

**Key mindset shift:**
Instead of:

> Inputs → Prediction

I learned to ask:

> Desired outcome → What inputs usually cause this?

**How this was done:**

* Filter dataset by desired outcome
* Compare averages between success and failure
* Use model feature importance for guidance

This felt much closer to real-world problem solving.

---

## Future Topics

*(These sections are intentionally empty — to be filled in as learning progresses)*

* Linear Regression
* Logistic Regression
* Cross Validation
* Bias / Variance Tradeoff
* Overfitting & Underfitting
* Clustering (K-Means)
* Dimensionality Reduction (PCA)
* Hyperparameter Tuning
* Time Series
* Causal Inference

---

## Notes to Future Me

* Confusion is part of learning
* If I can explain it simply, I probably understand it
* Models are tools, not answers
* Real insight comes from combining data + intuition
