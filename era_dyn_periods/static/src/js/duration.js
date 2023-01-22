odoo.define('era_dyn_periods.ageing', function (require) {
    'use strict';
    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var field_utils = require('web.field_utils');
    var rpc = require('web.rpc');
    var session = require('web.session');
    var utils = require('web.utils');
    var QWeb = core.qweb;
    var _t = core._t;

    var datepicker = require('web.datepicker');
    var time = require('web.time');

    var result= this._rpc({
        model:'account.move',
        method:'cal_task_duration',
    })
    console.log('Result = ',result)


});