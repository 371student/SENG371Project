import bottle
import json
import sys

@bottle.get('/')
def index():
    return """
        <a>
            it works!
        </a>
    """


@bottle.post('/start')
def start():
    # data = bottle.request.json

    return json.dumps({
        'name': 'nagini',
        'color': '#22ff00',
        'head_url': 'https://raw.githubusercontent.com/james-gray/nagini/master/SnakeHead.png',
        'taunt': choice(smacktalk)
    })


@bottle.post('/move')
def move():
    data = bottle.request.json

    width = len(data['board'])
    height = len(data['board'][0])

    bounds = {
        "up": 1,
        "down": height - 2,
        "right": width - 2,
        "left": 1,
    }

    nagini = [s for s in data['snakes'] if s['name'] == 'nagini'][0]

    directions = get_possible_directions(nagini, data['board'], bounds)
    if not directions:
        bounds = {
            "up": 0,
            "down": height - 1,
            "right": width - 1,
            "left": 0,
        }

        directions = get_possible_directions(nagini, data['board'], bounds)
        if not directions:
            # Commit suicide honorably so as not to give any victories to
            # the other inferior snakes!

            return json.dumps({
                'move': seppuku(nagini, data['board']),
                'taunt': 'You will always remember this as the day you almost caught Captain Jack Sparrow!'
            })

    direction = move_edge(nagini, bounds)

    food = [x for x, food in directions if food]

    if food:
        return json.dumps({
            'move': choice(food),
            'taunt': choice(smacktalk)
        })
    else:
        directions = [x for x, _ in directions]
        return json.dumps({
            'move': direction if direction in directions else choice(directions),
            'taunt': choice(smacktalk)
        })


@bottle.post('/end')
def end():
    # data = bottle.request.json

    return json.dumps({})


# Expose WSGI app
application = bottle.default_app()
