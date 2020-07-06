from app import app


@app.route('/')
def index():
    return "hello world"

@app.route('/test', defaults={'name' : None})
@app.route('/test/<name>')
def test(name):
    if name:
        return 'hello %s' % name
    else:
        return "hello"

@app.route('/testid/<int:id>', methods=['GET'])
def test_id(id):
    print(type(id))
    return 'hi'