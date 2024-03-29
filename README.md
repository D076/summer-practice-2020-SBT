# Auth/Validation and user permissions microservice

[![Build Status](https://travis-ci.com/D076/summer-practice-2020-SBT.svg?branch=master)](https://travis-ci.com/D076/summer-practice-2020-SBT)
[![codecov](https://codecov.io/gh/D076/summer-practice-2020-SBT/branch/master/graph/badge.svg)](https://codecov.io/gh/D076/summer-practice-2020-SBT)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/D076/summer-practice-2020-SBT/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/D076/summer-practice-2020-SBT/?branch=master)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/caf52ef7185f43d48e1017f9a6686126)](https://www.codacy.com/manual/D076/summer-practice-2020-SBT?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=D076/summer-practice-2020-SBT&amp;utm_campaign=Badge_Grade)
[![Requirements Status](https://requires.io/github/D076/summer-practice-2020-SBT/requirements.svg?branch=master)](https://requires.io/github/D076/summer-practice-2020-SBT/requirements/?branch=master)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/D076/summer-practice-2020-SBT/master)](https://github.com/D076/summer-practice-2020-SBT/commits/master)
[![GitHub contributors](https://img.shields.io/github/contributors/d076/summer-practice-2020-SBT)](https://github.com/D076/summer-practice-2020-SBT/graphs/contributors)

## About

This repository is a part of the summer internship at SberTech, a subsidiary of Sberbank's IT company. 
Internship was focused on design and development of a system implemented using a microservice architecture.

It was necessary to implement a platform that would allow performing the following actions:
+  Combine photos into collections
+  Share your collections with other users
+  Maintain a rating within each collection
+  Add tags to photos
+  Write annotations to photos

It was decided to create a system consisting of a set of microservices in the amount of four parts.
Development was carried out in teams of three to four people. Our team worked on design and development of a microservice for user data and access control.

#### List of microservices

+  [API Gateway and Service Discovery](https://github.com/lenivoe/summer-2020-SBT-team1)
+  [Auth/Validation and user permissions microservice](https://github.com/D076/summer-practice-2020-SBT)
+  [Microservice for content and metadata management](https://github.com/ASurtaev/SummerSberPractice)
+  [Collections and rating microservice](https://github.com/BorZzzenko/SummerPractice_SBT2020)

## Installation

Use the paсkage manager [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) for building.

Edit **application.cfg**:
+  Step 1: Fills DATABASE_URL with your database login and password (postgresql://user:password@host/database)
+  Step 2 (Optionally): Fills gateway host and port

#### Windows
```bash
git clone https://github.com/D076/summer-practice-2020-SBT/
cd summer-practice-2020-SBT
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
python manage.py runserver [-h HOST] [-p PORT]
```

#### Linux and macOS
```bash
git clone https://github.com/D076/summer-practice-2020-SBT/
cd summer-practice-2020-SBT
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 manage.py db init
python3 manage.py db migrate
python3 manage.py db upgrade
python3 manage.py runserver [-h HOST] [-p PORT]
```

For generating roles and permissions run **roles_permissions.sql** script in your database.
