from framework.framework import *
from src.states.home import Home

app = Application()
app.init_state(Home())
app.run()
