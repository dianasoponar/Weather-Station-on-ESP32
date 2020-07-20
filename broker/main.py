import machine, network, time, curl


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

# wifi = init_wifi("signalhuset", "signal+huset2017")
# wifi = init_wifi("HomeBox-10E0_5G", "a6cfdf567")
wifi = init_wifi("AndroidAPAD82", "odon3187")

dht = machine.DHT(machine.Pin(2), machine.DHT.DHT11)
# dht.read()  #Returns status, temperature (C) and humidity (%)

local_name = 'diana-1'
unique_id  = 'diana246813'
mqtt = network.mqtt(local_name,
    'mqtt://broker.hivemq.com',
    clientid=unique_id,
  #optional callbacks here
  )

mqtt.start()

while True:
    time.sleep(300)
    print(mqtt.publish('diana/weather', str(dht.read()[1])))
