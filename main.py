import logging
import subprocess

from pathlib import Path
from pygments.styles import get_all_styles

logging.basicConfig(level=logging.DEBUG)

def gen_pygments_css(css_dir="css/", styles_list=list(get_all_styles())):
    """Generate `CSS` stylesheets for each `Pygments` supported style.
    
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
        
        ```

    CSS stylesheets for all `Pygments` styles are output into a created `css/` 
    directory by default. 
    
    To generate a single stylesheet pass in a string containing the name of a 
    `Pygments` style or to generate multilple stylesheets pass in a list of 
    strings containing `Pygments` style names.
    
    Args:
        css_dir (str): Relative or absolute string of the location to output the 
            generated CSS stylesheets to.
        styles_list (list(str)): A string or list of strings containing the name 
            of `Pygments` styles. Defaults to a list of all style names returned 
            by the `get_all_styles()` function from `Pygments` 
            (https://pygments.org/docs/api/?highlight=get_all_styles#pygments.styles.get_all_styles).
    
    Returns:
        file_list (list(str)): A list of strings containing the location(s) of 
            the generated CSS stylesheet(s).
    """
    if isinstance(styles_list, str):
        styles_str = styles_list
        styles_list = list()
        styles_list.append(styles_str)
    css_dir = Path(css_dir).resolve()
    logging.info(f"Creating '{css_dir}' directory if it doesn't already exist.'")
    css_dir.mkdir(parents=True, exist_ok=True)
    
    file_list = list()
    logging.info("Generating CSS stylesheets.")
    for item in styles_list:
        file_location = f"{css_dir.resolve()}/{item}.css"
        file_list.append(file_location)
        logging.info(f"Style: {item}")
        logging.info(f"Location: {file_location}")
        subprocess.run([f"pygmentize -S {item} -f html -a .highlight > {file_location}"], shell=True)
    logging.info(f"Generated CSS stylesheets available at '{css_dir}'.")
    return file_list

if __name__ == "__main__":
    gen_pygments_css()
