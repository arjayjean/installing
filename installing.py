#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import subprocess
import typer

subprocess.run('clear')

app = typer.Typer()

def package(name):
    return name

def installing(package):
    installation = ['python3', '-m', 'pip', 'install', f'{package}']

    subprocess.run(installation)

    subprocess.run('clear')
@app.command()
def pip(name: str):
    installing(package(name))


if __name__ == "__main__":
    app()