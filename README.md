# [RESULTS JNTUH](http://resultsjntuh.vercel.app/) - SERVICE </h1>
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/29064b56066d4799b6167567f710bb8b)](https://app.codacy.com/gh/khaja-moiz/jnuthresults-api/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
[![Website](https://img.shields.io/badge/Website-Results%20Jntuh-blue?style=flat&logo=world&logoColor=white)](https://resultsjntuh.up.railway.app/)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/khaja-moiz/jnuthresults-api)
![LICENSE](https://img.shields.io/github/license/khaja-moiz/jnuthresults-api)

<p align="center">
  <br>
  django | python | BeautifulSoup 
</p>

The Backbone of JNTUHRESULTS-WEB where all the semester results of a student and the results of all the classmates are fetched

## HOW IT WORKS

* Jntuh website doesn't have any api and it does not authenticate when a request is made it just sends back the response of that request
* I made a request and i got a response and using beautiful soup i have parse the html and i got my results

## API
* https://jntuhresults.up.railway.app/api/single?htno={Roll_NO}
* https://jntuhresults.up.railway.app/api/multi?from={from_roll_no}&to={To_roll_no}&code={code}


## Running locally in development mode

To get started, just clone the repository and run `pip install and python manage.py runserver`:

    git clone https://github.com/khaja-moiz/jntuhresults-api.git
    cd JNTUHRESULTS-SERVICE
    pip install -r requirements.txt
    python manage.py runserver

Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

## Questions? Need Help? Found a bug?

If you've got questions about setup, deploying, special feature implementation, or just want to chat with the developer, please feel free to contact me on <a href="mailto:khwaja.moizuddin786@gmail.com">mail</a>

Found a bug ? Go ahead and [submit an issue](https://github.com/khaja-moiz/jntuhresults-api/issues). And, of course, feel free to submit pull requests with bug fixes or changes to the `dev` branch.

Also feel free to message me if you have any ideas for small website tools that you can't yet find online. Thanks!

## Thanks

- [django](https://www.djangoproject.com/) is a high-level Python web framework that encourages rapid development and clean, pragmatic design
- [python](https://www.python.org/) is a programming language that lets you work quickly
and integrate systems more effectively.
- [THILAK REDDY](https://github.com/ThilakReddyy) for fast deployment Backend served
 
