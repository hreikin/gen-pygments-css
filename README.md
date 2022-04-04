# Generate Pygments CSS Stylesheets

Generate `CSS` stylesheets for each `Pygments` supported style.
    
CSS stylesheets for all `Pygments` styles are output into a created `css/` 
directory by default. 
    
To generate a single stylesheet pass in a string containing the name of a 
`Pygments` style or to generate multilple stylesheets pass in a list of 
strings containing `Pygments` style names.
    
Example Usage:
    
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
        
# Create a list of strings containing the paths of all stylesheets.
my_list = gen_pygments_css()
        
# Call with a CSS selector defined.
gen_pygments_css(css_selector=".highlight")
        
```
