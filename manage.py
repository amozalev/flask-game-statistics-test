import app
import config

app = app.create_app()

if __name__ == '__main__':
    app.run(host=config.Config.HOST, port=config.Config.PORT)
