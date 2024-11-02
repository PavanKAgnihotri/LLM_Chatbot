#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 11:27:38 2024

@author: pavan
"""

import google.generativeai as genai
import os

sentences = [
    "<s> I study Computer Science </s>",
    "<s> I learn Computer Engineering </s>",
    "<s> We learn Computer Science </s>",
    "<s> We study Computer Science and Computer Engineering </s>"
]

# API KEY
genai.configure(api_key = os.environ["API_KEY"])

# Load the model
model = genai.GenerativeModel("gemini-1.5-flash")

embeddings = []
for s in sentences:
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=s,
        task_type="retrieval_document",
        title="Embedding of single string")
    embed_20 = result['embedding'][:20]
    embeddings.append(embed_20)
    
for i, e in enumerate(embeddings):
    print(f'Embedding for sentence {i+1}: {e}')
