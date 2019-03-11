from example_rt_mention import data

my_data = data[0]

media = my_data['quoted_status']['entities']['media'][0]

print(media['media_url']) # añadir :orig despues de la extensión para que sea mas grande