# Flask Application Deployment

## During Local Development

The method for running an application with a development server is explained on the following page. Note that it should not be used in a production environment.

[Flask Documentation on Development Server](https://flask.palletsprojects.com/en/latest/server/)

There are two ways to run `hello.py` on a development server:

1. Using the `flask run` command:
   
   ```bash
   $ flask --app hello run

2. Including the following run method in the code:
   ```python
   if __name__ == "__main__":
    app.run(debug=True)

3. 
