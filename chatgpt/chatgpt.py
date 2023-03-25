#!/usr/bin/env python
# coding=utf-8
import openai
import json
completion=openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"user","content":"can you tell me a english story?"},
        {"role":"user","content":"give me a next english story"}


    ]
    
)

print(completion.get('choices'))


