#!/usr/bin/env python
# encoding: utf-8

import plot
import pconfig
import json


if __name__ == "__main__":
    
    cfg = pconfig.read('rb_preserve.cfg')
    first_value, last_value = plot.data_span(cfg.get('settings', 'timeformat'))
    
    print """Content-Type: application/javascript

function min_secs(){
    return %f;
}

function max_secs(){
    return %f;
}

function default_begin(){
    return %d;
}

function config_json(){
    return %s;
}
""" % (first_value *1000, last_value *1000,
    int(cfg.get('settings', 'default_view_hours')),
    json.dumps(pconfig.json_out()))