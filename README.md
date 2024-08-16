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
   ```

To run the application:

   ```bash
   $ python hello.py
   ```

## Production Environment

The method for deploying to a production environment is explained on the following page:
[Flask Documentation on Deployment](https://flask.palletsprojects.com/en/3.0.x/deploying/)

In a production environment, a WSGI server should be used. There are also methods to use it in combination with an HTTP server such as Apache (Reverse Proxy).

Examples of WSGI servers (refer to the above page for details):
Gunicorn
Waitress
mod_wsgi
uWSGI

## Reverse Proxy Configuration with Apache Server

Instructions on configuring a reverse proxy with Apache Server are explained on the following page:
[Flask Documentation on Apache HTTPD Deployment](https://flask.palletsprojects.com/en/3.0.x/deploying/apache-httpd/)

For more detailed information, refer to Apache’s documentation or wiki:
[Apache Documentation](https://httpd.apache.org/docs/2.4/)
[Apache Wiki](https://cwiki.apache.org/confluence/display/httpd/)
