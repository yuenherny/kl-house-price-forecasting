# Outlier Detection

## Experimented techniques
The techniques we experimented are:
1. DBSCAN
2. HDBSCAN
3. OneClassSVM
4. OPTICS
5. BIRCH
6. KMeans

## Features used to train the models
The features we used to train the models are:
1. `built_up`
2. `land_area`
3. `price_psf`
where 2D is `built_up` and `land_area` and 3D is `built_up`, `land_area` and `price_psf`.

## Duplicates
We also experimented with duplicates (29,273 or 9.94%). Some models are trained with duplicates and some are trained without duplicates.
