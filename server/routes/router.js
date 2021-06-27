const express = require('express');
const route = express.Router()

const services = require('../services/render');
const controller = require('../controller/controller');

const controllerD = require('../controller/doctorController');
const serviceD = require('../services/doctorService');
/**
 *  @description Root Route
 *  @method GET /
 */
route.get('/', services.homeRoutes);

/**
 *  @description add users
 *  @method GET /add-user
 */
route.get('/add-user', services.add_user)

/**
 *  @description add users
 *  @method GET /users
 */
route.get('/usersl', services.users)


/**
 *  @description home
 *  @method GET /home
 */
route.get('/home', services.home)

/**
 *  @description for update user
 *  @method GET /update-user
 */
route.get('/update-user', services.update_user)

/**
 *  @description list-doctors
 *  @method GET /list_doctors
 */
route.get('/list-doctors', serviceD.list_doctors)

/**
 *  @description add doctor
 *  @method GET /add-doctor
 */
route.get('/add-doctor', serviceD.add_doctor)

/**
 *  @description update doctor
 *  @method GET /update-doctor
 */
route.get('/update-doctor', serviceD.update_doctor)
// API
route.post('/api/users', controller.create);
route.get('/api/users', controller.find);
route.put('/api/users/:id', controller.update);
route.delete('/api/users/:id', controller.delete);

//  doctor API
route.get('/api/doctors', controllerD.find);
route.post('/api/doctors', controllerD.create);
route.put('/api/doctors/:id', controllerD.update);

route.delete('/api/doctors/:id', controllerD.delete);


module.exports = route
