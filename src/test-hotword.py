#!/usr/bin/env python3

from precise_runner import PreciseEngine, PreciseRunner

engine = PreciseEngine('precise-engine', 'jao-sandy.pb') 
runner = PreciseRunner(engine, on_activation=lambda: print('hello'))
runner.start()