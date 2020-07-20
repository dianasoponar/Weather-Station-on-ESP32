import machine, network, time, curl, json
from forecast import Forecast
curl.options(bodylen=4096)

def init_wifi(apname, password, timeout=3000):
  """Connect to wifi. A timeout (milliseconds) will cause the function to block
  until the timeout has expired or a successful connection is made."""
  wifi = network.WLAN(network.STA_IF)
  wifi.active(True)
  wifi.connect(apname, password)
  if timeout > 0:
    time.sleep_ms(1000)
    now = time.ticks_ms()
    while True:
      if wifi.ifconfig()[0] != '0.0.0.0':
        print("Connected, IP: {}".format(wifi.ifconfig()[0]))
        break
      if time.ticks_ms() - now > timeout:
        break
  return wifi

wifi = init_wifi("signalhuset", "signal+huset2017")
# wifi = init_wifi("HomeBox-10E0_5G", "a6cfdf567")
# wifi = init_wifi("AndroidAPAD82", "odon3187")

status, header, data = curl.get('api.openweathermap.org/data/2.5/onecall?lat=55.6761&lon=12.5683&exclude=minutely,hourly,current&&units=metric&appid=4641ad3e90202b3e5b93bb82490ca04f')
weather = Forecast(json.loads(data)['daily'])

servo = machine.PWM(machine.Pin(17), freq=50)
pin_r = machine.PWM(machine.Pin(27))
pin_g = machine.PWM(machine.Pin(26))
pin_b = machine.PWM(machine.Pin(25))

def on_data(temp):
    print(temp[2])
    today = json.loads(data)['daily'][0]['weather'][0]
    print(today['main'])
    if today['main'] == 'Clear':
        servo.duty(7)
    elif today['main'] == 'Clouds':
        servo.duty(11)
    elif today['main'] == 'Rain':
        print("Rain")
        servo.duty(3)

    if (int(temp[2]) < 10):
        pin_r.duty(0)
        pin_g.duty(0)
        pin_b.duty(100)
        servo.duty(11)
    if (int(temp[2]) >= 10 and int(temp[2]) < 20):
        pin_r.duty(0)
        pin_g.duty(50)
        pin_b.duty(50)
        servo.duty(3)
    if (int(temp[2]) >= 20 and int(temp[2]) < 25):
        pin_r.duty(0)
        pin_g.duty(100)
        pin_b.duty(0)
    elif (int(temp[2]) >= 25 and int(temp[2]) < 30):
        pin_r.duty(50)
        pin_g.duty(50)
        pin_b.duty(0)
    elif (int(temp[2]) >= 30):
        servo.duty(7)
        pin_r.duty(100)
        pin_g.duty(0)
        pin_b.duty(0)

local_name = 'diana-2'
unique_id  = 'diana24681342'
mqtt = network.mqtt(local_name,
    'mqtt://broker.hivemq.com',
    clientid=unique_id,
    data_cb=on_data
  )
time.sleep(10)
mqtt.start()
connected = mqtt.subscribe('diana/weather')
print("MQTT connected:", connected)
