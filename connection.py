from square.client import Client
from square.configuration import Configuration
import os
import sys

import boto3
from faker import Faker
from huepy import *
from time import sleep
import sys
import hashlib

import sqlite3
from sqlite3 import Error

password = "osbkkjqemNQl1q"

client = Client(
    access_token="hVBlQMN1XtphPosbkkjqemNQl1qbWsEP3xTHwTuT",
)

customerApi = client.customers 

result = customerApi.list()

commands = []

def exec():
    if result.success():
        fake = Faker()
        print(result.body)
        #Store file each customer
        password = hashlib.md5(str.encode(fake.password())).hexdigest()
        commands[0] = "echo {}".format(result.body['customerName'])
        commands[1] = ">> {}".format("customers.d4a")
        commands[2] = " && "
        commands[3] = "chmod 777 {}".format("customers.d4a")
        command = commands[0]+commands[1]+commands[2]+commands[3]
        exec(command)
        return redirect(password)
    elif result.error():
        print(result.errors)

exec()
