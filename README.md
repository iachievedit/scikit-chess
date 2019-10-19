# scikit-chess

## What is this?

A playground for exploring machine learning with chess pieces and SciKit.

Currently covered:

* [Binary classifiers](https://en.wikipedia.org/wiki/Binary_classification)
* [One vs. All classifiers](https://en.wikipedia.org/wiki/Multiclass_classification#One-vs.-rest)

## Prerequisites
### macOS

* [Homebrew](https://brew.sh/)
* [Imagemagick](https://www.imagemagick.org/script/index.php) (`brew install imagemagick`)
* Python 3 (`brew install python`)
* virtualenv (`pip3 install virtualenv`)

### Ubuntu

## Getting Started

```
cd scikit-chess
pip3 install virtualenv
virtualenv -p python3.x env
source env/bin/activate
pip3 install -r requirements.txt
```

As of this writing `brew install python` will install Python 3.7, so use `virtualenv -p python3.7 env`.

## Generating the Dataset

```
./makeImages.py
./makeDataset.py
```

## Training a Binary Classifier

### Using the Jupyter Notebook

### Using Python
