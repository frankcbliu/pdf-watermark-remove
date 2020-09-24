# pdf-watermark-remove
convert pdf to imgs, then remove the watermark and convert them to pdf. 

## Usage

1. need to install poppler

on Mac, use:
```
brew install poppler
```

2. change the paths

open `remove-watermark.py`, and then change these to your own file/dir path

put the pdf file need to remove-watermark under the `input_dir`;
and then create a `output_dir` to receive the pdf after converting;
the most important, create a empty image dir to be the `img_dir`.

```python
# source pdf path
input_dir = '/Users/frank/Code/Python/from'
# target pdf path
output_dir = '/Users/frank/Code/Python/to'
# temp image dir path
img_dir = '/Users/frank/Code/Python/temp'
```

Notice! `img_dir` must be a empty dir, because the code will delete all the jpg file under the `img_dir` after completing the conversion.

3. run the code