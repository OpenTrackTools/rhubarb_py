from rhubarb import create_app

app = create_app()

if 'main' == __name__:
    app.run()
    