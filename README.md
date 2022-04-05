<div id="top"></div>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Commits][commit-shield]][commit-url]
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
![PyPI - Downloads](https://img.shields.io/pypi/dm/gen-pygments-css?style=for-the-badge)    <!-- This link wont work in the reference style. -->
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
<!-- [![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <!-- <a href="https://github.com/hreikin/gen-pygments-css">
    <img src="docs/assets/logo.png" alt="Logo" width="80" height="80">
  </a> -->

<h3 align="center">Generate Pygments CSS</h3>

  <p align="center">
    Generate CSS stylesheets for each Pygments supported style.
    <br />
    <a href="https://hreikin.github.io/gen-pygments-css/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hreikin/gen-pygments-css">View Demo</a>
    ·
    <a href="https://github.com/hreikin/gen-pygments-css/issues">Report Bug</a>
    ·
    <a href="https://github.com/hreikin/gen-pygments-css/issues">Request Feature</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <!-- <li><a href="#prerequisites">Prerequisites</a></li> -->
        <li><a href="#installation">Installation</a></li>
        <ul>
          <li><a href="#install-with-pip">Install With PIP</a></li>
          <li><a href="#install-from-source">Install From Source</a></li>
        </ul>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

Generate CSS stylesheets for each Pygments supported style.

- Github Link: [https://github.com/hreikin/gen-pygments-css](https://github.com/hreikin/gen-pygments-css)  
- PyPi Link: [https://pypi.org/project/gen-pygments-css/](https://pypi.org/project/gen-pygments-css/)  
- PDF Documentation: [https://hreikin.github.io/gen-pygments-css/pdf/gen-pygments-css-documentation-LATEST.pdf](https://hreikin.github.io/gen-pygments-css/pdf/gen-pygments-css-documentation-LATEST.pdf)

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

- [Pygments](https://github.com/pygments/pygments)
- [Python](https://www.python.org/)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- GETTING STARTED -->
## Getting Started

<!-- This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ``` -->

### Installation

To get a local copy up and running choose one of the below install instructions and follow the steps provided.

#### Install With PIP

The simplest way to install `gen-pygments-css` is to use `pip`:

```sh
pip install gen-pygments-css
```

#### Install From Source

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

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
### Usage

CSS stylesheets for all `Pygments` styles are output into a created `css/` 
directory by default, this can be overridden. 
    
```python

from gen_pygments_css.gen_pygments_css import gen_pygments_css
        
# Called with no arguments.
gen_pygments_css()
       
# Called with a string passed into the styles_list.
gen_pygments_css(styles_list="monokai")
        
# Called with a list of strings passed into the styles_list.
gen_pygments_css(styles_list=["monokai", "stata-dark"])
       
# Call with a CSS selector defined.
gen_pygments_css(css_selector=".highlight")

# Call with a multiple arguments defined.
gen_pygments_css(css_selector=".highlight", styles_list=["monokai", "stata-dark"])

# Call with a relative custom css_dir.
gen_pygments_css(css_dir="assets/styles/")

# Call with an absolute custome css_dir.
gen_pygments_css(css_dir="/home/user/project/assets/styles/")
        
# Call the function and create a list of strings containing the paths of all 
# stylesheets.
my_list = gen_pygments_css()

```

_For more examples, please refer to the [Documentation](https://hreikin.github.io/gen-pygments-css)_

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

<!-- - [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature -->

See the [open issues](https://github.com/hreikin/gen-pygments-css/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTACT -->
## Contact

Github Link: [https://github.com/hreikin/gen-pygments-css](https://github.com/hreikin/gen-pygments-css)  
PyPi Link: [https://pypi.org/project/gen-pygments-css/](https://pypi.org/project/gen-pygments-css/)  
PDF Documentation: [https://hreikin.github.io/gen-pygments-css/pdf/gen-pygments-css-documentation-LATEST.pdf](https://hreikin.github.io/gen-pygments-css/pdf/gen-pygments-css-documentation-LATEST.pdf)

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- ACKNOWLEDGMENTS -->
<!-- ## Acknowledgments

* []()
* []()
* []()

<p align="right">(<a href="#top">back to top</a>)</p> -->

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hreikin/gen-pygments-css.svg?style=for-the-badge
[contributors-url]: https://github.com/hreikin/gen-pygments-css/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hreikin/gen-pygments-css.svg?style=for-the-badge
[forks-url]: https://github.com/hreikin/gen-pygments-css/network/members
[stars-shield]: https://img.shields.io/github/stars/hreikin/gen-pygments-css.svg?style=for-the-badge
[stars-url]: https://github.com/hreikin/gen-pygments-css/stargazers
[issues-shield]: https://img.shields.io/github/issues/hreikin/gen-pygments-css.svg?style=for-the-badge
[issues-url]: https://github.com/hreikin/gen-pygments-css/issues
[license-shield]: https://img.shields.io/github/license/hreikin/gen-pygments-css.svg?style=for-the-badge
[license-url]: https://github.com/hreikin/gen-pygments-css/blob/master/LICENSE.txt
<!-- [linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555 -->
<!-- [linkedin-url]: https://linkedin.com/in/linkedin_username -->
<!-- [product-screenshot]: docs/assets/screenshot.png -->
[commit-shield]: https://img.shields.io/github/commit-activity/m/hreikin/gen-pygments-css?style=for-the-badge
[commit-url]: https://github.com/hreikin/gen-pygments-css/graphs/commit-activity