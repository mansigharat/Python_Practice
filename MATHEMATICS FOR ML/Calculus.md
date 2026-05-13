# Calculus Roadmap for Machine Learning

Learn these topics in this order:

---

# 1. Functions Basics

* What is a function?
* Graphs of functions
* Linear functions
* Polynomial functions
* Exponential functions

Very important because ML models are functions.

Example:

genui{"math_block_widget_always_prefetch_v2":{"content":"y=mx+b"}}

---

# 2. Limits

* What is a limit?
* Approaching a value
* Infinite limits
* Continuity

This is the foundation of derivatives.

---

# 3. Derivatives (MOST IMPORTANT)

Core topic for ML.

Learn:

* Meaning of derivative
* Rate of change
* Slope of curve

Example:

\frac{d}{dx}(x^2)=2x

ML connection:

* gradients
* optimization
* learning

---

# 4. Rules of Differentiation

* Power rule
* Product rule
* Quotient rule
* Chain rule

Chain rule is EXTREMELY important for backpropagation.

Example:

\frac{d}{dx}(f(g(x)))=f'(g(x))g'(x)

---

# 5. Partial Derivatives

Very important in ML.

Because ML models have many variables/weights.

Example:

\frac{\partial L}{\partial w}

Used in:

* gradient descent
* neural networks

---

# 6. Gradients

* Gradient vector
* Direction of maximum increase/decrease

Core idea behind optimization.

---

# 7. Gradient Descent

MOST IMPORTANT ML topic.

Learn:

* Loss function
* Learning rate
* Updating weights

Basic update equation:

w:=w-\eta\frac{\partial L}{\partial w}

This is literally how many ML models learn.

---

# 8. Integrals

* What is integration?
* Area under curve
* Accumulation

Example:

\int x^2,dx

ML connection:

* probability distributions
* continuous probability
* expected value

---

# 9. Multivariable Calculus

Needed later for deep learning.

Topics:

* Multivariable functions
* Partial derivatives
* Gradient vectors

---

# 10. Optimization

* Minima and maxima
* Convex functions
* Cost functions

Used everywhere in ML.

---

# MOST IMPORTANT for ML

If your goal is ML interviews/projects, prioritize:

✅ Derivatives
✅ Chain Rule
✅ Partial Derivatives
✅ Gradients
✅ Gradient Descent
✅ Optimization basics
✅ Basic Integrals

---

# Best Learning Strategy

For every topic:

1. Learn intuition
2. See graph visually
3. Solve small examples
4. Ask:

> “How is this used in ML?”
