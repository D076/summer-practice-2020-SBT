# Auth/Validation and user permissions microservice

[![Build Status](https://travis-ci.com/D076/summer-practice-2020-SBT.svg?branch=nightlyVersion)](https://travis-ci.com/D076/summer-practice-2020-SBT)
[![codecov](https://codecov.io/gh/D076/summer-practice-2020-SBT/branch/nightlyVersion/graph/badge.svg)](https://codecov.io/gh/D076/summer-practice-2020-SBT)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/D076/summer-practice-2020-SBT/badges/quality-score.png?b=nightlyVersion)](https://scrutinizer-ci.com/g/D076/summer-practice-2020-SBT/?branch=nightlyVersion)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/caf52ef7185f43d48e1017f9a6686126)](https://www.codacy.com/manual/D076/summer-practice-2020-SBT?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=D076/summer-practice-2020-SBT&amp;utm_campaign=Badge_Grade)
[![Requirements Status](https://requires.io/github/D076/summer-practice-2020-SBT/requirements.svg?branch=nightlyVersion)](https://requires.io/github/D076/summer-practice-2020-SBT/requirements/?branch=nightlyVersion)
[![GitHub last commit (branch)](https://img.shields.io/github/last-commit/D076/summer-practice-2020-SBT/nightlyVersion)](https://github.com/D076/summer-practice-2020-SBT/commits/nightlyVersion)
[![GitHub contributors](https://img.shields.io/github/contributors/d076/summer-practice-2020-SBT)](https://github.com/D076/summer-practice-2020-SBT/graphs/contributors)
[![Discord](https://img.shields.io/discord/315390629997838349)](https://discord.gg/ks5pT6U)

## Installation

Use the paсkage manager [pip](https://pip.pypa.io/en/stable/) and [virtualenv](https://virtualenv.pypa.io/en/latest/) for building.

#### Windows
```bash
git clone https://github.com/D076/summer-practice-2020-SBT/
cd summer-practice-2020-SBT
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
set APP_SETTINGS=config.DevelopmentConfig
set DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost/DBNAME
python manage.py runserver
```

#### Linux and macOS
```bash
git clone https://github.com/D076/summer-practice-2020-SBT/
cd summer-practice-2020-SBT
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
export APP_SETTINGS=config.DevelopmentConfig
export DATABASE_URL=postgresql://USERNAME:PASSWORD@localhost/DBNAME
python3 manage.py runserver
```
