# Generate Pygments CSS Stylesheets

## About The Project

Generate CSS stylesheets for each Pygments supported style.

- Github Link: [https://github.com/hreikin/gen-pygments-css](https://github.com/hreikin/gen-pygments-css)  
- PyPi Link: [https://pypi.org/project/gen-pygments-css/](https://pypi.org/project/gen-pygments-css/)  
- PDF Documentation: [https://hreikin.github.io/gen-pygments-css/pdf/gen-pygments-css-documentation-LATEST.pdf](https://hreikin.github.io/gen-pygments-css/pdf/tkintermd-documentation-LATEST.pdf)

### Built With

- [Pygments](https://github.com/pygments/pygments)
- [Python](https://www.python.org/)

## Installation

To get a local copy up and running choose one of the below install instructions and follow the steps provided.

### Install With PIP

The simplest way to install `gen-pygments-css` is to use `pip`:

```sh
pip install gen-pygments-css
```

### Install From Source

Alternatively you can install from source by following the steps below:

1. Clone the repo:
   ```sh
   git clone https://github.com/hreikin/gen-pygments-css.git
   cd gen-pygments-css/
   ```
2. Create and source a Python virtual environment:
   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```
3. Install requirements with `pip`:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

CSS stylesheets for all `Pygments` styles are output into a created `css/` 
directory by default, this can be overridden. 
    
```python
        
# Called with no arguments.
gen_pygments_css()
       
# Called with a string passed into the styles_list.
gen_pygments_css(styles_list="monokai")
        
# Called with a list of strings passed into the styles_list.
gen_pygments_css(styles_list=["monokai", "stata-dark"])
       
# Call with a custom css_dir, can be relative or absolute.
gen_pygments_css(css_dir="assets/styles/")
gen_pygments_css(css_dir="/home/user/project/assets/styles/")
        
# Call the function and create a list of strings containing the paths of all 
# stylesheets.
my_list = gen_pygments_css()
        
# Call with a CSS selector defined.
gen_pygments_css(css_selector=".highlight")
        
```