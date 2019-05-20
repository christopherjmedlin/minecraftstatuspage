from flask import Flask, render_template
from mcstatus import MinecraftServer


app = Flask(__name__, template_folder=".")


@app.route('/')
def index():
    try:
        server = MinecraftServer.lookup('mc.boomtown.xyz')
        status = server.status()
        return render_template('index.html', online=True,
                               players=status.players.online,
                               max_players=status.players.max,
                               version=status.version.name)
    except Exception:
        return render_template('index.html', online=False)
