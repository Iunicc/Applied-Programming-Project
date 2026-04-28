from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello, World!"}

#@=Decorator /name (name)=kann eigenen namen angeben, wenn name angegeben wird läuft Funktion darunter durch
@app.get("/name/{name}")
def greet_name(name: str):
    return {"message": f"Hello,{name}!"} #IP/name/Manuel -> Ausgabe im Browser

#Aufgabe: Weiteren Endpunkt bauen:
@app.get("/zahl/{zahl}")
def greet_name(zahl: int):
    return {zahl +1}