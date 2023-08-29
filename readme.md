<!-- PROJECT SHIELDS -->
[![PyTest][pytest]][pytest-url]
[![PyLint][pylint]][pylint-url]

<!-- PROJECT LOGO -->
<br />
<div align="center" id="readme-top">
  <a href="https://github.com/dariustb/gofish">
    <img src="https://i0.wp.com/www.thegamegal.com/wp-content/uploads/2020/04/go-fish.png?fit=1213%2C689&ssl=1" height=200 alt="GF Logo">
  </a>

  <h1 align="center">Go Fish</h1>

  <p align="center">
    Python Go Fish game
    <br />
    <a href="https://dariustb.github.io/GoFish/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/dariustb/gofish/issues">Report Bug</a>
    ·
    <a href="https://github.com/dariustb/gofish/issues">Request Feature</a>
  </p>
</div>

<!-- ABOUT THE PROJECT -->
## About The Project
Welcome to the Go Fish console game! This project brings the classic card game of Go Fish to life in a text-based format. 

Immerse yourself in the excitement of asking for and collecting matching sets of cards as you compete against computer-controlled players. Experience the thrill of strategy and luck as you try to build your sets while also preventing your opponents from doing the same.

With a user-friendly text interface, this project aims to capture the essence of the Go Fish card game while providing an engaging and enjoyable gameplay experience. Get ready to dive into a world of cards, tactics, and fun as you challenge yourself to become the ultimate Go Fish champion right from your console.

_Please [refer to the documentation][docs] for the full breakdown and logic explanation of the app._

### Built With
* ![Python][python.io]

### Prerequisites

* [VS Code][vscode] (1.76.2 or greater)
* [Python 3][python] (3.11.0 or greater)
  * [pip 3][python] (versions 22.3 - 23.0.1)

### Install Dependencies
```sh
pip install -r requirements.txt
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Usage
```sh
python src/app.py
```
### Local Development
#### Unit Test
```sh
python -m pytest
```
#### Linting Test
```sh
pylint src/ tests/
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[app]:  #
[docs]: https://dariustb.github.io/gofish/

<!-- Technologies -->
[vscode]:   https://code.visualstudio.com/
[python]:   https://www.python.org/

<!-- Featured images -->
[product-screenshot]:   #

<!-- CI Test badges -->
[pytest]:   https://github.com/dariustb/gofish/actions/workflows/pytest.yml/badge.svg
[pylint]:   https://github.com/dariustb/gofish/actions/workflows/pylint.yml/badge.svg
[gpages]:   https://github.com/dariustb/gofish/actions/workflows/pages/pages-build-deployment/badge.svg 
[pytest-url]:   https://github.com/dariustb/gofish/actions/workflows/pytest.yml
[pylint-url]:   https://github.com/dariustb/gofish/actions/workflows/pylint.yml
[gpages-url]:   https://github.com/dariustb/gofish/actions/workflows/pages/pages-build-deployment

<!-- Markdown Badges -->
[python.io]:    https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54