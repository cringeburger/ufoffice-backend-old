from resources import app
from resources.routes import (
    login, tasks, team, team_name, 
    leaderboard, leaderboard_place,
    notes
)

# ___Route list___
#   /login
#   /registration
#   /tasks      methods = ['GET', 'POST', 'PATCH']
#
#
#
#
#
#



@app.route('/')
def main():
    return '''
        <div class="flex">
            <h2 align="middle" class = "text">UFOffice api v1.0.0</h2>
        </div>
        <style>
            body{
                background-size: 100% 100%;
                background-repeat: no-repeat;
                background-image: url(https://sun9-4.userapi.com/impg/nfIdI4lWgA0M5Jp7gjdxjSwfn_aKQY4zKi4TDA/5fnvo893YMU.jpg?size=1532x858&quality=96&sign=9fa12502499a9f444af27ffb33aa5d64&type=album);
            }
            .text{
                font-size: 30pt;
                color: black;
            }
            .flex {
                align-content: center;
                text-align: center;
                text-shadow: 1px 1px 2px blue, 0 0 1em blue, 0 0 0.2em blue;
                width: 100%;
                height: 800px;
            }
        </style>
    '''
