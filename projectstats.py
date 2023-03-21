import scratchattach as scratch3
import time
from os import environ

session = scratch3.login(environ['username'], environ['password'])
projectid=796887707
conn = session.connect_cloud(projectid)
project = session.connect_project(projectid)

while(True):
    conn.set_var('loves', project.loves)
    conn.set_var('favorites', project.favorites)
    conn.set_var('remixes', project.remix_count)
    conn.set_var('views', project.views)
    project.update()
    print('Updated!')
    time.sleep(5)
