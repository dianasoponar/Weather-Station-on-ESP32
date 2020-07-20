import machine, display, time

class Forecast(object):
    def __init__(self, data):
         # Displat size: 240x135
         self.tft = display.TFT()

         # Display initialization
         self.tft.init(self.tft.ST7789, rot=self.tft.LANDSCAPE, miso=17, backl_pin=4, backl_on=1, mosi=19, clk=18, cs=5, dc=16, splash=False)
         self.tft.setwin(40,52,320,240)
         # If colors are wrong (white background)
         self.tft.tft_writecmd(0x21)
         self.tft.font(font=self.tft.FONT_Ubuntu, rotate=90)
         self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

         self.show_day_1(data[0])
         self.show_day_2(data[1])
         self.show_day_3(data[2])

    def show_day_1(self, day):
        date = str(time.gmtime(day['dt'])[2]) + " " + self.months[time.gmtime(day['dt'])[1]-1]
        self.tft.text(235, 5, date, color=self.tft.WHITE)
        if day['weather'][0]['main'] == 'Clear':
            self.draw_sun(205, 15)
        elif day['weather'][0]['main'] == 'Clouds' and day['weather'][0]['description'] == 'few clouds':
            self.draw_sun_clouds(205, 12)
        elif day['weather'][0]['main'] == 'Clouds':
            self.draw_clouds(205, 12, self.tft.CYAN)
        elif day['weather'][0]['main'] == 'Rain':
            self.draw_clouds(205, 12, self.tft.BLUE)
        self.tft.text(210, 55, str(day['temp']['day']) + "  C", color=self.tft.WHITE)
        self.tft.circle(210, 102, 3, color=self.tft.WHITE)
        self.tft.text(190, 5, str(day['weather'][0]['description']), color=self.tft.WHITE)

    def show_day_2(self, day):
        date = str(time.gmtime(day['dt'])[2]) + " " + self.months[time.gmtime(day['dt'])[1]-1]
        self.tft.text(160, 5, date, color=self.tft.WHITE)
        if day['weather'][0]['main'] == 'Clear':
            self.draw_sun(130, 15)
        elif day['weather'][0]['main'] == 'Clouds' and day['weather'][0]['description'] == 'few clouds':
            self.draw_sun_clouds(130, 12)
        elif day['weather'][0]['main'] == 'Clouds':
            self.draw_clouds(130, 12, self.tft.CYAN)
        elif day['weather'][0]['main'] == 'Rain':
            self.draw_clouds(130, 12, self.tft.BLUE)
        self.tft.text(135, 55, str(day['temp']['day']) + "  C", color=self.tft.WHITE)
        self.tft.circle(135, 102, 3, color=self.tft.WHITE)
        self.tft.text(115, 5, str(day['weather'][0]['description']), color=self.tft.WHITE)

    def show_day_3(self, day):
        date = str(time.gmtime(day['dt'])[2]) + " " + self.months[time.gmtime(day['dt'])[1]-1]
        self.tft.text(80, 5, date, color=self.tft.WHITE)
        if day['weather'][0]['main'] == 'Clear':
            self.draw_sun(50, 15)
        elif day['weather'][0]['main'] == 'Clouds' and day['weather'][0]['description'] == 'few clouds':
            self.draw_sun_clouds(50, 12)
        elif day['weather'][0]['main'] == 'Clouds':
            self.draw_clouds(50, 12, self.tft.CYAN)
        elif day['weather'][0]['main'] == 'Rain':
            self.draw_clouds(50, 12, self.tft.BLUE)
        self.tft.text(55, 55, str(day['temp']['day']) + "  C", color=self.tft.WHITE)
        self.tft.circle(55, 102, 3, color=self.tft.WHITE)
        self.tft.text(35, 5, str(day['weather'][0]['description']), color=self.tft.WHITE)

    def draw_sun(self, x, y):
        self.tft.circle(x, y, 9, color=self.tft.YELLOW, fillcolor=self.tft.YELLOW)

    def draw_clouds(self, x, y, color):
        self.tft.circle(x, y, 5, color=color, fillcolor=color)
        self.tft.circle(x, y + 7, 8, color=color, fillcolor=color)
        self.tft.circle(x, y + 17, 7, color=color, fillcolor=color)
        self.tft.circle(x, y + 25, 5, color=color, fillcolor=color)

    def draw_sun_clouds(self, x, y):
        self.tft.circle(x + 2, y + 22, 9, color=self.tft.YELLOW, fillcolor=self.tft.YELLOW)
        self.tft.circle(x, y, 5, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(x, y + 7, 8, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(x, y + 17, 7, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
        self.tft.circle(x, y + 25, 5, color=self.tft.CYAN, fillcolor=self.tft.CYAN)
