from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
from transformers import pipeline
# import joblib


# Define a function to initialize the summarizer
# def initialize_summarizer():
#     summarizer = pipeline("summarization", model="Falconsai/text_summarization")
#     return summarizer

# try:
#     summarizer = joblib.load('summarizer.pkl')
# except FileNotFoundError:
#     # If summarizer.pkl doesn't exist, initialize the summarizer and save it
#     summarizer = initialize_summarizer()
#     joblib.dump(summarizer, 'summarizer.pkl')

summarizer = pipeline("summarization", model="Falconsai/text_summarization")

@api_view(['GET','POST'])
def index(request):
    if request.method == "GET":
        return Response({"message":"This is a GET method."})
    elif request.method == "POST":
        data = request.data
        # print(data)
        string = data['text']
        # words = string.split()
        # first_10_words = ' '.join(words[:10])
        summary = summarizer(string, max_length=150, min_length=90, do_sample=False)
        summary = summary[0]['summary_text']
        return Response({"summary": summary})
    else:
        return Response({
            'status':400,
            'message':'Yes! rest framework is working fine.',
            'method_called':'called Invalid method'
        })
