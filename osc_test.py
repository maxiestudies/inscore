import time
from pythonosc.udp_client import SimpleUDPClient

ip = "192.168.0.109"
port = 7000

client = SimpleUDPClient(ip, port)  # Create client

client.send_message("/ITL/maxi", 'new')
client.send_message("/ITL/maxi", "reset")   # Send float message
client.send_message("/ITL/maxi", ['fullscreen', 1])

time.sleep(2)
client.send_message("/ITL/maxi/text", ['set', 'txt' ,'Play Motherf**er!'])
client.send_message("/ITL/maxi/text", ['y', -0.5])
client.send_message("/ITL/maxi/text", ['fontSize', 50])

time.sleep(1)
client.send_message("/ITL/maxi/countdown", ['set', 'txt' ,'three'])
client.send_message("/ITL/maxi/countdown", ['fontSize', 40])
client.send_message("/ITL/maxi/countdown", ['y', -0.3])

time.sleep(1)
client.send_message("/ITL/maxi/countdown", ['set', 'txt' ,'two'])

time.sleep(1)
client.send_message("/ITL/maxi/countdown", ['set', 'txt' ,'one'])

time.sleep(1)
client.send_message("/ITL/maxi/countdown", ['set', 'txt' ,'play!'])
client.send_message("/ITL/maxi/score", ['set', 'gmn','[ a b c _ ]'])

time.sleep(3)
client.send_message("/ITL/maxi/countdown", ['set', 'txt' ,'play! and...'])

time.sleep(1)
client.send_message("/ITL/maxi/countdown", ['set', 'txt' ,'play again!'])
client.send_message("/ITL/maxi/score", ['set', 'gmn', '[ f f# g _ ]'])

time.sleep(5)
client.send_message("/ITL/maxi/score", 'del')

time.sleep(1)
client.send_message("/ITL/maxi/video", ['set', 'video', 'Downloads/rain.mp4'])
time.sleep(1)
client.send_message("/ITL/maxi/video", ['play', 1])
time.sleep(10)

client.send_message("/ITL/maxi/video", ['play', 0])
time.sleep(0.3)
client.send_message("/ITL/maxi/video", 'del')
# client.send_message("/ITL/maxi", 'reset')

time.sleep(1)

client.send_message("/ITL/maxi/text", ['set', 'txt' ,'More music Motherf**er!'])
client.send_message("/ITL/maxi/text", ['y', -0.5])
client.send_message("/ITL/maxi/text", ['fontSize', 50])
time.sleep(0.3)
client.send_message("/ITL/maxi/score", ['set', 'gmn', '[ a a# b c d# d ]'])

time.sleep(5)

client.send_message("/ITL/maxi/score", 'del')
client.send_message("/ITL/maxi/countdown", ['set', 'txt' ,'this is the end'])
client.send_message("/ITL/maxi/text", ['fontSize', 50])
