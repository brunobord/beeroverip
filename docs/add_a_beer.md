# How to add a beer

## Image

* Grab the image file.
* Open it in an program that is able to resize an image (ex: gthumb, gimp...)
* Resize: the biggest dimension must be 500px.
* if necessary, rename the file (à la slug)
* Make a copy of that image in ``project/beers/media/beers``


## Fixtures:

Update the ``beers.json`` fixture using the ``beer_data_template.json`` file:

```json

    [
        {
            "pk": <beer_pk>,
            "model": "beers.beer",
            "fields": {
                "name": "<beer name>",
                "slug": "<beer slug>"
            }
        },
       {
            "pk": <img_pk>,
            "model": "beers.beerimage",
            "fields": {
                "credits": "<description>",
                "beer": <beer_pk>,
                "picture": "beers/<img_name>.jpg",
                "upload_date": "<now>"
            }
        }
    ]
```

Please note:

* beer_pk must be unique (increment)
* img_pk must be unique, and not necessarily identical to beer_pk
* upload_date takes the form: "YYYY-MM-DD hh:mm:ss"

**Important Note**: If the beer is already in the database, you'll just have to note its beer_pk and only add the image file to the fixture.

### Testing

Once the ``beers.json`` is ok, run the tests:

```bash
$ python manage.py test beers
```

Or, run the dev server and check the website:

```bash
$ python manage.py runserver
```

### Commit

If necessary, add the name of the contributor in the CONTRIBUTORS.md file.

Commit your changes:

```bash
$ cd /path/to/application/beers
$ git add .
$ git commit -a -m "with a nice commit message"
```

You can push your changes on your own fork on Github, and create a pull-request.
