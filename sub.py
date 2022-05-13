import os
import django
import mqtt
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_tutorial_4x.settings")
django.setup()


def handlerGenerator(models):
    def handler(client, userdata, msg):
        data = msg.payload.decode('utf-8')
        data_json = json.loads(data)

        models.objects.create(
            temperature=data_json["Temperature"],
            time=data_json["Time"],
        )

        print(data)

    return handler


if __name__ == "__main__":
    from weather.models import WeatherInfo

    scope = "6255c868649b297b8f217296"
    username = "625f2ba2649b297b8f2172aa"
    password = "1234"

    sub = mqtt.IdeaSkyMQTTSubscriber(
        scope, username, password, handlerGenerator(WeatherInfo)
    )
    sub.run()
