
<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]




<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/OliverSaarela/ml-probability">
    <img src="img/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Tennis match probabilities</h3>

  <p align="center">
    Predicts men's atp match outcomes using tensorflow machine learning.
    <br />
    <a href="https://github.com/OliverSaarela/ml-probability"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/OliverSaarela/ml-probability">View Demo</a>
    ·
    <a href="https://github.com/OliverSaarela/ml-probability/issues">Report Bug</a>
    ·
    <a href="https://github.com/OliverSaarela/ml-probability/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A learning project for machine learning.
Using data of tennis games to predict winners.

The project contains a HTTP server and a React site using that server to give prediction to users.

### Built With

* [Python](https://www.python.org/)
* [React](https://reactjs.org/)
* [TensorFlow](https://www.tensorflow.org/)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to use the software and how to install it.
* npm
```sh
npm install npm@latest -g
```
* [python 3.7.6](https://www.python.org/)

### Installation
 
1. Clone the repo
```sh
git clone https://github.com/OliverSaarela/ml-probability.git
```

2. Install NPM packages
```sh
npm install
```

3. Install Python packages
```sh
conda create --name <env> --file requirements.txt
```
Or if you already have an environment
```sh
conda install --file requirements.txt
```

<!-- USAGE EXAMPLES -->
## Usage
### Setting up
First to download the needed files run `data.py` file. Say yes to updating data. You can also retrain the model and regenerate the empty `picked_data.csv` used in making prediction this way.
![data_console](img/data_console.JPG)
### Server
To start the server run the `main.py` file.
The server starts on http://localhost:8080 by default. This can be changed by changing the constants in `main.py`.

An HTTP GET request returns a list of players in JSON.  
An HTTP POST expects a JSON object in the form of
```json
{
	"player1": "Nadal R",
	"player2": "Federer R",
	"surface": "Hard"
}
```
and it returns a prediction of match win chance as
```json
{
    "result": "Federer R Win chance against Nadal R on Hard court: 28.42%"
}
```

To shut down the server you need to a Keyboard Interrupt `Ctrl + C` on the terminal running it.
### UI
To start the user interface run the command
```sh
npm start
```
which will start react. By default it is usually on http://localhost:3000.

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/OliverSaarela/ml-probability/issues) for a list of proposed features (and known issues).



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- CONTACT -->
## Contact

Project Link: [https://github.com/OliverSaarela/ml-probability](https://github.com/OliverSaarela/ml-probability)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

### Data
* [Tennis match and player data](https://data.world/tylerudite/atp-match-data)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/OliverSaarela/ml-probability.svg?style=flat-square
[contributors-url]: https://github.com/OliverSaarela/ml-probability/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/OliverSaarela/ml-probability.svg?style=flat-square
[forks-url]: https://github.com/OliverSaarela/ml-probability/network/members
[stars-shield]: https://img.shields.io/github/stars/OliverSaarela/ml-probability.svg?style=flat-square
[stars-url]: https://github.com/OliverSaarela/ml-probability/stargazers
[issues-shield]: https://img.shields.io/github/issues/OliverSaarela/ml-probability.svg?style=flat-square
[issues-url]: https://github.com/OliverSaarela/ml-probability/issues
[license-shield]: https://img.shields.io/github/license/OliverSaarela/ml-probability.svg?style=flat-square
[license-url]: https://github.com/OliverSaarela/ml-probability/blob/master/LICENSE
[product-screenshot]: images/screenshot.png
