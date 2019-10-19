Title: Batch Normalization
Authors: voo4
Date: 2019-10-19
Category: papers
publications_src: content/bibliography.bib

Summary on [@DBLP:journals/corr/IoffeS15]

**Internal Covariate Shift** is defined as *the change in the distribution of network activations due to the change in network parameters during training.* It captures the change in activation values as training progresses. In a Deep Neural Network this change in distribution of inputs at each layer, as training progresses demands - carefuly paremeter initailization and slower learning rates. Batch Normalization is a technique that helps address these problems arising from internal covariate shift. 

Also batch normalizaiton helps by
- Permitting higher learning rates, and less careful initilization
- Acting as Regularizer, eliminating the need for Dropout
- Faster training. (Converges with 14 times fewer steps in the examples mentioned in the article)

## The problem
Training a Deep Neural Network is complicated - As outputs and gradients are affected by previous layers. Even careful parameter initialization can help keep inputs to activations in good regions, only to a limited extent/time. Beyond which gradients are zero either due to saturation or activations close to origin.

Problems arising from Internal Covariate Shift:

- When activations move out of linear regime of sigmoid, Gradients stop flowing.
 - And when using a relu, gradients are highly dependent on activation values (which experience an internal covariance shift). This might result in uncontrolled step sizes. Thus slower learning rates are required for convergence.

These problems are usually addressed using

- RELU as activation
- Careful initialization of weights ([@glorot2010understanding], [@DBLP:journals/corr/SaxeMG13])
- Small learning rates

## Batch Normalization

 Network training is known to converge faster if its inputs are whitened [@lecun1998efficient] - i.e., linearly transformed to have zero means and unit variances, and decorrelated.
 > It is know that convergence is usually faster if the average of each input is close to zero. In an extreme of all inputs being positive (or all inputs being negative) the weight updates have to be all of the same sign. The weights can only all decrease or all increase. If the actual solution requires some to decrease and some to increase, it can only be done by zigzagging. See [Youtube: Lecture 6 | Training Neural Networks I | CS231n](https://www.youtube.com/watch?v=wEoyxE0GP2M&feature=youtu.be&t=526) for a detailed explanation.
 
 Whiteninig the inputs to a neural network [Mean canellation + Decorrelation(PCA) + Covariance equalization] helps in better gradient flow. But the effects are diminished as we go deeper in the network. Batch normalization tries to apply the same at every layer, in an attempt to removing ill effects of the internal covariate shift.
 
 However a full whitening would require computation of Covariance matrix $\text{Cov}[x] = \mathbb{E}_{x \in \mathcal{X}}[xx^T] - \mathbb{E}[x]\mathbb{E}[x]^T$ and its inverse square root for computation of whitened activations. This is computationally complex and adds more complexity to the backpropogation. Hence decorrelation is typically skipped.
 
#### How it's done

##### At train time
> Each dimension's mean and variance is computed across the samples in the mini batch. The input is mean cancelled and scaled by inverse of variance.

For a layer with $d$-dimensional input $\mathrm{x}=\left(x^{(1)} \ldots x^{(d)}\right)$, each dimension is normalized
$$\widehat{x}^{(k)}=\frac{x^{(k)}-\mathrm{E}\left[x^{(k)}\right]}{\sqrt{\operatorname{Var}\left[x^{(k)}\right] + \epsilon}}$$

> The above normalization would result in constraining the inputs of every layer to $[-1, 1]$ (a soft constraint). This will make it impossible for the activations (say sigmoid) to ever learn to saturate. Hence additional provision is made to enable the normalization to become an identity function.

For each activation $x^{(k)}$ variables $\gamma^{(k)}, \beta^{(k)}$ are introduced which scale and shift the normalized value
$$
y^{(k)}=\gamma^{(k)} \widehat{x}^{(k)}+\beta^{(k)}
$$

This **Batch Normalizing Transformation** can be represented as:
$$ \mathrm{BN}_{\gamma, \beta}: x_{1 \ldots m} \rightarrow y_{1 \ldots m} $$


##### At evaluation time
> During evaluation/test, population statistics replace the batch statistics in batch normalization transformation

$$
\widehat{x}=\frac{x-\mathrm{E}[x]}{\sqrt{\operatorname{Var}[x]+\epsilon}}
$$

At every layer, for the estimates of $\mathrm{E}\left[x\right]$ and $\operatorname{Var}\left[x\right]$, population statistics are used. 

$$
\begin{aligned} \mathrm{E}[x] & = \mathrm{E}_{\mathcal{B}}\left[\mu_{\mathcal{B}}\right] \\ \operatorname{Var}[x] & = \frac{m}{m-1} \mathrm{E}_{\mathcal{B}}\left[\sigma_{\mathcal{B}}^{2}\right] \text{ An unbiased estimate for variance, considering } m \text{ batches} \end{aligned}
$$


#### With batch normalization, the gradients flow through additional paths
> Batch Normailzation is a differentiable transformation that introduces normalized activations into the network.

The mean, variance, etc., computed during normalization are considered for gradient backpropagation.

Let $x$ be an input to a layer $F(x,...)$. And $\mathcal{X} = x_{1..N}$ is the set of values of $x$ over the training set.

With batch normalization $F(x,...)$ is transformed to $F(\widehat{x},...)$, where $\widehat{x} = \text{Norm}(x, \mathcal{X})$ represents the whitening/normalization process.

In unnormalized graph backprop, gradients flowing to $x_i$ wouldn't flow through rest of $\mathcal{X}$:
$$\frac{\partial L}{\partial x_i} = \frac{\partial F}{\partial x_i}\frac{\partial L}{\partial F}  $$

In the normalized version backprop, $F(\widehat{x},...)$ gradients through $\widehat{x}_i$
$$\frac{\partial L}{\partial \widehat{x}_i} = \frac{\partial F}{\partial \widehat{x}_i}\frac{\partial L}{\partial F}  $$
further flow through $x_i$ and rest of $\mathcal{X}$, we need to calculate:
$$\frac{\partial \text{Norm}(x_i,\mathcal{X})}{\partial x_i} \text{ and jacobian }  \frac{\partial \text{Norm}(x_i,\mathcal{X})}{\partial \mathcal{X}} $$

### Benefits
- Activations can receive inputs in the linear regime throught all layers.
- Beneficial on the gradient flow through the network, by reducing the dependence of gradients on the scale of parameters. Thus higher learning rates can be used.
- Regularizes the model, reducing the need for Dropout.
  > A training example is seen in conjunction with the other examples in the mini-batch. Thus the network cannot produce deterministic values for *a* given training example. Thus acting like a regularizer. In other words, if the network tries to overfit a given example, it inadvertantly effects other training examples and thus will be penalized with a higher loss.

### Tensorflow implementation
**TODO**
