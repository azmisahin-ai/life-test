from flask import Flask, render_template
from flask_socketio import SocketIO
import random
import time
from threading import Thread
import json


app = Flask(__name__, static_folder="static", template_folder="templates")
socketio = SocketIO(app)


class Organism:
    def __init__(self, name, max_reproduction_count):
        self.name = name
        self.reproduction_count = 0
        self.max_reproduction_count = max_reproduction_count
        self.code = []
        self.position = {"x": 0, "y": 0, "z": 0}
        self.position["x"] = random.uniform(-5, 5)
        self.position["y"] = random.uniform(-5, 5)
        self.position["z"] = random.uniform(-5, 5)

    def reproduce(self):
        if self.reproduction_count < self.max_reproduction_count:
            new_organism = Organism(f"{self.name}>Child", self.max_reproduction_count)
            self.reproduction_count += 1
            sendData("reproduce", {"name": self.name, "position": self.position})
            return new_organism
        else:
            sendData("reached", {"name": self.name, "position": self.position})
            print(
                f"{self.name} has reached the maximum reproduction count and cannot reproduce."
            )
            print("reproduction_count",self.reproduction_count)
            print("max_reproduction_count",self.max_reproduction_count)
            return None

    def die(self, main_program):
        print(f"{self.name} has died.")
        sendData("died", {"name": self.name, "position": self.position})
        # Organizmanın ölümü durumunda kodu parçala ve ana programa ekle
        main_program.add_code(self.code)


class MainProgram:
    def __init__(self, max_code_pool_size=10000):
        self.organisms = []
        self.code_pool = []
        self.max_code_pool_size = max_code_pool_size

    def add_code(self, code):
        self.code_pool.extend(code)
        # Limit the size of the code_pool
        if len(self.code_pool) > self.max_code_pool_size:
            self.code_pool = self.code_pool[-self.max_code_pool_size:]

    def send_ping(self, organism):
        # Organizmadan ek süre ve kod iste
        additional_time = random.uniform(0, 1)
        organism.code = self.code_pool.copy()  # Organizmanın kodunu al
        organism.code.append(f"Additional Time: {additional_time}")
        organism.code.append(f"Received Ping at {time.time()}")
        return additional_time

    def run_simulation(self, generations):
        sendData("life", "success")

        results = []
        for generation in range(generations):
            result = {"generation": generation + 1, "organisms": []}

            for organism in self.organisms:
                additional_time = self.send_ping(organism)
                reproduction_chance = random.random()

                if reproduction_chance > 0.5:
                    new_organism = organism.reproduce()
                    if new_organism:
                        self.organisms.append(new_organism)

                time.sleep(additional_time)  # Ek süreyi bekle

                death_chance = random.random()
                if death_chance > 0.8:
                    organism.die(self)
                    self.organisms.remove(organism)

                # Organizma bilgilerini ekle
                result["organisms"].append(
                    {
                        "name": organism.name,
                        "reproduction_count": organism.reproduction_count,
                    }
                )
                # send all data
                sendData("update-ui", result)

            results.append(result)

        sendData("life", "danger")
        return results


@app.route("/")
def index():
    return render_template("index.html")


environment = {"reproduction": 0, "generation": 0}


def sendData(channel, data):
    jsonData = (json.dumps(data),)
    # Send Main Program
    socketio.emit(channel, jsonData)
    # socketio.sleep(1)


def run_simulation():
    print("run_simulation", environment)
    main_program = MainProgram()
    initial_organism = Organism(
        "Organism_", max_reproduction_count=int(environment["reproduction"])
    )
    main_program.organisms.append(initial_organism)
    simulation_results = main_program.run_simulation(
        generations=int(environment["generation"])
    )


@socketio.on("update-universe")
def handle_start_simulation(new_environment):
    global environment
    environment = new_environment
    print("new_environment", environment)
    thread = Thread(target=run_simulation)
    thread.start()


if __name__ == "__main__":
    socketio.run(app, debug=True, host="0.0.0.0", port=5011)
