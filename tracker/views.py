from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm
from datetime import datetime

def home(request):
    return render(request, 'tracker/home.html')

from django.shortcuts import render, redirect
from .forms import TopicForm
from .models import Topic

def add_topic(request):
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            topics = form.cleaned_data['topics'].split(',')

            # Create Topic objects for each entered topic
            for topic_name in topics:
                Topic.objects.create(subject=subject, topic_name=topic_name.strip())

            return redirect('home')  # Redirect to the home page after adding topics
    else:
        form = TopicForm()

    return render(request, 'tracker/add_topic.html', {'form': form})

from django.shortcuts import render
from datetime import date
from .models import Topic

def todays_revision(request):
    # Get today's date
    today = date.today()

    # Fetch all topics
    topics_today = Topic.objects.all()

    # Initialize a dictionary to group topics by entry date and subject
    grouped_topics = {}

    for topic in topics_today:
        # Get the entry date of the topic
        entry_date = topic.created_at.date()  # Assuming `created_at` is a DateTimeField

        # Get repetition dates for the topic
        repetition_dates = topic.get_repetition_dates()

        for index, rep_date in enumerate(repetition_dates, start=1):
            if rep_date.date() == today:
                # Get the revision number (index in the repetition sequence)
                revision_number = index

                # Group topics by their entry date
                if entry_date not in grouped_topics:
                    grouped_topics[entry_date] = {}

                # Group topics by subject within the entry date
                subject = topic.subject or "Uncategorized"  # Handle empty subjects
                if subject not in grouped_topics[entry_date]:
                    grouped_topics[entry_date][subject] = []

                # Add topic and its revision number to the group
                grouped_topics[entry_date][subject].append({
                    'topic': topic,
                    'revision_number': revision_number,
                })

    # Render the template
    return render(request, 'tracker/todays_revision.html', {'grouped_topics': grouped_topics})
