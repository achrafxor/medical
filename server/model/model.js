const mongoose = require('mongoose');

var schema = new mongoose.Schema({
    name : {
        type : String,
        required: true
    },
    email : {
        type: String,
        required: true,
        unique: true
    },
    gender : String,
    phone : String
})

const Patientdb = mongoose.model('patientdb', schema);

module.exports = Patientdb;