# module 1 creating a blockchain *- coding: utf-8 -*-

#importing the libraries

import datetime
import hashlib
import json
from flask import Flask, jsonify

#Part 1 -Building a Blockchain

class Blockchain:
    def _init_|self|:
        self.chain = []
        self.create_block(proof =1, previous_hash = '0')
    