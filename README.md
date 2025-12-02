# Team Activity Leaderboard App

## Team
Team Name: With My Boys
Members: David, John Kerby
Members: Jorda, Nathaniel Louie
Members: Masa, Sean Khyle
Members: Udiong, Arjay
Members: Vergara, Adrian

## Summary
Our team built a **Python-based Leaderboard application** that works through both:

- A **Command-Line Interface (CLI)** for adding and updating players
- A **Flask API** for accessing leaderboard data programmatically

This project helped us practice **OOP concepts**, working with a **CLI**, building a basic **REST API**, and collaborating as a team using **GitHub**.

## Roles
- Masa implemented CLI and Flask API
- David Developed the models and performed testing
- Jorda set up GitHub repository and code the 'app.py'
- Vergara Wrote the project documentation README.md
- Udiong make the pdf file

## Tools used
- Python 3  
- Flask   
- GitHub  
- Ngrok  
- VS Code  

## How to run the Project
1. python -m venv venv
2. activate venv
3. pip install -r requirements.txt
4. python app.py  # run api
5. python cli.py add "Name"  # add player
6. python cli.py score 1 10  # add score

## API
GET /players
POST /players { "name": "nat" }
POST /players/1/score { "points": 10 }