import scratchattach as scratch3
import time
from os import environ

session = scratch3.login(environ['username'], environ['password'])
connect = session.connect_cloud(796266004)

client = scratch3.CloudRequests(connect)

@client.request
def ping():
    print(f'{client.get_requester()} Pinged')
    return f'Received with timestamp : {client.get_timestamp()/1000}'

@client.request
def project_stats(argument1):
    print(f'{client.get_requester()} requested project stats with id : {argument1}')
    project = session.connect_project(argument1)
    try:
        data = []
        data.append(f'Title : {project.title}')
        data.append(f'Author : {project.author}')
        data.append(f'Loves : {project.loves}')
        data.append(f'Favorites : {project.favorites}')
        data.append(f'Remixes : {project.remix_count}')
        data.append(f'Views : {project.views}')
        return data
    except:
        return 'an error occurred'

@client.request
def user_stats(argument1):
    print(f'{client.get_requester()} requested user stats with username : {argument1}')
    user = session.connect_user(argument1)
    try:
        data = []
        data.append(f'Id : {user.id}')
        data.append(f'Country : {user.country}')
        data.append(f'Messages : {user.message_count()}')
        data.append(f'Followers : {user.follower_count()}')
        data.append(f'Followings : {user.following_count()}')
        data.append(f'Projects : {user.project_count()}')
        data.append(f'Join date : {user.join_date}')
        return data
    except:
        return 'an error occurred'

@client.event
def on_ready():
    print('Request handler is running')

client.run()
