const axios = require('axios');



exports.add_doctor = (req, res) =>{
    res.render('add_doctor');
}



exports.list_doctors = (req, res) => {
    // Make a get request to /api/users
    axios.get('http://localhost:3000/api/doctors')
        .then(function(response){
            res.render('list_doctor', { users : response.data });
        })
        .catch(err =>{
            res.send(err);
        })

}


exports.update_doctor = (req, res) =>{
    axios.get('http://localhost:3000/api/doctors', { params : { id : req.query.id }})
        .then(function(userdata){
            res.render("update_doctor", { user : userdata.data})
        })
        .catch(err =>{
            res.send(err);
        })
}
