# Rasa Chatbot

This project is a chatbot built with Rasa. It's designed to provide help in calculations for user.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

You need to have a version of higher than Python 3.6  but lower thant 3.10 installed on your machine. You can download Python [here](https://www.python.org/downloads/).

### Installation

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Humancannonball/rasa-calc.git
```

2. Navigate to the project directory:
    
```bash
cd rasa-calc
```
3. Install the required packages:
Set up your virtual enviroment by following the instructions on the Rasa website:
https://rasa.com/docs/rasa/installation/environment-set-up
Follow the instructions on the Rasa website to install Rasa Open Source:
https://rasa.com/docs/rasa/installation/environment-set-up


4. Train the model:

```bash
rasa train
```
5. Run the chatbot and action server in seperate terminals:
```bash
rasa run actions
```
```bash
rasa shell
```

