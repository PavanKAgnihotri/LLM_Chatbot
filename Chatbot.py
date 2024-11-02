#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 10:01:50 2024

@author: pavan
"""

import google.generativeai as genai
import os

# API KEY
genai.configure(api_key = os.environ["API_KEY"])

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

def conversation_summary(user_input):
    prompt = "Summarize the following conversation: " + user_input
    summary_result = model.generate_content(prompt)
    summary = summary_result.candidates[0].content.parts[0].text
    return summary

def chatbot():
    print('Welcome to Chatbot! Type "quit" or "exit" to end the conversation\n')
    old_conversation = ""
    while True:
        user_input = input('You: ')
        if user_input.lower() == 'quit' or user_input.lower() == 'exit':
            print('Ending the conversation. Thank you!')
            break
        
        if old_conversation:
            prompt = f"Based on this conversation summary, respond to the following: {old_conversation}\nUser: {user_input}"
        else:
            prompt = user_input
            
        response = model.generate_content(prompt)
        response_generated = response.candidates[0].content.parts[0].text
        print('Chatbot: ', response_generated)
        
        old_conversation = conversation_summary(old_conversation + " User: " + user_input + " Charbot: " + response_generated)
        
chatbot()