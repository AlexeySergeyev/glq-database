# Welcome to the main page of the Gravitationally Lensed Quasars (GLQ) Database

Gravitationally lensed quasars occur when the light from a distant quasar is bent and magnified by the gravitational field of an intervening massive object, such as a galaxy or galaxy cluster. This effect creates multiple, distorted images of the quasar, often forming a ring-like or arc structure around the lensing object. This phenomenon not only helps astronomers study the properties of quasars themselves but also provides a valuable tool for probing the distribution of dark matter and measuring the expansion rate of the universe, as it allows for the observation of galaxies and matter that are otherwise too faint or distant to detect.

![Caustic](lenses/static/lenses/caustic.jpg)
This database draws upon the <a href="https://www.cfa.harvard.edu/castles/"> CASTLES Survey </a> and the <a href="http://www-utap.phys.s.u-tokyo.ac.jp/~sdss/sqls/index.html">SQLS</a> gravitationally lensed quasar catalogs and includes some recently discovered GLQs. It features astrometric and photometric information exclusively about confirmed gravitationally lensed quasars. Note that it does not include static variability lensing objects, such as galaxy-galaxy lenses or weak lensing objects.

## Project Structure

The main application is `lenses` which is located in the `lenses/` directory. The project settings are located in `mysite/settings.py`.

## Installation

1. Clone the repository.
2. Install the dependencies using pip:

```sh
pip install -r requirements.txt
```

## Running the Application

You can start the application by running the following command in the terminal:

```code
python manage.py runserver
```

## Testing

To run the tests, use the following command:

```python
python lenses/tests.py
```

## Media Files

Media files are stored in the [media](media/) directory. The settings for media files can be found in [settings](mysite/settings.py).

## Database

The SQLite database file name is db.sqlite3.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License.

Please modify this template to fit your project's specific needs.
