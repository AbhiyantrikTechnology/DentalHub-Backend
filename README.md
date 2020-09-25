# About
[Dental Hub Open Source Project](https://dentalhubproject.org)is designed for community health professionals
delivering the Basic Package of Oral Care (topical fluorides, ART, simple extraction, and caries
risk assessment) in primary care settings.

Dental Hub records basic patient information, medical history, and screening questions that include
key metrics for oral health surveillance across a community population. A simplified odontogram for
recording treatments provided is easy to use for non-dentist, allied health professionals trained in
the Basic Package of Oral Care. Data can be aggregated in a back-end database that will reflect a
variety of trends to inform continued improvement of oral health care delivery in primary care
settings.

Dental Hub will help guide providers through a progression of interactions from history-taking to
differential diagnosis, treatment planning, and referral. A patient recall screen presents upon
login, making it easy for community-level providers to stay in close contact with patients for
continued care and follow-up.


## How to run?

### To run with docker-compose

Check configuration in `docker-compose.yml`  

1. To build docker `docker-compose build`
2. To run docker `docker-composer up`
3. To shutdown docker containers `docker-composer down`

### To run with virtualenv

Update `SECRET_KEY`, `DATABASES`, `CACHES` and email configuration in `dental/settings.py`. Then

1. To install requirements `pip install -r requirements/<requirement_name>`
2. To run the system  `python manage.py runserver`

## Contributing
We encourage you to contribute to DentalHub Backend! Please check out the [Contributing to
DentalHub Android App guide](https://github.com/AbhiyantrikTechnology/DentalHub-Backend/blob/master/CONTRIBUTING.md)
for guidelines about how to proceed. [Join us!](https://groups.google.com/forum/#!forum/dentalhub)


## License
[MIT](https://github.com/AbhiyantrikTechnology/DentalHub-Backend/blob/master/LICENSE)

## Discussion group
[dentalhub@googlegroups.com](https://groups.google.com/forum/#!forum/dentalhub)

