Title: Batch Normalization
Authors: voo4
Date: 2019-10-16
Category: papers
Status: draft
publications_src: content/bibliography.bib

# Batch Normalization

Summary on [@DBLP:journals/corr/IoffeS15]

## Introduction
- 14 times fewer training steps

## The problem
- Training is complicated due to multiple layers. Outputs and gradients are affected by multiple layers, harder to control.
- Internal covariate shift: Change in the distribution of layers' inputs
- Problems:
  - Saturation of sigmoids
  - Even with a  relu, gradients are highly dependent on output values at each layer. Which might result in haphazard steps with internal covariate shift. Thus slower learning rates are required to avoid missing minima.

## Existing attempts
- Relu
- Careful initialization
- Small learning rates

## Batch Normalization
- Attempts to reduce internal covariate shift.
- Also beneficial on the gradient flow through the network, by reducing the dependence of gradients on the scale of parameters.
- Thus can have much higher learning rates
- Also happens to regularize the model

- Internal Covariate Shift: Defined  as *the change in the distribution of network activations due to  the  change in network parameters during training.*

- [@series/lncs/LeCunBOM12] Network training converges faster if its inputs are whitened - i.e., linearly transformed to have zero means and unit variances, and decorrelated.
- Here we try to whiten inputs at each layer, to get the inputs closer to a fixed distribution, removing ill effects of the internal covariate shift

#### When normalizing, the gradients at a layer out of each test case flow through additional paths


Let  $\mathcal{X} = x_{1..N}$ is the set of values of $x$ an input to a layer $F(x,...)$ over the training set.

When normalizing $F(x,...)$ becomes $F(\hat{x},...)$, where $\hat{x} = \text{Norm}(x, \mathcal{X})$ represents the whitening/normalization process.

In unnormalized graph backprop, gradients flowing to $x_i$ would only be applicable to the $i^{th}$ training example's graph:
$$\frac{\partial L}{\partial x_i} = \frac{\partial F}{\partial x_i}\frac{\partial L}{\partial F}  $$

In the normalized version backprop, $F(\hat{x},...)$ gradients through $\hat{x_i}$
$$\frac{\partial L}{\partial \hat{x_i}} = \frac{\partial F}{\partial \hat{x_i}}\frac{\partial L}{\partial F}  $$
further flow through $x_i$ and entire $\mathcal{X}$, we need to calculate:
$$\frac{\partial \text{Norm}(x_i,\mathcal{X})}{\partial x_i} \text{ and jacobian }  \frac{\partial \text{Norm}(x_i,\mathcal{X})}{\partial \mathcal{X}} $$