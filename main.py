from flask import Flask

app = Flask(__name__)


def generate_html(message):
    version_number = '0001'
    html = """
        <!DOCTYPE html>
<html>
<body>

<h1>Simple Example</h1>

<button id="button" onclick="myFunction()">Click me</button>

<p id="demo"></p>

<script>
function myFunction() {
  document.getElementById("demo").innerHTML = "Hello World";
}
</script>

</body>
</html>""".format(message, version_number)
    return html


def greet():
    greeting = 'Welcome to CI/CD'
    return greeting


@app.route('/')
def hello_world():
    html = generate_html(greet())
    return html


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
