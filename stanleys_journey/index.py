import logging
from flask import Flask, render_template
from flask_ask import Ask, request, session, question, statement, version


app = Flask(__name__)
ask = Ask(app, "/")
logging.getLogger('flask_ask').setLevel(logging.DEBUG)


@ask.launch
def launch():
    speech_output = render_template('Welcome')
    card_title = "Welcome to Stanley's Journey"
    return question(speech_output).simple_card(title=card_title, content=speech_output).reprompt(speech_output)


@ask.intent("TheBeginning")
def stanleys_history():
    card_title = "Stanley's Backstory"
    speech_output = render_template('TheBeginning')
    return question(speech_output).simple_card(title=card_title, content=speech_output)


@ask.intent("WhatHappenedNext")
def what_happened_next():
    card_title = "What Happened next?"
    speech_output = render_template('WhatHappenedNext')
    return question(speech_output).simple_card(title=card_title, content=speech_output)


@ask.intent("HowDoesItEnd")
def how_does_it_end():
    card_title = "The end of Stanley's Story"
    speech_output = render_template('HowDoesItEnd')
    return question(speech_output).simple_card(title=card_title, content=speech_output)


## Stanley Learns to navigate
section = "Stanley Learns to Navigate"
@ask.intent("LearnToNavigate")
def navigate_beginning():
    speech_output = render_template('Lost_Beginning')
    return question(speech_output).simple_card(title=section, content=speech_output)

@ask.intent("NextDay")
def navigate_nextday():
    speech_output = render_template('Lost_NextDay')
    return question(speech_output).simple_card(title=section, content=speech_output)

@ask.intent("BurnMarks")
def navigate_fork():
    speech_output = render_template('Lost_BurnMarks')
    return question(speech_output).simple_card(title=section, content=speech_output)

@ask.intent("NoBurnMarks")
def navigate_fork():
    speech_output = render_template('Lost_NoBurnMarks')
    return question(speech_output).simple_card(title=section, content=speech_output)


@ask.intent("BridgeDecisionStream")
def navigate_bridge_stream():
    speech_output = render_template('Lost_Stream')
    return statement(speech_output).simple_card(title=section, content=speech_output)


@ask.intent("BridgeDecisionNoStream")
def navigate_bridge_nostream():
    speech_output = render_template('Lost_NoStream')
    return question(speech_output).simple_card(title=section, content=speech_output)


## Necessary for working with a live Alexa Skill on the store, without these, it wont get published.

@ask.intent('AMAZON.HelpIntent')
def help():
    card_title = "Help"
    speech_output = render_template('Help')
    return question(speech_output).simple_card(title=card_title, content=speech_output).reprompt(speech_output)

@ask.intent('AMAZON.StopIntent')
def stop():
	return statement("Goodbye")

@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")


@ask.session_ended
def session_ended():
    return "", 200


if __name__ == '__main__':
	app.run(debug=True)


#Potential stuff to log:
    # log.info("Request ID: {}".format(request.requestId))
    # log.info("Request Type: {}".format(request.type))
    # log.info("Request Timestamp: {}".format(request.timestamp))
    # log.info("Session New?: {}".format(session.new))
    # log.info("User ID: {}".format(session.user.userId))
    # log.info("Alexa Version: {}".format(version))