from uwsgidecorators import *

@twice()
def twfunc():
    print "twfunc! \n"

@pin_rising(99)
def on_pin3_rising_edge():
    print "pin99 rising edge\n"

def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    twfunc()
    return "Hello World"

