# One Hot Encoding

## Experimented techniques
We did not experiment with other techniques as literature showed that one hot encoding is the best for real estate price prediction.

## Features used to train the models
The encoded features are:
1. `township`
2. `building_type`
3. `tenure`

However `price_psf` and `price` are not encoded as they are the target variables and they correlate with each other, based on domain knowledge.
