import subprocess
import logging

from pathlib import Path
from pygments.styles import get_all_styles

logging.basicConfig(level=logging.DEBUG)

def gen_css(out_dir="css/"):
    """Generates `CSS` stylesheets for each `Pygments` supported style.
    
    Args:
        out_dir (str): Relative or absolute string of the location to output the 
            generated CSS stylesheets to.
    """
    styles = list(get_all_styles())
    css_dir = Path(out_dir).resolve()
    logging.info(f"Creating '{css_dir}' directory if it doesn't already exist.'")
    css_dir.mkdir(parents=True, exist_ok=True)
    logging.info("Generating CSS stylesheets.")
    for item in styles:
        logging.info(f"Style: {item}")
        logging.info(f"Location: {css_dir.resolve()}/{item}.css")
        subprocess.run([f"pygmentize -S {item} -f html > css/{item}.css"], shell=True)

if __name__ == "__main__":
    logging.debug("Logger initialized.")
    gen_css()
